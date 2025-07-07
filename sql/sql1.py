import pymysql
connection=pymysql.connect(
           host="127.0.0.1",
           user="root",
           password="252599"
)
cursor=connection.cursor()

cursor.execute("create database if not exists student_fulldet")
cursor.execute("use student_fulldet")
cursor.execute("drop table if exists student_d")
cursor.execute("create table if not exists student_d(id int primary key, name varchar(20), roll int, marks int)")
cursor.execute("insert ignore into student_d values(1,'Jenil', 10, 100),(2,'Jenil1',12,93)")




connection.commit()
cursor.close()
connection.close()


