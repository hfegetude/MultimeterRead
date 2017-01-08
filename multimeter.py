import serial


class Multimeter:
	"""docstring for ClassName"""
	def __init__(self):
		self.ser = serial.Serial('/dev/ttyUSB0', baudrate = 1200, bytesize = 7, stopbits=2, parity='N',timeout=5)

	def Parse(self, byte_string):
		if len(byte_string) == 10:
			return byte_string[3:8]
		elif len(byte_string) == 11:
			return byte_string[3:9]
		else:
			return '0.000'

	def GetData(self):
		self.ser.write('\n')
		byte_string = ''
		byte = self.ser.read(1)
		if (byte ==''):
			return '-100'

		while(not byte =='\r'  ):
			byte_string = byte_string + byte
			byte = self.ser.read(1)
			if (byte == ''):
				return 'MM disconnected'
		print byte_string
		return self.Parse(byte_string)

	def Close(self):
		self.ser.close()



		


