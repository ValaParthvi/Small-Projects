package main

import (
	"bufio"
	"fmt"
	boltdb "github.com/boltdb/bolt"
	"gopkg.in/oleiade/reflections.v1"
	"log"
	"os"
	"strings"
	"time"
	"github.com/fatih/color"
)

const buckName = "ideas"
const dbName = "keeper.db"

type Idea struct {
	IdeaName, Detail, Link string 
	Keywords               []string
}

func checkError(err error) {
	if err != nil {
		color.HiRed("Error occured: ")
		log.Fatal(err)
	}
}
func main() {
	db, err := boltdb.Open(dbName, 0600, &boltdb.Options{Timeout: 1 * time.Second})
	checkError(err)
	defer db.Close()
	buf := bufio.NewScanner(os.Stdin)
	fmt.Print("Add/List/Delete?")
	switch buf.Scan(); buf.Text() {
	case "Add":
		checkError(db.Update(addIdea))
	case "List":
		checkError(db.View(listIdeas))
	case "Delete":
		checkError(db.Update(deleteIdea))
	}
}

func addIdea(tx *boltdb.Tx) error {
	idea := Idea{}
	buf := bufio.NewScanner(os.Stdin)
	for _, field := range []string{"IdeaName", "Detail", "Link", "Keywords"} {
		fmt.Printf("Enter %s: ", field)
		buf.Scan()
		var val interface{}
		if field == "Keywords" {
			val = strings.Split(buf.Text(), ",")
		} else {
			val = buf.Text()
		}
		reflections.SetField(&idea, field, val)
	}
	bucket, err := tx.CreateBucketIfNotExists([]byte(buckName))
	checkError(err)
	err = bucket.Put([]byte(idea.IdeaName), []byte(fmt.Sprintf("\nIdea Name: %v\nDetails: %v\nLinks: %v\nKeywords:%v", idea.IdeaName, idea.Detail, idea.Link, idea.Keywords)))
	checkError(err)
	v := bucket.Get([]byte(idea.IdeaName))
	color.New(color.FgCyan).Add(color.Bold).Printf("Value stored correctly: %s\n", v)
	return nil
}

func listIdeas(tx *boltdb.Tx) error {
	bucket := tx.Bucket([]byte(buckName))
	buf := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter idea name to retrieve: ")
	buf.Scan()
	input := buf.Text()
	if input == "All" {
		cursor := bucket.Cursor()
		for key, value := cursor.First(); key != nil; key, value = cursor.Next() {
			color.Blue(string(value))
		}
	} else {
		color.Blue(string(bucket.Get([]byte(input))))
	}
	return nil
}

func deleteIdea(tx *boltdb.Tx) error {
	bucket := tx.Bucket([]byte(buckName))
	buf := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter entry to delete: ")
	buf.Scan()
	if buf.Text() == "All" {
		cursor := bucket.Cursor()
		for key, _ := cursor.First(); key != nil; key, _ = cursor.Next() {
			checkError(bucket.Delete(key))
		}
		color.Red("Everything deleted successfully.")
		} else {
		checkError(bucket.Delete([]byte(buf.Text())))
		color.Red("Delete successful.")
	}
	return nil
}
