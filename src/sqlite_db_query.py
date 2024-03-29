import sqlite3

def main():
    connection = sqlite3.connect("scratch.db")

    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS temp")
    cur.execute("CREATE TABLE IF NOT EXISTS temp ( a TEXT, b TEXT, c TEXT )")
    cur.execute("INSERT INTO temp VALUES('one','two','three')")
    cur.execute("INSERT INTO temp VALUES('four','five','six')")
    cur.execute("INSERT INTO temp VALUES('seven','eight','nine')")
    # connection.commit()

    cur.execute("SELECT * FROM temp")
    row = cur.fetchone()
    print(row)
    while row:
        row = cur.fetchone()
        print(row)

    cur.execute("DROP TABLE IF EXISTS temp")

    cur.close()   
    connection.commit()
    connection.close()

if __name__ =="__main__":
    main()