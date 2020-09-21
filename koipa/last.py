## 텍스트 파일을 읽어 데이터 베이스에 넣기 

import sqlite3 as s

conn = s.connect('koipa')
c = conn.cursor() 


### sqlite에서 실행 할 것 
### sqlite> .open c:\\dd\\ydb
### sqlite> CREATE TABLE Score(name CHAR(20), kor INT, eng INT, mat INT);
### sqlite에  data import 하기 
### sqlite>  .import  c:\\dd\\ss.txt  Score  


## 데이터 가져오기 

#c.execute(" SELECT * FROM Score ")
rows = c.fetchall()
print(" ----------------------------")
print("  이 름   국어   영어   수학 ")
print(" ----------------------------")

for row in rows:    
    print(" {}\t{}\t{}\t{}\t".format(row[0], row[1], row[2], row[3]))
print(" ----------------------------")


### UPDATE 후 다시 읽어 오기 


c.execute(" ALTER TABLE Score ADD total INT ")
c.execute(" ALTER TABLE Score ADD avg FLOAT ")

for row in rows:
    name = row[0]
    kor = row[1]
    eng = row[2]
    mat = row[3]
    total = kor + mat + eng
    avg = total / 3 
    c.execute(" UPDATE Score SET total = (?), avg = (?) WHERE name = (?)", (total, avg, name))
conn.commit()

print(" \n  *** UPDATE 후 출력 ***  ")
print(" --------------------------------------------")
print("  이 름   국어   영어   수학   총점    평균  ")
print(" --------------------------------------------")

for row in rows:    
    print(" {}\t{}\t{}\t{}\t{}\t{:.1f}".format(row[0], row[1], row[2], row[3], row[4], row[5]))  
print(" --------------------------------------------")


conn.commit()
c.close()
conn.close()
