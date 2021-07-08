import psycopg2
import time
import datetime
import os

con = psycopg2.connect(
            host = os.environ['HOST'].rstrip(),  
            database = os.environ['DATABASE'].rstrip(),
            user = os.environ['USER'].rstrip(),
            password = os.environ['PASSWORD'].rstrip())
cur = con.cursor()

#cur.execute("CREATE TABLE employees (ID serial PRIMARY KEY, Name VARCHAR(255) UNIQUE NOT NULL)")
#cur.execute("INSERT INTO public.employees(ID,Name) values (1,'Dinesh')")
#cur.execute("SELECT * FROM public.employees;")

cur.execute("SELECT version();")
rows = cur.fetchall()

print(rows)

#print("Hello")
#for f in rows:
#    print(f[0], f[1])

cur.close()
con.close()

while True:
    time.sleep(30)
    print("Hello World",datetime.datetime.now())
