def main():
    set_password = input("Set a new password: ")
    check_password(set_password)


def check_password(right_password):
    tries_left = 3
    while True:
        guess_password = input("What is the password?: ")
        tries_left = tries_left - 1
        if tries_left == 0:
            print("\nYour password has been locked")
            exit()
        if right_password == guess_password:
            print(f"\nYes the password is: {right_password}")
            exit()
        else:
            print(f"\nincorrect guess... try again \nYou have {tries_left} tries left.")
main()