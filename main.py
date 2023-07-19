# Lab 6 by Shashank Navale and Thomas Reggeti
# Version 2

def encode(password):
    encoded = ""  # initializes an empty string that will be returned after manipulation

    for element in password:
        if element == "7":
            encoded += "0"
        elif element == "8":
            encoded += "1"
        elif element == "9":
            encoded += "2"
        else:
            encoded += str(int(element)+3)  # runs through every element of the password and manipulates it

    return encoded  # returns back the encoded password to the main() function


def decode(password):
    pass


def main():
    while True:
        initial_password = ""  # initializes an empty string for the user inputted password
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        menu_option = int(input("Please enter an option: "))  # takes in user input for menu option

        if menu_option == 1:
            initial_password = input("Please enter your password to encode: ")
            encoded_password = encode(initial_password)  # encodes the user inputted password
            print("Your password has been encoded and stored!")

        elif menu_option == 2:
            if len(initial_password) == 0:  # checks if initial password is empty
                print("No password encoded yet. Please use Option 1.")
                continue  # re loops and asks for user input again

            decoded_password = decode()  # implement the decode function here
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif menu_option == 3:
            break  # breaks and exits out of the program

        else:
            print("This isn't a valid option! Please try again.\n")  # prompts user to enter valid option



if __name__ == '__main__':
    main()

