

names =[]
phone_numbers =[]
emails =[]


def add():
    while True:
        name = input('Enter Your Name: ').title().strip()
        names.append(name)
        if name.isdigit() or len(name)<3:
            print('Enter Valid Name!')
            continue
        else:
            break
                
    while True:
            phone_no = input("Enter your phone number: ")
            if len(phone_no) == 10 and phone_no.isdigit():
                phone_numbers.append(phone_no)
                break
                   
            else:
                print('Enter Valid Phone Number!')
                continue
    while True:
        email = input('Enter your email: ')
        if "@" in email  and email.endswith('@gmail.com'):
            emails.append(email)
            break
        else:
            print("Enter a valid email!")
            continue

    with open('contactbook.txt','a') as f:
            f.write(f'Name: {name}\n')     
            f.write(f'Phone Number: {phone_no}\n') 
            f.write(f'Email: {email}\n') 
            f.write('-'*40 + '\n')


def view():
    print('----ALL CONTACTS----')
    with open('contactbook.txt','r') as f:   
       data =f.read()
       print(data)      
  #need help here      
def search():
    user_search = input("Enter name or phone number to search: ").title().strip()
    for name in names:
        if name == user_input:
            t = names.index(name) 
            print('Contact Found!')
            print(f'''Name:{user_input}
                      Phone Number:{phone_numbers[t]}
                      Email:{emails[t]}''')
            
    for phn in phone_numbers:
        if phn == user_input:
           t = phone_numbers.index(phn)
        print('Contact Found!')
        print(f'''Name:{names[t]}
                     Phone Number:{user_input}
                     Email:{emails[t]}''')
        



        




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
             view()
        elif user_input == 3:
             search()
        elif user_input == 4:
            pass
        elif user_input == 5:
            pass
        elif user_input == 6:
            print('')
            break
    else:
        print('Choose a Option!')
        continue

           
