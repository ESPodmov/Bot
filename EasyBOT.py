import telebot
import time
import random

token = "1900972483:AAEZZWV9DVAIy1yRCws7NL4pZoo3sH4CBk4"

bot = telebot.TeleBot(token)

HELP = """/signup - записаться на процедуру
/instagram - инстаграм студии
/products - продукты от Екатерины Подымовой
/educationinfo - информация про обучение
/channel_master - канал для мастеров перманентного макияжа
/channel_customer - канал для клиентов со скидками и акциями"""


#кнопки возврата
relpy_btn_back_to_main_menu = telebot.types.KeyboardButton("Вернуться в главное меню ↩")
relpy_btn_back_to_products_menu = telebot.types.KeyboardButton("Вернуться к списку продуктов ↩")


#инлайн кнопки соц сетей и сайтов
inline_btn_instagram = telebot.types.InlineKeyboardButton("Instagram📱", url = "https://www.instagram.com/permanent_podymova")
inline_kb_instagram = telebot.types.InlineKeyboardMarkup().add(inline_btn_instagram)
inline_btn_whatsapp = telebot.types.InlineKeyboardButton("WhatsApp📱", url = "https://wa.me/79272362721")
inline_kb_whatsapp = telebot.types.InlineKeyboardMarkup().add(inline_btn_whatsapp)
inline_btn_education = telebot.types.InlineKeyboardButton("Учитесь у нас🎓", url = "https://ufapermanent.ru")
inline_kb_education = telebot.types.InlineKeyboardMarkup().add(inline_btn_education)


#да нет для обучения
reply_btn_no = telebot.types.KeyboardButton("Нет😔")# смайлики
reply_btn_yes = telebot.types.KeyboardButton("Да‼️")# смайлики


#раздел продуктов
reply_kb_yes_no = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(reply_btn_yes, reply_btn_no).add(relpy_btn_back_to_main_menu)
reply_btn_book = telebot.types.KeyboardButton("Энциклопедия по перманентному макияжу📚")# кнопка книги
reply_kb_products = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(reply_btn_book).add(relpy_btn_back_to_main_menu)# таблица продуктов


#да нет для книги
reply_btn_no_for_products = telebot.types.KeyboardButton("Нет😞")# смайлики
reply_btn_yes_for_products = telebot.types.KeyboardButton("Да🤩")# смайлики
reply_kb_yes_no_for_products = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(reply_btn_yes_for_products, reply_btn_no_for_products).add(relpy_btn_back_to_products_menu).add(relpy_btn_back_to_main_menu)


# процедура книги
def book_answerer(message):
    doc = open('PM book trial.docx', 'rb')
    bot.send_document(message.chat.id, doc, caption='Этот файл специально для вас!')
    bot.send_message(message.chat.id, '{}, вас заинтересовала пробная книга?🤔'.format(message.from_user.first_name), reply_markup=reply_kb_yes_no_for_products)


# кнопки старта
reply_btn_instagram = telebot.types.KeyboardButton("Инстаграм студии😇")
reply_btn_signup = telebot.types.KeyboardButton("Записаться на процедуру👀")
reply_btn_products = telebot.types.KeyboardButton("Продукты от Екатерины Подымовой💄")
reply_btn_education = telebot.types.KeyboardButton("Обучение в студии🤓")
reply_btn_channel_master = telebot.types.KeyboardButton("Канал для мастеров перманентного макияжа🎓")
reply_btn_channel_customer = telebot.types.KeyboardButton("Канал со скидками и акциями для клиентов😮")
reply_kb_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add(reply_btn_signup).add(reply_btn_instagram).add(reply_btn_products).add(reply_btn_education).add(reply_btn_channel_master).add(reply_btn_channel_customer)


#кнопки чата для мастеров
reply_btn_try_luck = telebot.types.KeyboardButton("Испытать удачу🍀")
reply_btn_get_straight_access = telebot.types.KeyboardButton("Доступ к каналу➡")
reply_kb_chat_master = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add(reply_btn_try_luck).add(reply_btn_get_straight_access).add(relpy_btn_back_to_main_menu)
inline_btn_master_channel = telebot.types.InlineKeyboardButton("Channel⤴", url = "https://t.me/joinchat/ReYHETpYZb9_HIG4")
inline_kb_master_channel = telebot.types.InlineKeyboardMarkup().add(inline_btn_master_channel)


#кнопки для клиентов
reply_btn_customer_1 = telebot.types.KeyboardButton("1️⃣")
reply_btn_customer_2 = telebot.types.KeyboardButton("2️⃣")
reply_btn_customer_3 = telebot.types.KeyboardButton("3️⃣")
relpy_kb_answers = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).row(reply_btn_customer_1, reply_btn_customer_2, reply_btn_customer_3).add(relpy_btn_back_to_main_menu)
reply_btn_answer_the_question = telebot.types.KeyboardButton("Ответить на вопрос🤓")
reply_kb_answer_the_question = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add(reply_btn_answer_the_question).add(relpy_btn_back_to_main_menu)
inline_btn_customer_channel = telebot.types.InlineKeyboardButton("Channel⤴", url = "https://t.me/joinchat/xIqmqolZDRBjNzE6")
inline_kb_customer_channel = telebot.types.InlineKeyboardMarkup().add(inline_btn_customer_channel)


#процедура ссылки на чат с мастерами
def channel_master_access(message):
    bot.send_message(message.chat.id, "Здесь вы сможете найти полезные советы и лайфхаки по перманетному макияжу😉", reply_markup=inline_kb_master_channel)
    bot.send_message(message.chat.id, "Будем рады увидеть вас в нашем канале🤗", reply_markup=reply_kb_start)


#процедура удачи
def try_your_luck(message):
    number = random.randint(1, 10000)
    control_number = random.randint(1, 10000)
    if number == control_number:
        doc_full = open('PM full book.docx', 'rb')
        lucky_message = """Вау, вот это удача🤯🥴
С такими как вы можно и разориться📉"""
        bot.send_message(message.chat.id, lucky_message)
        bot.send_document(message.chat.id, doc_full, caption="А вот и ваша книга😌")
        bot.send_message(message.chat.id, "Ну и конечно ваша ссылка на канал для мастеров🤫", reply_markup=inline_kb_master_channel)
        bot.send_message(message.chat.id, "Будем рады увидеть вас в нашем канале🤗", reply_markup=reply_kb_start)
    else:
        hah_number = random.randint(1, 40)
        if hah_number == 4:
            text = """Не повезло😜
Кхм, простите за эмоции🤐"""
            bot.send_message(message.chat.id, text)
        elif hah_number == 6:
            text_1 = """Хе-хе-хе😛
Да что со мной🤕"""
            bot.send_message(message.chat.id, text_1)
        else:
            bot.send_message(message.chat.id, "Пока не повезло")


#процедура вопроса
def question(message):
    bot.send_photo(message.chat.id, open('photo1.jpeg','rb'), "1️⃣")
    bot.send_photo(message.chat.id, open('photo2.jpeg','rb'), "2️⃣")
    bot.send_photo(message.chat.id, open('photo3.jpeg','rb'), "3️⃣")
    bot.send_message(message.chat.id, "Какая из работ лучше?🧐", reply_markup=relpy_kb_answers)# дописать добавив фото, потом объявиьт все текста в обработке текстов

#процедура ответа
def answer(message):
    text = "Верно, это лучшая работа, как и остальные две😏"
    bot.send_message(message.chat.id, text) #   тут должна быть ссылка на чат с клиентами
    time.sleep(3)
    text_new = "А вот и ваша ссылочка на чат😇"
    bot.send_message(message.chat.id, text_new, reply_markup=inline_kb_customer_channel)
    bot.send_message(message.chat.id, "Будем рады увидеть вас в нашем канале🤗", reply_markup=reply_kb_start)

#хендлер для start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте, {}, я бот студии Екатерины Подымовой, я помогу вам найти то, что вы ищете😇".format(message.from_user.first_name), reply_markup=reply_kb_start)

#хендлер для help
@bot.message_handler(commands=["help"])# help обработчик
def help_answerer(message):
    bot.send_message(message.chat.id, HELP)

#хендлер для sign up
@bot.message_handler(commands=["signup"])# обработчик записей
def sign_up_answerer(message):
    ANSWER = """❗️Для записи позвоните по номеру:
    +79272362721📞
    Либо перейдите по ссылке:"""
    bot.send_message(message.chat.id, ANSWER, reply_markup=inline_kb_whatsapp)

#хендлер для instagram
@bot.message_handler(commands=["instagram"])# обработчик команды инстаграм
def instagram_answerer(message):
    bot.send_message(message.chat.id, "Здесь вы можете увидеть работы мастера🥰", reply_markup=inline_kb_instagram)

#хендлер для products
@bot.message_handler(commands=["products"])# обработчик комманды продукты
def products_answerer(message):
    bot.send_message(message.chat.id, "Здесь вы можете ознакомиться с нашими обучающими материалами и продуктами🤫", reply_markup=reply_kb_products)

#хендлер для education info
@bot.message_handler(commands=["educationinfo"])
def education_info_answerer(message):
    info = """В нашей школе вы сможете получить:

Бесценный опыт и навыки, приобретёте новую престижную творческую профессию. Откроются новые горизонты - возможность заниматься любимым делом, в удобном для вас режиме, и открытие собственного бизнеса.Обучение в режиме non stop: большой объём теоретической информации в сжатые сроки. И очень много практики В нашем деле, без практики, невозможно стать хорошим специалистом Поэтому, занятия проводятся энергично, без воды, только конкретные знания, навыки."""
    bot.send_message(message.chat.id, info)
    time.sleep(5)
    bot.send_message(message.chat.id, "Заинтересовало ли вас наше предложение?🧐", reply_markup=reply_kb_yes_no)

#хендлер для channel_master
@bot.message_handler(commands=["channel_master"])
def channel_master_answerer(message):
    text_message = "Мастер перманентного макияжа должен быть смелым, решительным, а главное настойчивым и терпеливым❗❗❗"
    bot.send_message(message.chat.id, text_message)
    time.sleep(2)
    text_message_2 = """Поэтому мы предлагаем испытать ваши терпение и удачу🤯
Испытать удачу🍀 - у вас будет возможность с шансом 1/10000 получить Энциклопедию по перманентному макияжу📚 стоимостью в 3500 рублей абсолютно бесплатно🤑(количество попыток неограничено) и получить доступ к каналу для мастеров по преманетному макияжу
Доступ к каналу➡ - прямая ссылка на канал для мастеров перманентного макияжа"""
    bot.send_message(message.chat.id, text_message_2, reply_markup=reply_kb_chat_master)

#хендлер для channel_customer
@bot.message_handler(commands=["channel_customer"])
def channel_customer_answerer(message):
    text_message = """Наш клиент должен иметь чувство стиля и красоты💫
Мы должны удостовериться, что вы именно тот клиент, которого мы ищем, поэтому прежде чем получить доступ в уникальный канал, вы должны ответить на один вопрос😉"""
    bot.send_message(message.chat.id, text_message, reply_markup=reply_kb_answer_the_question)



#обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Да‼️':
        bot.send_message(message.chat.id, "Тогда переходите по ссылке и ознакомьтесь со всеми подробностями и другими курсами😉", reply_markup=inline_kb_education)
        time.sleep(4)
        bot.send_message(message.chat.id, "Мы будем очень рады, если вы присоединитесь к нам😊", reply_markup=reply_kb_start)
    elif message.text == 'Нет😔':
        bot.send_message(message.chat.id, "Ничего страшного, надеюсь, вы найдете у нас что-нибудь для себя😘", reply_markup=reply_kb_start)
    elif message.text == 'Инстаграм студии😇':
        instagram_answerer(message)
    elif message.text == 'Записаться на процедуру👀':
        sign_up_answerer(message)
    elif message.text == 'Продукты от Екатерины Подымовой💄':
        products_answerer(message)
    elif message.text == 'Обучение в студии🤓':
        education_info_answerer(message)
    elif message.text == 'Энциклопедия по перманентному макияжу📚':
        book_answerer(message)
    elif message.text == 'Вернуться в главное меню ↩':
        bot.send_message(message.chat.id, 'Возврат в главное меню...', reply_markup=reply_kb_start)
    elif message.text == 'Нет😞':
        bot.send_message(message.chat.id, "Ничего страшного, надеюсь, вы найдете у нас что-нибудь для себя😘", reply_markup=reply_kb_products)
    elif message.text == 'Да🤩':
        bot.send_message(message.chat.id, "Замечательно, тогда свяжитесь с Екатериной😎", reply_markup=inline_kb_whatsapp)
        time.sleep(3)
        bot.send_message(message.chat.id, "А пока Екатерина отвечает, можете ознакомиться с другими предложениями и продуктами🥳", reply_markup=reply_kb_products)
    elif message.text == 'Вернуться к списку продуктов ↩':
        bot.send_message(message.chat.id, 'Возрат к списку продуктов...', reply_markup=reply_kb_products)
    elif message.text == "Доступ к каналу➡":
        channel_master_access(message)
    elif message.text == 'Испытать удачу🍀':
        try_your_luck(message)
    elif message.text == 'Канал для мастеров перманентного макияжа🎓':
        channel_master_answerer(message)
    elif message.text == 'Канал со скидками и акциями для клиентов😮':
        channel_customer_answerer(message)
    elif message.text == 'Ответить на вопрос🤓':
        question(message)
    elif message.text == ('1️⃣' or '2️⃣' or '3️⃣'):
        answer(message)
    else:
        bot.send_message(message.chat.id, "Извините, {}, к сожалению я не знаю как на это ответить, воспользуйтесь /help и посмотрите список доступных команд🤖".format(message.from_user.first_name))

bot.polling(none_stop=True, interval=0)
