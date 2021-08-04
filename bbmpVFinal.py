# BBMP Complaint Management System
# A Joint Effort between 2 individuals who just want to sleep and eat.

import os
import sys
import random
from tabulate import tabulate
import copy

name = ''
phone = ''
pincode = ''
wardno = ''
complaint = ''
x = 1

# Validate function used to validate the phone number during user login.


def validate(phone, passw):
    file = open("users.txt", "r")
    re = file.readlines()
    for line in re:
        userlist = line.split('\t')
        ph = userlist[0]
        pas = userlist[1]
        if ph == phone and pas == passw:
            return True

# check function used to check if the phone number is already registered


def check(phone):
    file = open("users.txt", "r")
    re = file.readlines()
    for line in re:
        userlist = line.split('\t')
        ph = userlist[0]
        if ph == phone:
            return False

# register function used to register a new user


def register():
    os.system('cls')
    print()
    print('Register your account'.center(60, "-"))
    print()
    print("Enter your details".center(60, "*"))
    print()
    phone = input("Phone: ")
    passw = input("Password: ")
    if(phone.isnumeric() and len(phone) == 10):
        acc = check(phone)
        if acc == False:
            print("Phone number already exists")
        else:
            file = open("users.txt", "a")
            user = [phone, passw]
            for i in user:
                file.write(i+'\t')
            file.write('\n')
        return
    else:
        print("The Phone Number which is provided is Invalid. Please Do Provide a Valid Number")


# lodge function used to lodge a new complaint

def lodge(phone):
    global x
    os.system('cls')
    print("")
    print("You Have Chosen To Lodge A Complaint")
    print("***********************************************************************************************************************")
    print("")
    #phone = input("Please enter your Phone Number to continue: ")
    name = input("Enter your Name: ")
    pincode = input("Enter your area Pincode: ")
    while len(pincode) != 6:
        pincode = input("Pincode Entered is Invalid. Enter a Valid PinCode: ")
    wardno = input("Enter your ward number: ")
    while(1 > int(wardno) or int(wardno) > 198):
        wardno = input(
            "WardNumber Entered is Invalid. Enter a Valid Ward Number: ")
    complaint = input('Please enter your Complaint description: ')
    status = "0"
    print("")
    x = int(phone[:5])+random.randint(100, 999)
    x1 = str(x)
    list1 = [x1, phone, name, pincode, wardno, complaint, status]
    file = open("complaints.txt", "a")
    for i in list1:
        file.write(i+'\t')
    file.write('\n')
    print("This Is Your COMPLAINT ID: "+x1 +
          "\nPlease Do Provide the ID whenever you need to modify or delete a complaint\nThank You\n")
    file.close()
    input("Press ANY Key To Continue:")
    os.system('cls')
    return

# display function used for displaying the user complaints.


def display(phone):
    print("")
    flag = 1
    file = open("complaints.txt", "r")
    re = file.readlines()
    os.system('cls')
    listM = []
    #phone = input("Enter your phone number to search your complaint: ")
    print("")
    print("Your Complaint Details are".center(125, '*'))
    for line in re:
        list2 = line.split('\t')
        list2.remove('\n')
        if(list2[1] == phone):
            if list2[6] == '0':
                list2[6] = "Pending"
            else:
                list2[6] = "Resolved"
            listM.append(list2)
            flag = 0
    if flag == 1:
        print("Details not found")
    else:
        print(tabulate(listM, headers=["ComplaintID", "Phone", "Name",
              "Pincode", "Ward Number", "Complaint", "Status"], tablefmt="pretty"))
    input("Press ANY Key To Continue:")
    os.system('cls')
    return


# display_all function is used to display all the complaints to the admin

def display_all():
    print("")
    file = open("complaints.txt", "r")
    re = file.readlines()
    listM = []
    os.system('cls')
    print("")
    print("Complaint Details: ".center(125, '*'))
    for line in re:
        list2 = line.split('\t')
        list2.remove('\n')
        if list2[6] == '0':
            list2[6] = "Pending"
        else:
            list2[6] = "Resolved"
        listM.append(list2)
    print(tabulate(listM, headers=["ComplaintID", "Phone", "Name",
          "Pincode", "Ward Number", "Complaint", "Status"], tablefmt="psql"))
    input("Press ANY Key To Continue:")
    os.system('cls')
    return


# Modify function used to modify the complaint

def modify(phone):
    flag = 1
    file = open("complaints.txt", 'r+')
    re = file.readlines()
    os.system('cls')
    listM = []
    list3 = []
    #phone = input("Enter Your Mobile Phone Number:\t")
    cid = input("Enter Your Complaint ID\t")
    print("")
    file.seek(0)
    for line in re:
        list2 = line.split('\t')
        list3 = list2.copy()
        if (list2[0] == cid and list2[1] == phone):
            if(list2[6] == '0'):
                flag = 0
                print()
                print("Your Complaint Details are".center(125, '*'))
                print("")
                list3.remove('\n')
                if list3[6] == '0':
                    list3[6] = "Pending"
                else:
                    list3[6] = "Resolved"
                listM.append(list3)
                print(tabulate(listM, headers=[
                      "ComplaintID", "Phone", "Name", "Pincode", "Ward Number", "Complaint", "Status"], tablefmt="psql"))
                list2[5] = input("Enter the modification in the complaint:\t")
                news = '\t'.join(list2)
                file.write(news)
                print("")
                print("The Complaint has been Modified".center(120, "*"))
                print("")
            else:
                print(
                    "The Complaint has already been handled thus Furthur Modification is not Possible")
                flag = 0
        else:
            file.write(line)
        file.truncate()
    if(flag == 1):
        print("The Complaint ID/Phone Number Doesn't match or the Complaint doesn't Exist. Try Again")
    file.close()
    input("Press ANY Key To Continue:")
    os.system('cls')
    return


# modif_admin function used to update the status of completion of the complaints by the admin

def modify_admin():
    flag = 1
    file = open("complaints.txt", 'r+')
    re = file.readlines()
    os.system('cls')
    cid = input("Enter Complaint ID: ")
    print("")
    file.seek(0)
    for line in re:
        list2 = line.split('\t')
        if (list2[0] == cid):
            flag = 0
            print()
            print("Complaint Details are".center(125, '*'))
            print("")
            print("Complaint ID: ".ljust(50, '.'), list2[0].rjust(75))
            print("Phone".ljust(50, '.'), list2[1].rjust(75))
            print("Name".ljust(50, '.'), list2[2].rjust(75))
            print("Pincode".ljust(50, '.'), list2[3].rjust(75))
            print("Ward Number".ljust(50, '.'), list2[4].rjust(75))
            print("Complaint".ljust(50, '.'), list2[5].rjust(75))
            if list2[6] == "0":
                print("Status".ljust(50, '.'), "Pending".rjust(75))
            else:
                print("Status".ljust(50, '.'), "Resolved".rjust(75))
            print("")
            list2[6] = input(
                "Enter the Status of the complaint(1 for Resolved / 0 for Pending): ")
            news = '\t'.join(list2)
            file.write(news)
            print("")
            if list2[6] == "1":
                print("The Complaint has been Resolved!!".center(120, "*"))
            else:
                print("The Complaint is Pending!!".center(120, "*"))
            print("")
        else:
            file.write(line)
        file.truncate()
    if(flag == 1):
        print("The Complaint ID/Phone Number Doesn't match or the Complaint doesn't Exist. Try Again")
    file.close()
    input("Press ANY Key To Continue:")
    os.system('cls')
    return

# delete function used to delete the user complaints


def delete(phone):
    flag = 1
    file = open("complaints.txt", 'r+')
    re = file.readlines()
    os.system('cls')
    #phone = input("Enter Your Mobile Phone Number:\t")
    cid = input("Enter Your Complaint ID\t")
    print("")
    file.seek(0)
    for line in re:
        list2 = line.split('\t')
        if (list2[0] == cid and list2[1] == phone):
            flag = 0
            print()
            print("Your Complaint Details are".center(125, '*'))
            print("")
            print("Complaint ID: ".ljust(50, '.'), list2[0].rjust(75))
            print("Phone".ljust(50, '.'), list2[1].rjust(75))
            print("Name".ljust(50, '.'), list2[2].rjust(75))
            print("Pincode".ljust(50, '.'), list2[3].rjust(75))
            print("Ward Number".ljust(50, '.'), list2[4].rjust(75))
            print("Complaint".ljust(50, '.'), list2[5].rjust(75))
            print("")
            print("\nComplaint Has Been Deleted\n")
        else:
            file.write(line)
        file.truncate()
    if(flag == 1):
        print("The Complaint ID/Phone Number Doesn't match or the Complaint doesn't Exist. Try Again")
    file.close()
    input("Press ANY Key To Continue:")
    os.system('cls')
    return


# Execution starts from here....
choice = 1
z = 1
k = 1
password1 = "Raghav123"
password2 = "Nawang123"
print("Welcome to the BBMP Complaint Management Portal".center(120, "-"))
print("")
print("")

while(z != 0):
    choice = 1
    print("Please Do Identify Yourself:")
    print("")
    print("1. Administrator")
    print("2. User")
    print("0. EXIT")
    z = int(input("Press the number corresponding to the role : "))
    if z == 1:
        os.system('cls')  # Administrator
        passw = input("Please enter your password to continue: ")
        while (passw != password1 and passw != password2):
            os.system('cls')
            passw = input(
                "Incorrect Password. Enter the Correct Password or press 0 to return to the Main Menu: ")
            if passw == "0":
                print()
                os.system('cls')
                choice = 0
                break
        os.system('cls')
        while(choice != 0):
            print("")
            print("")
            print("BBMP Complaint Management System".center(120, "*"))
            print("")
            print("MENU:")
            print("")
            print("1. Display The Complaints")
            print("2. Update the status")
            print("0. Log Out")
            print()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_all()
            elif choice == 2:
                modify_admin()
            elif choice == 0:
                print()
                os.system('cls')
            else:
                print("Invalid Choice. Choose Again!")

    elif z == 2:  # User
        os.system('cls')
        while(choice != 0):
            print("")
            print("")
            print("Account".center(60, "*"))
            print("1.Login")
            print("2.Sign-up")
            print("0.Exit")
            print()
            option = input("Enter your option:")
            if option == "1":
                os.system('cls')
                phone = input("Enter your phone number: ")
                passw = input("Enter your password: ")
                res = validate(phone, passw)
                if res != True:
                    k = 0
                    os.system('cls')
                    print()
                    print("Invalid Credentials!!")
                else:
                    k = 1
                while k == 1:
                    print("BBMP Complaint Management System".center(120, "*"))
                    print("")
                    print("MENU:")
                    print("")
                    print("1. Lodge a complaint")
                    print("2. Display your Complaints")
                    print("3. Delete your complaint")
                    print("4. Modify Your Complaint")
                    print("0. Log Out")
                    print()
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        lodge(phone)
                    elif choice == 2:
                        display(phone)
                    elif choice == 3:
                        delete(phone)
                    elif choice == 4:
                        modify(phone)
                    elif choice == 0:
                        os.system('cls')
                        break
                    else:
                        print("Invalid Choice. Choose Again!")
            elif option == "2":
                os.system('cls')
                register()
            else:
                print()
                os.system('cls')
                sys.exit()

    elif z == 0:
        os.system('cls')
        sys.exit()

    else:
        os.system('cls')
        print("Invalid Choice. Choose Again!")
        print("")
