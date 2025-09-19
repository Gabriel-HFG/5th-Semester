def send_invitation(receiver, sender="Princess Peach"):

    print(f"""
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},
        
        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """)


def main():

    list = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser"]
    for i in list:
        receiver = i
        if receiver == "Princess peach":
            continue
        send_invitation(receiver)

main()