import sqlite3 as s

conn = s.connect('tdb')
c = conn.cursor() 


## 테이블 만들고, 데이터 입력 
c.execute(" drop  table  if exists Man")
c.execute(" create table Man(name char(20), age int)")

c.execute(" insert into Man values('만수', 27) ")
c.execute(" insert into Man values('문수', 22) ")


## 데이터 가져오기 

c.execute(" select * from Score ")
rows = c.fetchall()
print(" ----------------------------")
print("  이 름   국어   영어   수학 ")
print(" ----------------------------")
for row in rows:
    print(" {}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3]))
print(" ----------------------------")

conn.commit()

c.close()
conn.close()
