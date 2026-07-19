import json

menu = """
1. Add Contact
2. Show Contacts
3. Search Contact
4. Delete Contact
5. Exit
"""

def add_contact():
    contact_name = input("please enter contact name: ")
    contact_phone = input("please enter contact phone number: ")
    contact_mail = input("please enter contact mail: ")

    new_contact = {
             "name" : contact_name,
            "phone" : contact_phone,
            "mail" : contact_mail
        }
    

    if len(contact_name) >= 3 and len(contact_phone)>= 8 and len(contact_mail) >= 8:
        try:
            with open("contacts.json","r") as contacts_file:
                contacts = json.load(contacts_file)
        except (FileNotFoundError, json.JSONDecodeError):
            contacts = []
        contacts.append(new_contact)
        with open("contacts.json","w") as contacts_file:
            json.dump(contacts,contacts_file)
        print("contact add!!!")
    else:
        print("enter valid input")

while True:
    print(menu)
    user_choice = int(input("please enter yor choice: "))

    if user_choice == 5:
        break
    elif user_choice == 1:
        add_contact()