menu = """
1. Add Contact
2. Show Contacts
3. Search Contact
4. Delete Contact
5. Exit
"""

while True:
    print(menu)
    user_choice = int(input("please enter yor choice: "))

    if user_choice == 5:
        break