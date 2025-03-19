import pymysql

class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password=input("Enter your password here"), #password to access the database
            database="billing_db"
        )
        self.cursor = self.conn.cursor()

    def insert_customer(self, name, phone, email):
        sql = "INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (name, phone, email))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_bill(self, customer_id, amount):
        sql = "INSERT INTO bills (customer_id, amount) VALUES (%s, %s)"
        self.cursor.execute(sql, (customer_id, amount))
        self.conn.commit()

    def fetch_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        return self.cursor.fetchall()

    def fetch_bills(self):
        self.cursor.execute("SELECT bills.id, customers.name, bills.amount, bills.date FROM bills JOIN customers ON bills.customer_id = customers.id")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
