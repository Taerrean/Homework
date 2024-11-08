import sqlite3
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS email_idx ON Users (email)")

#for i in range(1, 11):
    #cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{str(i)}0", "1000"))
#for j in range(1, 11, 2):
    #cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{j}"))
#for k in range(1, 11, 3):
    #cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{k}",))
#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", ("60",))
#users = cursor.fetchall()
#for user in users:
    #print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

#cursor.execute(" DELETE FROM Users WHERE id = ?", (6, ))

cursor.execute(" SELECT COUNT(*) FROM Users")
acc_num = cursor.fetchone()[0]

cursor.execute(" SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]

avg = total_balance/acc_num
print(avg)


connection.commit()
connection.close()