import telebot
from telebot import types





bot = telebot.TeleBot('6088848645:AAGXuio8eEIACIXmzqlcgueAll-wT9RmBTI')



@bot.message_handler(commands=['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Привет👋')
    markup.add(btn1)
    bot.send_message(message .chat.id, 'Привет, здесь ты можешь подтянуть свой английский , нажми кнопку что бы начать!', reply_markup=markup)



@bot.message_handler(content_types=['text'])

def text(message):
    if message.text == 'Привет👋':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=4)
        btn1 = types.KeyboardButton(text='Новые слова📕')
        btn2 = types.KeyboardButton(text='Глаголы🚗')
        btn3 = types.KeyboardButton(text='Времена🕙')
        btn4 = types.KeyboardButton(text='Правила✊')
        btn5 = types.KeyboardButton(text='Произношение🗣')
        btn6 = types.KeyboardButton(text='Переводчик🔄')
        btn7 = types.KeyboardButton(text='Сайт изучение📱')
        btn8 = types.KeyboardButton(text='Информацияℹ️')
        kb.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8)
        bot.send_message(message.chat.id,'''    
Новые слова - список слов для словарного запаса
--------------------------------------------
Глаголы - список глаголов в каждом времени
--------------------------------------------
Правила - базовые правила английского языка
--------------------------------------------
Информация - автор , цель создания и тд ''',reply_markup=kb)

    elif message.text == 'Новые слова📕' :

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        btn1 = types.KeyboardButton(text='Существительные📕')
        btn2 = types.KeyboardButton(text='Прилагательные📗')
        btn3 = types.KeyboardButton(text='Предлоги📙')
        btn4 = types.KeyboardButton(text='Союзы📘')
        btn5 = types.KeyboardButton(text='Обратно⏪')
        markup1.add(btn1,btn2,btn3,btn4,btn5)
        bot.send_message(message.chat.id, 'Выбери какие новые слова хочешь увидеть! ', reply_markup=markup1)

    elif message.text == 'Существительные📕':
        file = open('Телеграмм бот/Newword1.png', 'rb')
        bot.send_photo(message.chat.id, file, '📕Существительные📕')

    elif message.text == 'Прилагательные📗':
        file = open('Телеграмм бот/Newword2.png', 'rb')
        bot.send_photo(message.chat.id, file, '📗Прилагательные📗')

    elif message.text == 'Предлоги📙':
        file = open('Телеграмм бот/Newword3.png', 'rb')
        bot.send_photo(message.chat.id, file, '📙Предлоги📙')

    elif message.text == 'Союзы📘':
        file = open('Телеграмм бот/Newword4.png', 'rb')
        bot.send_photo(message.chat.id, file, 'Союзы📘')

    elif message.text == 'Обратно⏪':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton(text='Новые слова📕')
        btn2 = types.KeyboardButton(text='Глаголы🚗')
        btn3 = types.KeyboardButton(text='Времена🕙')
        btn4 = types.KeyboardButton(text='Правила✊')
        btn5 = types.KeyboardButton(text='Произношение🗣')
        btn6 = types.KeyboardButton(text='Переводчик🔄')
        btn7 = types.KeyboardButton(text='Сайт изучение📱')
        btn8 = types.KeyboardButton(text='Информацияℹ️')
        kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, '''
Новые слова - список слов для словарного запаса
--------------------------------------------
Глаголы - список глаголов в каждом времени
--------------------------------------------
Правила - базовые правила английского языка
--------------------------------------------
Информация - автор  ''', reply_markup=kb)



    elif message.text == 'Глаголы🚗' :
        file = open('Телеграмм бот/Verbs.png', 'rb')
        bot.send_photo(message.chat.id, file, '🚗Глаголы всех времен🚗')


    elif message.text == 'Правила✊' :
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(text='Much/Many⛄️💧')
        btn2 = types.KeyboardButton(text='This/These☘️🌎')
        btn3 = types.KeyboardButton(text='At/In/On время🕐🕔')
        btn4 = types.KeyboardButton(text='At/In/On место🌆🌃')
        btn5 = types.KeyboardButton(text='Обратно⏪')
        markup1.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Выбери какие новые слова хочешь увидеть! ', reply_markup=markup1)

    elif message.text == 'Much/Many⛄️💧':
        file = open('Телеграмм бот/Rule.png', 'rb')
        bot.send_photo(message.chat.id, file, '⛄️💧Much/Many⛄️💧')

    elif message.text == 'This/These☘️🌎':
        file = open('Телеграмм бот/rule2.png', 'rb')
        bot.send_photo(message.chat.id, file, '☘️🌎This/These that/those☘️🌎')

    elif message.text == 'At/In/On время🕐🕔':
        file = open('Телеграмм бот/rule3.png', 'rb')
        bot.send_photo(message.chat.id, file, '🕐🕔At/In/On Время🕐🕔')

    elif message.text == 'At/In/On место🌆🌃':
        file = open('Телеграмм бот/rule4.png', 'rb')
        bot.send_photo(message.chat.id, file, '🌆🌃At/In/On место🌆🌃')

    elif message.text == 'Обратно⏪':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton(text='Новые слова📕')
        btn2 = types.KeyboardButton(text='Глаголы🚗')
        btn3 = types.KeyboardButton(text='Времена🕙')
        btn4 = types.KeyboardButton(text='Правила✊')
        btn5 = types.KeyboardButton(text='Произношение🗣')
        btn6 = types.KeyboardButton(text='Переводчик🔄')
        btn7 = types.KeyboardButton(text='Сайт изучение📱')
        btn8 = types.KeyboardButton(text='Информацияℹ️')
        kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, '''Новые слова - список слов для словарного запаса
--------------------------------------------
Глаголы - список глаголов в каждом времени
--------------------------------------------
Правила - базовые правила английского языка
--------------------------------------------
Информация - автор , цель создания и тд ''', reply_markup=kb)

    elif message.text == 'Времена🕙':
        file = open('Телеграмм бот/time.png', 'rb')
        bot.send_photo(message.chat.id,file,'🕙Времена английского языка🕙')

    elif message.text == 'Произношение🗣':
        file = open('Телеграмм бот/proiznoshenie.mp4', 'rb')
        bot.send_video(message.chat.id, file, '🗣Произношение🗣')

    elif message.text == 'Переводчик🔄':
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='🔄Переводчик🔄', url='https://translate.google.ru/')
        kb.add(btn1)
        bot.send_message(message.chat.id, '🔄Гугл Переводчик🔄', reply_markup=kb)


    elif message.text == 'Сайт изучение📱':

        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Сайт📱', url='https://test-english.com/grammar-points/a1/')
        kb.add(btn1)
        bot.send_message(message.chat.id,'📱Сайт для изучения языка📱',reply_markup=kb)


    elif message.text == 'Информацияℹ️' :
        bot.send_message(message.chat.id,'''Автор - @MeowGavGavgav
Здесь у тебя не получится выучить английский , но он может тебе не забыть английский , и припоминать информацию! ''')








bot.polling()
