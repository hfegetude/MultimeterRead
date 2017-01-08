#!/usr/bin/python
import multimeter as mt
import database as db
import time
import sys



if (not len(sys.argv) == 2):
	print 'Yo my nigga, just giv me time.....'
	quit()
else:
	minutes = int(sys.argv[1])


multi = mt.Multimeter()

future = 0

while True:
	if(time.time() > future):
		dabase = db.DataBase()
		dabase.InsertData(multi.GetData() , time.time() )
		dabase.CloseDB()
		future = time.time() + 60*minutes


dabase.CloseDB()
multi.Close()

