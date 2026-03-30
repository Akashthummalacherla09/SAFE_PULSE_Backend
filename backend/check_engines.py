import pymysql
pymysql.install_as_MySQLdb()
import os

conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='safepulse_db')
cursor = conn.cursor()
cursor.execute("SELECT table_name, engine FROM information_schema.tables WHERE table_schema = 'safepulse_db'")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}")
conn.close()
