def cipher():
    ans_start = input("Do you want to start?")
    ans_start = ans_start.upper()
    while(ans_start in 'YES'):
        print("What do you prefer to do?")
        ans =  input("Press E to Encrypt. Press D to Decrypt: ")
        ans = ans.upper()

        if(ans=='E'):
            user_input = input("Enter the text you want to Decrypt: ")
            intab = 'abcdefghijklmnopqrstuvwxyz1234567890'
            outtab ='0987654321zyxwvutsrqponmlkjihgfedcba'
            encryption = ''
            encryption = encryption.maketrans(intab,outtab)
            print("Decrypted code is:")
            print(user_input.translate(encryption))


        elif(ans=='D'):
            user_input = input("Enter the text you want to Encrypt: ")
            intab ='0987654321zyxwvutsrqponmlkjihgfedcba'
            outtab = 'abcdefghijklmnopqrstuvwxyz1234567890'
            decryption = ''
            decryption = decryption.maketrans(intab,outtab)
            print("Encrypted code is:")
            print(user_input.translate(decryption))

        else:
            print("Please enter 'E' to Encrypt or 'D' to Decrypt.")
        ans_start = input("Do you want to do it again?")
        ans_start = ans_start.upper()


def main():
    cipher()

if __name__ == '__main__':
    main()
