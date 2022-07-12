from operator import truediv
import sqlite3


conn = sqlite3.connect('database.db')


print('opened db')


# conn.execute('CREATE TABLE links (long TEXT, short TEXT, ip TEXT, clicks INT)')

# conn.execute('DROP TABLE links')

long, short, ip, clicks = 'long', 'short', 'ipaddress', 0

# conn.execute('INSERT INTO links (long, short, ip, clicks) VALUES (?, ?, ?, ?)', (long, short, ip, clicks))



def add_link(long, short, ip, clicks):
    try:
        cur = conn.cursor()
        cur.execute('INSERT INTO links (long, short, ip, clicks) VALUES (?, ?, ?, ?);', (long, short, ip, clicks))
        conn.commit()
        return True
    except:
        conn.rollback()
        raise Exception('Error in insert operation')


def get_all_links():
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM links;')
        rows = cur.fetchall()
        return rows
    except:
        conn.rollback()
        raise Exception('Error in getting all links')


def delete_all_links():
    try:
        cur = conn.cursor()
        cur.execute('DELETE FROM links;')
        conn.commit()
        return True
    except:
        conn.rollback()
        raise Exception('Error in deleting all users')


def get_long_link(short):
    try:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM links WHERE short = "{short}";')
        rows = cur.fetchall()
        return rows[0]
    except:
        conn.rollback()
        raise Exception(f'Error in getting link for {short}')




# Delete single link
def delete_link(short):
    try:
        cur = conn.cursor()
        cur.execute(f'DELETE FROM links WHERE short = "{short}"')
        conn.commit()
        return True
    except:
        conn.rollback()
        raise Exception(f'Error in deleting link for {short}')




# Get links by ip
def get_links_by_ip(ip):
    try:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM links WHERE ip = "{ip}"')
        rows = cur.fetchall()
        return rows
    except:
        conn.rollback()
        raise Exception(f'Error in getting links for ip {ip}')




# Check if link exists already
def check_short_exists(short):
    try:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM links WHERE short = "{short}";')
        rows = cur.fetchall()
        if len(rows) == 0:
            return False
        else:
            return True
    except:
        conn.rollback()
        raise Exception(f'Error in asserting if short link exists {short}')




# Get number of clicks
def check_number_clicks(short):
    try:
        cur = conn.cursor()
        cur.execute(f'SELECT clicks FROM links WHERE short = "{short}"')
        rows = cur.fetchall()
        return rows[0][0]
    except:
        conn.rollback()
        raise Exception(f'Error in asserting number of clicks of {short}')





# Patch number of clicks
def add_clicked_to_link(short):
    try:
        current = check_number_clicks(short)
        cur = conn.cursor()
        cur.execute(f'UPDATE links SET clicks = {int(current)+1} WHERE short = "{short}"')
        conn.commit()
        return True
    except:
        conn.rollback()
        raise Exception(f'Error in updating the number of clicks of {short}')
    











# delete_all_links()

add_link('longest', 'shortest2', 'myip2', 1)

print(get_all_links())

print(check_number_clicks('shortest3'))

add_clicked_to_link('shortest3')

print(check_number_clicks('shortest3'))


# delete_link('shortest3')

# print(get_links_by_ip('myip2'))

# print(get_all_links())

# print(get_long_link('shortest2'))

# print('dropped')
