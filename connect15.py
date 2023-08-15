import mysql.connector as c

mydb=c.connect(
  host="localhost",
  user="root",
  password="root",
  database="admin"
)
cur = mydb.cursor()
cur.execute("select * from p1")
data=cur.fetchone()
print(data)
print("Total no of rows=",cur.rowcount)
print("***********************")
data=cur.fetchmany(2)
print(data)
print("Total no of rows=",cur.rowcount)
data=cur.fetchone()
print(data)
print("Total no of rows=",cur.rowcount)
print("************fetchall***********")
data=cur.fetchall()
print(data)
print("Total no of rows=",cur.rowcount)
