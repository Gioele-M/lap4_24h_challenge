import sqlite3


conn = sqlite3.connect('database.db')


print('opened db')


# conn.execute('CREATE TABLE links (long TEXT, short TEXT, ip TEXT, clicks INT)')

# conn.execute('DROP TABLE links')

long, short, ip, clicks = 'long', 'short', 'ipaddress', 0

# conn.execute('INSERT INTO links (long, short, ip, clicks) VALUES (?, ?, ?, ?)', (long, short, ip, clicks))



def addLink(long, short, ip, clicks):
    try:
        cur = conn.cursor()
        cur.execute('INSERT INTO links (long, short, ip, clicks) VALUES (?, ?, ?, ?)', (long, short, ip, clicks))
        conn.commit()
        return True
    except:
        conn.rollback()
        raise Exception('Error in insert operation')


def getAllLinks():
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM links')
        rows = cur.fetchall()
        return rows
    except:
        conn.rollback()
        raise Exception('Error in getting all links')


def deleteAllLinks():
    try:
        cur = conn.cursor()
        cur.execute('DELETE FROM links')
        conn.commit()
        return True
    except:
        conn.rollback()
        raise Exception('Error in deleting all users')




addLink('longest', 'shortest', 'myip', 4)

# deleteAllLinks()
print(getAllLinks())

# print('dropped')
