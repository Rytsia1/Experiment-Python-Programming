import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        major TEXT
    )
""")

# Insert 5 student records
students = [
    ("Dio", 20, "Computer Science"),
    ("Fina", 22, "Mathematics"),
    ("Rifath", 21, "Physics"),
    ("Adel", 23, "Chemistry"),
    ("Jogi", 19, "Biology")
]
cursor.executemany("INSERT INTO student (name, age, major) VALUES (?, ?, ?)", students)
conn.commit()

# Query and print all students
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print("All students:")
for row in rows:
    print(row)

# Update age of student with name 'Fina' to 25
cursor.execute("UPDATE student SET age = 25 WHERE name = 'Fina'")
conn.commit()
print("\nAfter updating Fina's age:")
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

# Delete student with id = 3
cursor.execute("DELETE FROM student WHERE id = 3")
conn.commit()
print("\nAfter deleting id=3:")
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
