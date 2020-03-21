import telebot
from telebot import types

bot = telebot.TeleBot('801147421:AAGKv4NMXvexN3Fq5wrbvr30w4ktbi9Guhk')

@bot.message_handler(commands=['start'])
def start(message):
    image = open("image/first_image.jpg", 'rb')
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_1 = types.KeyboardButton(text="/Playlist")
    button_2 = types.KeyboardButton(text="/Website")
    keyboard.add(button_1, button_2)
    bot.send_photo(message.chat.id, image)
    bot.send_message(message.chat.id, "В этом боте ты можешь послушать мой плейлист, на разных площадках\n\n"
                                      "Apple Music, Spotify\n\n"
                                      "А также можешь посетить мою веб-страницу нажав по ссылке Website!", reply_markup=keyboard)

@bot.message_handler(commands=['Playlist'])
def playlist(message):
    picture = open("image/second_image.jpg", 'rb')
    bot.send_photo(message.chat.id, picture,
                   caption="Apple music: https://music.apple.com/ru/playlist/lilartti-music/pl.u-V9D7mRksBMXo2L0 \n\n"
                    "Spotify: https://open.spotify.com/playlist/0wU98KEtjhCwLZVKyQYMSu?si=CrM3QqpDR86cUhA7e2275w")

@bot.message_handler(commands=['Website'])
def website(message):
    photo = open("image/jacko.jpg", 'rb')
    bot.send_photo(message.chat.id, photo, caption = "На этом сайте вы можете увидеть топ моих любимых исполнителей и изучить каждого, как в плане музыки так и биографии,"
                                              " а также прослушать плейлист собранный мной!\n\n"
                                              "Link: http://lilarttimusic.pythonanywhere.com/")


bot.polling()

