import telebot
import graph
import database
import matplotlib.pyplot as plt
import pylab
from telebot import types
bot = telebot.TeleBot("---")

markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('GetGraph')
itembtnb = types.KeyboardButton('GetDB')
markup.row(itembtna)
markup.row(itembtnb)
def SavePlotData(x_vector, y_vector):
	plt.plot(x_vector, y_vector)
	plt.ylabel('Voltage')
	plt.xlabel('Time')
	pylab.savefig('plot.png')


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):

	text = "Hola " + message.chat.first_name + " bienvenido al bot!"
	bot.reply_to(message, text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'GetGraph')
def handle_graph(message):
	db = database.DataBase()
	vol = db.GetVol()
	time = db.GetTime()

	SavePlotData(time, vol)
	db.CloseDB()
	graph = open('plot.png', 'rb')
	bot.send_photo(message.chat.id , graph, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'GetDB')
def handle_graph(message):
	db = database.DataBase()
	graph.SavePlotData(db.GetVol(), db.GetTime())
	db.CloseDB()
	base = open('data.db', 'rb')
	bot.send_document(message.chat.id , base, reply_markup=markup)



bot.polling()
