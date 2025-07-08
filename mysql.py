import pymysql
def connection():
    connection=pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="12345678"
    )

    cursor=connection.cursor()
connection()
def create_database(connection, db_name):
    cursor.execute(f"create database if not exists {db_name}")
    cursor = connection.cursor()
def use_database(connection, db_name):
    cursor.execute(f"use {db_name}")
    cursor = connection.cursor()
def create_table(connection, db_name, table_name):
    cursor = connection.cursor()
    cursor.execute(f"drop table if exists {table_name}")
    cursor.execute(f'''create table if not exists {table_name}(order_id int primary key, customer_name varchar(20), product varchar(20), quantity int, price int) ''')


cursor.execute("insert ignore into shop values(1,'John','Apple', 10,5 ),(2,'Alice', 'Banana',5,2),(3,'John','Apple',15,5),(4,'Alice', 'Mango',3,10), (5,'John','Mango',2,10),(6,'Bob','Banana',7,2),(7,'Bob','Apple',8,5)")
cursor.execute("select * from shop")
cursor.execute("update shop set quantity = 3 where order_id=5")
cursor.execute("update shop set quantity = 4 where order_id=4")
cursor.execute("alter table shop rename column order_id to id")
cursor.execute("select * from shop")
cursor.execute("select product, sum(quantity) as SumOfQ from shop group by product")

items=cursor.fetchall()
for item in items:
    print(item)

connection.commit()
cursor.close()
connection.close()