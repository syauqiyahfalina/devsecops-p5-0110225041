import sqlite3
from pathlib import Path
DATABASE_PATH=Path(__file__).with_name("store.db")

def get_connection():
    db=sqlite3.connect(DATABASE_PATH)
    db.row_factory=sqlite3.Row
    return db

def initialize_database():
    with get_connection() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,
            price INTEGER NOT NULL CHECK(price>=0),stock INTEGER NOT NULL CHECK(stock>=0))""")
        db.execute("""CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,customer_name TEXT NOT NULL,
            product_id INTEGER NOT NULL,quantity INTEGER NOT NULL CHECK(quantity>0),
            total INTEGER NOT NULL CHECK(total>=0),status TEXT NOT NULL)""")
        db.execute("""CREATE TABLE IF NOT EXISTS payments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,order_id INTEGER NOT NULL,
            method TEXT NOT NULL,amount INTEGER NOT NULL,status TEXT NOT NULL,reference TEXT NOT NULL)""")
        if db.execute("SELECT COUNT(*) FROM products").fetchone()[0]==0:
            db.executemany("INSERT INTO products(name,price,stock) VALUES(?,?,?)",[
                ("Buku",15000,20),("Pulpen",5000,50),("Tas Kanvas",45000,10)])
