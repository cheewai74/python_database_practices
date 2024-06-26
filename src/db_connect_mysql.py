import mysql.connector as mysql

def main():
    db = mysql.connect(host="127.0.0.1", user="root", password="password")
    cur = db.cursor()

    cur.execute("SELECT VERSION()")
    version = cur.fetchone()[0]
    print(f"MariaDB MYSQL version {version}")

    cur.close()
    db.close()

if __name__=="__main__":
    main()