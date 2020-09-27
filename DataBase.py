import sqlite3


class DateBase:
	def __init__(self, dbPath : str):
		self.connection = sqlite3.connect(dbPath)

	def InsertRow(self, tableName : str, columnValues: list):
		pass
		# ...
		# script = f"INSERT INTO VALUES({})"
		# self.connection.execute(script)

	def SelectColum(self, tableName : str, columns : list):
		pass
		# ...
		# script = f"SELECT {} FROM {tableName})"
		# self.connection.execute(script)

	def Test(self):
		c = self.connection.cursor()
		c.execute("SELECT * FROM x")
		print(c.fetchall())

	def __del__(self):
		self.connection.close()


data = DateBase("test.bd")
# data.connection.execute("CREATE TABLE x(test_val TINYTEXT)")
# data.connection.commit()
data.connection.execute("INSERT INTO x VALUES('test_text_val')")
data.connection.commit()
data.Test()

