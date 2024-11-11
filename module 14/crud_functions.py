import sqlite3
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')
    connection.commit()
    connection.close()
initiate_db()
#for i in range(1, 5):
        #cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f"Product{i}", f"Описание {i}", i * 100))
        #connection.commit()
def get_all_products(table_name):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    products = cursor.fetchall()
    connection.close()
    return products
connection.commit()
connection.close()
