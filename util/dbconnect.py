import MySQLdb
import MySQLdb.cursors
from MySQLdb import escape_string as thwart
import os

data = open('/var/www/andrewbberger/andrewbberger/.key').read().strip()
child_data = open('/var/www/andrewbberger/andrewbberger/.child_key').read().strip()

def db_connection(db=''):
    conn = MySQLdb.connect(host='localhost',
                           user='andrew',
                           passwd=data,
                           db='andrewbberger'
                           )
    c = conn.cursor()
    return c, conn

def db_execute(statement, db='FX_OANDA', user='child'):
    conn = MySQLdb.connect(host='localhost',
                           user=user,
                           passwd=child_data,
                           db=db,
                           cursorclass=MySQLdb.cursors.DictCursor
                           )
    c = conn.cursor()
    try:
        c.execute(statement)
        conn.commit()

        return result
    except Exception as e:
        conn.rollback()
        return e
    finally:
        conn.close()

def db_log(username, ip, path):
    conn = MySQLdb.connect(host='localhost',
                           user='andrew',
                           passwd=data,
                           db='andrewbberger'
                           )
    c = conn.cursor()
    username = 'na' if not username else username
    try:
        c.execute("insert into log (username, ip, tracking) values (%s, %s, %s)",
                    (thwart(username), thwart(ip), thwart(path)))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        return e
    finally:
        conn.close()
    return False
    

if __name__ == '__main__':
    from sys import argv
    c, conn = db_connection()
    c.execute('SELECT username, email FROM users;')
    result = c.fetchall()
    for ret in result:
        print(ret)
