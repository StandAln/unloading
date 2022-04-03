import telebot
from telebot import types

bot = telebot.TeleBot('5185615037:AAEcb74wIg766GRsLcUZyHFpBGiFh-Lunno')


@bot.message_handler(commands=['start'])
def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard = True)

    menu.add(*[types.KeyboardButton(name) for name in ['Для чего необходимы выгрузки?', 'Какие выгрузки необходимы?']])
    menu.add(*[types.KeyboardButton(name) for name in ['Формат выгрузок', 'Обзор каждой выгрузки']])
    menu.add(*[types.KeyboardButton(name) for name in ['Автом-cкая проверка выгрузок', 'Дополнительные вопросы']])
    menu.add(*[types.KeyboardButton(name) for name in ['Пожелания и обратная связь']])
     
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Выбери интерусующую информацию в меню'.format(message.from_user), reply_markup=menu)

   
@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Для чего необходимы выгрузки?':
            submenu1 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            submenu1.add(*[types.KeyboardButton(name) for name in ['Абонентские выгрузки', 'Справочные выгрузки']])
            submenu1.add(*[types.KeyboardButton(name) for name in ['Выгрузки платежей', 'Выгрузки по соединениям']])
            submenu1.add(*[types.KeyboardButton(name) for name in ['В главное меню']])
            
            bot.send_message(message.chat.id, '573 Приказ,ASN, подменю с набором выгрузок', reply_markup=submenu1)
            
        elif message.text == 'Абонентские выгрузки':
            bot.send_message(message.chat.id, 'Назначение абонентских выгрузок и перечисление')
        elif message.text == 'Справочные выгрузки':
            bot.send_message(message.chat.id, 'Назначение справочных выгрузок и перечисление')
        elif message.text == 'Выгрузки платежей':
            bot.send_message(message.chat.id, 'Назначение выгрузок по платежам и перечисление')
        elif message.text == 'Выгрузки по соединениям':
            bot.send_message(message.chat.id, 'Назначение выгрузок по соединением и перечисление')
        
            
        elif message.text == 'Какие выгрузки необходимы?':
                       
            bot.send_poll(message.chat.id, 'Выбери предоставляемые услуги', ('ШПД без NAT и RADIUS','ШПД с NAT и/или RADIUS', 'Wi-Fi', 'ТфОП', 'VOIP', 'Мобильная связь'), False, allows_multiple_answers=True)
        
        
        
        elif message.text == 'Формат выгрузок':
            bot.send_message(message.chat.id, 'Описание формата файла,наполнения и имени файла')
        elif message.text == 'Обзор каждой выгрузки':
            bot.send_message(message.chat.id, 'Подменю по выгрузкам,с выводом инфы и с подменю полей с выводом инфы')
        elif message.text == 'Автом-cкая проверка выгрузок':
            bot.send_message(message.chat.id, 'Ссылка на jancheker')
        elif message.text == 'Дополнительные вопросы':
            bot.send_message(message.chat.id, 'Подменю на абонентов Wi-Fi,физиков за юриков, куда и с каким интервалом выкладывать')
        elif message.text == 'Пожелания и обратная связь':
            bot.send_message(message.chat.id, 'Почта january.crm')

        elif message.text == 'В главное меню':
            menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
            menu.add(*[types.KeyboardButton(name) for name in ['Для чего необходимы выгрузки?', 'Какие выгрузки необходимы?']])
            menu.add(*[types.KeyboardButton(name) for name in ['Формат выгрузок', 'Обзор каждой выгрузки']])
            menu.add(*[types.KeyboardButton(name) for name in ['Автом-cкая проверка выгрузок', 'Дополнительные вопросы']])
            menu.add(*[types.KeyboardButton(name) for name in ['Пожелания и обратная связь']])
            bot.send_message(message.chat.id, 'Главное меню', reply_markup=menu)
 
 
 
@bot.poll_answer_handler() 
def bot_poll(poll_answer: types.PollAnswer):
    #print(poll_answer)
    if poll_answer == 'VOIP':
        print('Правильно!')
    else:
        print('Неправильно!')
 
        
bot.polling(none_stop = True)
    