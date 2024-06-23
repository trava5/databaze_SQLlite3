import sqlite3

connection = sqlite3.connect("test.db")

print(connection.total_changes)

cursor = connection.cursor()

# cursor.execute("CREATE TABLE kokot (name TEXT, species TEXT, tank_number INTEGER)")

cursor.execute("INSERT INTO fish VALUES ('Dammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

rows1 = cursor.execute("SELECT name, species, tank_number FROM kokot").fetchall()
print(rows)

print(connection.total_changes)