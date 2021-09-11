import telebot
import dados

token = dados.token
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def say_hello(message):
    chat_id = message.chat.id
    bot.sendmessage(chat_id, "Seja bem vindo a maior loja de consultaveis do telegram<br> User Oficial: @Kevin71 <br> Grupo Oficial: @revoada71")
 
bot.polling() 
    