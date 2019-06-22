import sqlite3
conn=sqlite3.connect('Database.db')
c=conn.cursor()
sql="""
DROP TABLE IF EXISTS User1;
CREATE TABLE User1 (
Id integer unique primary key autoincrement,
Name text);

"""
c.executescript(sql)
print('Table Created Successfully')
conn.commit()