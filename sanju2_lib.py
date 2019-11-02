import sqlite3
import datetime
from datetime import date,datetime

conn = sqlite3.connect('lib_db3.db')

cur = conn.cursor()

menu = '''
1.add user
2.add librarian
3.add books
4.update user details
5.update books details
6.delete user
7.delete books
8.read books details 
9.Submit your book.
10.list of books
'''
print(menu)
option = int(input("Enter your option: "))

if option == 1:
    personal_id=int(input("enter your personal id :"))
    name = input('enter name : ')
    password =input("enter your password :")
    contact = input("enter contact : ")
    fees = " "
    cur.execute('''INSERT INTO Users VALUES(?,?,?,?,?);''',[personal_id,name,password,contact,fees])
    
    
    print("Registration successful")
    
    print("##Register user details  is ###")
    
    cur.execute('''SELECT * FROM Users;''')
    ulist = cur.fetchall()
    for person_id in ulist:
        print(person_id)
        cur.execute('''SELECT * FROM Users;''')
        ulist = cur.fetchall() 

    

elif option == 2:
    name = input('enter name : ')
    contact = int(input("enter contact : "))
    Address=input("enter Address  :")

    cur.execute('''INSERT INTO Libararian VALUES(?,?,?);''',[name,Address,contact])
    print("Libararian Registerion Successful ")

elif option == 3:
    isbn_no = int(input("enter your isbn  number :"))
    name = input('enter book name : ')
    author = input('enter author name  : ')
    pubcompany = input('enter pubcompany : ')
    rdate = date(int(input('enter year:')),int(input('enter month:')),int(input('enter day:')))
    ruser = input('enter ruser : ')
    sdate = " "
    cur.execute('''INSERT INTO Books VALUES(?,?,?,?,?,?,?);''',[isbn_no,name,author,pubcompany,rdate,ruser,sdate])
    print("Book Add successful")

elif option ==4 :
    contact = input("enter your  new contact : ")
    name   = input("enter your new  name : ")
    person_id = int(input("enter  person id you want update  : "))
    cur.execute('''UPDATE Users SET contact = ? , name = ? WHERE person_id = ?;''',[contact,name,person_id])
    print("update Details Successfully")

elif option == 5:
    renteduser = input("enter new  renteduser : ")
    rdate = date(int(input('enter year:')),int(input('enter month:')),int(input('enter day:')))
    isbn_no = int(input("enter book isbn_no : "))
    cur.execute('''UPDATE Books SET Rented_User = ? , Rented_date = ? WHERE Isbn_no = ?;''',[renteduser,rdate,isbn_no])
    print("## update details Successfully ##")
    

elif option == 6:

    cur.execute('''SELECT person_id FROM Users;''')
    nplist = cur.fetchall()      #fetchall is uses for fetcha aal data from data base
    print(nplist)
    person_id = input("enter your personal id  :")
    np = (person_id)
    print(np)
    
    #if np in nplist:
    print('Welcome')
    person_id = input("enter person id  you want to delete : ")
    cur.execute('''DELETE FROM Users WHERE person_id = ?;''',[person_id])
    #else:
        #print("Register")

elif option == 7:
    Isbn_no = input("enter your  book  Isbn_no : ")
    cur.execute('''DELETE FROM Books WHERE Isbn_no = ?;''',[Isbn_no])
    print("Delete Successfully")

elif option == 8:
    isbn_no = input("enter your isbn number  : ")
    cur.execute('''SELECT * FROM Books WHERE Isbn_no = ?;''',[isbn_no])
    details = cur.fetchall()
    print(details)

elif option ==9:
    sdate = date(int(input('enter year:')),int(input('enter month:')),int(input('enter day:')))
    isbn_no =int(input("enter your book isbn no :"))
    cur.execute('''UPDATE Books SET Submit_Date=? WHERE Isbn_no =?''',[sdate,isbn_no])
    print("Book Submit")
elif  option == 10:
    cur.execute('''SELECT * FROM Books;''')
    book_list = cur.fetchall()
    for row in book_list:
        print(row)
        
        
cur.execute('''SELECT Rented_date,Rented_user,Submit_Date FROM Books;''')
book_list = cur.fetchall() 
#date and time print and rent cost of book 
tday = datetime.now() #using today date time import
for row in book_list:

        date_object = datetime.strptime(row[0], "%Y-%m-%d")
        if (tday - date_object).days > 14:
            print(row[0]+' has used the book for two weeks.')
        num_of_days=(tday-date_object).days

        i = 0

        if num_of_days>20:
            i += 20
        if num_of_days > 20 and num_of_days < 25:
            i += 0
        if num_of_days > 24 and num_of_days < 30:
            i += 25
        if num_of_days > 29 and num_of_days < 35:
            i += 30+25
        if num_of_days > 34 and num_of_days < 40:
            i += 30+25+35
        if num_of_days > 39 and num_of_days < 45:
            i += 30+25+35+40
            

        cur.execute('''UPDATE Users SET fees = ? WHERE name = ?;''',[i,row[0]])
        cur.execute('''SELECT * FROM Users WHERE name = ?;''',[row[0]])
        udetails = cur.fetchall()
        #print('updated : ', udetails)






conn.commit()
conn.close()


