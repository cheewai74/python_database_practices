import sqlite3

def main():
    db = sqlite3.connect("D:\git\python_database_practices\db\scratch.db")
    cur = db.cursor()
  
    cur.execute("DROP TABLE IF EXISTS temp")
    cur.execute("CREATE TABLE IF NOT EXISTS temp ( a TEXT, b TEXT, c TEXT )")
    cur.execute("INSERT INTO temp VALUES('one','two','three')")
    cur.execute("INSERT INTO temp VALUES('four','five','six')")
    cur.execute("INSERT INTO temp VALUES('seven','eight','nine')")
    db.commit()

    cur.execute("SELECT * FROM temp")
    row = cur.fetchone()
    print(row)
    while row:
        row = cur.fetchone()
        print(row)

    cur.execute("DROP TABLE IF EXISTS temp")
    cur.close()
    db.close()

    if __name__ =="__main__":
        main()