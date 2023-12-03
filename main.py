#@Author Mounika Bandhamravuri
#random key generator
import random
new_key = ""
new_key_list = []
string = "abcdefghijklmnopqrstuvwxyz"
for i in string:
  new_key_list.append(i)

new_key_list = random.sample(new_key_list, len(new_key_list))
new_key = new_key.join(new_key_list)
print("Current Decryption Key :" + new_key)
#converting key to bytes
new_key = bytes(new_key, 'utf-8')

#encryption key
encryption_key = b"abcdefghijklmnopqrstuvwxyz"
#decryption key
dcryption_key = new_key
#encryption table mapping
encryption_table = bytes.maketrans(encryption_key, dcryption_key)
#decryption key mapping
decryption_table = bytes.maketrans(dcryption_key, encryption_key)


#function to decrpt with a specific key value
def decrypt(dk, message):
    encryption_key = b"abcdefghijklmnopqrstuvwxyz"
    decrytion_key = dk
    encrytion_table = bytes.maketrans(encryption_key, decrytion_key)

    decryption_table = bytes.maketrans(decrytion_key, encryption_key)
    result = message.translate(decryption_table)

    return result


#initilized Vars:

choice = ''
result = ''
message = ''
dk = ''

#main driver code

while choice != '0':
    choice = input(
        "Do you want to encrypt or decrypt the message: \n 1 to encrypt \n 2 to decrypt \n 3 to decrypt with a key \n Q to Quit \n >>"
    )
    if choice == "1":
        message = input("Enter encryption Message: ")
        result = message.translate(encryption_table)
        print("\nEncryption For Given Message: " + result + "\n" + " \n" +
              "Decryption KEY = " + str(new_key) + "\n\n")
    elif choice == "2":
        message = input("Enter Decryption message: ")
        result = message.translate(decryption_table)
        print(result + "\n\n")
    elif choice == "3":
        message = input("Enter Decrytion Message: ")
        dk = input("Enter Decryption Key: ")
        result = decrypt(bytes(dk, 'utf-8'), message)
        print("Decrpted message with given Key: " + dk + "\n" + result + "\n\n")
    elif choice == "Q" or "q":
        exit()
    else:
        print("Invalid Input please try again ")