import sqlite3

# SQLite Типы данных
# integer - целое число
# real - число с точкой
# text - текстовая строка

# insert into DB (столбец1,) values (Null, 'A Aagrh!');
# UPDATE таблица SET поле1 = значение1, поле2 = значение2 WHERE условие


class DataBase:
	def __init__(self, dbPath: str):
		self.conn = sqlite3.connect(dbPath)

	def createTable(self, NameTable: str, Values: list):
		# Values = ['field1 type1', 'field2 type2', ]
		self.NameTable = NameTable
		cursor = self.conn.cursor()

		TypeField = ', '.join(Values)
		script = f"CREATE TABLE {self.NameTable} ({TypeField})"
		cursor.execute(script)
		self.conn.commit()

	def insert(self, IdUser: int):
		cursor = self.conn.cursor()

		script = f"INSERT INTO {self.NameTable} (id, relevance) VALUES ({IdUser}, 'Y')"
		cursor.execute(script)
		self.conn.commit()

	def update(self, IdUser: int, Values: dict):
		# Values = {field1: value1, field2: value2}
		cursor = self.conn.cursor()

		for field, value in Values.items():
			if type(value) is str:
				script = f"UPDATE {self.NameTable} SET {field} = '{value}' WHERE relevance = 'Y' and id = {IdUser}"
			else:
				script = f"UPDATE {self.NameTable} SET {field} = {value} WHERE relevance = 'Y' and id = {IdUser}"
			cursor.execute(script)
			self.conn.commit()

	def selectRelevance(self, ColumnsName: list):
		# ColumnsName = [field1, field1, ]
		cursor = self.conn.cursor()

		columns = ', '.join(ColumnsName)
		script = f"SELECT {columns} FROM {self.NameTable} WHERE relevance = 'Y'"
		cursor.execute(script)
		self.conn.commit()
		return cursor.fetchall()

	def select(self, ColumnsName: list):
		# ColumnsName = [field1, field1, ]
		cursor = self.conn.cursor()

		columns = ', '.join(ColumnsName)
		script = f"SELECT {columns} FROM {self.NameTable}"
		cursor.execute(script)
		self.conn.commit()

		self.results = cursor.fetchall()
		return self.results

	def __del__(self):
		self.conn.close()

# Если программу запускаете впервые
DB = DataBase('test.db')
column_name = [
    'id integer',
    'name text'
]
DB.createTable('InfoOnUsers', column_name)
stroka = DB.select(['*'])
stroka

