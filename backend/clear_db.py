import pymysql
pymysql.install_as_MySQLdb()

conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='safepulse_db')
cursor = conn.cursor()
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
cursor.execute("SHOW TABLES")
tables = [row[0] for row in cursor.fetchall()]
for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS `{table}`")
    print(f"Dropped {table}")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
conn.commit()
conn.close()
