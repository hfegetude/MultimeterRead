import sqlite3

class DataBase(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.conn = sqlite3.connect('data.db')

	def InsertData(self, data, time):

		c = self.conn.cursor()
		# Insert a row of data
		c.execute("INSERT INTO MultiData VALUES (NULL ,?, ?)",[(data), (time),])
		# Save (commit) the changes
		self.conn.commit()
	
	def LastTime(self):
		c = self.conn.cursor()		
		c.execute("SELECT TIME FROM MultiData")
		return c.fetchall().pop()[0]

	def CloseDB(self):
		self.conn.close()

	def GetVol(self):
		c = self.conn.cursor()		
		c.execute("SELECT VOLT  FROM MultiData")
		return self.ToVectorVol(c.fetchall())

	def GetTime(self):
		c = self.conn.cursor()
		c.execute("SELECT TIME  FROM MultiData")
		return self.ToVectorTime(c.fetchall())

	def ToVectorTime(self, numbs):
		vect1 = list()
		while(len(numbs) > 0 ):
			vect1.append(numbs.pop()[0])
			
		return vect1

	def ToVectorVol(self, numbs):
		vect1 = list()
		while(len(numbs) > 0 ):
			vect1.append(float(numbs.pop()[0]))
			
		return vect1


