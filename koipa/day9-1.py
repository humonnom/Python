import sqlite3 as s3
conn = s3.connect("tdb")
cursor = conn.cursor()

cursor.execute('DROP TABLE if exists Man')
cursor.execute( 'CREATE TABLE Man( name char(20), age int)' )

cursor.execute( "INSERT INTO Man values('철수', 25)" )
cursor.execute( "INSERT INTO Man values('영희', 22)" )

conn.commit()

cursor.close()
conn.close()
