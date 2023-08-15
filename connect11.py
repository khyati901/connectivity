import mysql.connector as c

mydb=c.connect(
  host="localhost",
  user="root",
  password="root",
  database="admin"
)

cur = mydb.cursor()
id=int(input("Enter emp ID="))
nm=input("Enter emp name=")      
cur.execute("insert into p1 values({},'{}')".format(id,nm))
mydb.commit()
print("Insert data record successfully")
