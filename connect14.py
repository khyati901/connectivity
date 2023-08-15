import mysql.connector as c

mydb=c.connect(
  host="localhost",
  user="root",
  password="root",
  database="admin"
)

cur = mydb.cursor()

id=int(input("Enter emp ID for deletion="))
      
cur.execute("delete from p1 where eid={}".format(id))
mydb.commit()
print("record deleted successfully")
 
