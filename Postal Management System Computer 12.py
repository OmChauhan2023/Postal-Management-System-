import csv
from tabulate import tabulate
import mysql.connector as mycon




con = mycon.connect(host="localhost", user="root", password="root", database="om")
cur = con.cursor()






def menu():
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("|          POSTAL MANAGEMENT SYSTEM           |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("|  1.Sign In                                  |")
    print("|  2.About Us                                 |")
    print("|  3.Exit                                     |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    ch = input("Enter your choice:")
    if ch == '1':
        login()
    elif ch == '2':
        about_us()
    elif ch == '3':
        exit()
    else:
        print()
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|              INVALID INPUT                  |")
        print("|                                             |")
        print("|---------------------------------------------|")
        print()
        menu()





import pickle

f1 = open("admin.dat", 'ab')
rec = []
pickle.dump(rec, f1)
f1.close()
f = open("admin.dat", 'rb')
user = pickle.load(f)
f.close()

status = " "


def login():
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("|                 LOGIN SYSTEM                |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("| 1. - Yes                                    |")
    print("| 2. - No                                     |")
    print("| 3. - Reset Password                         |")
    print("| 4. - Quit                                   |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    status = input("Do you already have an existing user id?: ")
    if status == "1":
        old()
    elif status == "2":
        new()
    elif status == "3":
        resetpass()
    elif status == "4":
        menu()
    else:
        print()
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|                  INVALID INPUT              |")
        print("|                                             |")
        print("|---------------------------------------------|")
        print()
        login()





def old():
    import pickle
    f = open('admin.dat', 'rb')
    user = pickle.load(f)
    f.close()
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    a = 0
    for data in user:
        if username in data and password in data:
            mainmenu()
            a += 1

    if a == 0:
        print("User doesn't exist or password is incorrect!")
        login()





def new():
    new_name = input("Enter a Username: ")
    a = 0
    for data in user:
        if new_name in data:
            print("\nUsername already exists\n")
            login()
            a += 1
    if a == 0:
        new_pass = input("Enter a Password: ")
        data = [new_name, new_pass]
        user.append(data)
        f1 = open('admin.dat', 'wb')
        pickle.dump(user, f1)
        f1.close()
        print("\nRegistration Completed . Sign In Again\n")
        login()






def resetpass():
    file = open("admin.dat", 'rb+')
    username = input("Enter the username: ")
    file.seek(0)
    while True:
        position = file.tell()
        p1 = pickle.load(file)
        for i in p1:
            if i[0] == username:
                i[1] = input("Enter new password: ")
                file.seek(position)
                pickle.dump(p1, file)
                print("Password Succesfully Changed! Please Sign In Again")
                file.close()
                login()





def about_us():
    f = open("aboutus.txt",'r')
    a = f.read()
    print(a)
    menu()
    
    

def exit():
    f = open("exit.txt",'r')
    a = f.read()
    print(a)
    menu()



def mainmenu():
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                  MAIN MENU                  |")
    print("|                                             |")
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("| 1. Add Post                                 |")
    print("| 2. Edit Details                             |")
    print("| 3. See all the Details                      |")
    print("| 4. Log out                                  |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    ch = input("Enter your choice: ")
    if ch == '1':
        add_post()
    elif ch == '2':
        edit()
    elif ch == '3':
        see_cust_det()
    elif ch == '4':
        menu()
    else:
        print()
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|                  INVALID INPUT              |")
        print("|                                             |")
        print("|---------------------------------------------|")
        print()
        mainmenu()





def tracking():
    global l
    l = []
    cur.execute('select Tracking_ID from senderrs')
    data = cur.fetchall()
    track = data[-1][0]
    for i in data:
        l += (i[0],)
    for i in range(1, 1000):
        if i in l:
            continue
        else:
            l += (i,)
            track = i
        break
    return track






def add_post():
    track = tracking()
    t = l[-1]
    print('')
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|            ADDING SENDER'S DETAIL           |")
    print("|                                             |")
    print("|---------------------------------------------|")
    name = input("Enter sender's name: ")
    while True:
        mob = input("Enter mobile number: ")
        if not mob.isdigit():
            print("Enter only numbers\n")
            continue
        elif len(mob) != 10:
            print("Enter 10 digit number\n")
            continue
        else:
            break
    while True:
        Email_ID = input("Enter Email_ID: ")
        if "@" not in Email_ID:  
            print("Enter Valid Email_ID")
        else:
            break
    address = input("Enter the sender's address: ")
    cur.execute("insert into senderrs values({},'{}','{}','{}','{}')".format(t, name, mob, Email_ID, address))
    con.commit()
    print('')
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|            ENTER RECIEVER'S DETAIL          |")
    print("|                                             |")
    print("|---------------------------------------------|")
    name = input("Enter receiver's name: ")
    while True:
        mob = input("Enter mobile number: ")
        if not mob.isdigit():
            print("Enter only numbers\n")
            continue
        elif len(mob) != 10:
            print("Enter 10 digit number\n")
            continue
        else:
            break
    while True:
        Email_ID = input("Enter Email_ID: ")
        if "@" not in Email_ID:  
            print("Enter Valid Email_ID")
        else:
            break
    address = input("Enter the receiver's address: ")
    cur.execute("insert into reciever values({},'{}','{}','{}','{}')".format(t, name, mob,Email_ID, address))
    con.commit()
    print("|---------------------------------------------|")
    print("|                                             |")
    print('|    Your tracking number is ==>', track, '   |')
    print("|                                             |")
    print("|---------------------------------------------|")
    print('')
    date = input("Enter today's date(DD-MM-YYYY): ")
    with open("'{}'.csv".format(t), 'w+', newline='') as f:
        c = csv.writer(f)
        det = [['Track_ID', 'Date', 'Description'], [t + 0.1, date, 'Post added']]
        c.writerows(det)
    print('')
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|          Post added successfully            |")
    print("|                                             |")
    print("|---------------------------------------------|")
    print()
    print(" Sender's details ")
    cur.execute("select * from senderrs")
    data = cur.fetchall()
    h = ['Tracking ID', 'Name', 'Mobile', 'Email_ID', 'Address']
    for i in data:
        if i[0] == track:
            print(tabulate(data, headers=h, tablefmt='fancy_grid'))
    print(" Receiver's details ")
    cur.execute("select * from reciever")
    data = cur.fetchall()
    h = ['Tracking ID', 'Name', 'Mobile', 'Email_ID', 'Address']
    for i in data:
        if i[0] == track:
            print(tabulate(data, headers=h, tablefmt='fancy_grid'))
    mainmenu()






def edit():
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                   EDIT                      |")
    print("|                                             |")
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("|  1. Update Details                          |")
    print("|  2. Delete Details                          |")
    print("|  3. Go back to Mainmenu                     |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        update()
    elif ch == 2:
        delete()
    elif ch == 3:
        mainmenu()
    else:
        print()
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|                  INVALID INPUT              |")
        print("|                                             |")
        print("|---------------------------------------------|")
        print()
        edit()






def update():
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                   UPDATE                    |")
    print("|                                             |")
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("|  1. Senders details                         |")
    print("|  2. Receivers details                       |")
    print("|  3. Go back to Edit page                    |")
    print("|  4. Go back to Mainmenu                     |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    cs = input("Enter your choice: ")
    print()
    if cs == '1':
        n = input("Enter sender's name: ")
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|               SENDER'S DETAIL               |")
        print("|                                             |")
        print("|---------------------------------------------|")
        senderrs(n)
    elif cs == '2':
        n = input("Enter receiver's name: ")
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|              RECEIVER'S DETAIL              |")
        print("|                                             |")
        print("|---------------------------------------------|")
        receiver(n)
    elif cs == '3':
        edit()
    elif cs == '4':
        mainmenu()
    else:
        print()
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|                  INVALID INPUT              |")
        print("|                                             |")
        print("|---------------------------------------------|")
        print()
        update()







def search(n, v):
    h = ['Tracking ID', 'Name', 'Mobile', 'Email_ID', 'Address']
    if v == 's':
        cur.execute("select * from senderrs where name='{}'".format(n))
        data = cur.fetchall()
        if data != []:
            h = ['Tracking ID', 'Name', 'Mobile', 'Email_ID', 'Address']
            print(tabulate(data, headers=h, tablefmt='fancy_grid'))
        else:
            print()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                                             |")
            print("|            Sender's name not found          |")
            print("|            Try again!                       |")
            print("|                                             |")
            print("|                                             |")
            print("|---------------------------------------------|")
            print()
            update()
    elif v == 'r':
        cur.execute("select * from reciever where name='{}'".format(n))
        data = cur.fetchall()
        if data != []:
            h = ['Tracking ID', 'Name', 'Mobile', 'Email_ID', 'Address']
            print(tabulate(data, headers=h, tablefmt='fancy_grid'))
        else:
            print()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                                             |")
            print("|            Reciever's name not found        |")
            print("|            Try again!                       |")
            print("|                                             |")
            print("|                                             |")
            print("|---------------------------------------------|")
            print()
            update()






def senderrs(n):
    import mysql.connector as mycon
    con = mycon.connect(host="localhost", user="root", password="root", database="om")
    cur = con.cursor()
    search(n, 's')
    while True:
        d = {1: 'Name', 2: 'Mobile', 3: 'Email_ID', 4: 'Address', 5: 'Done Updating'}
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|               EDITING LINES                 |")
        print("|                                             |")
        print("|---------------------------------------------|")
        for i in d:
            print(' ' + str(i) + '.', d[i])
            print()
            print("---------------------------------------------")
            print()
        a = input("Enter your choice (number): ")
        if a == '1':
            nn = input("Enter the new name : ")
            cur.execute("update senderrs set Name='{}' where Name='{}'".format(nn, n))
            con.commit()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  UPDATED                    |")
            print("|                                             |")
            print("|---------------------------------------------|")

        elif a == '2':
            nmn = input("Enter the new mobile no. : ")
            cur.execute("update senderrs set Mobile='{}' where Name='{}'".format(nmn, n))
            con.commit()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  UPDATED                    |")
            print("|                                             |")
            print("|---------------------------------------------|")
        elif a == '3':
            ne = input("Enter the new Email_ID : ")
            cur.execute("update senderrs set Email_ID='{}' where Name='{}'".format(ne, n))
            con.commit()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  UPDATED                    |")
            print("|                                             |")
            print("|---------------------------------------------|")
        elif a == '4':
            na = input("Enter the new Address : ")
            cur.execute("update senderrs set Address='{}' where Name='{}'".format(na, n))
            con.commit()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  UPDATED                    |")
            print("|                                             |")
            print("|---------------------------------------------|")
        elif a == '5':
            update()
        else:
            print()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  INVALID INPUT              |")
            print("|                                             |")
            print("|---------------------------------------------|")
            print()
            senderrs(n)
        update()






def receiver(n):
    import mysql.connector as mycon
    con = mycon.connect(host="localhost", user="root", password="root", database="om")
    cur = con.cursor()
    search(n, 'r')
    while True:
        d = {1: 'Name', 2: 'Mobile', 3: 'Email_ID', 4: 'Address', 5: 'Done updating'}
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|              EDITING DETAILS                |")
        print("|                                             |")
        print("|---------------------------------------------|")
        for i in d:
            print(' ' + str(i) + '.', d[i])
        a = input("Enter your choice (number): ")
        print("---------------------------------------------")
        if a == '1':
            nn = input("Enter the new name : ")
            cur.execute("update reciever set Name='{}' where Name='{}'".format(nn, n))
            con.commit()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  UPDATED                    |")
            print("|                                             |")
            print("|---------------------------------------------|")
        elif a == '2':
            nmn = input("Enter the new mobile no. : ")

            cur.execute("update reciever set Mobile='{}' where Name='{}'".format(nmn, n))
            con.commit()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  UPDATED                    |")
            print("|                                             |")
            print("|---------------------------------------------|")
        elif a == '3':
            ne = input("Enter the new Email_ID : ")
            cur.execute("update reciever set Email_ID='{}' where Name='{}'".format(ne, n))
            con.commit()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  UPDATED                    |")
            print("|                                             |")
            print("|---------------------------------------------|")
        elif a == '4':
            na = input("Enter the new Address : ")
            cur.execute("update reciever set Address='{}' where Name='{}'".format(na, n))
            con.commit()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  UPDATED                    |")
            print("|                                             |")
            print("|---------------------------------------------|")
        elif a == '5':
            update()
        else:
            print()
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                  INVALID INPUT              |")
            print("|                                             |")
            print("|---------------------------------------------|")
            print()
            receiver(n)
        update()





def delete():
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                 DELETE DETAILS              |")
    print("|                                             |")
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("| 1. Delete by Tracking ID                    |")
    print("| 2. Delete by Name                           |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    ch = input("Enter your choice: ")
    if ch == '1':
        delete_by_trackID()
    elif ch == '2':
        delete_by_name()
    else:
        print()
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|                  INVALID INPUT              |")
        print("|                                             |")
        print("|---------------------------------------------|")
        print()
        delete()





def delete_by_trackID():
    t = int(input("Enter your tracking ID: "))
    cur.execute("delete from senderrs where Tracking_ID={}".format(t))
    con.commit()
    cur.execute("delete from reciever where Tracking_ID={}".format(t))
    con.commit()
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|              Record Deleted                 |")
    print("|                                             |")
    print("|---------------------------------------------|")
    edit()







def delete_by_name():
    n = input("Enter sender's name: ")
    cur.execute('select * from senderrs')
    data = cur.fetchall()
    for i in data:
        if i[1] == n:
            cur.execute("delete from senderrs where name='{}'".format(n))
            con.commit()
            t = i[0]
            cur.execute("delete from reciever where Tracking_ID={}".format(t))
            con.commit()
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|              Record Deleted                 |")
    print("|                                             |")
    print("|---------------------------------------------|")
    edit()







def see_cust_det():
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                   Details                   |")
    print("|                                             |")
    print("|---------------------------------------------|")
    print("|                                             |")
    print("|                                             |")
    print("| 1. See Sender's details                     |")
    print("| 2. See Receiver's details                   |")
    print("| 3. Go back to Mainmenu                      |")
    print("|                                             |")
    print("|                                             |")
    print("|---------------------------------------------|")
    c = int(input("Enter choice: "))
    if c == 1:
        n = input("Enter Sender's Name: ")
        cur.execute("select * from senderrs where name='{}'".format(n))
        data = cur.fetchall()
        if data != []:
            h = ['Tracking ID', 'Name', 'Mobile', 'Email_ID', 'Address']
            print(tabulate(data, headers=h, tablefmt='fancy_grid'))
            mainmenu()
        else:
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                                             |")
            print("|    Sender's name not found                  |")
            print("|    Try again                                |")
            print("|                                             |")
            print("|                                             |")
            print("|---------------------------------------------|")
            print()
            see_cust_det()
    elif c == 2:
        n = input("Enter Receiver's Name: ")
        cur.execute("select * from reciever where name='{}'".format(n))
        data = cur.fetchall()
        if data != []:
            h = ['Tracking ID', 'Name', 'Mobile', 'Email_ID', 'Address']
            print(tabulate(data, headers=h, tablefmt='fancy_grid'))
            mainmenu()
        else:
            print("|---------------------------------------------|")
            print("|                                             |")
            print("|                                             |")
            print("|    Reciever's name not found                |")
            print("|    Try again                                |")
            print("|                                             |")
            print("|                                             |")
            print("|---------------------------------------------|")
            print()
            see_cust_det()
    elif c == 3:
        mainmenu()
    else:
        print()
        print("|---------------------------------------------|")
        print("|                                             |")
        print("|                  INVALID INPUT              |")
        print("|                                             |")
        print("|---------------------------------------------|")
        print()
        see_cust_det()

menu()