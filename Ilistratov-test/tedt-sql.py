# import sqlite3

# conn = sqlite3.connect("test.db")
# conn.execute("CREATE TABLE user_names(name TINYTEXT, handle TINYTEXT)")
# conn.commit()
# conn.execute('''INSERT INTO user_names VALUES('Ilia', 'Ilistratov')''')
# conn.execute('''INSERT INTO user_names VALUES('Kirill', 'ReDwile')''')
# conn.commit()
# c = conn.cursor()
# c.execute("SELECT name FROM user_names")
# print(c.fetchall()[0][0])
# conn.close()
