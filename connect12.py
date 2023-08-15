import mysql.connector as c

mydb=c.connect(
  host="localhost",
  user="root",
  password="root",
  database="admin"
)

cur = mydb.cursor()
while True:
 id=int(input("Enter emp ID="))
 nm=input("Enter emp name=")      
 cur.execute("insert into p1 values({},'{}')".format(id,nm))
 mydb.commit()
 print("Insert record successfully")
 x=int(input("Press 1 for more entry \nPress 2 for exit \n Enter the choice="))
 if x==2:
     break
