#-------------------------------------------------------------------------------
# Name:        Contact Book
# Purpose:
#
# Author:      Hamza Khan
#
# Created:     25-05-2024
# Copyright:   (c) Hamza Khan 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

contact = {}
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(ley,contact.get(key)))

while True:
    choice = int(input(" 1. Add New Contact \n 2. Search Contact \ 3. Display Contact \n 4. Edit Contact \n 5. Delete Contact \n 6. Exit\n Enter Your Choice "))
    if choice == 1:
        name = input("Enter The Contact Name ")
        phone = input("Enter The Mobile Number ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter The Contact Name ")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[seacrh_name])
        else:
            print("Name is not found in Contact Book")
    elif choice == 3:
            if not contact:
                print("Empty Contact Book")
            else:
                display_contact()
    elif choice == 4:
        edit_contact = input("Enter The Contact to be Edited ")
        if edit_contact in contact:
            phone = input("Enter Mobile Number")
            contact[edit_contact]=phone
            print("Contact Updated")
            display_contact()
        else:
            print("Name is not Found in Contact Book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact? y/n ")
            if confirm =='y' or  confirm =='Y':
                    contact.pop(del_contact)
            display_contact()
        else:
                print("Name is not found in Contact Book")
    else:
        break

