import mariadb
import sys

conf = {
        'host':'localhost',
        'port':3306,
        'user':'alice',
        'password':'pass',
        'database':'highlow'
        }

table_name = 'user'


# try:
conn = mariadb.connect(
        user=conf.get('user'),
        password=conf.get('password'),
        host=conf.get('host'),
        port=conf.get('port'),
        database=conf.get('database'),
        autocommit=True
        )
# except mariadb.Error as e:
    # print(f"Error connection to MariaDB platform: {e}")
    # sys.exit(1)


cur = conn.cursor()
