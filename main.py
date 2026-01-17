
names=[]
phone_numbers =[]
emails =[]


def load_contacts():
     names.clear()
     phone_numbers.clear()
     emails.clear()

     with open('contactbook.txt','r') as f:
          lines = f.readlines()
          name=phone=email=None
          for line in lines:
                line=line.strip()
                if line.startswith('Name:'):
                    name = line.replace('Name: ','')
                elif line.startswith("Phone Number:"):
                    phone =line.replace('Phone Number:','')
                elif line.startswith("Email:"):
                    email = line.replace('Email: ','')
                elif line.startswith('-') and name:
                     names.append(name)
                     phone_numbers.append(phone)
                     emails.append(email)
                     name = phone = email = None

          if name:
            names.append(name)
            phone_numbers.append(phone)
            emails.append(email)
               


def add():
    while True:
        name = input('Enter Your Name: ').title().strip()
        if name.isdigit() or len(name)<3:
            print('Enter Valid Name!')
            continue
        else:
            
            break
                
    while True:
            phone_no = input("Enter your phone number: ")
            if len(phone_no) == 10 and phone_no.isdigit():
                
                break
                   
            else:
                print('Enter Valid Phone Number!')
                continue
    while True:
        email = input('Enter your email: ')
        if "@" in email  and email.endswith('@gmail.com'):
           
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


def search():
            load_contacts()
        
            user_option = input("To search using name(Enter 'n') or phone number(Enter -'p') ")
            if user_option =='n':
                user_search = input('Enter name: ').title().strip()
                for i in range(len(names)):
                    if names[i] == user_search:
                        print("Contact Found!")
                        print(f"Name: {names[i]}")
                        print(f"Phone Number: {phone_numbers[i]}")
                        print(f"Email: {emails[i]}")

                        return
                        
                print('Contact Not Found')    
            elif user_option =='p': 
                user_search = input('Enter Number: ')       
                for i in range(len(phone_numbers)):

                        if phone_numbers[i] == user_search:
                           print("Contact Found!")
                           print(f"Name: {names[i]}")
                           print(f"Phone Number: {phone_numbers[i]}")
                           print(f"Email: {emails[i]}")
      
                        return
                print('Contact not found')     

            else:
                 print('Invalid Option!')

def update():
    load_contacts()
    user_update = input("Enter name to update: ").capitalize().strip()
    if user_update in names:
        t = names.index(user_update)
        print('What do you want to update(Enter the choiced number.)?: ')
        print('1. Phone Number')
        print('2. Email')
        print('3. Both')
        choice = int(input('Choose Option: '))
        if choice== 1:
           while True:
            new_phn = input('Enter new number: ')
            if len(new_phn) == 10:
                    phone_numbers[t] = new_phn
                    print('Contact Updated!')
                    break
            else:
                 print('Invalid Number.')
                 continue
        elif choice == 2:
                    while True:
                        new_email = input('Enter new email: ')
                        if new_email.endswith('@gmail.com'):
                            emails[t] = new_email
                            break
                        else:
                             print('Invalid Email.')
                             print('Contact Updated!')
                             continue                   
        elif choice == 3:
                    while True:
                        new_phn = input('Enter new number: ')
                        if len(new_phn) == 10:
                            phone_numbers[t] = new_phn
                            break
                        else:
                            print('Invalid Number.')
                            continue   
                    while True:
                        new_email = input('Enter new email: ')
                        if new_email.endswith('@gmail.com'):
                            emails[t] = new_email
                            print('Contact Updated!')
                            break
                        else:
                             print('Invalid Email.')
                             continue                      
        with open("contactbook.txt", "w") as f:
            for j in range(len(names)):
                f.write(f"Name: {names[j]}\n")
                f.write(f"Phone Number: {phone_numbers[j]}\n")
                f.write(f"Email: {emails[j]}\n")
                f.write("-" * 40 + "\n")             
    else:
         print('Contact Does Not Exist!')    
     
def delete():
     load_contacts()
     user_del = input('Enter name to delete: ').title().strip()
     if user_del not in names:
          print('Contact Do Not Exist.')  
          return
     confirmation = input('Are you sure? (y/n): ')
     if confirmation == 'y':
        i = names.index(user_del)
        del names[i]
        del emails[i]
        del phone_numbers[i]
        print('Contact deleted')  
 
     with open("contactbook.txt", "w") as f:
            for j in range(len(names)):
                f.write(f"Name: {names[j]}\n")
                f.write(f"Phone Number: {phone_numbers[j]}\n")
                f.write(f"Email: {emails[j]}\n")
                f.write("-" * 40 + "\n")    


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
            update()
        elif user_input == 5:
            delete()
        elif user_input == 6:
            print('')
            break
    else:
        print('Choose a Option!')
        continue

           
