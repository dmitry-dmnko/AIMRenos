import psycopg2

conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
cur = conn.cursor()

def create_table():
    conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tracker (FCID INTEGER"
                "                                   ,initial_date DATE"
                "                                   ,final_date DATE"
                "                                   ,delivery_date DATE"
                "                                   ,instalation_date DATE)")
    conn.commit()
    conn.close()


def insert(fcid, initial_date, final_date):
    conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO tracker VALUES(%s,%s,%s)", (fcid, initial_date, final_date))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tracker")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
    conn.commit()
    conn.close()

def create_aimuupd_table():
    conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS aim_update (FCID INTEGER"
                "                                       ,fc_name TEXT"
                "                                       ,marketing_designation TEXT"
                "                                       ,language_designation TEXT"
                "                                       ,fixture_code TEXT"
                "                                       ,fixture_name TEXT"
                "                                       ,zone TEXT"
                "                                       ,subzone TEXT"
                "                                       ,fixture_instance_priority INTEGER"
                "                                       ,within_10_feet BOOLEAN)")
    conn.commit()
    conn.close()

# insert('apple',5,10)
# delete('orange')
# update(20, 30, 'apple')

# print(view())
create_aimuupd_table()