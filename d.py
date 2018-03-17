import  MySQLdb
db=MySQLdb.connect("localhost","","","stud15")
cursor = db.cursor()
cursor.execute("create table employe2(name char(20) not null,age int,sex char(1),income float)")
cursor.execute("insert into employe2 values('anna','24','f','20000')")
cursor.execute("insert into employe2 values('athira','22','f','30000')")
cursor.execute("insert into employe2 values('adhi','25','m','50000')")
cursor.execute("select * from employe2")
data=cursor.fetchall()
for i in data:
	print('{0:4}|{1}|{2}|{3}'.format(i[0],i[1],i[2],i[3]))
cursor.execute("update employe2 set name='anna' where age=24")
cursor.execute("select * from employe2")
data=cursor.fetchall()
for i in data:
	print('{0:4}|{1}|{2}|{3}'.format(i[0],i[1],i[2],1[3]))
cursor.execute("commit")
db.close()
