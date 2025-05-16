import json
import os

# Add Contact Function
def add_contact(contact):
        n = int(input("How many contacts do you want to enter: "))
        for i in range(0,n):
            print(f"Contact {len(contact) + 1}: ")
            nm = input("Enter name: ")
            phNo = int(input("Enter Phone Number: "))
            eml = input("Enter E-mail: ")
            contact[(len(contact)+1)] = [nm, phNo, eml]
            print(f"Contact {len(contact)} is Added.")
        with open("contacts.json", "w") as f:
            json.dump(contact,f)


# Edit Contact Function
def edit_contact(contact):
    n = int(input("How many contacts do you want to edit: "))
    if(len(contact) < n):
            print(f"Error! {n} Contacts are not present. Total Conatct Present: {len(contact)}")
    else:
        for i in range(0,n):
            x = input("Enter contact name which you want to edit: ")
            for key,value in sorted(contact.items()):
                if(value[0].lower()==x.lower()):
                    value[0] = input("Enter new name: ")
                    value[1] = int(input("Enter new Phone Number: "))
                    value[2] = input("Enter new E-mail: ")
                    print(f"Contact {x} is updated to {value[0]}.")
                    with open("contacts.json", "w") as f:
                        json.dump(contact,f)
                    return contact
            print(f"{x} is not present in the contact.")

    return contact


# View Contact Function
def view_contact(contact):
    if(int(len(contact)) == 0):
        print("No Contact Available...")
    else:
        for key,value in sorted(contact.items()):
            print("Contact",key, ": ", "\nName: ", value[0], "\nPhone Number: ", value[1], "\nEmail: ", value[2])
    return


# Search Contact Function
def search_contact(contact):
    x = input("Enter contact name which you want to search: ")
    for key,value in sorted(contact.items()):
        if(value[0].lower()==x.lower()):
            print("Contact ",key, ": ", "\nName: ", value[0], "\nPhone Number: ", value[1], "\nEmail: ", value[2])
            return
    print(f"No contact named {x} is present.")
    return


# Delete Contact Function
def delete_contact(contact):
    if(len(contact) == 0):
        print("No Contact Available...")
    else:
        x = input("Enter the contact name you want to delete: ")
        for key,value in sorted(contact.items()):
            if(value[0].lower()==x.lower()):
                contact.pop(key)
                print(f"Contact {x} is deleted successfully")
                with open("contacts.json", "w") as f:
                    json.dump(contact, f)
                return contact
        print(f"Contact {x} is not present")
    return contact


# Contact Manager Block
def contactManager():
    cont = 'y'
    if(os.path.exists("D:/IDRAK AI Software House/contacts.json")):
        with open("contacts.json", "r") as f:
            contact = json.load(f)
    else:
        contact = {}
    while(cont.lower() == 'y'):
        print("-----Simple Contact Manager-----")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contact")
        print("4. Search Contact")
        print("5. Delete Contact")
        try:
            choice = int(input("Enter your choice (1-5): "))
            if(choice>0 and choice <=5):
                None
            else:
                while(choice<0 or choice>5):
                    choice = int(input("Please! Enter choice between 1-5: "))
            if(choice == 1):
                try:
                    add_contact(contact)
                except Exception as e:
                    print(e)
            elif(choice == 2):
                try:
                    edit_contact(contact)
                except Exception as e:
                    print(e)
            elif(choice == 3):
                try:
                    view_contact(contact)
                except Exception as e:
                    print(e)
            elif(choice == 4):
                try:
                    search_contact(contact)
                except Exception as e:
                    print(e)
            elif(choice == 5):
                try:
                    delete_contact(contact)
                except Exception as e:
                    print(e)
        except:
            print("Please Enter an Integer between 1 to 5")

         # Quit or Continue this Application
        cont = input("Do you want to continue? (Y/N) : ")
        if(cont == 'n' or cont == 'N'):
            x = input("Do you want to save the contacts.json file: (Y/N)")
            if(x.lower() == 'y'):
                print("File is saved...")
            elif(x.lower() == 'n'):
                try:
                    os.remove("D:/IDRAK AI Software House/contacts.json")
                except OSError as error:
                    print(error, " File is not present...")
            print("Quiting the Application...")
            exit(0)
        elif(cont == 'y' or cont == 'Y'):
            None
        elif(cont!='n' or cont!='N' or cont!="y" or cont!="Y"):
            while(cont!='n' or cont!='N' or cont!="y" or cont!="Y"):
                cont = input("Invalid Input! Please Enter (Y/N): ")
                if(cont == 'n' or cont == 'N'):
                    x = input("Do you want to save the contacts.json file: (Y/N)")
                    if(x.lower() == 'y'):
                        print("File is saved...")
                    elif(x.lower() == 'n'):
                        try:
                            os.remove("D:/IDRAK AI Software House/contacts.json")
                        except OSError as error:
                            print(error, " File is not present...")
                    print("Quiting the Application...")
                    exit(0)
                elif(cont == 'y' or cont == 'Y'):
                    break




# Main Block
if __name__ == "__main__":
    contactManager()