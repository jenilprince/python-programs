import pymysql

def connect_to_database():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="12345678",
    )

def setup_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS new_database")
    cursor.execute("USE new_database")
    cursor.execute("DROP TABLE IF EXISTS data_table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data_table (
            id INT PRIMARY KEY,
            name VARCHAR(20),
            product VARCHAR(20),
            quantity INT,
            price INT
        )
    """)

def insert_items(cursor):
    m = int(input("Enter the number of items you want: "))
    for i in range(1, m + 1):
        id1 = int(input(f"Enter id {i}: "))
        name1 = input(f"Enter name {i}: ")
        product1 = input(f"Enter product {i}: ")
        quantity1 = int(input(f"Enter quantity {i}: "))
        price1 = int(input(f"Enter price {i}: "))

        cursor.execute(
            "INSERT IGNORE INTO data_table VALUES (%s, %s, %s, %s, %s)",
            (id1, name1, product1, quantity1, price1)
        )

def fetch_by_id(cursor):
    inp = int(input("Enter ID to search: "))
    cursor.execute("SELECT * FROM data_table WHERE id = %s", (inp,))
    items = cursor.fetchall()
    for row in items:
        print(row)

def main():
    connection = connect_to_database()
    cursor = connection.cursor()

    setup_database(cursor)
    insert_items(cursor)
    fetch_by_id(cursor)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
