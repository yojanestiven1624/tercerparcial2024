import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print ("Base de Datos de autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute
    ("""
    CREATE TABLE resource_totals (
    total_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER,
    total_budget DECIMAL(10,2),
    total_time_days INTEGER,
    resources_allocated TEXT,
    last_calculated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plan_id) REFERENCES strategic_plan(plan_id)
    ;)
    """)
    print("Tabla creada")
    conn.commit()
    conn.close()

if __name__== "__main__":
    #createDB()
    createTable()




