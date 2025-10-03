import psycopg2

# PostgreSQL default database (postgres) se connect ho rahe hain
conn = psycopg2.connect(
    dbname="postgres",        # default DB se connect karte hain database create karne ke liye
    user="postgres",          # tera PostgreSQL user
    password="@Ayushi1610",   # tera password
    host="localhost",
    port="5432"
)

conn.autocommit = True
cursor = conn.cursor()

# Naya database create karna
cursor.execute("CREATE DATABASE my1project;")

cursor.close()
conn.close()

print("✅ Database 'my1project' created successfully!")
