import sqlite3
import random

connection = sqlite3.connect("test.db")

n = 1000000
tuples = list()
for _ in range(n):
    a = 2500 * random.random()
    b = 2500 * random.random()
    tuples.append((a, b))

sql = "INSERT INTO Reals (A, B) VALUES (?, ?)"
with connection as cur:
    cur.executemany(sql, tuples)

tuples = list()
for _ in range(n):
    a = int(2500 * random.random())
    b = int(2500 * random.random())
    tuples.append((a, b))

sql = "INSERT INTO Integers (A, B) VALUES (?, ?)"
with connection as cur:
    cur.executemany(sql, tuples)


    