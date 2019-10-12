import pymysql
import pandas as pd
#established a connection with my server
db = pymysql.connect("localhost", "test", "test1", "engg_students")

print("**The connection to engg_students has been established**")

cursor = db.cursor()

cursor.execute("SELECT * FROM engstudb" )

data = cursor.fetchall()

df = pd.read_sql("SELECT * FROM engstudb LIMIT 30", db)


print(" A sample of the data is : \n", df)






