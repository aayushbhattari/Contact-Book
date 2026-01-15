

def add():
    while True:
        name = input('Enter Your Name: ').lower().strip()
        if name.isdigit() or len(name)<4:
            print('Enter Valid Name!')
            continue
        else:
            pass
        while True:
            phone_no = input("Enter your phone number: ")
            if len(phone_no) == 10 and phone_no.isdigit():
                pass
            else:
                print('Enter Valid Phone Number!')
                continue
            while True:
                email = input('Enter your email: ')
                if "@" in email and email.isalnum():
                    pass
                else:
                    print("Enter a valid email!")
                    continue

       





print('----- CONTACT BOOK ----- \n')
print('''1. Add new contact
2. View all contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit''')

while True:
    user_input = input("Choose an Option: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 0:
            print('Choose a Valid Option!')
            continue
        if user_input == 1:
             add()
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            pass
        elif user_input == 6:
            pass
    else:
        print('Choose a Option!')
        continue

           
