from config import TOKEN
import telebot
import time
from telebot import types


bot = telebot.TeleBot(TOKEN)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "Запускает бота🚀"),
        telebot.types.BotCommand("restart", "Перезагружает бота🔄"),
    ])

@bot.callback_query_handler(func=lambda call: call.data in ['bt1', 'bt2', 'bt3', 'bt4', 'bt5', 'bt6', 'bt7', 'bt8', 'bt9', 'bt10', 'bt11', 'bt12', 'bt13', 'bt14', 'bt15', 'bt16', 'bt17', 'bt18', 'bt19', 'bt20', 'bt21', 'bt22', 'bt23', 'bt24', 'bt25', 'bt26', 'bt27'] )
def back_to_start(call):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)

@bot.message_handler(commands=["start"])
def start_bot(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}! Кто я такой? Я ТГ бот, созданный @KingAMR35, который помогает людям выбирать профессию и полностью рассказать о ней. Этот бот поможет найти себя в будущем!")
    bot.send_message(message.chat.id, "Также, если вы заметите какие-нибудь баги или увидели, что не хватает какой-то профессии, то пишите в ЛС @KingAMR35. Он все исправит!😃👨‍💻")
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Обычный поиск", callback_data="button1")
    button7777777777 = types.InlineKeyboardButton(text="Углублённый поиск --В разработке--", callback_data="button7777777777")
    keyboard.add(button1)
    keyboard.add(button7777777777)
    bot.send_message(message.chat.id, "Выберите поиск, чтобы начать", reply_markup=keyboard)
    
@bot.message_handler(commands=["restart"])
def restart_bot(message):
    bot.send_message(message.chat.id, "Подождите чуть-чуть, идёт перезагрузка🔄")
    time.sleep(3)
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}! Кто я такой? Я ТГ бот, созданный @KingAMR35, который помогает людям выбирать профессию и полностью рассказать о ней. Этот бот поможет найти себя в будущем!")
    bot.send_message(message.chat.id, "Также, если вы заметите какие-нибудь баги или увидели, что не хватает какой-то профессии, то пишите в ЛС @KingAMR35. Он все исправит!😃👨‍💻")
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Обычный поиск", callback_data="button1")
    button7777777777 = types.InlineKeyboardButton(text="Углублённый поиск --В разработке--", callback_data="button7777777777")
    keyboard.add(button1)
    keyboard.add(button7777777777)
    bot.send_message(message.chat.id, "Выберите поиск, чтобы начать", reply_markup=keyboard)




@bot.callback_query_handler(func=lambda call: True)
def callback_inline_message(call):
    if call.message:
        if call.data == "button1":
            keyboard = types.InlineKeyboardMarkup()
            button2 = types.InlineKeyboardButton(text="1. Спорт🥇🏃‍♀️", callback_data="button2")
            button3 = types.InlineKeyboardButton(text="2. Школа🏫", callback_data="button3")
            button4 = types.InlineKeyboardButton(text="3. Программирование👨‍💻", callback_data="button4")
            button5 = types.InlineKeyboardButton(text="4. Художество🎨", callback_data="button5")
            button6 = types.InlineKeyboardButton(text="5. Музыка🎼🎵", callback_data="button6")
            button7 = types.InlineKeyboardButton(text="6. Экология♻️", callback_data="button7")
            button8 = types.InlineKeyboardButton(text="7. Книги📚", callback_data="button8")
            button9 = types.InlineKeyboardButton(text="8. Проектирование📏✏️", callback_data="button9")
            button10 = types.InlineKeyboardButton(text="10. География🌍🌎", callback_data="button10")
            button11 = types.InlineKeyboardButton(text="9. Управление транспортом🚘🚌", callback_data="button11")
            button00 = types.InlineKeyboardButton(text=" Ещё", callback_data="button00")
            keyboard.add(button2, button3)
            keyboard.row(button4)
            keyboard.row(button5, button6)
            keyboard.add(button7, button8)
            keyboard.row(button9)
            keyboard.row(button11)
            keyboard.row(button10, button00)
            bot.send_message(call.message.chat.id, "Выберите своё любимое хобби из этого списка",reply_markup=keyboard)
#====================================================ЕЩЁ   
        if call.data == 'button00':
            keyboard = types.InlineKeyboardMarkup()
            button12 = types.InlineKeyboardButton(text="11. Строительство🏚🧱", callback_data="button12")
            button13 = types.InlineKeyboardButton(text="12. Работа с животными🦮🐈‍⬛🐾", callback_data="button13")
            button14 = types.InlineKeyboardButton(text="13. Ботаника☘️🌵🌳", callback_data="button14")
            button15 = types.InlineKeyboardButton(text="19. Медицина💉💊", callback_data="button15")
            button16 = types.InlineKeyboardButton(text="15. Военнослужащий🪖", callback_data="button16")
            button17 = types.InlineKeyboardButton(text="14. Юриспруденция✍️", callback_data="button17")
            button18 = types.InlineKeyboardButton(text="20. Финансы💶💰", callback_data="button18")
            button19 = types.InlineKeyboardButton(text="16. Маркетинг📦📢", callback_data="button19")
            button20 = types.InlineKeyboardButton(text="17. Философия📖🧐", callback_data="button20")
            button21 = types.InlineKeyboardButton(text="18. Готовка еды🌭🍔🌮", callback_data="button21")
            keyboard.row(button12)
            keyboard.row(button13)
            keyboard.row(button14)
            keyboard.row(button17)
            keyboard.row(button16)
            keyboard.row(button19)
            keyboard.row(button20)
            keyboard.row(button21)
            keyboard.row(button15, button18)
            bot.send_message(call.message.chat.id, "Вот вам еще варианты",reply_markup=keyboard)
#=========================================================================СПОРТ
        if call.data == 'button2':
            
            keyboard = types.InlineKeyboardMarkup()
            button01 = types.InlineKeyboardButton(text="Менеджер", callback_data="button01")
            button02 = types.InlineKeyboardButton(text="Комментатор", callback_data="button02")
            button03 = types.InlineKeyboardButton(text="Спортивный юрист", callback_data="button03")
            button04 = types.InlineKeyboardButton(text="Арбитр", callback_data="button04")
            button05 = types.InlineKeyboardButton(text="Фитнес-тренер", callback_data="button05")
            button06 = types.InlineKeyboardButton(text="Спортивный психолог", callback_data="button06")
            button07 = types.InlineKeyboardButton(text="Каппер", callback_data="button07")
            bt1 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt1")
            keyboard.add(button01, button07)
            keyboard.row(button03, button04)
            keyboard.row(button05, button02)
            keyboard.row(button06)
            keyboard.row(bt1)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов", reply_markup=keyboard)
        if call.data == 'button01':
            bot.send_message(call.message.chat.id, "Спортивный менеджер -- Специалист по организации спортивных мероприятий и соревнований.")
            bot.send_message(call.message.chat.id, "Зарплата спортивного менеджера в России — 50 000–150 000 рублей, в Москве — 65 000–150 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/c9b6f5d5c1c344ef50aa38f8e72e2d8b/'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button02':
            bot.send_message(call.message.chat.id, "Комментатор -- Журналист, который в режиме реального времени освещает события матча, турнира и любых соревнований.")
            bot.send_message(call.message.chat.id,"Зароботок комментатора зависит от того, насколько качественно он/она комментирует. Например, Дмитрий Бажанов — 70 тысяч рублей, а Александр Неценко — 220 тысяч рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/10381346702738854910?text=%D0%BA%D0%B0%D0%BA%20%D1%81%D1%82%D0%B0%D1%82%D1%8C%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%BC%20%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%B0%20%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE&path=yandex_search&parent-reqid=1745949620873808-9624093097306583990-balancer-l7leveler-kubr-yp-klg-129-BAL&from_type=vast'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button03':
            bot.send_message(call.message.chat.id, "Спортивный юрист -- Специалист, который специализируется на разрешении споров, в которые могут быть вовлечены спортсмены, сопровождении трансферов спортсменов между клубами, консультациях по трудовым контрактам.")
            bot.send_message(call.message.chat.id,"В начале профессионального пути спортивный юрист может рассчитывать на 45–50 тыс. рублей в месяц. Зарплата ведущих юристов крупных спортивных организаций начинается со 100 тыс. рублей, достигая в среднем 150–200 тыс. рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/4794a22be06ffe7885c1544fdac9dca2/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button04':
            bot.send_message(call.message.chat.id, "Арбитр -- Рефери, который контролирует соблюдение правил во время игры или поединка.")
            bot.send_message(call.message.chat.id, "В России опытные судьи на высших уровнях, включая Российскую Премьер-Лигу, могут зарабатывать от 50 000 рублей и выше за матч. Начинающие арбитры получают в районе 10 000–20 000 рублей за матч.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f5e02a64001c11a59bd1ca3fbb3511bd/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button05':
            bot.send_message(call.message.chat.id, "Фитнес-тренер -- Инструктор, который руководит тренировками в фитнес-центрах. Он может вести групповые или индивидуальные занятия, быть инструктором в тренажёрном зале.")
            bot.send_message(call.message.chat.id, "Одно занятие принесёт тренеру около 500 рублей. За месяц зарплата колеблется в районе 50–100 тысяч рублей ")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/1e477f52fd3db6f7946e53bbcae39db9/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button07':
            bot.send_message(call.message.chat.id, "Каппер -- Аналитик, который профессионально играет на ставках и консультирует других в этой сфере.")
            bot.send_message(call.message.chat.id, "Зарплата каппера (спортивного аналитика) в апреле 2025 года в России — 60 000–150 000 рублей, в Москве — 75 000–250 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/39035899874dbe6bb546916629fb82f9/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button06':
            bot.send_message(call.message.chat.id, "Спортивный психолог -- Специалист, который оказывает помощь и поддержку в укреплении психологических качеств, которые смогут привести к победе, справиться с нагрузками и стрессом, наладить атмосферу в команде.")
            bot.send_message(call.message.chat.id, "В крупных мегаполисах зарплата начинающего специалиста может составлять от 40 000 до 80 000 рублей, а опытного — от 80 000 рублей и выше. В менее крупных городах зарплата начинающего специалиста — от 30 000 до 60 000 рублей, а специалистов с опытом — от 60 000 рублей и выше.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/d35eff1f9272ac5fd0ac8ccf8406ac00/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#====================================================================ШКОЛА
        if call.data == 'button3':
            

            keyboard = types.InlineKeyboardMarkup()
            button001 = types.InlineKeyboardButton(text="Учитель", callback_data="button001")
            button002 = types.InlineKeyboardButton(text="Заместитель директора", callback_data="button002")
            button003 = types.InlineKeyboardButton(text="Методист", callback_data="button003")
            button004 = types.InlineKeyboardButton(text="Библиотекарь", callback_data="button04")
            button005 = types.InlineKeyboardButton(text="Секретарь", callback_data="button005")
            button006 = types.InlineKeyboardButton(text="Инженер-техник", callback_data="button006")
            bt2 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt2")
            keyboard.add(button001)
            keyboard.row(button003, button004)   
            keyboard.row(button005, button006)
            keyboard.row(button002)
            keyboard.row(bt2)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)
        if call.data == 'button001':
            bot.send_message(call.message.chat.id, "Учитель -- Преподает предметы для школьников, проводит уроки в младших и старших классах")
            bot.send_message(call.message.chat.id, "Средняя зарплата учителя в Самарской области составила 31 892 рубля.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/101766872b8a45d4e7818316b57d6333/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button002':
            bot.send_message(call.message.chat.id, "Заместитель директора -- Утверждает расписание занятий, управляет учебными планами в школе, организует образовательные процессы.")
            bot.send_message(call.message.chat.id, "Средняя зарплата заместителя директора в Самаре в 2024 году — 84 995 рублей. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 50 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-203717660_456239137?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button003':
            bot.send_message(call.message.chat.id, "Методист -- Занимается организацией учебного процесса, разрабатывает учебные планы и расписание, организует повышение квалификации педагогов и аттестацию учеников.")
            bot.send_message(call.message.chat.id, "Средняя зарплата по должности методиста в России в 2025 году составляет 51 000 рублей. Чаще всего зарплаты находятся в диапазоне от 32 000 до 70 000 рублей. Минимальная зафиксированная зарплата — 25 000 рублей, максимальная — 180 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/5c40cd35ca1ca762cfcbb0ca3767cc07/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button004':
            bot.send_message(call.message.chat.id, "Библиотекарь -- Поддерживает информационные ресурсы образовательной организации, помогает школьникам найти нужную литературу.")
            bot.send_message(call.message.chat.id, "Зарплата библиотекаря в России составляет 20 000–65 000 рублей, а в Москве — 46 570–100 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/e8a7bf32e2f31946b439e7088cfff4fd/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button005':
            bot.send_message(call.message.chat.id, "Секретарь -- Ведёт документооборот и корреспонденцию, занимается выдачей справок, отвечает на звонки и координирует работу руководства.")
            bot.send_message(call.message.chat.id, "Секретарь-делопроизводитель — 30 000–35 000 рублей. Секретарь/помощник генерального директора — от 50 000 рублей (опыт от 1 года). Секретарь руководителя — 40 000 рублей (опыт от 3 лет).")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/2183426f19ed67f994ce2e41554665db/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button006':
            bot.send_message(call.message.chat.id, "Инженер-техник -- Отвечает за техническую исправность инженерных систем в здании школы (водопровод, сантехника, электричество) и обеспечивает плановое обслуживание и ремонт оборудования.")
            bot.send_message(call.message.chat.id, "Инженер-техник по обслуживанию видеонаблюдения — 45 000–50 000 рублей в месяц. Сервисный инженер по ремонту цифровой техники — от 70 000 до 120 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/892b17dbf5e8f2ca6926c484c69e7783/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#===================================================================ПРОГРАММИРОВАНИЕ
        if call.data == 'button4':
            
            
            keyboard = types.InlineKeyboardMarkup()
            button0001 = types.InlineKeyboardButton(text="Разработчик программного обеспечения", callback_data="button0001")
            button0002 = types.InlineKeyboardButton(text="Веб-разработчик", callback_data="button0002")
            button0003 = types.InlineKeyboardButton(text="Разработчик игр", callback_data="button0003")
            button0004 = types.InlineKeyboardButton(text="Аналитик данных", callback_data="button0004")
            button0005 = types.InlineKeyboardButton(text="Специалист по кибербезопасности", callback_data="button0005")
            button0006 = types.InlineKeyboardButton(text="Системный администратор", callback_data="button0006")
            bt3 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt3")
            keyboard.add(button0001)
            keyboard.row(button0002, button0003)
            keyboard.row(button0004)
            keyboard.row(button0005)
            keyboard.row(button0006)
            keyboard.row(bt3)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)
        if call.data == 'button0001':
            bot.send_message(call.message.chat.id, "Разработчик программного обеспечения -- Создаёт приложения и системы, которые решают различные задачи. Работает с языками программирования (Python, Java, C++).")
            bot.send_message(call.message.chat.id, "Для начинающих разработчиков без опыта — от 40 000 до 70 000 рублей в месяц. Для разработчиков со средним опытом работы — от 70 000 до 120 000 рублей в месяц. Для опытных разработчиков с более чем 5-летним опытом — от 120 000 до 200 000 рублей и более в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/98280519d51c57e5b0160998222c6454/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button0002':
            bot.send_message(call.message.chat.id, "Веб-разработчик -- Специализируется на создании и поддержке веб-сайтов и веб-приложений. Делится на фронтенд-разработчиков (работают с пользовательским интерфейсом) и бэкенд-разработчиков (занимаются серверной частью).")
            bot.send_message(call.message.chat.id, "В среднем по России backend-разработчики зарабатывали 200 тыс. рублей в месяц, frontend-разработчики — 170 тыс. рублей, а fullstack-специалисты — около 190 тыс. рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/b15c54be7dd0cc7366a749f35e4b0be1/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button0003':
            bot.send_message(call.message.chat.id, "Разработчик игр -- Создаёт видеоигры для различных платформ, включая ПК, консоли и мобильные устройства. Использует игровые движки (Unity и Unreal Engine), а также языки программирования (C# и C++).")
            bot.send_message(call.message.chat.id, "Начинающий разработчик игр: от 30 000 до 70 000 рублей в месяц. Разработчик игр со средним опытом (2–5 лет): от 70 000 до 150 000 рублей в месяц. пытный разработчик игр (более 5 лет опыта): от 150 000 до 300 000 рублей в месяц или даже выше в зависимости от специализации и проекта.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/9c462c3d98a516613a2ace9adec19435/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button0004':
            bot.send_message(call.message.chat.id, "Аналитик данных -- Собирает, обрабатывает и анализирует большие объёмы данных для получения ценной информации. Использует инструменты и технологии (SQL, Python и R), а также методы машинного обучения и статистического анализа. ")
            bot.send_message(call.message.chat.id, "Младший аналитик — от 50 000 до 80 000 рублей в месяц. Аналитик среднего уровня — от 80 000 до 150 000 рублей в месяц. Старший аналитик — от 150 000 до 250 000 рублей в месяц и выше.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/4c059ca8c926a0dd022fcfe31b36f273/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button0005':
            bot.send_message(call.message.chat.id, "Специалист по кибербезопасности -- Защищает компьютерные системы и сети от кибератак и несанкционированного доступа. Разрабатывает и внедряет меры безопасности, проводит аудит систем и обучает сотрудников правилам безопасности.")
            bot.send_message(call.message.chat.id, "Средняя зарплата директора по кибербезопасности в России составляла 500 тыс. Руководитель ИБ-отдела получал в среднем 300 тыс. рублей, а специалист по информационной безопасности — 230 тыс. рублей. ")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/11434983178649684272?text=%D0%BA%D0%B0%D0%BA%20%D1%81%D1%82%D0%B0%D1%82%D1%8C%20%D0%A1%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%81%D1%82%20%D0%BF%D0%BE%20%D0%BA%D0%B8%D0%B1%D0%B5%D1%80%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BD%D0%B5%20%D0%B4%D0%BE%D0%BB%D0%B3%D0%BE%D0%B5&path=yandex_search&parent-reqid=1745953690699480-9003549385599599822-balancer-l7leveler-kubr-yp-vla-158-BAL&from_type=vast'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button0006':
            bot.send_message(call.message.chat.id, "Системный администратор -- Отвечает за установку, настройку и поддержку компьютерных систем и сетей. Обеспечивает бесперебойную работу серверов, сетевого оборудования и программного обеспечения. ")
            bot.send_message(call.message.chat.id, "Средний размер оплаты труда системного администратора — 156 577 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/6914020291219887218?from=tabbar&parent-reqid=1745946190762568-11633477674474500941-balancer-l7leveler-kubr-yp-sas-91-BAL&text=%D0%BA%D0%B0%D0%BA+%D1%81%D1%82%D0%B0%D1%82%D1%8C+%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9+%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE+%D0%BD%D0%B5+%D0%B4%D0%BE%D0%BB%D0%B3%D0%BE%D0%B5'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#=========================================================ХУДОЖЕСТВО
        if call.data == 'button5':
            keyboard = types.InlineKeyboardMarkup()
            button00001 = types.InlineKeyboardButton(text="Живописец", callback_data="button00001")
            button00002 = types.InlineKeyboardButton(text="Иллюстратор", callback_data="button00002")
            button00003 = types.InlineKeyboardButton(text="Скульптор", callback_data="button00003")
            button00004 = types.InlineKeyboardButton(text="Графический дизайнер", callback_data="button00004")
            button00005 = types.InlineKeyboardButton(text="Концепт-художник", callback_data="button00005")
            button00006 = types.InlineKeyboardButton(text="Художник-постановщик", callback_data="button00006")
            bt4 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt4")
            keyboard.add(button00001, button00002)
            keyboard.row(button00003, button00005)
            keyboard.row(button00004)
            keyboard.row(button00006)
            keyboard.row(bt4)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button00001':
            bot.send_message(call.message.chat.id, "Живописец -- Создаёт произведения искусства, используя краски и холсты. Может специализироваться на различных жанрах, таких как портреты, пейзажи, натюрморты и абстрактное искусство.")
            bot.send_message(call.message.chat.id, "Для начинающих художников-живописцев заработок может составлять от 20 000 до 40 000 рублей в месяц. Для специалистов среднего уровня средний уровень дохода может составлять от 40 000 до 80 000 рублей в месяц. Опытные и признанные художники-живописцы могут получать несколько сотен тысяч и даже миллионов рублей в год")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/105cdf3571aff813433f9d905e64cb68/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button00002':
            bot.send_message(call.message.chat.id, "Иллюстратор -- Создаёт изображения для книг, журналов, рекламных материалов и других печатных изданий. Работает в различных стилях и техниках, от традиционных рисунков до цифровых иллюстраций.")
            bot.send_message(call.message.chat.id, "Средняя зарплата иллюстратора в России в 2024 году — 58 162 рубля. Чаще всего в вакансиях встречается зарплата 40 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/12b9d47b022cc98086fb65696e65cbd1/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button00003':
            bot.send_message(call.message.chat.id, "Скульптор -- Создаёт трёхмерные произведения искусства из различных материалов, таких как глина, камень, металл и дерево. Требует не только художественного таланта, но и физических навыков для работы с инструментами и материалами.")
            bot.send_message(call.message.chat.id, "Начинающие специалисты получают около 25–40 тысяч рублей в месяц. Опытные мастера, работающие в крупных учреждениях культуры, на заказах или в частных студиях, могут зарабатывать от 50 до 80 тысяч рублей и выше.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-68291293_456239053?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button00004':
            bot.send_message(call.message.chat.id, "Графический дизайнер -- Создаёт визуальные концепции для различных медиа, включая печатные и цифровые. Работает с текстом, изображениями и цветами, чтобы создать привлекательные и функциональные дизайны для рекламы, веб-сайтов, логотипов и многого другого.")
            bot.send_message(call.message.chat.id, "Junior: 30 000–40 000 рублей. Middle: 70 000–90 000 рублей. Senior: 120 000–150 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/c00635aee28dd8c8fafebfb4046cb0d9/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button00005':
            bot.send_message(call.message.chat.id, "Концепт-художник -- Разрабатывает визуальные концепции для фильмов, видеоигр и других медиа. Создаёт эскизы и иллюстрации, которые помогают визуализировать персонажей, локации и объекты.")
            bot.send_message(call.message.chat.id, "Начинающий концепт-художник (до 2 лет опыта) — от 30 000 до 50 000 рублей в месяц. Концепт-художник со средним опытом (2–5 лет опыта) — от 50 000 до 80 000 рублей в месяц. Опытный концепт-художник (более 5 лет опыта) — от 80 000 до 150 000 рублей и выше в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-58151545_456241083?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button00006':
            bot.send_message(call.message.chat.id, "Художник-постановщик -- Создаёт окружающую атмосферу в кадре фильма или на сцене. Разрабатывает эскизы, подбирает декорации, мебель, реквизит, ищет интересные места для съёмок.")
            bot.send_message(call.message.chat.id, "Зарплата художника-постановщика (в кино и на телевидении) в России составляет 30 000–62 923 рубля, в Москве — 48 000–100 000 рублей. ")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/30b09e6cfa4d8088029ab4596d9b6f06/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#===========================================================МУЗЫКА
        if call.data == 'button6':
            keyboard = types.InlineKeyboardMarkup()
            button000001 = types.InlineKeyboardButton(text="Музыкант-исполнитель", callback_data="button000001")
            button000002 = types.InlineKeyboardButton(text="Композитор", callback_data="button000002")
            button000003 = types.InlineKeyboardButton(text="Дирижёр", callback_data="button000003")
            button000004 = types.InlineKeyboardButton(text="Музыкальный педагог", callback_data="button000004")
            button000005 = types.InlineKeyboardButton(text="Музыкальный терапевт", callback_data="button000005")
            button000006 = types.InlineKeyboardButton(text="Музыкальный менеджер", callback_data="button000006")
            button000007 = types.InlineKeyboardButton(text="Саунд-дизайнер", callback_data="button000007")
            bt5 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt5")
            keyboard.add(button000003, button000002)
            keyboard.row(button000007)
            keyboard.row(button000005)
            keyboard.row(button000001)
            keyboard.row(button000006)
            keyboard.row(button000004)
            keyboard.row(bt5)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button000001':
            bot.send_message(call.message.chat.id, "Музыкант-исполнитель -- Играет на музыкальных инструментах или поёт. Может выступать соло или в составе оркестров, ансамблей и хоров.")
            bot.send_message(call.message.chat.id, "Зарплата музыканта в России может составлять от 30 000 до 100 000 рублей, в Москве — от 40 000 до 120 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/6feabbfc5fce1a7e8f36f9a8a322e352/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button000002':
            bot.send_message(call.message.chat.id, "Композитор -- Создаёт оригинальные музыкальные произведения. Может писать музыку для оркестров, хоров, театров, кино и телевидения.")
            bot.send_message(call.message.chat.id, "Начинающий композитор может зарабатывать от 20 000 до 50 000 рублей в месяц. Опытный композитор со стажем работы 5–10 лет может зарабатывать 60 000–120 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/a0edd6634c706fd4fbc9904180eb3350/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button000003':
            bot.send_message(call.message.chat.id, "Дирижёр -- Руководит оркестрами, хорами и другими музыкальными коллективами. Помогает музыкантам исполнять произведения наилучшим образом.")
            bot.send_message(call.message.chat.id, "На начальном этапе карьеры зарплата может составлять от 40 000 до 80 000 рублей в месяц. В крупных городах и столицах, а также при работе с известными оркестрами, заработок дирижёра может достигать 200 000 рублей и более.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/decc484d39445254a1e9697e79a2bef9/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button000004':
            bot.send_message(call.message.chat.id, "Музыкальный педагог -- Обучает студентов игре на музыкальных инструментах, вокалу и теории музыки. Может работать в школах, колледжах, университетах или давать частные уроки.")
            bot.send_message(call.message.chat.id, "В общеобразовательных школах — около 20–30 тысяч рублей. В специализированных музыкальных школах — в среднем 45 тысяч рублей. В высших учебных заведениях — от 70 до 100 тысяч рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/5a9fbe08ffe36931d852f876db897eb2/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button000005':
            bot.send_message(call.message.chat.id, "Музыкальный терапевт -- Использует музыку для улучшения физического, эмоционального и психологического состояния пациентов.")
            bot.send_message(call.message.chat.id, "Зарплата может начинаться от 35000 при опыте работы 1-3 года. Опытные зарабатывают от 70000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/45ed9cd64aa724237acbc082fe465fdf/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button000006':
            bot.send_message(call.message.chat.id, "Музыкальный менеджер -- Занимается организацией и управлением карьерой артистов и музыкальных групп.")
            bot.send_message(call.message.chat.id, "Зарплата музыкального менеджера в апреле 2025 года в России — 40 000–100 000 рублей, в Москве — 50 000–200 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-111695825_456239206?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button000007':
            bot.send_message(call.message.chat.id, "Саунд-дизайнер -- Создаёт звуковые эффекты и музыкальные композиции для фильмов, видеоигр, театральных постановок и других медиа.")
            bot.send_message(call.message.chat.id, "Начинающий зарабатывает от 30000 до 60000 рублей в месяц. Со средним опытом - от 60000 до 100000 рублей. Опытные профессионалы получают от 100000 до 200000 рублей и выше, особенно в Москве.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/69d13322b8a9cc0e28ba0e3e3d698fe7/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#=================================================================ЭКОЛОГИЯ
        if call.data == 'button7':
            keyboard = types.InlineKeyboardMarkup()
            button100 = types.InlineKeyboardButton(text="Эколог", callback_data="button100")
            button101 = types.InlineKeyboardButton(text="Ландшафтный архитектор", callback_data="button101")
            button102 = types.InlineKeyboardButton(text="Экологический консультант", callback_data="button102")
            button103 = types.InlineKeyboardButton(text="Экологический инженер", callback_data="button103")
            button104 = types.InlineKeyboardButton(text="Гидролог", callback_data="button104")
            button105 = types.InlineKeyboardButton(text="Экологический юрист", callback_data="button105")
            button106 = types.InlineKeyboardButton(text="Урбанист-эколог", callback_data="button106")
            button107 = types.InlineKeyboardButton(text="Специалист по переработке", callback_data="button107")
            bt6 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt6")
            keyboard.add(button104, button100)
            keyboard.row(button106)
            keyboard.row(button105)
            keyboard.row(button107)
            keyboard.row(button101)
            keyboard.row(button103)
            keyboard.row(button102)
            keyboard.row(bt6)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)
        
        if call.data == 'button100':
            bot.send_message(call.message.chat.id, "Эколог -- Изучает взаимодействие живых организмов с их окружающей средой, проводит исследования и разрабатывает стратегии для сохранения экосистем.")
            bot.send_message(call.message.chat.id, "Средняя зарплата эколога в России в 2025 году составляет 63 614 рублей. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 50 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-212328337_456239130?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button101':
            bot.send_message(call.message.chat.id, "Ландшафтный архитектор -- роектирует и планирует зелёные пространства, такие как парки, сады и городские зоны отдыха.")
            bot.send_message(call.message.chat.id, "Зарплата ландшафтного архитектора в России составляет 45 000–160 000 рублей, в Москве — 50 000–200 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/13977536523088995652'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button102':
            bot.send_message(call.message.chat.id, "Экологический консультант -- Предоставляет экспертные советы по вопросам охраны окружающей среды, работает с различными организациями, помогая им соблюдать экологические нормы и стандарты.")
            bot.send_message(call.message.chat.id, "Начинающие экологи с опытом до 2 лет получают от 45 000 до 70 000 рублей. Специалисты со стажем от 2 до 5 лет зарабатывают от 70 000 до 120 000 рублей. Ведущие экологи с опытом более 5 лет получают от 120 000 до 180 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/05c40247599e30318f311095c479e5ba/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button103':
            bot.send_message(call.message.chat.id, "Экологический инженер -- Разрабатывает и внедряет технологии и системы, направленные на защиту окружающей среды.")
            bot.send_message(call.message.chat.id, "Начинающие специалисты (менее 2 лет опыта) — от 50 000 до 80 000 рублей в месяц. Специалисты с опытом (2–5 лет) — от 80 000 до 120 000 рублей в месяц. Опытные инженеры-экологи (более 5 лет) — от 120 000 и выше рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/aa69c7fb4fd0c093b41782e0bbc2540d/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button104':
            bot.send_message(call.message.chat.id, "Гидролог -- Исследует экологические процессы в водной среде, помогает сохранить водоёмы чистыми.")
            bot.send_message(call.message.chat.id, "Начинающий гидролог. Зарплата может варьироваться от 30 000 до 60 000 рублей в месяц в зависимости от региона. Гидролог со средним опытом. Средний уровень зарплаты может составлять от 50 000 до 90 000 рублей в месяц. Старший гидролог или руководящая должность. Зарплата для более опытных и руководящих гидрологов может достигать от 80 000 до 150 000 рублей и выше в зависимости от обязанностей и региона.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/1456d0a8ca77d01907e8a6ae51f8a96f/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button105':
            bot.send_message(call.message.chat.id, "Экологический юрист -- Разрабатывает нормативные акты в сфере экологии, а также работает в юридических отделах компаний.")
            bot.send_message(call.message.chat.id, "В среднем юрист-эколог в Москве зарабатывает 70–90 тысяч рублей. В Санкт-Петербурге — 60–80 тысяч рублей. В регионах России — 50–70 тысяч рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/12782364799494788027?from=tabbar&parent-reqid=1745954481361979-5365874030127996612-balancer-l7leveler-kubr-yp-sas-95-BAL&text=%D0%BA%D0%B0%D0%BA+%D1%81%D1%82%D0%B0%D1%82%D1%8C+%D0%AD%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9+%D1%8E%D1%80%D0%B8%D1%81%D1%82+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button106':
            bot.send_message(call.message.chat.id, "Урбанист-эколог -- Для строительства новых городов проектирует их с учётом текущей экологической обстановки.")
            bot.send_message(call.message.chat.id, "Урбанист-эколог: начальная зарплата — 60 000–80 000 рублей в месяц. Средний уровень опыта: 80 000–120 000 рублей в месяц. Старший урбанист-эколог: средний уровень опыта — 100 000–150 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/3637bc1b60e9d99911d7ba9cd5546c0b/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button107':
            bot.send_message(call.message.chat.id, "Специалист по переработке -- Разрабатывает и внедряет технологии повторного использования отходов, совершенствует работу предприятия, чтобы уменьшить расход ресурсов.")
            bot.send_message(call.message.chat.id, "Начинающий специалист — 35 000 рублей в месяц. Опытный специалист — 60 000 рублей в месяц. Профессионал — 80 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/b9fe708fa489f7dcb8977a85fb263deb/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#===================================================================КНИГИ
        if call.data == 'button8':
            keyboard = types.InlineKeyboardMarkup()
            button108 = types.InlineKeyboardButton(text="Библиотекарь", callback_data="button108")
            button109 = types.InlineKeyboardButton(text="Писатель", callback_data="button109")
            button110 = types.InlineKeyboardButton(text="Редактор", callback_data="button110")
            button111 = types.InlineKeyboardButton(text="Литературный агент", callback_data="button111")
            button112 = types.InlineKeyboardButton(text="Критик", callback_data="button112")
            button113 = types.InlineKeyboardButton(text="Сотрудник книжного сайта", callback_data="button113")
            button114 = types.InlineKeyboardButton(text="Работник издательства", callback_data="button114")
            bt7 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt7")
            keyboard.add(button108, button109)
            keyboard.row(button110, button112)
            keyboard.row(button111)
            keyboard.row(button114)
            keyboard.row(button113)
            keyboard.row(bt7)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button108':
            bot.send_message(call.message.chat.id, "Библиотекарь -- Работает с читателями, составляет каталоги, ведёт инвентаризации и сверки.")
            bot.send_message(call.message.chat.id, "Средняя зарплата библиотекаря в России — 31 546 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/e8a7bf32e2f31946b439e7088cfff4fd/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button109':
            bot.send_message(call.message.chat.id, "Писатель -- Для работы писателем нужен талант, желание совершенствоваться и умение воспринимать критику.")
            bot.send_message(call.message.chat.id, "Средняя зарплата писателя в России в 2025 году — 89 945 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/11190164585268879777'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button110':
            bot.send_message(call.message.chat.id, "Редактор -- Редакторы и корректоры работают с книгами и текстами, совершенствуют публикации. ")
            bot.send_message(call.message.chat.id, "Зарплата редактора в издательстве в Москве — от 20 000 до 400 000 рублей")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/58b122d7845a0a2ca796897016cf03ef/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button111':
            bot.send_message(call.message.chat.id, "Литературный агент -- Выступает посредником между автором и издателем, защищает интересы автора, ведя переговоры о заключении договора на издание и размере гонорара.")
            bot.send_message(call.message.chat.id, "Литературные агенты могут зарабатывать от 1500 рублей с заказа.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/c072f4c726ae6a7ff9b5dc105779743e/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button112':
            bot.send_message(call.message.chat.id, "Литературный критик -- Критик должен хорошо разбираться в литературе, отслеживать актуальные тенденции и уметь оценивать новинки книжного рынка.")
            bot.send_message(call.message.chat.id, "Начинающие критики обычно получают оклад в размере 25 000–30 000 рублей в месяц. Опытные и известные критики могут зарабатывать от 50 000 до 150 000 рублей в месяц, а в некоторых случаях и больше. Максимальная зарплата - 500000 рублей")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f5f056aa6cd60a3ca8db1a05c0dc50d7/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button113':
            bot.send_message(call.message.chat.id, "Сотрудник книжного сайта -- Работает на специализированных сайтах, которые имеют отношение к книгам и чтению.")
            bot.send_message(call.message.chat.id, "Зарплата редактора сайта может быть следующей: Москва — от 25 000 до 160 000 рублей в месяц. Санкт-Петербург — от 25 000 до 45 000 рублей")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/d84349475a8e7e7d2e5368c60c9b2bff/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button114':
            bot.send_message(call.message.chat.id, "Работник издательства -- В издательстве работают переводчики, редакторы, маркетологи, дизайнеры и другие специалисты.")
            bot.send_message(call.message.chat.id, "Зарплата издателя в России составляет 40 000–150 000 рублей, в Москве — 60 000–170 000 рублей. ")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/332116278444031340'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#===============================================================ПРОЕКТИРОВАНИЕ
        if call.data == 'button9':
            keyboard = types.InlineKeyboardMarkup()
            button115 = types.InlineKeyboardButton(text="Архитектурный визуализатор", callback_data="button115")
            button116 = types.InlineKeyboardButton(text="Инженер-конструктор", callback_data="button116")
            button117 = types.InlineKeyboardButton(text="Специалист по дизайну", callback_data="button117")
            button118 = types.InlineKeyboardButton(text="3D-моделлер", callback_data="button118")
            button119 = types.InlineKeyboardButton(text="Инженер-проектировщик", callback_data="button119")
            bt8 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt8")
            keyboard.add(button115)
            keyboard.row(button116)
            keyboard.row(button117)
            keyboard.row(button118)
            keyboard.row(button119)
            keyboard.row(bt8)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button115':
            bot.send_message(call.message.chat.id,"Архитектурный визуализатор -- Создаёт 3D-модели зданий, чтобы сделать проект понятным и привлекательным для заказчиков и инвесторов.")
            bot.send_message(call.message.chat.id, "Зарплата архитектурного визуализатора в апреле 2025 года в России составляет 40 000–162 000 рублей, в Москве — 70 000–200 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-24321381_456240138?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button116':
            bot.send_message(call.message.chat.id,"Инженер-конструктор -- Занимается разработкой и проектированием различных механизмов и устройств. В его обязанности входит создание чертежей, проведение расчётов и тестирование разработанных решений.")
            bot.send_message(call.message.chat.id, "Москва: инженер-конструктор — 80 000–150 000 рублей, ведущий инженер-конструктор — 130 000–220 000 рублей, главный конструктор — 200 000–350 000 рублей. ")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video27317256_456239029?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button117':
            bot.send_message(call.message.chat.id,"Специалист по дизайну -- Работает над созданием изделий, которые должны быть не только функциональными, но и привлекательными для пользователя. ")
            bot.send_message(call.message.chat.id, "Средняя зарплата дизайнера в России в найме составит 120 000 рублей в месяц, дизайнеры-фрилансеры — около 70 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/e3cb8a251f614c71c45f4b46d03f4de9/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button118':
            bot.send_message(call.message.chat.id,"3D-моделлер -- Создаёт трёхмерные объекты для различных целей: от игр и кино до образовательных программ и рекламы")
            bot.send_message(call.message.chat.id, "Начинающий 3D-моделлер (0–2 года опыта). Стартовая заработная плата может быть в диапазоне от 40 000 до 70 000 рублей в месяц. D-моделлер со средним опытом (2–5 лет опыта). Заработная плата может колебаться от 70 000 до 120 000 рублей в месяц. Опытный 3D-моделлер (более 5 лет опыта). Опытные специалисты могут ожидать заработную плату от 120 000 рублей и выше, вплоть до 200 000 рублей и более в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/270a5a21ea688d12ff1b44ec79dbdfe2/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button119':
            bot.send_message(call.message.chat.id,"Инженер-проектировщик -- Отвечает за разработку проектной документации для строительства зданий, сооружений, инфраструктурных и прочих объектов, а также за контроль реализации проекта.")
            bot.send_message(call.message.chat.id, "Средняя зарплата инженера-проектировщика в России в году составляет 95 152 рубля. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 100 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/7244739ed99ece83e530c9b1ffc40fbd/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        

#========================================================ГЕОГРАФИЯ
        if call.data == 'button10':
            keyboard = types.InlineKeyboardMarkup()
            button120 = types.InlineKeyboardButton(text="Картограф", callback_data="button120")
            button121 = types.InlineKeyboardButton(text="Климатолог", callback_data="button121")
            button122 = types.InlineKeyboardButton(text="Геомаркетолог", callback_data="button122")
            button123 = types.InlineKeyboardButton(text="Менеджер по туризму", callback_data="button123")
            button124 = types.InlineKeyboardButton(text="Инженер-геолог", callback_data="button124")
            bt9 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt2")
            keyboard.add(button120, button121)
            keyboard.row(button122, button124)
            keyboard.row(button123)
            keyboard.row(bt9)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button120':
            bot.send_message(call.message.chat.id,"Картограф -- Специалист по созданию, обновлению и анализу бумажных и электронных карт.")
            bot.send_message(call.message.chat.id, "Начинающий специалист может рассчитывать на зарплату в пределах 25 000–40 000 рублей в месяц. Специалист со средним опытом (от 2–3 лет) может получать от 40 000 до 60 000 рублей в месяц. Опытный картограф с 5 и более лет опыта и высокой квалификацией может рассчитывать на 60 000 рублей и выше в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/b6902a8d7939f386fde95b5f44ccdc0c/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button121':
            bot.send_message(call.message.chat.id,"Климатолог -- Учёный, занимающийся исследованием изменений климата.")
            bot.send_message(call.message.chat.id, "Зарплата климатолога составляет: в России — 110 000–189 000 рублей; в Москве — 85 000–100 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/b3b86d8fce557f4d36a619cf2047bfc2/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button122':
            bot.send_message(call.message.chat.id,"Геомаркетолог -- Современная специальность, изучающая применение маркетинговых инструментов и программ в зависимости от географической локализации.")
            bot.send_message(call.message.chat.id, "По некоторым данным, руководитель какого-либо направления может зарабатывать до 200 000 рублей в месяц, а стажёр — не более 50 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/c6f21c60a38ce63a5e6c2a29437b03f2/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button123':
            bot.send_message(call.message.chat.id,"Менеджер по туризму -- Специалист в области HoReCa, занимающийся организацией туров и продажей путёвок клиентам.")
            bot.send_message(call.message.chat.id, "Менеджер по туризму зарабатывает: от 150 000 рублей за месяц, при опыте работы 1–3 года. До 250 000 рублей за месяц, до вычета налогов. От 90 000 до 300 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-173549187_456239052?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button124':
            bot.send_message(call.message.chat.id,"Инженер-геолог -- Строительная специальность, охватывающая изучение почвы перед строительством или реконструкцией зданий и сооружений.")
            bot.send_message(call.message.chat.id, "Примерные диапазоны среднемесячной заработной платы в зависимости от опыта работы: начинающий специалист может рассчитывать на оклад от 30 000 до 35 000 рублей; пециалист с опытом работы от 3 до 5 лет может зарабатывать от 40 000 до 60 000 рублей; максимальная зарплата у инженера-геолога может достигать 150 000 рублей и выше.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-142383557_456239316?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#=================================================УПРАВЛЕНИЕ ТРАНСПОРТОМ
        if call.data == 'button11':
            keyboard = types.InlineKeyboardMarkup()
            button125 = types.InlineKeyboardButton(text="Моряк", callback_data="button125")
            button126 = types.InlineKeyboardButton(text="Пилот", callback_data="button126")
            button127 = types.InlineKeyboardButton(text="Авиационный техник", callback_data="button127")
            button128 = types.InlineKeyboardButton(text="Логист", callback_data="button128")
            button129 = types.InlineKeyboardButton(text="Машинист", callback_data="button129")
            bt10 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt10")
            keyboard.row(button125, button126)
            keyboard.row(button129, button128)
            keyboard.row(button127)
            keyboard.row(bt10)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button125':
            bot.send_message(call.message.chat.id,"Моряк -- Работает на судах, занимается их управлением, обслуживанием и ремонтом.")
            bot.send_message(call.message.chat.id, "Средняя зарплата Моряка в России за 2025 год ‒ 116 239 рублей. За месяц заработная плата изменилась на 6.5% ‒ с 124 269 до 116 239 рублей. А чаще всего в вакансиях встречается зарплата 150 000 рублей (модальная).")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/63cb89d3156e7f91d143bacf67c1e107/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button126':
            bot.send_message(call.message.chat.id,"Пилот -- Управляет самолётом. Предполагает большую ответственность и предельную концентрацию.")
            bot.send_message(call.message.chat.id, "Средняя зарплата пилота в России — 182 984 рубля. Чаще всего в вакансиях встречается зарплата 210 000 рублей (модальная).")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-43077955_456255824?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button127':
            bot.send_message(call.message.chat.id,"Авиационный техник -- Занимается обслуживанием и ремонтом воздушных судов.")
            bot.send_message(call.message.chat.id, "Средняя зарплата авиационного техника в России —  81 000 рублей. Чаще всего зарплаты находятся в диапазоне от 52 000 до 110 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-160510130_456239564?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button128':
            bot.send_message(call.message.chat.id,"Логист --  Планирует и управляет перевозками грузов, разрабатывает маршруты, координирует работу водителей и других сотрудников, контролирует процесс доставки.")
            bot.send_message(call.message.chat.id, "Средняя заработная плата специалиста в России — 63 887 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/318606190057a3514ec06366376740f7/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button129':
            bot.send_message(call.message.chat.id,"Машинист -- Управляет поездами и другими железнодорожными транспортными средствами.")
            bot.send_message(call.message.chat.id, "Средняя зарплата машиниста электропоезда в России составляет 100 000 рублей. Чаще всего зарплаты находятся в диапазоне от 80 000 до 120 000 рублей. Минимальная зафиксированная зарплата — 65 000 рублей, максимальная — 145 000 рублей. ")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-204126606_456239532?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#==================================================================СТРОИТЕЛЬСТВО
        if call.data == 'button12':
            keyboard = types.InlineKeyboardMarkup()
            button130 = types.InlineKeyboardButton(text="Архитектор", callback_data="button130")
            button131 = types.InlineKeyboardButton(text="Проектировщик", callback_data="button131")
            button132 = types.InlineKeyboardButton(text="Инженер-строитель", callback_data="button132")
            button133 = types.InlineKeyboardButton(text="Бетонщик", callback_data="button133")
            button134 = types.InlineKeyboardButton(text="Энергетик", callback_data="button134")
            button135 = types.InlineKeyboardButton(text="Прораб", callback_data="button135")
            bt11 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt11")
            keyboard.row(button135, button133)
            keyboard.row(button130)
            keyboard.row(button134)
            keyboard.row(button131)
            keyboard.row(button132)
            keyboard.row(bt11)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button130':
            bot.send_message(call.message.chat.id,"Архитектор -- Разрабатывает проект здания и оформляет документацию. Отдельное направление — ландшафтный архитектор, который планирует также работы по благоустройству прилегающей территории.")
            bot.send_message(call.message.chat.id, "Начинающие специалисты могут рассчитывать на зарплату от 70 000 до 90 000 рублей в месяц, тогда как опытные архитекторы с реализованными проектами и стажем от 3 лет получают до 260 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-228736629_456239021?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button131':
            bot.send_message(call.message.chat.id,"Проектировщик -- Готовит чертежи на базе архитектурного плана. Разрабатывает схемы расположения в здании систем водоснабжения, электричества, канализации, вентиляции.")
            bot.send_message(call.message.chat.id, "Средняя зарплата проектировщика в России в 2025 году составляет 95 658 рублей. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 100 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/7c76b85448646ec015f87224857c9d41/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button132':
            bot.send_message(call.message.chat.id,"Инженер-строитель -- Может работать как с документацией, так и непосредственно на стройплощадке. Инженер занимается планированием и организацией работ, руководит другими специалистами, контролирует процесс строительства объекта.")
            bot.send_message(call.message.chat.id, "Зарплата инженера-строителя в марте 2025 года в России составляет 70 000–200 000 рублей, а в Москве — 100 000–250 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/eb2d15a26d566c88c87bd337481d7310/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button133':
            bot.send_message(call.message.chat.id,"Бетонщик --  Специалист, работающий с бетоном, занимается заливкой, армированием и отделкой бетонных конструкций.")
            bot.send_message(call.message.chat.id, "Средняя зарплата бетонщика в России в 2025 году — 141 653 рубля.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f24049c1eaebc9b40342c22607df5487/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button134':
            bot.send_message(call.message.chat.id,"Энергетик -- Проектирует и монтирует электросети, а также занимается их обслуживанием и ремонтом. Отвечает не только за бесперебойное электроснабжение в здании, но и за безопасность сетей в процессе эксплуатации.")
            bot.send_message(call.message.chat.id, "Средняя зарплата энергетика в России в 2025 году составляет 86 067 рублей. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 100 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-20155733_456239202?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button135':
            bot.send_message(call.message.chat.id,"Прораб -- Специалист, который управляет строительным процессом на площадке, контролирует выполнение работ.")
            bot.send_message(call.message.chat.id, "В Москве и других крупных городах с активно развивающимся строительным сектором прорабам в среднем предлагают зарплату от 110 000 до 175 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f5f77a139c5d2acedcae423b24045849/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#==================================================================Работа с животными
        if call.data == 'button13':
            keyboard = types.InlineKeyboardMarkup()
            button136 = types.InlineKeyboardButton(text="Ветеринар", callback_data="button136")
            button137 = types.InlineKeyboardButton(text="Зоолог", callback_data="button137")
            button138 = types.InlineKeyboardButton(text="Грумер", callback_data="button138")
            button139 = types.InlineKeyboardButton(text="Дрессировщик", callback_data="button139")
            button140 = types.InlineKeyboardButton(text="Селекционер", callback_data="button140")
            button141 = types.InlineKeyboardButton(text="Охраник природы", callback_data="button141")
            bt12 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt12")
            keyboard.row(button137, button138)
            keyboard.row(button136)
            keyboard.row(button139)
            keyboard.row(button140)
            keyboard.row(button141)
            keyboard.row(bt12)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)
            
        if call.data == 'button136':
            bot.send_message(call.message.chat.id,"Ветеринар -- Занимается лечением и профилактикой заболеваний у животных. Диагностирует болезни, проводит операции, делает прививки и оказывает помощь в экстренных случаях. ")
            bot.send_message(call.message.chat.id, "Ветеринарный врач-практикант — от 25 тыс. до 40 тыс. руб. в месяц. Ветеринарный врач среднего уровня — от 40 тыс. до 100 тыс. руб. в месяц. Ветеринарный врач с опытом работы — от 70 тыс. до 250 тыс. руб. в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://ok.ru/video/7199655315'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button137':
            bot.send_message(call.message.chat.id,"Зоолог -- Изучает жизнь и поведение животных в их естественной среде. Зоологи проводят исследования, связанные с экологией, популяцией и поведением животных.")
            bot.send_message(call.message.chat.id, "Зоолог зарабатывает: начинающий зоолог, аспирант или младший научный сотрудник — 20 000–40 000 рублей; зоолог со средним стажем или научный сотрудник — 40 000–70 000 рублей; зоолог с большим опытом или ведущий научный сотрудник — 70 000–100 000 рублей и выше.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/62ccedc6db2f72c6b1582be00e23bf68/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button138':
            bot.send_message(call.message.chat.id,"Грумер -- Занимается уходом за внешним видом домашних питомцев, таких как собаки и кошки. Проводит стрижки, купание, чистку ушей, подстригает когти и может выявить внешние проблемы со здоровьем питомца.")
            bot.send_message(call.message.chat.id, "Начинающий грумер в малом городе зарабатывает от 30 000 до 45 000 рублей в месяц при работе в поликлинике или стационаре. Специалист с опытом в городе среднего размера. Получает от 45 000 до 70 000 рублей в месяц, особенно при совмещении приёма, дежурств и участии в социальных программах.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/dd04126411a80fd3a116eddb3ff1322a/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button139':
            bot.send_message(call.message.chat.id,"Дрессировщик -- Обучает животных командам и трюкам. Работает с домашними питомцами, дикими животными в цирках или зоопарках, а также обучает собак для помощи людям с ограниченными возможностями.")
            bot.send_message(call.message.chat.id, "Зарплата дрессировщика в России составляет 50 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/2faede914376535133738515f40f2ebf/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button140':
            bot.send_message(call.message.chat.id,"Селекционер -- Выводит новые породы животных, анализирует наследственные качества, занимается улучшением продуктивности.")
            bot.send_message(call.message.chat.id, "Начинающий уровень или ассистент селекционера: от 30 000 до 60 000 рублей в месяц. Средний уровень: около 50 000–70 000 рублей в месяц. Опытные селекционеры: 80 000–120 000 рублей в месяц, в некоторых случаях доход может быть и выше.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://ok.ru/video/424637499939'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button141':
            bot.send_message(call.message.chat.id,"Охраник природы -- Работает с экологическими организациями, помогает сохранять природные территории и защищать животных.")
            bot.send_message(call.message.chat.id, "Охраник природы зарабатывает: специалист с опытом 2–3 года — от 70 000 до 100 000 рублей в месяц; специалист с опытом 4–6 лет — от 100 000 до 150 000 рублей в месяц; специалист с опытом более 7 лет — от 150 000 рублей и выше в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/525255d1c93d197a42b90cfe49278200/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#==================================================================РАБОТА С РАСТЕНИЯМИ
        if call.data == 'button14':
            keyboard = types.InlineKeyboardMarkup()
            button142 = types.InlineKeyboardButton(text="Ботаник", callback_data="button142")
            button143 = types.InlineKeyboardButton(text="Фитопатолог", callback_data="button143")
            button144 = types.InlineKeyboardButton(text="Агроном", callback_data="button144")
            button145 = types.InlineKeyboardButton(text="Садовник", callback_data="button145")
            button146 = types.InlineKeyboardButton(text="Цветовод", callback_data="button146")
            button147 = types.InlineKeyboardButton(text="Флорист", callback_data="button147")
            bt13 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt13")
            keyboard.row(button142, button144)
            keyboard.row(button145, button147)
            keyboard.row(button143, button146)
            keyboard.row(bt13)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button142':
            bot.send_message(call.message.chat.id,"Ботаник -- Специалист, который занимается изучением растений. Ботаники работают в научных учреждениях, таких как ботанические сады, научно-исследовательские институты, университеты.")
            bot.send_message(call.message.chat.id, "Студент-ботаник или начинающий специалист. Зарплата может составлять 15 000–30 000 рублей. Научный сотрудник-ботаник. Зарплата может варьироваться от 35 000 до 60 000 рублей, в зависимости от опыта и степени. Старший научный сотрудник/куратор гербария или коллекции. Зарплата может находиться в диапазоне 50 000–80 000 рублей.Профессор ботаники. Зарплата профессора может варьироваться от 60 000 до 120 000 рублей или даже выше в зависимости от учебного заведения и наличия научных публикаций.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/524380844a6964ea51a60e7833f5d434/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button143':
            bot.send_message(call.message.chat.id,"Фитопатолог -- Специалист, который занимается изучением болезней растений. Фитопатологи работают в сельскохозяйственных учреждениях, таких как агрохимические лаборатории, карантинные службы.")
            bot.send_message(call.message.chat.id, "Старший биолог/фитопатолог/агроном в Москве, оплата труда — от 50 000 до 150 000 рублей за месяц на руки.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f9e552abc37c1af165affe0a25e4b0a1/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button144':
            bot.send_message(call.message.chat.id,"Агроном -- Специалист из сферы земледелия и сельского хозяйства. Его основная работа — выращивание и сбор урожая в промышленных масштабах.")
            bot.send_message(call.message.chat.id, "Новичкам предлагают зарплату от 30 000 рублей в месяц. Для специалистов с опытом от 1 до 3 лет нет вакансий с зарплатой ниже 35 000–50 000 рублей в месяц. Стаж 3–6 лет позволяет претендовать на вакансии с зарплатой от 70 000 рублей, а через 5–6 лет с момента начала работы — от 100 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/58507c3ddfa1cf47e51eb287bbe31bf2/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button145':
            bot.send_message(call.message.chat.id,"Садовник -- Специалист, который ухаживает за садами и парками, планирует посадки, подрезает деревья и кустарники, следит за их состоянием.")
            bot.send_message(call.message.chat.id, "Средняя зарплата садовника по России составляет 26 000 рублей в месяц, самая высокая — 62 000 рублей. А средняя зарплата по Москве — 139 тысяч рублей в месяц, максимальная — 339 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/82b746cd23fa3f36a367c3bfa44a49ae/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button146':
            bot.send_message(call.message.chat.id,"Цветовод -- Специалист, который занимается выращиванием цветов. Цветоводы работают в цветочных магазинах, теплицах, ландшафтных компаниях.")
            bot.send_message(call.message.chat.id, "Средняя зарплата цветовода в Москве в 2025 году — 67 175 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/895dffaab668a501f8ee7566b0a49f39/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button147':
            bot.send_message(call.message.chat.id,"Флорист -- Специалист, который составляет цветочные композиции для разных целей: от украшения свадеб и праздников до интерьерного декора.")
            bot.send_message(call.message.chat.id, "В среднем по России флористы получают около 45 000–55 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/88dd9cfe280623741df260ff486c1240/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)

#========================================================Юриспруденция
        if call.data == 'button17':
            keyboard = types.InlineKeyboardMarkup()
            button148 = types.InlineKeyboardButton(text="Адвокат", callback_data="button148")
            button149 = types.InlineKeyboardButton(text="Прокурор", callback_data="button149")
            button150 = types.InlineKeyboardButton(text="Нотариус", callback_data="button150")
            button151 = types.InlineKeyboardButton(text="Следователь", callback_data="button151")
            button152 = types.InlineKeyboardButton(text="Судья", callback_data="button152")
            button153 = types.InlineKeyboardButton(text="Преподаватель права", callback_data="button153")
            button154 = types.InlineKeyboardButton(text="Арбитражный управляющий", callback_data="button154")
            bt14 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt14")
            keyboard.row(button148, button149)
            keyboard.row(button150, button152)
            keyboard.row(button151)
            keyboard.row(button153)
            keyboard.row(button154)
            keyboard.row(bt14)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button148':
            bot.send_message(call.message.chat.id,"Адвокат -- Консультирует по правовым вопросам и помогает в разрешении юридических конфликтов.")
            bot.send_message(call.message.chat.id, "Средняя зарплата адвоката в России — 100 000 рублей. Однако эта цифра сильно варьируется: от 40 000 рублей у начинающих специалистов до 300 000 рублей у опытных юристов.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/5017696919203052195'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button149':
            bot.send_message(call.message.chat.id,"Прокурор -- Поддерживает государственное обвинение в суде, следит за соблюдением законности и правопорядка, проводит проверки по фактам преступлений и контролирует работу следственных органов.")
            bot.send_message(call.message.chat.id, "Зарплата прокурора в России составляет 24 000–75 000 рублей, в Москве — 120 000–150 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/13172690762146465984'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button150':
            bot.send_message(call.message.chat.id,"Нотариус -- В обязанности входит удостоверение сделок, заверение копий документов, выдача доверенностей и других нотариальных действий.")
            bot.send_message(call.message.chat.id, "Средняя зарплата нотариуса в России в 2025 году — 58 164 рубля.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/691062dfa0f628b06849ca0224358132/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button151':
            bot.send_message(call.message.chat.id,"Следователь --  Расследует уголовные дела, собирает доказательства, проводит допросы свидетелей и обвиняемых, участвует в судебных процессах.")
            bot.send_message(call.message.chat.id, "Зарплата следователя в России — 35 000–85 000 рублей, в Москве — 60 000–130 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-38029_456240291?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button152':
            bot.send_message(call.message.chat.id,"Судья -- Рассматривает дела всех направлений, выносит решения на основе представленных доказательств и законодательства, следит за соблюдением процессуальных норм и прав участников процесса.")
            bot.send_message(call.message.chat.id, "Зарплата судьи в России составляет 32 000–55 000 рублей, в Москве — 120 000–160 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/beca5af380c3fe2b0da692cf35f4baba/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button153':
            bot.send_message(call.message.chat.id,"Преподаватель права --  В обязанности входит обучение студентов юридических специальностей, разработка учебных программ и проведение научных исследований в области права.")
            bot.send_message(call.message.chat.id, "В частной школе: начальный уровень — от 40 000 до 60 000 рублей в месяц; средний уровень — от 50 000 до 80 000 рублей в месяц; высокий уровень — от 70 000 до 120 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/1b25ec43cb6c179d47d26070c9feb3df/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button154':
            bot.send_message(call.message.chat.id,"Арбитражный управляющий -- Контролирует активы должника, а также следит за удовлетворением интересов кредиторов.")
            bot.send_message(call.message.chat.id, "Зарплата арбитражного управляющего в России составляет 50 000–100 000 рублей, а в Москве — 70 000–250 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/3687752771929485176'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)

#====================================================================ВОЕННОСЛУЖАЩИЙ
        if call.data == 'button16':
            keyboard = types.InlineKeyboardMarkup()
            button155 = types.InlineKeyboardButton(text="Десантник", callback_data="button155")
            button156 = types.InlineKeyboardButton(text="Снайпер", callback_data="button156")
            button157 = types.InlineKeyboardButton(text="Артиллерист", callback_data="button157")
            button158 = types.InlineKeyboardButton(text="Разведчик", callback_data="button158")
            button159 = types.InlineKeyboardButton(text="Военный врач", callback_data="button159")
            button160 = types.InlineKeyboardButton(text="Танкист", callback_data="button160")
            bt15 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt15")
            keyboard.row(button155, button156)
            keyboard.row(button157, button160)
            keyboard.row(button158)
            keyboard.row(button159)
            keyboard.row(bt15)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button155':
            bot.send_message(call.message.chat.id,"Десантник -- Специально подготовленный солдат, который начинает бой в воздухе, когда летит на парашюте.")
            bot.send_message(call.message.chat.id, "Десантник зарабатывает от 210000 рублей до 400000 рублей")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/e05248078a1d6554fb07a98d003b3bd1/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button156':
            bot.send_message(call.message.chat.id,"Снайпер -- Специально обученный стрелок, который привлекается для выполнения задач по стрельбе с дальних расстояний по противнику.")
            bot.send_message(call.message.chat.id, "В среднем зарабатывают около 200-300 тыс. руб. в месяц, это без доплат за выполнение заданий. За успешную секретную операцию, на счёт может упасть в качестве премии до 1000000 руб.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://ok.ru/video/1836420237877'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button157':
            bot.send_message(call.message.chat.id,"Артиллерист -- Человек, находящийся на военной службе в артиллерийских войсках. Такие специалисты присутствуют в сухопутных, ракетных, воздушных, морских силах российской армии.")
            bot.send_message(call.message.chat.id, "Артиллерист зарабатывает от 230 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/4866903015485217474'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button158':
            bot.send_message(call.message.chat.id,"Разведчик -- Добывает сведения, которые помогают командирам решить, где лучше наступать, по каким дорогам могут пройти солдаты или проехать машины.")
            bot.send_message(call.message.chat.id, "Средняя зарплата рядового разведчика составляет около 60 000 рублей в месяц без учёта дополнительных выплат. Это базовая сумма, которая может варьироваться в зависимости от должности, опыта работы и других факторов.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/b5d90d0f503ea5227696ba9128ba5307/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button159':
            bot.send_message(call.message.chat.id,"Военный врач -- Человек с высшим медицинским образованием и воинским званием. Во время боевых действий врач оказывает неотложную помощь в специально оснащённых мобильных пунктах.")
            bot.send_message(call.message.chat.id, "Средняя зарплата военного врача в России в составляет 67 199 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://ok.ru/video/777726199115'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button160':
            bot.send_message(call.message.chat.id,"Танкист -- Профессиональный военнослужащий, служащий в танковых, бронетанковых, мотострелковых или танковых ремонтных подразделениях сухопутных войск.")
            bot.send_message(call.message.chat.id, "Танкист зарабатывает от 395 000 ₽/месяц")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/d280e770aa384def855c7e7948fa768c/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        
        
#===========================================================МАРКЕТИНГ
        if call.data == 'button19':
            keyboard = types.InlineKeyboardMarkup()
            button161 = types.InlineKeyboardButton(text="Менеджер по маркетингу", callback_data="button161")
            button162 = types.InlineKeyboardButton(text="Специалист по продвижению", callback_data="button162")
            button163 = types.InlineKeyboardButton(text="Маркетинговый консультант", callback_data="button163")
            button164 = types.InlineKeyboardButton(text="Контент-маркетолог", callback_data="button164")
            button165 = types.InlineKeyboardButton(text="Рекламный дизайнер", callback_data="button165")
            button166 = types.InlineKeyboardButton(text="Маркетинговый аналитик", callback_data="button166")
            bt16 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt16")
            keyboard.row(button161)
            keyboard.row(button162)
            keyboard.row(button163)
            keyboard.row(button164)
            keyboard.row(button165)
            keyboard.row(button166)
            keyboard.row(bt16)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)
            
        if call.data == 'button161':
            bot.send_message(call.message.chat.id,"Менеджер по маркетингу -- Отвечает за разработку и реализацию стратегий, проведение исследований рынка и анализ конкурентов.")
            bot.send_message(call.message.chat.id, "Средняя зарплата менеджера по маркетингу в Самаре — 53 910 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-167096943_456240552?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button162':
            bot.send_message(call.message.chat.id,"Специалист по продвижению -- Занимается продвижением товаров и услуг, подбирает стратегии рекламы и участвует в рекламных кампаниях.")
            bot.send_message(call.message.chat.id, "Средняя зарплата специалиста по продвижению в Самаре — 81 667 рублей, модальная (наиболее часто встречающаяся) — 82 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-101115520_456239287?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button163':
            bot.send_message(call.message.chat.id,"Маркетинговый консультант --  Предоставляет экспертные советы и рекомендации компаниям по разработке и реализации маркетинговых стратегий.")
            bot.send_message(call.message.chat.id, "Средняя зарплата специалиста по маркетингу в России —  64 603 рубля. Чаще всего в вакансиях встречается зарплата 50 000 рублей (модальная).")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/c47271f7f8212716477676daf2be9bc9/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button164':
            bot.send_message(call.message.chat.id,"Контент-маркетолог -- Создаёт и продвигает контент (статьи, блоги, видео, инфографику), который привлекает и удерживает целевую аудиторию.")
            bot.send_message(call.message.chat.id, "Зарплата контент-маркетолога в России может составлять 30 000–120 000 рублей, в Москве — 50 000–150 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f6711c519e4dd88d854da1d54d042e4c/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button165':
            bot.send_message(call.message.chat.id,"Рекламный дизайнер --  Создаёт визуальные материалы для рекламных кампаний, включая баннеры, плакаты, флаеры и другие маркетинговые материалы.")
            bot.send_message(call.message.chat.id, "На старте карьеры в регионах зарплата составляет 30–55 тысяч рублей в месяц, в Москве — 50–85 тысяч рублей в месяц. Специалисты с опытом в дизайне получают 45–90 тысяч рублей в месяц в регионах, 75–120 тысяч рублей в месяц в Москве. На руководящих позициях в регионах зарплата составляет 70–100 тысяч рублей в месяц, в Москве — 100–150 тысяч рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/aa38531ffde66aa03488ba227c23db4d/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button166':
            bot.send_message(call.message.chat.id,"Маркетинговый аналитик -- Собирает и анализирует данные о рынке, конкурентах и потребителях. Создаёт отчёты и прогнозы, помогая компании принимать обоснованные решения.")
            bot.send_message(call.message.chat.id, "Средняя зарплата маркетингого аналитика составляет 73 250 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/ee8128f02b8f1326992533ec53b392ff/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        

#======================================================Философия
        if call.data == 'button20':
            keyboard = types.InlineKeyboardMarkup()
            button167 = types.InlineKeyboardButton(text="Философ", callback_data="button167")
            button168 = types.InlineKeyboardButton(text="Научный сотрудник", callback_data="button168")
            button169 = types.InlineKeyboardButton(text="Биоэтик", callback_data="button169")
            button170 = types.InlineKeyboardButton(text="Коуч", callback_data="button170")
            button171 = types.InlineKeyboardButton(text="Социолог", callback_data="button171")
            button172 = types.InlineKeyboardButton(text="Философский консультант", callback_data="button172")
            bt17 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt17")
            keyboard.row(button167, button169)
            keyboard.row(button171, button170)
            keyboard.row(button168)
            keyboard.row(button172)
            keyboard.row(bt17)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button167':
            bot.send_message(call.message.chat.id,"Философ -- Автор научных исследований и публикаций, занимающийся анализом связей современных общественных процессов с историческими событиями и факторами.")
            bot.send_message(call.message.chat.id, "Зарплата философа в России составляет 50 000–140 000 рублей, в Москве — 45 000–160 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/90cc08f3761026295711d3f077570ad9/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button168':
            bot.send_message(call.message.chat.id,"Научный сотрудник -- Участвует в профильных научных исследованиях с целью конкретного практического применения.")
            bot.send_message(call.message.chat.id, "Зарплата научного сотрудника в России может составлять от 45 000 до 180 000 рублей, в Москве — от 70 000 до 173 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f28d7c13ca089d193da9c9c65e12917f/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button169':
            bot.send_message(call.message.chat.id,"Биоэтик -- Решает вопросы этичности использования инновационных технологий, связанных с генной инженерией, трансплантологией, биомедициной, кибернетикой, искусственным интеллектом и нанотехнологиями.")
            bot.send_message(call.message.chat.id, "Специалист с опытом до 3 лет: от 50 000 до 80 000 рублей в месяц. Биоэтик с опытом 3–7 лет: от 80 000 до 120 000 рублей в месяц. Специалист с опытом более 7 лет: от 120 000 рублей и выше в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f455c49536fe203457a9d3f77f8ada67/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button170':
            bot.send_message(call.message.chat.id,"Коуч -- Профессионал, объединяющий философию с психологией. Задачи личных или групповых коучей — разработка авторских методик по личностному развитию, выявлению талантов и способностей, проработке психологических травм и блоков.")
            bot.send_message(call.message.chat.id, "В России зарплата коуча может составлять 60 000–200 000 рублей, а в Москве — 100 000–350 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-227577916_456239061?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button171':
            bot.send_message(call.message.chat.id,"Социолог -- Рассматривает философию в качестве науки для изучения с целью полезного применения в обществе.")
            bot.send_message(call.message.chat.id, "Зарплата социолога в России составляет 30 000–91 000 рублей, а в Москве — 50 000–180 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-28944118_456239750?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button172':
            bot.send_message(call.message.chat.id,"Философский консультант -- Помогает клиентам осмыслить жизненные дилеммы, применяя логический анализ и этические рассуждения к конкретным ситуациям.")
            bot.send_message(call.message.chat.id, "Наиболее распространённая ставка для философских консультантов — от 75 до 150 долларов в час. Некоторые особенно востребованные практикующие специалисты с хорошими связями могут зарабатывать 450 долларов за часовую сессию.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/ceef669597186826981d261a2805fbe5/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)

#====================================================ГОТОВКА ЕДЫ
        if call.data == 'button21':
            keyboard = types.InlineKeyboardMarkup()
            button173 = types.InlineKeyboardButton(text="Шеф-повар", callback_data="button173")
            button174 = types.InlineKeyboardButton(text="Кондитер", callback_data="button174")
            button175 = types.InlineKeyboardButton(text="Пекарь", callback_data="button175")
            button176 = types.InlineKeyboardButton(text="Менеджер ресторана", callback_data="button176")
            button177 = types.InlineKeyboardButton(text="Технолог пищевой промышленности", callback_data="button177")
            button178 = types.InlineKeyboardButton(text="Повар-кондитер", callback_data="button178")
            button179 = types.InlineKeyboardButton(text="Фуд-блогер", callback_data="button179")
            bt18 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt18")
            keyboard.row(button173, button174)
            keyboard.row(button175, button179)
            keyboard.row(button176)
            keyboard.row(button178)
            keyboard.row(button177)
            keyboard.row(bt18)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)
        
        if call.data == 'button173':
            bot.send_message(call.message.chat.id,"Шеф-повар --  Отвечает за создание меню, управление кухней и приготовление блюд.")
            bot.send_message(call.message.chat.id, "Средняя зарплата шеф-повара в России в 2024 году — 99 794 рубля.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/b85859bdab20922c30502b4d769ae6eb/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button174':
            bot.send_message(call.message.chat.id,"Кондитер -- Занимается приготовлением десертов, тортов и других сладостей.")
            bot.send_message(call.message.chat.id, "Средняя зарплата кондитера в России в 2025 году — 64 759 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f11b704fbca1490813e716627ef2b390/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button175':
            bot.send_message(call.message.chat.id,"Пекарь -- Выпекает хлеб, булочки и другие изделия из теста.")
            bot.send_message(call.message.chat.id, "Средняя зарплата пекаря в России в 2025 году составляет 57 370 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/d784c936dc08463c933fd6b550948ee1/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button176':
            bot.send_message(call.message.chat.id,"Менеджер ресторана -- Отвечает за управление рестораном, координацию работы персонала, взаимодействие с клиентами и решение организационных вопросов.")
            bot.send_message(call.message.chat.id, "Средняя зарплата менеджера ресторана в России в 2025 году — 75 247 рублей. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 60 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f57ddcc7a67c74070dc5460546b90c95/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button177':
            bot.send_message(call.message.chat.id,"Технолог пищевой промышленности -- Разрабатывает рецепты для приготовления пищи, выбирает подходящее сырьё, следит за соблюдением санитарных и гигиенических норм.")
            bot.send_message(call.message.chat.id, "Средняя зарплата технолога пищевого производства в России составляет примерно от 40 000 до 80 000 рублей в месяц. Более опытные специалисты могут зарабатывать от 80 000 до 120 000 рублей и выше, в зависимости от конкретных условий труда и обязанностей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-224268130_456239036?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button178':
            bot.send_message(call.message.chat.id,"Повар-кондитер -- Готовит выпечку и десерты, следит за исправностью оборудования и чистотой рабочего места, декорирует сладкие блюда.")
            bot.send_message(call.message.chat.id, "Средняя зарплата повара-кондитера в России в 2025 году — 69 034 рубля.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-129894712_456239713?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button179':
            bot.send_message(call.message.chat.id,"Фуд-блогер -- Рассказывает подписчикам об интересных заведениях общепита или делится с ними оригинальными рецептами.")
            bot.send_message(call.message.chat.id, "Средний годовой доход фуд-блогеров — от 35 000 до 125 500 долларов в год.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/9e20f66d7ff01a97366f12b1b12d2bc7/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)

#============================================================Медицина💉💊
        if call.data == 'button15':
            keyboard = types.InlineKeyboardMarkup()
            button180 = types.InlineKeyboardButton(text="Гинеколог", callback_data="button180")
            button181 = types.InlineKeyboardButton(text="Дерматолог", callback_data="button181")
            button182 = types.InlineKeyboardButton(text="Кардиолог", callback_data="button182")
            button183 = types.InlineKeyboardButton(text="Офтальмолог", callback_data="button183")
            button184 = types.InlineKeyboardButton(text="Онколог", callback_data="button184")
            button185 = types.InlineKeyboardButton(text="Ортопед", callback_data="button185")
            button186 = types.InlineKeyboardButton(text="Оториноларинголог ", callback_data="button186")
            button187 = types.InlineKeyboardButton(text="Педиатр", callback_data="button187")
            button188 = types.InlineKeyboardButton(text="Психиатр", callback_data="button188")
            button189 = types.InlineKeyboardButton(text="Реаниматолог", callback_data="button189")
            button190 = types.InlineKeyboardButton(text="Стоматолог", callback_data="button190")
            button191 = types.InlineKeyboardButton(text="Терапевт", callback_data="button191")
            button192 = types.InlineKeyboardButton(text="Травматолог", callback_data="button192")
            button193 = types.InlineKeyboardButton(text="Уролог", callback_data="button193")
            button194 = types.InlineKeyboardButton(text="Фармацевт", callback_data="button194")
            button195 = types.InlineKeyboardButton(text="Венеролог", callback_data="button195")
            button0000000001 = types.InlineKeyboardButton(text="Хирург", callback_data="button0000000001")
            bt19 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt19")
            keyboard.row(button191, button193)
            keyboard.row(button184, button185)
            keyboard.row(button187, button188)
            keyboard.row(button180)
            keyboard.row(button181)
            keyboard.row(button182)
            keyboard.row(button183)
            keyboard.row(button186)
            keyboard.row(button189)
            keyboard.row(button190)
            keyboard.row(button192)
            keyboard.row(button194)
            keyboard.row(button195)
            keyboard.row(button0000000001)
            keyboard.row(bt19)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button180':
            bot.send_message(call.message.chat.id,"Гинеколог -- Занимается диагностикой и лечением гинекологических заболеваний.")
            bot.send_message(call.message.chat.id, "Зарплата гинеколога в России — 45 000–110 000 рублей, в Москве — 55 000–100 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/4abc55a925946d6c79062d5ee055be25/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button181':
            bot.send_message(call.message.chat.id,"Дерматолог -- Изучает строение, функционирование и заболевания кожи и её придатков — волос, ногтей, а также слизистых оболочек, методы их профилактики и лечения.")
            bot.send_message(call.message.chat.id, "Москва. Врач-дерматолог-косметолог может зарабатывать от 300 000 до 1 000 000 рублей в месяц. Санкт-Петербург. Заработная плата дерматологов варьируется от 100 000 до 300 000 рублей в месяц, в зависимости от опыта и квалификации.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/16824723784782198804'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button182':
            bot.send_message(call.message.chat.id,"Кардиолог -- Занимается изучением сердечно-сосудистой системы человека: строения и развития сердца и сосудов, их функций, а также заболеваний.")
            bot.send_message(call.message.chat.id, "Средняя зарплата кардиолога в Москве в 2025 году — 123 504 рубля. При этом модальная зарплата (наиболее часто встречающаяся) — 140 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-223488032_456239095?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button183':
            bot.send_message(call.message.chat.id,"Офтальмолог -- Специализируется на диагностике и лечении болезней органов зрения.")
            bot.send_message(call.message.chat.id, "Зарплата офтальмолога в России в марте 2025 года составляет 30 000–104 000 рублей, в Москве — 50 000–150 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/fe24e6447f0344bf7895ad52e3fa2f9d/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button184':
            bot.send_message(call.message.chat.id,"Онколог -- Изучает опухоли, их причины и условия происхождения и патогенез, методы профилактики и лечения.")
            bot.send_message(call.message.chat.id, "Москва. Онкологи зарабатывают от 150 000 до 200 000 рублей в месяц, в зависимости от квалификации и места работы. Санкт-Петербург. Средний доход специалистов составляет около 120 000 рублей в месяц, с возможностью увеличения в частных клиниках.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://ok.ru/video/6669208128221'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button185':
            bot.send_message(call.message.chat.id,"Ортопед -- Занимается диагностикой, лечением и профилактикой заболеваний опорно-двигательного аппарата: болезни и травмы костей, сухожилий, связок, суставов.")
            bot.send_message(call.message.chat.id, "Средняя зарплата ортопеда в России в 2024 году составила 105 500 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/ff61483966c4a615c298c92416603ec2/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button186':
            bot.send_message(call.message.chat.id,"Оториноларинголог --  Специализируется на диагностике и лечении уха, горла, носа, а также патологий головы и шеи.")
            bot.send_message(call.message.chat.id, "Средняя зарплата отоларинголога в России в 2025 году составляет 79 523 рубля. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 100 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-50207175_456246815?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button187':
            bot.send_message(call.message.chat.id,"Педиатр -- Занимается лечением заболеваний у детей, начиная с младенческого возраста.")
            bot.send_message(call.message.chat.id, "Зарплата педиатра (детского врача) в России составляет от 36 000 до 110 000 рублей, в Москве — от 80 000 до 200 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/8da8f81bfc0561a56c6ee974974d1f20/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button188':
            bot.send_message(call.message.chat.id,"Психиатр -- Работает с людьми, страдающими от различных психических расстройств.")
            bot.send_message(call.message.chat.id, "Врач-психиатр зарабатывает в среднем от 70 000 до 220 000 рублей в месяц. В государственных клиниках нижняя граница зарплаты составляет около 70 000–100 000 рублей, в частных клиниках доход может достигать 150 000–220 000 рублей при совмещении нескольких мест работы.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/22a0a8e693af534f040be5a2ee997b03/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button189':
            bot.send_message(call.message.chat.id,"Реаниматолог -- Занимается реанимацией (поддержанием и восстановлением жизненно важных функций организма).")
            bot.send_message(call.message.chat.id, "Зарплата анестезиолога-реаниматолога в России в марте 2025 года может составлять 70 000–150 000 рублей, а в Москве — 80 000–220 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-165213420_456240977?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button190':
            bot.send_message(call.message.chat.id,"Стоматолог -- Специализируется на лечении болезней зубов, челюстей и других органов ротовой полости.")
            bot.send_message(call.message.chat.id, "Средняя зарплата врача-стоматолога в России — 95 000 рублей. Чаще всего зарплаты находятся в диапазоне от 40 000 до 150 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/b32c9110b6b9a434776fe7af571096e9/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button191':
            bot.send_message(call.message.chat.id,"Терапевт -- Занимается диагностикой, изучением причин, лечением и профилактикой заболеваний внутренних органов.")
            bot.send_message(call.message.chat.id, "В частных клиниках Москвы терапевт может зарабатывать до 350 тысяч рублей, в Санкт-Петербурге — до 300 тысяч рублей, в Самаре — до 240 тысяч рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/5beb9c4afc17ee2c47ffa79bf14f0df7/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button192':
            bot.send_message(call.message.chat.id,"Травматолог -- Изучает воздействие на организм человека различных травмирующих воздействий, последствия травм, методы их лечения.")
            bot.send_message(call.message.chat.id, "Начинающий специалист в малом городе. Зарабатывает от 35 000 до 60 000 рублей в месяц, работая в государственной поликлинике или больнице. Опытный врач в среднем городе. Получает от 60 000 до 90 000 рублей в месяц при работе в стационаре, приёмном покое или травматологическом отделении. равматолог в крупном городе (Москва, Санкт-Петербург, Казань и др.). Заработок составляет от 90 000 до 150 000 рублей в месяц, особенно при совмещении с дежурствами и операционной деятельностью.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://ok.ru/video/6434234042961'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button193':
            bot.send_message(call.message.chat.id,"Уролог -- Изучает заболевания органов мочевой системы, мужской половой системы, заболеваний надпочечников и других патологических процессов в забрюшинном пространстве и разрабатывает методы их лечения и профилактики.")
            bot.send_message(call.message.chat.id, "Москва. Урологи зарабатывают от 110 000 до 195 000 рублей в месяц, в зависимости от квалификации и места работы. Санкт-Петербург. Средний доход специалистов составляет около 70 000 рублей в месяц, с возможностью увеличения в частных клиниках.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/a8fef0e701c19a63f4b4a374be44ef33/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button194':
            bot.send_message(call.message.chat.id,"Фармацевт --  Готовит лекарства по рецептам врачей, обеспечивает хранение и комплектование медикаментов, отпускает готовые лекарства без рецептов, оказывает первую доврачебную помощь.")
            bot.send_message(call.message.chat.id, "Фармацевт зарабатывает от 78 000 ₽ за месяц, до вычета налогов")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-126291013_456239033?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button195':
            bot.send_message(call.message.chat.id,"Венеролог -- Изучает и лечит инфекции, передающиеся половым путём.")
            bot.send_message(call.message.chat.id, "В негосударственных организациях венеролог с опытом работы и всеми необходимыми действующими документами может зарабатывать ежемесячно от 100 000 рублей. В государственном учреждении здравоохранения врач в среднем зарабатывает около 40 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/972e8959f1a360173f479b6bc14f39c8/?r=plwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button0000000001':
            bot.send_message(call.message.chat.id,"Хирург -- врач, специализирующийся на проведении хирургических операций для лечения различных заболеваний, травм и патологий.")
            bot.send_message(call.message.chat.id, "Cредняя зарплата хирурга в России в 2025 году — 92 811 рублей. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 100 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/55fb5023ee8eec07003358a19dc2dce8/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
#=======================================================================ФИНАНСЫ
        if call.data == 'button18':
            keyboard = types.InlineKeyboardMarkup()
            button196 = types.InlineKeyboardButton(text="Финансовый аналитик", callback_data="button196")
            button197 = types.InlineKeyboardButton(text="Аудитор", callback_data="button197")
            button198 = types.InlineKeyboardButton(text="Бухгалтер", callback_data="button198")
            button199 = types.InlineKeyboardButton(text="Финансовый консультант", callback_data="button199")
            button200 = types.InlineKeyboardButton(text="Риск-менеджер", callback_data="button200")
            button201 = types.InlineKeyboardButton(text="Финансовый директор", callback_data="button201")
            button202 = types.InlineKeyboardButton(text="Экономист", callback_data="button202")
            button203 = types.InlineKeyboardButton(text="Экономист-финансист", callback_data="button203")
            bt20 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt20")
            keyboard.row(button196)
            keyboard.row(button197, button198)
            keyboard.row(button199)
            keyboard.row(button200)
            keyboard.row(button201)
            keyboard.row(button202)
            keyboard.row(button203)
            keyboard.row(bt20)
            bot.send_message(call.message.chat.id, "Нажмите на профессию, про которую вы хотите узнать больше интересных фактов",reply_markup=keyboard)

        if call.data == 'button196':
            bot.send_message(call.message.chat.id,"Финансовый аналитик -- Специалист анализирует финансовое состояние компаний, рынков и инвестиционных проектов.")
            bot.send_message(call.message.chat.id, "Начинающие специалисты (опыт до 1–2 лет). Финансовые аналитики без опыта или с минимальным стажем работы получают в среднем 70 000–100 000 рублей в месяц. Специалисты среднего звена (опыт 2–5 лет). Аналитики с опытом работы от 2 до 5 лет зарабатывают в среднем 120 000–200 000 рублей в месяц. Опытные аналитики (опыт более 5 лет). Финансовые аналитики с опытом работы более 5 лет и хорошим послужным списком могут рассчитывать на зарплату от 200 000 до 350 000 рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/f7bae49b52a218b496ff962faa6fd0a3/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button197':
            bot.send_message(call.message.chat.id,"Аудитор -- Проверяет финансовую отчётность компаний на соответствие законодательству и стандартам бухгалтерского учёта.")
            bot.send_message(call.message.chat.id, "Средняя зарплата аудитора в России — 69 000 рублей. Чаще всего зарплаты находятся в диапазоне от 42 000 до 95 000 рублей. Минимальная зафиксированная зарплата — 30 000 рублей, максимальная — 220 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-41197189_456239787?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button198':
            bot.send_message(call.message.chat.id,"Бухгалтер -- Ведёт учёт финансовых операций компаний, составляет финансовую отчётность и обеспечивает соблюдение налогового законодательства.")
            bot.send_message(call.message.chat.id, "Средняя зарплата бухгалтера в России в 2025 году — 65 472 рубля. При этом модальная зарплата (наиболее часто встречающаяся сумма) — 50 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://yandex.ru/video/preview/10281651685906592087'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button199':
            bot.send_message(call.message.chat.id,"Финансовый консультант -- Помогает людям и компаниям управлять своими финансами, разрабатывает инвестиционные стратегии, планирует бюджет и консультирует по вопросам налогообложения.")
            bot.send_message(call.message.chat.id, "Некоторые средние зарплаты: начинающий консультант: 45 000–70 000 рублей; консультант с опытом 2–3 года: 80 000–120 000 рублей; ведущий консультант: 130 000–200 000 рублей; персональный финансовый советник: от 250 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-100885008_456240951?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button200':
            bot.send_message(call.message.chat.id,"Риск-менеджер -- Занимается оценкой и управлением финансовыми рисками, с которыми сталкиваются компании.")
            bot.send_message(call.message.chat.id, "Начальный уровень: аналитик по управлению рисками — около 50 000–80 000 рублей в месяц. Средний уровень: старший аналитик по управлению рисками — около 120 000–180 000 рублей в месяц. Высший уровень: директор по управлению рисками — около 250 000–400 000 рублей в месяц, возможны бонусы и дополнительные льготы. Вице-президент по управлению рисками: около 400 000–700 000 рублей в месяц, плюс бонусы и дополнительные льготы.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-140226666_456239159?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button201':
            bot.send_message(call.message.chat.id,"Финансовый директор -- Отвечает за экономическую, финансовую и инвестиционную стороны жизни бизнеса.")
            bot.send_message(call.message.chat.id, "В столице средний уровень зарплат варьируется от 600 000 до 1 500 000 рублей в месяц, а в Санкт-Петербурге — от 450 000 до 1 200 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://vkvideo.ru/video-32342123_456243038?ref_domain=yastatic.net'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button202':
            bot.send_message(call.message.chat.id,"Экономист -- Исследует, планирует и сопровождает экономическую сторону финансово-хозяйственной деятельности компании.")
            bot.send_message(call.message.chat.id, "Новичок может получать около 35 тысяч рублей. Опытный специалист с навыками управления может зарабатывать от 60–70 тысяч рублей. Для этого нужно проработать в сфере 1–3 года. На должностях ведущего или главного экономиста зарплата составляет около 200 тысяч рублей. Финансовый директор зарабатывает от 250 тысяч рублей в месяц.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/5d9d2706b36c378787ad54086bf56da1/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
        if call.data == 'button203':
            bot.send_message(call.message.chat.id,"Экономист-финансист -- Занимается выполнением различных финансовых операций: составляет финансовые сметы и отчёты, контролирует проведение биржевых операций и налогообложение, проведение различных торговых операций, анализирует финансовые документы.")
            bot.send_message(call.message.chat.id, "Зарплата экономиста-финансиста в России — 37 800–81 000 рублей, в Москве — 100 000–150 000 рублей.")
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Тык', url='https://rutube.ru/video/8eeb683b6121b669c96c8881ddfef949/?r=plemwd'))
            bot.send_message(call.message.chat.id, "Нажми на кнопку, чтобы лучше ознакомиться с данной профессией(видео)", reply_markup=markup)
            
            
#==========================================================================================================================================
#==========================================================================================================================================
#==========================================================================================================================================
#==========================================================================================================================================
#==========================================================================================================================================
#==========================================================================================================================================
#==========================================================================================================================================
#==========================================================================================================================================
#==========================================================================================================================================


        if call.data == "button7777777777":
            keyboard = types.InlineKeyboardMarkup()
            button204 = types.InlineKeyboardButton(text="Математические предметы", callback_data='button204')
            button205 = types.InlineKeyboardButton(text="Гуманитарные науки", callback_data='button205')
            button223 = types.InlineKeyboardButton(text="Естественно научные предметы", callback_data='button223')
            keyboard.row(button204)
            keyboard.row(button205)
            keyboard.row(button223)
            bot.send_message(call.message.chat.id, "Выберете раздел, который вам нравится или нравился в школе", reply_markup=keyboard)
         
        if call.data == 'button204':
            keyboard = types.InlineKeyboardMarkup()
            button206 = types.InlineKeyboardButton(text="Алгебра", callback_data='button206')
            button207 = types.InlineKeyboardButton(text="Геометрия", callback_data='button207')
            button208 = types.InlineKeyboardButton(text="Планиметрия", callback_data='button208')
            button232 = types.InlineKeyboardButton(text="Высшая математика", callback_data='button232')
            button233 = types.InlineKeyboardButton(text="Тригонометрия", callback_data='button233')
            button234 = types.InlineKeyboardButton(text="Стереометрия", callback_data='button234')
            button250 = types.InlineKeyboardButton(text="Ознакомиться🔎", callback_data='button250')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button206)
            keyboard.row(button207)
            keyboard.row(button208)
            keyboard.row(button232)
            keyboard.row(button233)
            keyboard.row(button234)
            keyboard.row(button250)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите предмет, который вы больше всего знаете. Если вы не понимаете значение какого-то предмета, то нажмите на --Ознакомиться--.", reply_markup=keyboard)
            
        if call.data == 'button250':
            keyboard = types.InlineKeyboardMarkup()
            button251 = types.InlineKeyboardButton(text="Алгебра", callback_data='button251')
            button252 = types.InlineKeyboardButton(text="Геометрия", callback_data='button252')
            button253 = types.InlineKeyboardButton(text="Планиметрия", callback_data='button253')
            button254 = types.InlineKeyboardButton(text="Высшая математика", callback_data='button254')
            button255 = types.InlineKeyboardButton(text="Тригонометрия", callback_data='button255')
            button256 = types.InlineKeyboardButton(text="Стереометрия", callback_data='button256')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button251)
            keyboard.row(button252)
            keyboard.row(button253)
            keyboard.row(button254)
            keyboard.row(button255)
            keyboard.row(button256)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите предмет, с которым вы хотите ознакомиться.", reply_markup=keyboard)
            
        if call.data == 'button251':
            bot.send_message(call.message.chat.id, "Алгебра -- это раздел математики, посвящённый изучению операций над элементами множеств произвольной природы, обобщающий обычные операции сложения и умножения чисел.")
        if call.data == 'button252':
            bot.send_message(call.message.chat.id, "Геометрия -- это раздел математики, изучающий пространственные структуры и отношения, а также их обобщения. Охватывает разнообразные аспекты: от простых двухмерных форм (треугольники, круги) до трёхмерных объектов (сферы, кубы)")
        if call.data == 'button253':
            bot.send_message(call.message.chat.id, "Планиметрия -- это раздел геометрии, изучающий свойства фигур, расположенных на плоскости.")
        if call.data == 'button254':
            bot.send_message(call.message.chat.id, "Высшая математика -- это это совокупность разделов математики, которые изучают абстрактные структуры и их свойства, не относящихся к элементарной математике. Также так называют курс обучения в средних и высших учебных заведениях, включающий высшую алгебру и математический анализ.")
        if call.data == 'button255':
            bot.send_message(call.message.chat.id, "Тригонометрия -- это раздел математики, изучающий отношения между сторонами и углами треугольников. Основана на тригонометрических функциях, которые описывают отношения между углами и сторонами прямоугольного треугольника.")
        if call.data == 'button256':
            bot.send_message(call.message.chat.id, "Стереометрия -- это раздел геометрии, в котором изучаются свойства пространственных фигур, то есть фигур, не принадлежащих одной плоскости.")
        
        
        if call.data == 'button206':
            keyboard = types.InlineKeyboardMarkup()
            button275 = types.InlineKeyboardButton(text="Начальная алгебра", callback_data='button275')
            button276 = types.InlineKeyboardButton(text="Квадратичные уравнения", callback_data='button276')
            button277 = types.InlineKeyboardButton(text="Степени и радикалы", callback_data='button277')
            button278 = types.InlineKeyboardButton(text="Логарифмы и экспоненты", callback_data='button278')
            button279 = types.InlineKeyboardButton(text="Матрицы и вектора", callback_data='button279')
            button280 = types.InlineKeyboardButton(text="Комплексные числа ", callback_data='button280')
            button281 = types.InlineKeyboardButton(text="Теория вероятностей", callback_data='button281')
            button282 = types.InlineKeyboardButton(text="Дискретная математика", callback_data='button282')
            button293 = types.InlineKeyboardButton(text="Ознакомиться🔎", callback_data='button293')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button275)
            keyboard.row(button276)
            keyboard.row(button277)
            keyboard.row(button278)
            keyboard.row(button279)
            keyboard.row(button280)
            keyboard.row(button281)
            keyboard.row(button282)
            keyboard.row(button293)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите раздел, который вы больше всего знаете. Если вы не понимаете значение какого-то предмета, то нажмите на --Ознакомиться--.", reply_markup=keyboard)
            
        if call.data == 'button293':
            keyboard = types.InlineKeyboardMarkup()
            button294 = types.InlineKeyboardButton(text="Начальная алгебра", callback_data='button294')
            button295 = types.InlineKeyboardButton(text="Квадратичные уравнения", callback_data='button295')
            button296 = types.InlineKeyboardButton(text="Степени и радикалы", callback_data='button296')
            button297 = types.InlineKeyboardButton(text="Логарифмы и экспоненты", callback_data='button297')
            button298 = types.InlineKeyboardButton(text="Матрицы и вектора", callback_data='button298')
            button299 = types.InlineKeyboardButton(text="Комплексные числа", callback_data='button299')
            button300 = types.InlineKeyboardButton(text="Теория вероятностей", callback_data='button300')
            button301 = types.InlineKeyboardButton(text="Дискретная математика", callback_data='button301')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button294)
            keyboard.row(button295)
            keyboard.row(button296)
            keyboard.row(button297)
            keyboard.row(button298)
            keyboard.row(button299)
            keyboard.row(button300)
            keyboard.row(button301)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите раздел, c которым вы хотите ознакомиться", reply_markup=keyboard)
            
            
        if call.data == 'button294':
            bot.send_message(call.message.chat.id, "Начальная алгебра -- это решение линейных уравнений, неравенств, графиков, систем уравнений и неравенств.")
        if call.data == 'button295':
            bot.send_message(call.message.chat.id, "Квадратичные уравнения -- это алгебраическое уравнение второй степени вида")
        if call.data == 'button296':
            bot.send_message(call.message.chat.id, "Степени и радикалы -- это понятия в математике, связанные с разными операциями: многократным умножением числа на само себя и извлечением корня из числа или выражения.")
        if call.data == 'button297':
            bot.send_message(call.message.chat.id, "Логарифмы и экспоненты -- это оказатель степени, в которую нужно возвести основание, чтобы получить заданное число. Логарифмы — обратная операция возведения в степень.")
        if call.data == 'button298':
            bot.send_message(call.message.chat.id, "Матрицы и вектора -- это упорядоченная таблица чисел, которая представляет собой совокупность строк и столбцов, на пересечении которых находятся её элементы. Матрицы используют для решения уравнений и работы с линейными преобразованиями.")
        if call.data == 'button299':
            bot.send_message(call.message.chat.id, "Комплексные числа -- это числа, которые представляют собой комбинацию действительного и мнимого чисел. Они используются в математике для расширения понятия числовых систем, например, для решения задач, которые невозможно было решить в действительных числах.")
        if call.data == 'button300':
            bot.send_message(call.message.chat.id, "Теория вероятностей -- это раздел математики, изучающий законы и закономерности случайных явлений и экспериментов. Ее цель — описать неопределённость и предсказать поведение случайных событий с некоторой степенью точности.")
        if call.data == 'button301':
            bot.send_message(call.message.chat.id, "Дискретная математика -- это раздел математики, изучающий дискретные структуры — объекты, состоящие из отдельных, чётко различимых элементов, в отличие от непрерывных структур, которые могут принимать любые значения в определённых пределах.")
            
        if call.data == 'button275':
            keyboard = types.InlineKeyboardMarkup()
            button302 = types.InlineKeyboardButton(text="Экономисты", callback_data='button302')
            button303 = types.InlineKeyboardButton(text="Бухгалтеры", callback_data='button303')
            button304 = types.InlineKeyboardButton(text="Специалисты по продажам", callback_data='button304')
            button305 = types.InlineKeyboardButton(text="Программисты", callback_data='button305')
            button306 = types.InlineKeyboardButton(text="Проектировщики", callback_data='button306')
            button307 = types.InlineKeyboardButton(text="Медицинские работники", callback_data='button307')
            button308 = types.InlineKeyboardButton(text="Учёные", callback_data='button308')
            button309 = types.InlineKeyboardButton(text="Педагоги", callback_data='button309')
            button310 = types.InlineKeyboardButton(text="Электрики", callback_data='button310')
            button311 = types.InlineKeyboardButton(text="Ознакомиться🔎", callback_data='button311')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button302)
            keyboard.row(button303)
            keyboard.row(button304)
            keyboard.row(button305)
            keyboard.row(button306)
            keyboard.row(button307)
            keyboard.row(button308)
            keyboard.row(button309)
            keyboard.row(button310)
            keyboard.row(button311)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите раздел, который вам больше всего нравится. Если вы не понимаете значение какого-то предмета, то нажмите на --Ознакомиться--.", reply_markup=keyboard)
            
        if call.data == 'button304':
            keyboard = types.InlineKeyboardMarkup()
            button337 = types.InlineKeyboardButton(text="Менеджер по продажам", callback_data='button337')
            button338 = types.InlineKeyboardButton(text="Торговый представитель", callback_data='button338')
            button339 = types.InlineKeyboardButton(text="Менеджер по работе с клиентами", callback_data='button339')
            button340 = types.InlineKeyboardButton(text="Специалист по закупкам", callback_data='button340')
            button341 = types.InlineKeyboardButton(text="Менеджер по развитию бизнеса", callback_data='button341')
            button342 = types.InlineKeyboardButton(text="Менеджер по дистрибуции", callback_data='button342')
            button343 = types.InlineKeyboardButton(text="Специалист по маркетингу", callback_data='button343')
            button344 = types.InlineKeyboardButton(text="Менеджер по интернет-продажам", callback_data='button344')
            button345 = types.InlineKeyboardButton(text="Менеджер по корпоративным продажам", callback_data='button345')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button337)
            keyboard.row(button338)
            keyboard.row(button339)
            keyboard.row(button340)
            keyboard.row(button341)
            keyboard.row(button342)
            keyboard.row(button343)
            keyboard.row(button344)
            keyboard.row(button345)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите профессию, который вам больше всего нравится.", reply_markup=keyboard)
            
        if call.data == 'button337':
            bot.send_message(call.message.chat.id, "Менеджер по продажам -- это специалист, который занимается продвижением товаров или услуг компании, взаимодействует с клиентами и обеспечивает выполнение планов продаж.")
            bot.send_message(call.message.chat.id, " В большинстве случаев зарплата состоит из двух частей: оклада и премии. Премию платят за результат — например, в виде процента от продаж. ")
        if call.data == 'button338':
            bot.send_message(call.message.chat.id, "Торговый представитель -- это  специалист в области продаж и маркетинга, который представляет продукцию или услуги компании перед потенциальными клиентами, партнёрами или розничными точками продаж.")
            bot.send_message(call.message.chat.id, '''Размер заработной платы торгового представителя зависит от компании, обязанностей и опыта работы. 
Эксклюзивный торговый представитель в ГК «Черноголовка» — от 120 000 рублей, полный рабочий день, опыт от 1 года. 
Торговый представитель/менеджер по продажам в ООО «Элитные Агросистемы» — от 85 000 рублей, полный рабочий день, опыт от 1 года.''')
        if call.data == 'button339':
            bot.send_message(call.message.chat.id, "Менеджер по работе с клиентами-- это специалист, который выступает связующим звеном между компанией и её покупателями. Его задача — создавать долгосрочные отношения, помогая бизнесу становиться успешнее.")
            bot.send_message(call.message.chat.id, "Средняя зарплата менеджера по работе с клиентами в России в 2025 году — 57 000 рублей. Чаще всего зарплаты находятся в диапазоне от 38 000 до 75 000 рублей. Минимальная зафиксированная зарплата — 30 000 рублей, максимальная — 650 000 рублей.")
        if call.data == 'button340':
            bot.send_message(call.message.chat.id, "Специалист по закупкам -- это профессионал, который отвечает за приобретение товаров, услуг и материалов для организации.")
            bot.send_message(call.message.chat.id, '''Примерный доход эксперта по закупкам: 
Новички (0–2 года опыта) — 35 000–55 000 рублей. 
Опытные (2–5 лет стажа) — 55 000–85 000 рублей. 
Профи (5+ лет опыта) — 85 000–150 000+ рублей.''')
        if call.data == 'button341':
            bot.send_message(call.message.chat.id, "Менеджер по развитию бизнеса -- это специалист, который отвечает за поиск и реализацию новых возможностей для роста компании. Он анализирует рыночные тренды, разрабатывает стратегии для расширения бизнеса, ведёт переговоры с потенциальными партнёрами и помогает компании выйти на новые рынки. ")
            bot.send_message(call.message.chat.id, '''Заработная плата может отличаться в зависимости от города: 
Москва — 115 000 рублей; 
Санкт-Петербург — 100 000 рублей; 
Красноярск — 90 000 рублей; 
Воронеж — 80 000 рублей; 
Екатеринбург — 75 000 рублей.''')
        if call.data == 'button342':
            bot.send_message(call.message.chat.id, "Менеджер по дистрибуции -- это специалист, который отвечает за продвижение товаров от производителя к конечному потребителю. Его работа включает организацию каналов продаж, стимулирование сбыта и внедрение маркетинговых стратегий. ")
            bot.send_message(call.message.chat.id, '''Размер заработной платы может отличаться в зависимости от города: 
Москва — 133 000 рублей; 
Рязань — 100 000 рублей; 
Ростов-на-Дону — 100 000 рублей''')
        if call.data == 'button343':
            bot.send_message(call.message.chat.id, "Специалист по маркетингу - это профессионал, который создаёт и реализует стратегии продвижения продуктов или услуг компании на рынке. ")
            bot.send_message(call.message.chat.id, "Заработная плата зависит от уровня компетенций специалиста, типа занятости, локации работодателя и других факторов. Средний размер оплаты труда маркетолога — 106 940 рублей в месяц.")
        if call.data == 'button344':
            bot.send_message(call.message.chat.id, "Менеджер по интернет-продажам -- это специалист, который отвечает за организацию и развитие продаж товаров или услуг через интернет. ")
            bot.send_message(call.message.chat.id, '''Размер заработной платы может отличаться в зависимости от города: 
Химки — 75 000 рублей; 
Москва — 55 000 рублей;
Санкт-Петербург — 48 000 рублей''')
        if call.data == 'button345':
            bot.send_message(call.message.chat.id, "Менеджер по корпоративным продажам -- это специалист, который отвечает за взаимодействие с ключевыми клиентами компании (B2B-сегмент). В отличие от обычного менеджера по продажам, он работает с крупными заказчиками, заключает долгосрочные контракты и выстраивает стратегические партнёрства.")
            bot.send_message(call.message.chat.id, "Средняя зарплата менеджера по корпоративным продажам в Самаре — 82 453 рубля, медианная — 84 929 рублей, модальная (наиболее часто встречающаяся) — 90 000 рублей.")
            
            
        if call.data == 'button305':
            keyboard = types.InlineKeyboardMarkup()
            button357 = types.InlineKeyboardButton(text="Веб-разработчик", callback_data='button357')
            button358 = types.InlineKeyboardButton(text="Мобильный разработчик", callback_data='button358')
            button359 = types.InlineKeyboardButton(text="Системный администратор", callback_data='button359')
            button360 = types.InlineKeyboardButton(text="Администратор баз данных", callback_data='button360')
            button361 = types.InlineKeyboardButton(text="Инженер по кибербезопасности", callback_data='button361')
            button362 = types.InlineKeyboardButton(text="Инженер по DevOps", callback_data='button362')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button357)
            keyboard.row(button358)
            keyboard.row(button359)
            keyboard.row(button360)
            keyboard.row(button361)
            keyboard.row(button362)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите профессию, который вам больше всего нравится.", reply_markup=keyboard)
            
        if call.data == 'button357':
            bot.send_message(call.message.chat.id, "Веб-разработчик -- это  это специалист, который занимается созданием и поддержкой сайтов и веб-приложений. Он может работать как над внешним видом, так и над внутренней частью сайта.")
            bot.send_message(call.message.chat.id, "Заработная плата зависит от уровня компетенций специалист: Junior — 82 825 рублей в месяц; Senior — 187 529 рублей в месяц; Lead — 217 500 рублей в месяц.")
        if call.data == 'button358':
            bot.send_message(call.message.chat.id, "Мобильный разработчик -- это специалист, который создаёт программное обеспечение для мобильных устройств, таких как смартфоны и планшеты. Он работает с платформами iOS и Android.")
            bot.send_message(call.message.chat.id, '''Некоторые размеры зарплат в зависимости от уровня специалиста:
Junior-разработчики без опыта работы получают от 50 до 80 тысяч рублей в месяц.
Middle-разработчики с опытом от одного до трёх лет могут зарабатывать 200 тысяч рублей в месяц и выше.
Senior-специалисты с опытом более трёх лет вносят значительный вклад в разработку и управление проектами. Их заработок начинается от 250 тысяч рублей в месяц и может быть выше.''')
        if call.data == 'button359':
            bot.send_message(call.message.chat.id, "Системный администратор -- это специалист в области информационных технологий, отвечающий за бесперебойную работу IT-инфраструктуры компании. Он устанавливает и настраивает операционные системы, следит за состоянием серверов и сетей, обеспечивает безопасность данных и помогает сотрудникам в решении технических вопросов.")
            bot.send_message(call.message.chat.id, '''Начинающий специалист (Junior) — 50 000–70 000 рублей в месяц;
сисадмин с опытом (Middle) — 80 000–120 000 рублей;
опытный специалист (Senior) — от 120 000 рублей и выше.''')
        if call.data == 'button360':
            bot.send_message(call.message.chat.id, "Администратор баз данных -- это специалист, отвечающий за управление, обслуживание и оптимизацию баз данных в компании. Его главная задача — обеспечить доступность, целостность и безопасность данных, которые являются основой для принятия управленческих решений, анализа, работы клиентских приложений и внутренних бизнес-процессов. ")
            bot.send_message(call.message.chat.id, "Зарплата администратора базы данных в России составляет 34 000–120 000 рублей, в Москве — 40 000–120 000 рублей.")
        if call.data == 'button361':
            bot.send_message(call.message.chat.id, "Инженер по кибербезопасности -- это эксперт, который отвечает за разработку, внедрение и поддержку систем защиты информации.")
            bot.send_message(call.message.chat.id, '''Зарплата инженера по кибербезопасности зависит от опыта, уровня квалификации, региона и конкретной компании:
Начинающий специалист (Junior) может рассчитывать на оклад в пределах 50–80 тыс. рублей в месяц.
Специалист среднего уровня (Middle) в регионах получает в среднем от 90 000 до 140 000 рублей в месяц.
Опытные сотрудники (Senior) в регионах получают от 150 до 220 тыс. рублей в месяц.''')
        if call.data == 'button362':
            bot.send_message(call.message.chat.id, "Инженер по DevOps -- это специалист, который объединяет процессы разработки и эксплуатации программного обеспечения. Аббревиатура DevOps образована от английских слов development («разработка») и operations («эксплуатация»).")
            bot.send_message(call.message.chat.id, '''По данным сервиса GeekLink,  средняя зарплата DevOps-инженеров в зависимости от грейда:
junior — 116 000 рублей;
middle — 223 986 рублей;
senior — 296 027 рублей;
lead — 437 529 рублей.''')
            
            
        if call.data == 'button306':
            keyboard = types.InlineKeyboardMarkup()
            button390 = types.InlineKeyboardButton(text="Архитектор", callback_data='button390')
            button391 = types.InlineKeyboardButton(text="Инженер-проектировщик", callback_data='button391')
            button392 = types.InlineKeyboardButton(text="Дизайнер", callback_data='button392')
            button393 = types.InlineKeyboardButton(text="Инженер-конструктор", callback_data='button393')
            button394 = types.InlineKeyboardButton(text="Системный архитектор", callback_data='button394')
            button395 = types.InlineKeyboardButton(text="Инженер по автоматизации", callback_data='button395')
            button396 = types.InlineKeyboardButton(text="Инженер по экологии", callback_data='button396')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button390)
            keyboard.row(button391)
            keyboard.row(button392)
            keyboard.row(button393)
            keyboard.row(button394)
            keyboard.row(button395)
            keyboard.row(button396)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите профессию, который вам больше всего нравится.", reply_markup=keyboard)
        
        if call.data == 'button390':
            bot.send_message(call.message.chat.id, "Архитектор -- это специалист, который занимается проектированием зданий и других объектов, а также контролирует процесс строительства.")
            bot.send_message(call.message.chat.id, '''Заработная плата архитектора зависит от его опыта работы, занимаемой должности, региона и других факторов:
Начинающие специалисты получают 30 000–70 000 рублей в месяц.
Специалисты с опытом работы — 60 000–200 000 рублей в месяц.
Главные архитекторы и руководители архитектурных бюро зарабатывают 150 000–400 000 рублей в месяц.''')
        if call.data == 'button391':
            bot.send_message(call.message.chat.id, "Инженер-проектировщик -- это специалист, который отвечает за разработку проектов различных объектов, таких как здания, мосты, дороги или сложные инженерные системы.")
            bot.send_message(call.message.chat.id, '''Опыт работы:
Новички — на старте карьеры заработок проектировщика редко превышает 40 000–60 000 рублей в месяц. 
Средний уровень — после 2–5 лет работы уровень зарплаты может достигать 70 000–120 000 рублей.
Профессионалы — специалисты с опытом от 5 лет и выше, работающие на крупных проектах, зарабатывают 150 000–300 000 рублей ежемесячно, а иногда и больше.
Специализация. Например, в нефтегазовой отрасли средний доход инженера — 110 000–180 000 рублей, а ведущие специалисты и руководители проектных групп — до 250 000–350 000 рублей в месяц. ''')
        if call.data == 'button392':
            bot.send_message(call.message.chat.id, "Дизайнер -- это общее название профессии для специалистов, которые разрабатывают визуальные концепции, макеты и продукты в разных индустриях: от рекламы до моды.")
            bot.send_message(call.message.chat.id, '''Некоторые направления дизайна и предполагаемый уровень зарплаты:
UX/UI-дизайн. Специалисты изучают поведение пользователей, создают логику взаимодействия и проектируют интерфейсы. Зарплаты — от 100 до 350 тысяч рублей.
Моушн-дизайн. Специалисты создают анимацию для рекламы, интерфейсов, игр и социальных сетей. Доходы — от 70 до 200+ тысяч рублей.
Графический дизайн. Специалисты разрабатывают логотипы, фирменные стили, рекламные материалы. Зарплаты — от 40 до 150 тысяч рублей.
3D-дизайн. С помощью 3D-графики создают почти все современные фильмы и компьютерные игры. Доходы — от 80 до 300+ тысяч рублей.
Продуктовый дизайн. Специалисты работают над цифровыми продуктами на всех этапах — от исследований до запуска. Зарплаты — от 150 до 400 тысяч рублей.''')
        if call.data == 'button393':
            bot.send_message(call.message.chat.id, "Инженер-конструктор -- это специалист, который разрабатывает, проектирует и оптимизирует технические изделия, механизмы и конструкции.")
            bot.send_message(call.message.chat.id, '''Стаж и уровень компетенции:
Новичок (0–1 год, без опыта) — 45 000–65 000 рублей.
Младший инженер с опытом до 2 лет — 65 000–90 000 рублей.
Инженер-конструктор с опытом 3–5 лет — 90 000–130 000 рублей.
Ведущий инженер, главный конструктор — от 150 000 рублей и выше.''')
        if call.data == 'button394':
            bot.send_message(call.message.chat.id, "Системный архитектор -- это специалист, который отвечает за проектирование и внедрение сложных информационных систем. Он разрабатывает общую структуру системы, определяет взаимодействие компонентов и обеспечивает соответствие решения требованиям бизнеса.")
            bot.send_message(call.message.chat.id, "Средняя зарплата системного архитектора в России — 220 000 рублей на руки. Чаще всего зарплаты находятся в диапазоне от 120 000 до 320 000 рублей. Минимальная зафиксированная зарплата — 50 000 рублей, максимальная — 500 000 рублей. ")
        if call.data == 'button395':
            bot.send_message(call.message.chat.id, "Инженер по автоматизации -- это специалист, который разрабатывает, настраивает и поддерживает системы автоматизации, используемые в различных отраслях промышленности и производства.")
            bot.send_message(call.message.chat.id, '''Примерные диапазоны зарплат в зависимости от уровня опыта: 
Начинающий специалист (Junior) — 60 000–90 000 рублей;
Опытный (Middle) — 100 000–180 000 рублей;
Ведущий инженер (Senior) — 200 000–300 000 рублей (особенно в нефтегазе и энергетике).''')
        if call.data == 'button396':
            bot.send_message(call.message.chat.id, "Инженер по экологии -- это специалист, который разрабатывает и внедряет мероприятия по охране окружающей среды на промышленных предприятиях и в организациях.")
            bot.send_message(call.message.chat.id, '''Распределение заработной платы по уровню опыта:
Начинающий специалист (0–2 года опыта) — 30–50 тысяч рублей.
Специалист с опытом (3–5 лет) — 50–80 тысяч рублей.
Ведущий инженер-эколог (5–10 лет) — 70–120 тысяч рублей.
Главный эколог предприятия (10+ лет) — 100–200 тысяч рублей.''')
            
        if call.data == 'button307':
            keyboard = types.InlineKeyboardMarkup()
            button397 = types.InlineKeyboardButton(text="Врач", callback_data='button397')
            button398 = types.InlineKeyboardButton(text="Медсестра", callback_data='button398')
            button399 = types.InlineKeyboardButton(text="Фармацевт", callback_data='button399')
            button401 = types.InlineKeyboardButton(text="Медицинский лаборант", callback_data='button401')
            button402 = types.InlineKeyboardButton(text="Медицинский психолог", callback_data='button402')
            button403 = types.InlineKeyboardButton(text="Медицинский администратор", callback_data='button403')
            button405 = types.InlineKeyboardButton(text="Медицинский исследователь", callback_data='button404')
            button404 = types.InlineKeyboardButton(text="Медицинский диагност", callback_data='button405')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button397)
            keyboard.row(button398)
            keyboard.row(button399)
            keyboard.row(button401)
            keyboard.row(button402)
            keyboard.row(button403)
            keyboard.row(button404)
            keyboard.row(button405)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите профессию, который вам больше всего нравится.", reply_markup=keyboard)
            
        if call.data == 'button397':
            bot.send_message(call.message.chat.id, "Врач -- это специалист с высшим медицинским образованием, который использует свои навыки, знания и опыт в профилактике и лечении заболеваний, поддержании нормальной жизнедеятельности организма человека.")
            bot.send_message(call.message.chat.id, '''Некоторые примеры зарплат врачей по специальностям:
Врач-терапевт. Средняя зарплата — 87 384 рубля в месяц.
Врач скорой помощи. В среднем по России — порядка 73 140 рублей в месяц.
Врач-хирург. Доход в 2025 году — 84 960 рублей.
Врач-педиатр. Участковые врачи-педиатры получают в среднем 70 486 рублей в месяц.''')
        if call.data == 'button398':
            bot.send_message(call.message.chat.id, "Медсестра -- это специалист со средним профессиональным образованием, который оказывает помощь пациентам, выполняет назначения доктора и обеспечивает уход в различных медучреждениях.")
            bot.send_message(call.message.chat.id, '''В государственных поликлиниках:
патронажная медсестра — 40 000 рублей;
палатная медсестра — более 40 000 рублей;
участковая медсестра — почти 43 000 рублей.''')
        if call.data == 'button399':
            bot.send_message(call.message.chat.id, "Фармацевт -- это специалист с медицинским образованием, который обеспечивает рациональное использование лекарственных препаратов и консультирует пациентов по вопросам медикаментозной терапии.")
            bot.send_message(call.message.chat.id, '''Заработная плата фармацевта зависит от многих факторов, в том числе от:
компетенции и возможностей специалиста;
уровня образования и стажа.
Средняя предлагаемая зарплата фармацевтов-провизоров в России составила 68,1 тыс. рублей. Это на 6,5 тыс. рублей больше, чем за аналогичный период прошлого года.''')
        if call.data == 'button400':
            bot.send_message(call.message.chat.id, "Медицинский лаборант -- это лицензированный специалист в области здравоохранения, который проводит диагностические исследования биологических жидкостей, крови и других тканей организма. Работает в диагностических лабораториях поликлиник, больниц и медицинских центров.")
            bot.send_message(call.message.chat.id, '''Некоторые примеры зарплат медицинских лаборантов:
фельдшер-лаборант — 40 000 рублей (ГБУЗ СОКГВВ);
лаборант-микробиолог — 40 000–50 000 рублей (ЦККЛС);
медицинский лабораторный техник (фельдшер-лаборант) — 30 000–45 000 рублей (ГБУЗ СО «СГКП №15»).''')
        if call.data == 'button401':
            bot.send_message(call.message.chat.id, "Медицинский психолог -- это специалист, работающий на стыке психологии и медицины. Он помогает пациентам справляться с психологическими трудностями, связанными с болезнями, лечением и реабилитацией.")
            bot.send_message(call.message.chat.id, '''Уровень дохода зависит от региона трудоустройства, сферы занятости и опыта работы.
В госучреждениях — от 40 до 70 тысяч рублей в месяц.
В коммерческих организациях — от 100 до 200 тысяч рублей.
Опытные психологи с медицинским образованием, которые занимаются частной практикой, могут зарабатывать по 7–10 тысяч рублей в час.''')
        if call.data == 'button402':
            bot.send_message(call.message.chat.id, "Медицинский администратор -- это  специалист, который организует и координирует работу медицинского учреждения или его подразделений, обеспечивая эффективное взаимодействие между пациентами, врачами и персоналом.")
            bot.send_message(call.message.chat.id, '''Заработная плата может отличаться в зависимости от города:
Москва — 67 000 рублей;
Краснодар — 65 000 рублей;
Санкт-Петербург — 54 000 рублей;
Нижний Новгород — 48 000 рублей;''')
        if call.data == 'button403':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''Размер заработной платы может отличаться в зависимости от города:
Москва — 145 000 рублей;
Смоленск — 95 000 рублей;
Санкт-Петербург — 81 000 рублей;
Пермь — 50 000 рублей.''')
        if call.data == 'button404':
            bot.send_message(call.message.chat.id, "Медицинский диагност -- это специалист, который занимается исследованием всех систем и органов организма пациента для определения причин имеющихся проблем.")
            bot.send_message(call.message.chat.id, '''Врачам функциональной диагностики предлагалась зарплата:
В Москве — от 90 до 150 тысяч рублей и выше, средняя — 133 500 рублей, чаще — 150 000 рублей в месяц.
В Санкт-Петербурге — 80–130 тысяч рублей.
В Новосибирске — 70–110 тысяч рублей.''')
        if call.data == 'button405':
            bot.send_message(call.message.chat.id, "Медицинский исследователь -- специалист, который занимается изучением различных аспектов медицины, таких как новые методы лечения, диагностика заболеваний и профилактика.")
            bot.send_message(call.message.chat.id, '''Заработная плата может отличаться в зависимости от города:
Москва — 145 000 рублей;
Смоленск — 95 000 рублей;
Санкт-Петербург — 81 000 рублей.''')    
        
        if call.data == 'button308':
            keyboard = types.InlineKeyboardMarkup()
            button406 = types.InlineKeyboardButton(text="Физик", callback_data='button406')
            button407 = types.InlineKeyboardButton(text="Химик", callback_data='button407')
            button408 = types.InlineKeyboardButton(text="Биолог", callback_data='button408')
            button409 = types.InlineKeyboardButton(text="Математик", callback_data='button409')
            button410 = types.InlineKeyboardButton(text="Геолог", callback_data='button410')
            button411 = types.InlineKeyboardButton(text="Астроном", callback_data='button411')
            button412 = types.InlineKeyboardButton(text="Эколог", callback_data='button412')
            button413 = types.InlineKeyboardButton(text="Психолог", callback_data='button413')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button406)
            keyboard.row(button407)
            keyboard.row(button408)
            keyboard.row(button409)
            keyboard.row(button410)
            keyboard.row(button411)
            keyboard.row(button412)
            keyboard.row(button413)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите профессию, который вам больше всего нравится.", reply_markup=keyboard)
            
        if call.data == 'button406':
            bot.send_message(call.message.chat.id, "Физик -- это учёный, который изучает законы природы и физические явления, исследует свойства материи, энергии и их взаимодействия друг с другом в пространстве и времени.")
            bot.send_message(call.message.chat.id, '''Зарплата физика зависит от сферы, в которой он работает:
В сфере промышленности зарплата варьируется от 40 до 400 тыс. рублей
В секторе науки зарплата повышается с присвоением более высокой учёной степени. Оклад младшего научного сотрудника составляет 30–60 тыс. рублей, у профессора, заведующего кафедрой — 70–150 тыс. рублей в месяц.
В образовательной сфере зарплаты самые низкие: школьному учителю физики предлагают 25–50 тыс. рублей, преподавателю вуза — в 1,5–2 раза больше.''')
        if call.data == 'button407':
            bot.send_message(call.message.chat.id, "Химик -- это специалист, который изучает состав, строение, свойства веществ и химические процессы, происходящие в природе и производстве.")
            bot.send_message(call.message.chat.id, '''Научные исследования:
начинающие исследователи — от 25 000 до 40 000 рублей в месяц;
опытные учёные — от 40 000 до 80 000 рублей и выше.

Промышленность:
начинающие специалисты — от 30 000 до 50 000 рублей в месяц;
опытные химики — от 50 000 до 90 000 рублей в месяц.''')
        if call.data == 'button408':
            bot.send_message(call.message.chat.id, "Биолог -- это специалист, который изучает живые организмы, их строение, функции, эволюцию и взаимодействие с окружающей средой. Биологи проводят научные исследования на разных уровнях организации живой материи: от молекул и клеток до экосистем и биосферы в целом.")
            bot.send_message(call.message.chat.id, '''Зарплата биолога в России может варьироваться в зависимости от уровня образования, опыта работы и места работы:
Начальный уровень — от 50 000 до 70 000 рублей в месяц (биологи без опыта).
Средний уровень — от 70 000 до 100 000 рублей в месяц (опытные специалисты, в крупных городах и на известных проектах эта сумма может быть значительно выше).
Эксперт — от 100 000 до 150 000 рублей в месяц (топовые биологи, работающие на высокобюджетных проектах).''')
        if call.data == 'button409':
            bot.send_message(call.message.chat.id, "Математик -- это специалист, занимающийся изучением, анализом и решением математических задач. Он разрабатывает теории, строит модели, анализирует данные и применяет математические методы для решения практических и теоретических проблем в науке, технике, экономике и других сферах.")
            bot.send_message(call.message.chat.id, '''Заработная плата математика зависит от опыта, места работы и региона.
начинающий специалист — 25 000–40 000 рублей;
с опытом — 40 000–80 000 рублей;
ведущий исследователь/профессор — 80 000–150 000 рублей.''')
        if call.data == 'button410':
            bot.send_message(call.message.chat.id, "Геолог -- это специалист, который изучает состав, строение и историю развития Земли. Он исследует горные породы, минералы, полезные ископаемые, подземные воды и другие компоненты земной коры.")
            bot.send_message(call.message.chat.id, '''Заработная плата геологов зависит от региона, уровня опыта и сферы деятельности:
Начальный уровень — от 60 000 до 80 000 рублей в месяц (геологи без опыта).
Средний уровень — от 80 000 до 120 000 рублей в месяц (опытные специалисты, в крупных городах и на известных проектах эта сумма может быть значительно выше).
Эксперт — от 120 000 до 200 000 рублей в месяц (топовые геологи, работающие на высокобюджетных проектах).''')
        if call.data == 'button411':
            bot.send_message(call.message.chat.id, "Астроном -- это учёный, который изучает структуру, движение и происхождение небесных тел и космоса.")
            bot.send_message(call.message.chat.id, '''Заработная плата астрономов зависит от уровня образования, опыта, места работы и других факторов:
Начальный уровень. Астрономы без опыта могут зарабатывать от 60 000 до 80 000 рублей в месяц.
Средний уровень. Опытные специалисты могут получать от 80 000 до 120 000 рублей в месяц. В крупных городах и на известных проектах эта сумма может быть значительно выше.
Эксперт. Топовые астрономы, работающие на высокобюджетных проектах, могут зарабатывать от 120 000 до 200 000 рублей в месяц.''')
        if call.data == 'button412':
            bot.send_message(call.message.chat.id, "Эколог -- это  специалист, который изучает взаимодействие живых организмов с окружающей средой. Он отвечает за выявление и решение экологических проблем, связанных с загрязнением, изменением климата и другими факторами.")
            bot.send_message(call.message.chat.id, '''Зарплата эколога зависит от опыта, квалификации и региона:
Москва: 80 000–180 000 рублей в месяц.
Санкт-Петербург: 70 000–150 000 рублей в месяц.
Города с тяжёлой промышленностью (Норильск, Череповец): 90 000–200 000 рублей в месяц.
Региональные центры (Екатеринбург, Казань): 60 000–130 000 рублей в месяц.''')
        if call.data == 'button413':
            bot.send_message(call.message.chat.id, "Психолог -- это специалист, который изучает психические процессы и поведение людей. Его основная задача — помочь клиентам в решении личных и социальных проблем с использованием разных методов и техник.")
            bot.send_message(call.message.chat.id, '''Клинический психолог (работа в медучреждениях, реабилитационных центрах) — 50 000 рублей в месяц, диапазон — 40 000–80 000 рублей.
Семейный психолог (консультирование пар и родителей) — 100 000 рублей в месяц, диапазон — 70 000–200 000 рублей.
Детский и подростковый психолог — 80 000 рублей в месяц, диапазон — 50 000–150 000 рублей.''')
            
        if call.data == 'button309':
            keyboard = types.InlineKeyboardMarkup()
            button414 = types.InlineKeyboardButton(text="Учитель", callback_data='button414')
            button415 = types.InlineKeyboardButton(text="Воспитатель", callback_data='button415')
            button416 = types.InlineKeyboardButton(text="Преподаватель вуза", callback_data='button416')
            button417 = types.InlineKeyboardButton(text="Тьютор", callback_data='button417')
            button418 = types.InlineKeyboardButton(text="Методист", callback_data='button418')
            button419 = types.InlineKeyboardButton(text="Логопед", callback_data='button419')
            button420 = types.InlineKeyboardButton(text="Психолог-педагог", callback_data='button420')
            button421 = types.InlineKeyboardButton(text="Консультант по образованию", callback_data='button421')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button414)
            keyboard.row(button415)
            keyboard.row(button416)
            keyboard.row(button417)
            keyboard.row(button418)
            keyboard.row(button419)
            keyboard.row(button420)
            keyboard.row(button421)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите профессию, который вам больше всего нравится.", reply_markup=keyboard)
            
        if call.data == 'button414':
            bot.send_message(call.message.chat.id, "Учитель -- это педагог, который занимается обучением и воспитанием. Он передаёт ученикам знания по различным предметам, развивает их способности и интересы, формирует у них навыки и компетенции, необходимые для успешной жизни в обществе.")
            bot.send_message(call.message.chat.id, '''Средняя зарплата учителя —  31 699 рублей, модальная (наиболее часто встречающаяся) —  22 000 рублей.
''')
        if call.data == 'button415':
            bot.send_message(call.message.chat.id, "Воспитатель -- это  педагог, который занимается воспитанием и обучением детей, преимущественно дошкольного возраста (до 7 лет). Также воспитатели работают с более старшими воспитанниками, например в детском лагере или школе-интернате.")
            bot.send_message(call.message.chat.id, '''Уровень оплаты труда воспитателей может отличаться в зависимости от города:
Москва — 60 000 рублей;
Санкт-Петербург — 48 000 рублей;
Самара — 38 000 рублей.''')
        if call.data == 'button416':
            bot.send_message(call.message.chat.id, "Преподаватель вуза -- это специалист, который осуществляет учебный процесс в высших учебных заведениях, ведёт лекции и семинары, а также занимается научной деятельностью")
            bot.send_message(call.message.chat.id, '''Среднемесячная зарплата профессорско-преподавательского состава вузов России составила 136,5 тыс. рублей.
''')
        if call.data == 'button417':
            bot.send_message(call.message.chat.id, "Тьютор -- это репетитор, частный педагог, неформальная педагогическая должность.")
            bot.send_message(call.message.chat.id, '''Частная практика. Средний доход в месяц — 20 000–92 000 рублей, почасовая ставка — 300–3 000 рублей.
Работа в образовательных центрах. Средний доход в месяц — 30 000–60 000 рублей, почасовая ставка — 300–1 000 рублей.
Онлайн-тьютор. Средний доход в месяц — 20 000–80 000 рублей, почасовая ставка — 300–2 000 рублей.''')
        if call.data == 'button418':
            bot.send_message(call.message.chat.id, "Методист -- это специалист в сфере образования и корпоративного обучения, который отвечает за разработку и внедрение эффективных методик, организацию учебного процесса и повышение квалификации педагогов и сотрудников.")
            bot.send_message(call.message.chat.id, '''Начинающие методисты — от 30 000 до 50 000 рублей в месяц.
Опытные методисты (более 5 лет опыта) — от 50 000 до 100 000 рублей в месяц.
Высококвалифицированные методисты и руководители отделов методической работы — от 100 000 рублей в месяц и выше, в зависимости от региона и организации.''')
        if call.data == 'button419':
            bot.send_message(call.message.chat.id, "Логопед -- это специалист, который занимается диагностикой, коррекцией и профилактикой нарушений речи у детей и взрослых. ")
            bot.send_message(call.message.chat.id, '''Детский сад. 25 000–35 000 рублей в месяц, фиксированный оклад, работа с группами детей.
Школа, центр образования. 30 000–45 000 рублей в месяц, коррекция письма и чтения, инклюзивное обучение.
Медицинский центр. 40 000–70 000 рублей в месяц, работа с пациентами после инсульта, травм.
Онлайн-работа. 50 000–120 000 рублей в месяц, консультации через видеозвонки, платформы, масштабирование, авторские курсы.''')
        if call.data == 'button420':
            bot.send_message(call.message.chat.id, "Психолог-педагог -- это специалист, который сочетает знания педагогики и психологии для работы с детьми, подростками и их родителями в школьной и внешкольной среде.")
            bot.send_message(call.message.chat.id, '''Некоторые примеры средней зарплаты:
Москва — 75–90 тысяч рублей в месяц (высокая конкуренция, городские надбавки).
Санкт-Петербург — 60–75 тысяч рублей (развитая система образования).''')
        if call.data == 'button414':
            bot.send_message(call.message.chat.id, "Консультант по образованию -- это специалист, который помогает ученикам, их родителям, а иногда и образовательным учреждениям в выборе наилучшего образовательного пути.")
            bot.send_message(call.message.chat.id, '''Уровень дохода консультанта по образованию зависит от специализации, опыта работы и репутации специалиста.
Москва — 100–300 тысяч рублей в зависимости от опыта;
Санкт-Петербург — 90–250 тысяч рублей в зависимости от опыта.''')
            
        if call.data == 'button310':
            keyboard = types.InlineKeyboardMarkup()
            button422 = types.InlineKeyboardButton(text="Электрик", callback_data='button422')
            button423 = types.InlineKeyboardButton(text="Электромонтажник", callback_data='button423')
            button424 = types.InlineKeyboardButton(text="Электрослесарь", callback_data='button424')
            button425 = types.InlineKeyboardButton(text="Электротехник", callback_data='button425')
            button426 = types.InlineKeyboardButton(text="Электроэнергетик", callback_data='button426')
            button427 = types.InlineKeyboardButton(text="Электромеханик", callback_data='button427')
            button428 = types.InlineKeyboardButton(text="Электробезопасник", callback_data='button428')
            button429 = types.InlineKeyboardButton(text="Электроизолировщик", callback_data='button429')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button422)
            keyboard.row(button423)
            keyboard.row(button424)
            keyboard.row(button425)
            keyboard.row(button426)
            keyboard.row(button427)
            keyboard.row(button428)
            keyboard.row(button429)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите профессию, который вам больше всего нравится.", reply_markup=keyboard)
            
        if call.data == button422:
            bot.send_message(call.message.chat.id, "Электрик -- это специалист, который занимается установкой, обслуживанием и ремонтом электрических систем и оборудования. ")
            bot.send_message(call.message.chat.id, '''Заработок электрика зависит от компании, должности и опыта работы. Несколько примеров:
50 000 рублей — электрик в ООО «СЛАДПРОМ», полный рабочий день, опыт от 1 года.
75 000–81 000 рублей — слесарь-электрик по ремонту технологического оборудования АЗС в ООО «АРП», полный рабочий день.
100 000–150 000 рублей — электрик/электромонтажник в Wowworks, без опыта, ежедневные выплаты.''')
        if call.data == button423:
            bot.send_message(call.message.chat.id, "Электромонтажник -- это специалист, занимающийся установкой, наладкой, ремонтом и обслуживанием электрооборудования. Он работает с электропроводкой, электрощитами, розетками, выключателями и другими элементами, обеспечивая безопасное и стабильное функционирование электрических сетей.")
            bot.send_message(call.message.chat.id, '''Некоторые примеры зарплат электромонтажников в разных компаниях:
ПАО «ГИДРОАВТОМАТИКА». Электромонтажник по силовым сетям и электрооборудованию — 59 200–70 000 рублей, полный рабочий день, опыт от 1 года.
«ЭнергоСтрой». Электромонтажник 4–5 разряда — от 130 000 до 180 000 рублей, вахтовый метод работы.''')
        if call.data == button424:
            bot.send_message(call.message.chat.id, "Электрослесарь -- это специалист, который специализируется на обслуживании, ремонте и установке электрооборудования и электрических систем.")
            bot.send_message(call.message.chat.id, '''Примерные показатели заработной платы электрослесарей:
Начинающий электрослесарь — примерно от 25 000 до 35 000 рублей в месяц.
Электрослесарь среднего уровня — примерно от 35 000 до 50 000 рублей в месяц.
Опытный электрослесарь — от 50 000 до 80 000 рублей и выше в месяц.''')
        if call.data == button425:
            bot.send_message(call.message.chat.id, "Электротехник -- это специалист, работающий с электрическими системами и оборудованием. Он занимается проектированием, монтажом, наладкой, диагностикой, ремонтом и обслуживанием электрических устройств.")
            bot.send_message(call.message.chat.id, '''Примерные диапазоны зарплат электротехников:
Стажёр или начинающий специалист (без опыта) — 25 000–40 000 рублей.
Специалист со средним опытом (2–5 лет в профессии) — 40 000–70 000 рублей.
Опытный специалист (более 5 лет в профессии) — 70 000–120 000 рублей.
Ведущий инженер или специалист в узкой области — 120 000–200 000 рублей и выше.''')
        if call.data == button426:
            bot.send_message(call.message.chat.id, "Электроэнергетики -- это инженеры, технические специалисты и руководители, обеспечивающие весь путь энергии: от производства на электростанциях до конечного потребителя. ")
            bot.send_message(call.message.chat.id, '''Инженер-энергетик (традиционные источники) — 120 000 рублей. Требуемое образование — высшее техническое.
Специалист по возобновляемой энергетике — 145 000 рублей. Требуемое образование — высшее техническое, сертификация.
Диспетчер энергосистемы — 110 000 рублей. Требуемое образование — высшее техническое.''')
        if call.data == button427:
            bot.send_message(call.message.chat.id, "Электромеханик -- это специалист, который занимается установкой, обслуживанием, диагностикой, ремонтом и проектированием электромеханического оборудования.")
            bot.send_message(call.message.chat.id, '''Некоторые ориентировочные диапазоны заработной платы электромехаников в России в зависимости от опыта работы и позиции:
Начинающий специалист (рабочий): от 20 000 до 35 000 рублей в месяц.
Электромеханик с опытом работы 1–3 года (рабочий): от 30 000 до 45 000 рублей в месяц.
Техник-электромеханик или электромеханик с большим опытом (более 3 лет): от 40 000 до 60 000 рублей в месяц.''')
        if call.data == button428:
            bot.send_message(call.message.chat.id, "Электробезопасник -- это специалист, отвечающий за контроль за эксплуатацией электрооборудования.")
            bot.send_message(call.message.chat.id, '''Начинающие электрики с базовыми навыками и минимальным опытом работы получают 35–45 тысяч рублей.
Электрики с опытом 3–5 лет и средней категорией допуска по электробезопасности могут рассчитывать на ежемесячный доход в 70–100 тысяч рублей.
Высококвалифицированные электрики с опытом работы более 10 лет, высшей категорией допуска и дополнительными специализациями (например, в области промышленной автоматики) могут зарабатывать от 150 до 250 тысяч рублей в месяц и выше.''')
        if call.data == button429:
            bot.send_message(call.message.chat.id, "Электроизолировщик -- это специалист, занимающийся изоляцией электрооборудования, в частности кабелей, проводов, трансформаторов. ")
            bot.send_message(call.message.chat.id, '''В среднем зарплатные предложения электроизолировщиков по городам:
Москва: 90 000–130 000 рублей;
Санкт-Петербург: 80 000–150 000 рублей;
Красноярск: 130 000–140 000 рублей;''')
            
            
        if call.data == 'button302':
            keyboard = types.InlineKeyboardMarkup()
            button321 = types.InlineKeyboardButton(text="Экономист-аналитик", callback_data='button321')
            button322 = types.InlineKeyboardButton(text="Инвест-аналитик", callback_data='button322')
            button323 = types.InlineKeyboardButton(text="Маркетолог", callback_data='button323')
            button324 = types.InlineKeyboardButton(text="Страховой агент", callback_data='button324')
            button325 = types.InlineKeyboardButton(text="Кредитный менеджер", callback_data='button325')
            button326 = types.InlineKeyboardButton(text="Банковский работник", callback_data='button326')
            button327 = types.InlineKeyboardButton(text="Бизнес-аналитик", callback_data='button327')
            button328 = types.InlineKeyboardButton(text="Финансовый консультант", callback_data='button328')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button321)
            keyboard.row(button322)
            keyboard.row(button323)
            keyboard.row(button324)
            keyboard.row(button325)
            keyboard.row(button326)
            keyboard.row(button327)
            keyboard.row(button328)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите пофессию, которая вам больше всего нравится.", reply_markup=keyboard)
        
        if call.data == 'button321':
            bot.send_message(call.message.chat.id, "Экономист-аналитик -- это  специалист, который занимается анализом экономических данных, исследованием рынка, прогнозированием экономических трендов и оценкой влияния различных факторов на экономику.")
            bot.send_message(call.message.chat.id, '''Экономист-аналитик зарабатывает:
100 000–120 000 рублей в месяц на руки предлагает группа компаний «Триумф» экономисту-аналитику с опытом 1–3 года.")
От 230 000 рублей в месяц до вычета налогов предлагает компания «Наяда» экономисту-аналитику с опытом 3–6 лет
От 160 000 до 205 000 рублей в месяц предлагает компания «УК Инфраструктурные Инвестиции» ведущему экономисту-аналитику энергетического холдинга.''')
        if call.data == 'button322':
            bot.send_message(call.message.chat.id, "Инвест-аналитик -- это специалист, занимающийся анализом и оценкой потенциальных инвестиционных возможностей. Его основная задача — помочь клиентам и компании принимать обоснованные решения по вложениям средств.")
            bot.send_message(call.message.chat.id, '''Инвест-аналитик зарабатывает: 
начальный уровень: от 80 000 до 120 000 рублей в месяц (для аналитиков без опыта). 
Средний уровень: от 120 000 до 180 000 рублей в месяц (для опытных специалистов). 
В крупных городах и на известных проектах эта сумма может быть значительно выше. Эксперт: от 180 000 до 250 000 рублей в месяц (для топовых инвестиционных аналитиков, работающих на высокобюджетных проектах).''')
        if call.data == 'button323':
            bot.send_message(call.message.chat.id, "Маркетолог -- это специалист, который занимается исследованием рынка, анализом спроса и предложения, разработкой и реализацией маркетинговых стратегий для продвижения товаров и услуг.")
            bot.send_message(call.message.chat.id, "Средний размер оплаты труда маркетолога — 106 940 рублей в месяц.")
        if call.data == 'button324':
            bot.send_message(call.message.chat.id, "Страховой агент -- это официальный представитель страховой компании, осуществляющий операции по заключению договоров имущественного и личного страхования с физ. и юр. лицами.")
            bot.send_message(call.message.chat.id, "Средняя зарплата страхового агента в России —  60 000 рублей. Чаще всего зарплаты находятся в диапазоне от 40 000 до 80 000 рублей. Минимальная зафиксированная зарплата —  30 000 рублей, максимальная —  230 000 рублей.")
        if call.data == 'button325':
            bot.send_message(call.message.chat.id, "Кредитный менеджер -- это специалист, который занимается оформлением и выдачей кредитов. Его задача — оценить кредитоспособность клиентов, разработать кредитные предложения и подготовить документацию для заключения кредитных соглашений.")
            bot.send_message(call.message.chat.id, "Средний доход кредитного менеджера в Москве и Санкт-Петербурге составляет 100 000–480 000 рублей, в регионах — 45 000–130 000 рублей")
        if call.data == 'button326':
            bot.send_message(call.message.chat.id, "Банковский работник -- это профессионал, который обеспечивает функционирование финансового учреждения через взаимодействие с клиентами и управление банковскими продуктами и услугами.")
            bot.send_message(call.message.chat.id, '''Кассир — 40 000–70 000 рублей в месяц. 
Специалист по кредитованию — 70 000–120 000 рублей в месяц. Бизнес-аналитик — 90 000–150 000 рублей в месяц. 
Финансовый менеджер — 100 000–200 000 рублей в месяц. 
Руководитель отдела — 150 000–300 000 рублей в месяц.''')
        if call.data == 'button327':
            bot.send_message(call.message.chat.id, "Бизнес-аналитик -- это специалист, который анализирует деятельность организаций и предлагает мероприятия, необходимые для повышения эффективности их работы. Он помогает наладить производство, рационально использовать ресурсы, оптимизировать бизнес-процессы.")
            bot.send_message(call.message.chat.id, "Средний размер оплаты труда бизнес-аналитика — 182 513 рублей в месяц. ")
        if call.data == 'button328':
            bot.send_message(call.message.chat.id, "Финансовый консультант -- это эксперт, который помогает клиентам разрабатывать и реализовывать финансовые стратегии.")
            bot.send_message(call.message.chat.id, '''Начинающий консультант — 45 000–70 000 рублей; 
Консультант с опытом 2–3 года — 80 000–120 000 рублей; 
Ведущий консультант — 130 000–200 000 рублей; 
Персональный финансовый советник — от 250 000 рублей.''')
        
        if call.data == 'button303':
            keyboard = types.InlineKeyboardMarkup()
            button329 = types.InlineKeyboardButton(text="Аудитор", callback_data='button329')
            button330 = types.InlineKeyboardButton(text="Финансовый аналитик", callback_data='button330')
            button331 = types.InlineKeyboardButton(text="Налоговый консультант", callback_data='button331')
            button332 = types.InlineKeyboardButton(text="Главный бухгалтер", callback_data='button332')
            button333 = types.InlineKeyboardButton(text="Финансовый менеджер", callback_data='button333')
            button334 = types.InlineKeyboardButton(text="Кассир", callback_data='button334')
            button335 = types.InlineKeyboardButton(text="Специалист по бюджетированию", callback_data='button335')
            button336 = types.InlineKeyboardButton(text="Экономист", callback_data='button336')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button329)
            keyboard.row(button330)
            keyboard.row(button331)
            keyboard.row(button332)
            keyboard.row(button333)
            keyboard.row(button334)
            keyboard.row(button335)
            keyboard.row(button336)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите пофессию, которая вам больше всего нравится.", reply_markup=keyboard)
            
        if call.data == 'button329':
            bot.send_message(call.message.chat.id, "Аудитор -- это специалист, который проводит независимую проверку финансовой, налоговой и деловой деятельности организаций, выявляет ошибки и нарушения, а также даёт рекомендации по улучшению учёта и контроля.")
            bot.send_message(call.message.chat.id, "Зарплата аудитора в России — от 55 000 до 106 545 рублей. В Москве — от 80 000 до 200 000 рублей.")
        if call.data == 'button330':
            bot.send_message(call.message.chat.id, "Финансовый аналитик -- это специалист, который занимается изучением финансовой информации, анализом финансовых данных и созданием прогнозов на основе своего анализа.")
            bot.send_message(call.message.chat.id, '''Начинающие специалисты (опыт до 1–2 лет) — в среднем 70 000–100 000 рублей в месяц. 
Специалисты среднего звена (опыт 2–5 лет) — в среднем 120 000–200 000 рублей в месяц.
Опытные аналитики (опыт более 5 лет) — от 200 000 до 350 000 рублей в месяц. Особенно высоко оплачиваются специалисты с опытом работы в международных компаниях и профессиональными сертификатами (CFA, ACCA).")
Руководители финансовой аналитики — от 350 000 до 700 000 рублей и выше. В крупных компаниях и инвестиционных фондах эта сумма может достигать 1 000 000–1 500 000 рублей в месяц.''')
        if call.data == 'button331':
            bot.send_message(call.message.chat.id, "Налоговый консультант -- это специалист, который помогает предпринимателям и организациям правильно рассчитывать налоги, выбирать оптимальную систему налогообложения и соблюдать требования законодательства. Сфера налогового консалтинга находится на пересечении экономики, права и бухгалтерии.")
            bot.send_message(call.message.chat.id, "Средний доход налогового консультанта в Москве — от 80 000 до 180 000 рублей.")
        if call.data == 'button332':
            bot.send_message(call.message.chat.id, "Главный бухгалтер -- это специалист, который руководит бухгалтерией организации и отвечает за её финансовые вопросы. Он подчиняется руководителю предприятия и является его правой рукой в финансовых вопросах.")
            bot.send_message(call.message.chat.id, "Реальный диапазон доходов варьируется значительно шире — от 35 000 до 260 000 рублей в зависимости от масштабов компании и сложности работы.")
        if call.data == 'button333':
            bot.send_message(call.message.chat.id, "Финансовый менеджер -- это это специалист, который управляет финансовыми ресурсами компании, планирует, анализирует и контролирует финансовую деятельность организации для достижения финансовых целей и устойчивого развития.")
            bot.send_message(call.message.chat.id, "Зарплата финансового менеджера варьируется в зависимости от региона и масштаба компании, в которой он работает. По данным портала hh.ru на июль 2025 года, зарплата финансового менеджера в России — 60 000–150 000 рублей. В Москве — 80 000–206 000 рублей.")
        if call.data == 'button334':
            bot.send_message(call.message.chat.id, "Кассир -- это специалист, который осуществляет денежные операции и обслуживает клиентов в различных организациях. В его обязанности входит работа с наличными деньгами, банковскими картами, ведение кассовой документации и обеспечение сохранности денежных средств.")
            bot.send_message(call.message.chat.id, "Средняя зарплата кассира в Москве составила 71 583 рубля, модальная (наиболее часто встречающаяся) — 70 000 рублей.")
        if call.data == 'button335':
            bot.send_message(call.message.chat.id, "Специалист по бюджетированию -- это профессионал, занимающийся планированием, контролем и анализом бюджетов организации. Он работает на стыке экономики и финансов, обеспечивая эффективное распределение ресурсов.")
            bot.send_message(call.message.chat.id, "Уровень дохода зависит от опыта специалиста, региона работы и других факторов. Например, топовые специалисты по бюджетированию, работающие на высокобюджетных проектах, могут получать от 130 000 до 180 000 рублей в месяц.")
        if call.data == 'button336':
            bot.send_message(call.message.chat.id, "Экономист -- это  специалист по экономике или по её разделам, эксперт по экономическим вопросам промышленности, сельского хозяйства, банковского дела и так далее.")
            bot.send_message(call.message.chat.id, '''Новичок может получать около 35 тысяч рублей. 
Опытный специалист с навыками управления может зарабатывать от 60–70 тысяч рублей.
Для этого нужно проработать в сфере 1–3 года. 
Ведущий или главный экономист может получать около 200 тысяч рублей. 
Финансовый директор — от 250 тысяч рублей в месяц.''')
            
        if call.data == 'button311':
            keyboard = types.InlineKeyboardMarkup()
            button312 = types.InlineKeyboardButton(text="Экономисты", callback_data='button312')
            button313 = types.InlineKeyboardButton(text="Бухгалтеры", callback_data='button313')
            button314 = types.InlineKeyboardButton(text="Специалисты по продажам", callback_data='button314')
            button315 = types.InlineKeyboardButton(text="Программисты", callback_data='button315')
            button316 = types.InlineKeyboardButton(text="Проектировщики", callback_data='button316')
            button317 = types.InlineKeyboardButton(text="Медицинские работники", callback_data='button317')
            button318 = types.InlineKeyboardButton(text="Учёные", callback_data='button318')
            button319 = types.InlineKeyboardButton(text="Педагоги", callback_data='button319')
            button320 = types.InlineKeyboardButton(text="Электрики", callback_data='button320')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button312)
            keyboard.row(button313)
            keyboard.row(button314)
            keyboard.row(button315)
            keyboard.row(button316)
            keyboard.row(button317)
            keyboard.row(button318)
            keyboard.row(button319)
            keyboard.row(button320)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите раздел, с которым вы хотите ознакомиться", reply_markup=keyboard)
            
        if call.data == 'button312':
            bot.send_message(call.message.chat.id, "Экономисты -- это специалисты, которые изучаетют экономические процессы, анализируют ресурсы, потребности и взаимосвязи в экономике. Они применяют знания в области финансов, статистики, макро- и микроэкономики для прогнозирования и разработки стратегий экономического развития.")
        if call.data == 'button313':
            bot.send_message(call.message.chat.id, "Бухгалтер -- это специалист, который управляет финансами компании, отслеживает доходы и расходы, начисляет зарплаты, рассчитывает налоги и составляет отчётную документацию для руководства, налоговой и других контролирующих органов.")
        if call.data == 'button314':
            bot.send_message(call.message.chat.id, "Специалист по продажам -- это профессионал, который занимается реализацией товаров или услуг компании. Его задача — увеличивать продажи, находить новых клиентов и поддерживать лояльность постоянных покупателей.")
        if call.data == 'button315':
            bot.send_message(call.message.chat.id, "Программист -- это специалист, который занимается разработкой программного обеспечения и приложений. Он создаёт компьютерные программы, которые могут выполнять различные задачи, начиная от простых утилит до сложных систем управления.")
        if call.data == 'button316':
            bot.send_message(call.message.chat.id, "Проектировщик -- это специалист, который занимается разработкой и созданием планов, эскизов, схем или моделей для реализации различных объектов или систем в соответствии с определёнными требованиями и стандартами. Основная задача — создать проект, который будет эстетичным, безопасным, экономически эффективным и соответствующим нормам и стандартам.")
        if call.data == 'button317':
            bot.send_message(call.message.chat.id, "Медицинские работники -- это специалисты, которые прошли профессиональную подготовку и сертификацию в области медицины и участвуют в процессе оказания медицинских услуг.")
        if call.data == 'button318':
            bot.send_message(call.message.chat.id, "Учёные -- это специалисты в какой-либо научной области, внёсшие вклад в науку. Они могут быть экспертами в одной или нескольких областях науки: медицине, физике, биологии, математике, социологии и т. д..")
        if call.data == 'button319':
            bot.send_message(call.message.chat.id, "Педагог -- это профессионал в области образования и воспитания, который занимается планированием, организацией, проведением и анализом учебно-воспитательного процесса.")
        if call.data == 'button320':
            bot.send_message(call.message.chat.id, "Электрики -- это специалист, который занимается установкой, обслуживанием и ремонтом электрических систем и оборудования.")
            
        if call.data == 'button276':
            keyboard = types.InlineKeyboardMarkup()
            button430 = types.InlineKeyboardButton(text="Инженеры", callback_data='button430')
            button431 = types.InlineKeyboardButton(text="Физики", callback_data='button431')
            button432 = types.InlineKeyboardButton(text="Архитекторы", callback_data='button432')
            button433 = types.InlineKeyboardButton(text="Разработчики ПО", callback_data='button433')
            button434 = types.InlineKeyboardButton(text="Экология", callback_data='button434')
            button435 = types.InlineKeyboardButton(text="Преподаватели", callback_data='button435')
            button439 = types.InlineKeyboardButton(text="Ознакомиться🔎", callback_data='button439')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button430)
            keyboard.row(button431)
            keyboard.row(button432)
            keyboard.row(button433)
            keyboard.row(button434)
            keyboard.row(button435)
            keyboard.row(button439)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите раздел, который вам больше всего нравится. Если вы не понимаете значение какого-то предмета, то нажмите на --Ознакомиться--.", reply_markup=keyboard)
            
            
        if call.data == 'button430':
            keyboard = types.InlineKeyboardMarkup()
            button446 = types.InlineKeyboardButton(text="Инженер-строитель", callback_data='button446')
            button447 = types.InlineKeyboardButton(text="Инженер-механик", callback_data='button447')
            button448 = types.InlineKeyboardButton(text="Аэрокосмический инженер", callback_data='button448')
            button449 = types.InlineKeyboardButton(text="Нефтяник", callback_data='button449')
            button450 = types.InlineKeyboardButton(text="Инженер-эколог", callback_data='button450')
            button451 = types.InlineKeyboardButton(text="Инженер-химик", callback_data='button451')
            button452 = types.InlineKeyboardButton(text="Инженер-программист", callback_data='button452')
            button453 = types.InlineKeyboardButton(text="Инженер-технолог", callback_data='button453')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button446)
            keyboard.row(button447)
            keyboard.row(button448)
            keyboard.row(button449)
            keyboard.row(button450)
            keyboard.row(button451)
            keyboard.row(button452)
            keyboard.row(button453)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите раздел, который вы больше всего знаете. Если вы не понимаете значение какого-то предмета, то нажмите на --Ознакомиться--.", reply_markup=keyboard)
            
        if call.data == 'button446':
            bot.send_message(call.message.chat.id, "Инженер-строитель -- это специалист, который занимается проектированием, строительством и эксплуатацией зданий и других сооружений. Он разрабатывает конструктивные решения, осуществляет расчёт нагрузок и выбирает материалы для строительства.")
            bot.send_message(call.message.chat.id, '''Однако доходы значительно различаются в зависимости от региона, опыта работы и специализации:
Начинающие специалисты без опыта получают 40 000–55 000 рублей;
Инженеры с опытом 3–5 лет — 65 000–90 000 рублей, ведущие;
Специалисты и руководители проектов — 100 000–150 000 рублей и выше.''')
        if call.data == 'button447':
            bot.send_message(call.message.chat.id, "Инженер-механик -- это специалист, который проектирует, конструирует, тестирует и обслуживает механические системы. Он применяет знания в области механики, материаловедения, прочности и других инженерных дисциплин для создания эффективных и безопасных изделий.")
            bot.send_message(call.message.chat.id, '''Начальный уровень. Инженеры-механики без опыта могут зарабатывать от 80 000 до 100 000 рублей в месяц.
Средний уровень. Опытные специалисты могут получать от 120 000 до 150 000 рублей в месяц. В крупных городах и на известных проектах эта сумма может быть значительно выше.
Эксперт. Топовые инженеры-механики, работающие на высокобюджетных проектах, могут зарабатывать от 180 000 до 250 000 рублей в месяц.''')
        if call.data == 'button448':
            bot.send_message(call.message.chat.id, "Аэрокосмический инженер -- это профессионал, который использует знания в области науки и техники для проектирования, строительства и испытаний различных типов самолётов, ракет и космических кораблей.")
            bot.send_message(call.message.chat.id, '''Зарплата аэрокосмического инженера может составлять от 100 до 400 тысяч рублей в месяц.
''')
        if call.data == 'button449':
            bot.send_message(call.message.chat.id, "Нефтяник -- это специалист, который занимается добычей, переработкой и транспортировкой нефти и газа.")
            bot.send_message(call.message.chat.id, '''Зарплата сотрудников в сфере добычи нефти и природного газа, в том числе нефтяников, составила 225,9 тыс. рублей в месяц.
''')
        if call.data == 'button450':
            bot.send_message(call.message.chat.id, "Инженер-эколог -- это специалист, работающий на стыке инженерии и экологии. Он занимается оценкой и минимизацией воздействия человеческой деятельности на окружающую среду.")
            bot.send_message(call.message.chat.id, '''Заработная плата инженера-эколога зависит от региона работы, размера предприятия, а также уровня работы:
Начинающий специалист (0–2 года опыта) — 30–50 тысяч рублей.
Специалист с опытом (3–5 лет) — 50–80 тысяч рублей.
Ведущий инженер-эколог (5–10 лет) — 70–120 тысяч рублей.
Главный эколог предприятия (10+ лет) — 100–200 тысяч рублей.''')
        if call.data == 'button451':
            bot.send_message(call.message.chat.id, "Инженер-химик -- это специалист, который применяет знания химии, физики, математики и инженерных наук для разработки, оптимизации и управления химическими процессами и технологиями. ")
            bot.send_message(call.message.chat.id, '''Средняя зарплата инженера-химика в России составила 69 105 рублей. Чаще всего в вакансиях встречается зарплата 60 000 рублей (модальная).
''')
        if call.data == 'button452':
            bot.send_message(call.message.chat.id, "Инженер-программист -- это специалист в сфере информационных технологий, который занимается созданием программного обеспечения, новых информационных продуктов и технологий. Он обладает знаниями как в области инженерии, так и в сфере программирования.")
            bot.send_message(call.message.chat.id, '''Заработок зависит от опыта работы, региона поиска, специализации и условий работодателя.
В Санкт-Петербурге — 170 000 рублей.
В городах-миллионниках вроде Новосибирска, Казани, Екатеринбурга — 130 000–180 000 рублей.''')
        if call.data == 'button453':
            bot.send_message(call.message.chat.id, "Инженер-технолог -- это специалист, который разрабатывает, внедряет и оптимизирует производственные процессы. Он создаёт технологические инструкции, подбирает оборудование и материалы, контролирует соблюдение стандартов качества и безопасности на производстве.")
            bot.send_message(call.message.chat.id, '''Средняя зарплата инженера-технолога в России —  95 485 рублей
''')
        
        #Физики
        if call.data == 'button431':
            keyboard = types.InlineKeyboardMarkup()
            button454 = types.InlineKeyboardButton(text="Физик-экспериментатор", callback_data='button454')
            button455 = types.InlineKeyboardButton(text="Инженер-физик", callback_data='button455')
            button456 = types.InlineKeyboardButton(text="Астроном", callback_data='button456')
            button457 = types.InlineKeyboardButton(text="Биофизик", callback_data='button457')
            button458 = types.InlineKeyboardButton(text="Геофизик", callback_data='button458')
            button459 = types.InlineKeyboardButton(text="Химик-физик", callback_data='button459')
            button460 = types.InlineKeyboardButton(text="Нанофизик", callback_data='button460')
            button461 = types.InlineKeyboardButton(text="Гидрофизик", callback_data='button461')
            keyboard.row(button454)
            keyboard.row(button455)
            keyboard.row(button456)
            keyboard.row(button457)
            keyboard.row(button458)
            keyboard.row(button459)
            keyboard.row(button460)
            keyboard.row(button461)
            bot.send_message(call.message.chat.id, "Выберите профессию, которая вам больше всего нравится", reply_markup=keyboard)

        if call.data == 'button454':
            bot.send_message(call.message.chat.id, "Физик-экспериментатор -- это учёный, который ставит лабораторные опыты и эксперименты с целью открытия новых физических эффектов или проверки теоретических гипотез.")
            bot.send_message(call.message.chat.id, '''Зарплата физика-экспериментатора может составлять от 120 000 до 250 000 рублей в месяц.
''')
        if call.data == 'button455':
            bot.send_message(call.message.chat.id, "Инженер-физик -- это учёный, который изучает структуру, движение и происхождение небесных тел и космоса. ")
            bot.send_message(call.message.chat.id, '''Начинающий инженер-физик (0–2 года опыта) — от примерно 30 000 до 70 000 рублей в месяц. Это может зависеть от компании, региона и сложности задач.
Инженер-физик с опытом (2–5 лет опыта) — примерно 60 000–120 000 рублей в месяц.
Старший инженер-физик (5+ лет опыта) — примерно 100 000–200 000 рублей и выше в месяц, особенно если он занимает руководящие или экспертные позиции.''')
        if call.data == 'button456':
            bot.send_message(call.message.chat.id, "Астроном -- это учёный, который изучает структуру, движение и происхождение небесных тел и космоса. ")
            bot.send_message(call.message.chat.id, '''Начальный уровень. Астрономы без опыта могут зарабатывать от 60 000 до 80 000 рублей в месяц.
Средний уровень. Опытные специалисты могут получать от 80 000 до 120 000 рублей в месяц. В крупных городах и на известных проектах эта сумма может быть значительно выше.
Эксперт. Топовые астрономы, работающие на высокобюджетных проектах, могут зарабатывать от 120 000 до 200 000 рублей в месяц.''')
        if call.data == 'button457':
            bot.send_message(call.message.chat.id, "Биофизик -- это учёный или специалист, который изучает биологические процессы и явления с помощью принципов и методов физики.")
            bot.send_message(call.message.chat.id, '''Начальный уровень — от 60 000 до 80 000 рублей в месяц (биофизики без опыта).
Средний уровень — от 90 000 до 120 000 рублей в месяц (опытные специалисты, в крупных городах и на известных проектах эта сумма может быть значительно выше).
Эксперт — от 130 000 до 180 000 рублей в месяц (топовые биофизики, работающие на высокобюджетных проектах, а иногда и значительно больше).''')
        if call.data == 'button458':
            bot.send_message(call.message.chat.id, "Геофизик -- это специалист, который изучает физические процессы и свойства Земли. Он анализирует и интерпретирует геологические, геофизические и гидрологические данные для исследования строения, состава и динамики Земли.")
            bot.send_message(call.message.chat.id, '''Начальный уровень — от 70 000 до 100 000 рублей в месяц (геофизики без опыта).
Средний уровень — от 100 000 до 150 000 рублей в месяц (опытные специалисты, в крупных городах и на известных проектах эта сумма может быть значительно выше).
Эксперт — от 150 000 до 200 000 рублей в месяц (топовые геофизики, работающие на высокобюджетных проектах).''')
        if call.data == 'button459':
            bot.send_message(call.message.chat.id, "Химик-физик -- это экспериментатор, занимающийся различными исследованиями в области химической физики и физики, в частности поиском новых видов материалов.")
            bot.send_message(call.message.chat.id, '''В Москве может зарабатывать от 80 000 до 150 000 рублей в месяц до вычета налогов.
''')
        if call.data == 'button460':
            bot.send_message(call.message.chat.id, "Нанофизик -- это учёный, специализирующийся в области нанофизики, которая изучает свойства материалов и явления, происходящие на атомном и молекулярном уровне, в масштабе от одного до нескольких сотен нанометров.")
            bot.send_message(call.message.chat.id, '''Зарплата геофизика зависит от региона, уровня образования и опыта работы:
Начальный уровень — от 70 000 до 100 000 рублей в месяц (геофизики без опыта).
Средний уровень — от 100 000 до 150 000 рублей в месяц (опытные специалисты, в крупных городах и на известных проектах эта сумма может быть значительно выше).
Эксперт — от 150 000 до 200 000 рублей в месяц (топовые геофизики, работающие на высокобюджетных проектах).''')
        if call.data == 'button461':
            bot.send_message(call.message.chat.id, "Гидрофизик -- это  специалист в области гидрофизики — раздела геофизики, изучающего физические свойства водной оболочки Земли (гидросферы) и происходящие в ней процессы.")
            bot.send_message(call.message.chat.id, '''Зарплата геофизика в России составляет 55 000–250 000 рублей, в Москве — 90 000–220 000 рублей. 
''')
        
        #Архитекторы
        if call.data == 'button432':
            keyboard = types.InlineKeyboardMarkup()
            button462 = types.InlineKeyboardButton(text="Дизайнер интерьера", callback_data='button462')
            button463 = types.InlineKeyboardButton(text="Проектировщик фасадов", callback_data= 'button463')
            button464 = types.InlineKeyboardButton(text="Ландшафтный архитектор", callback_data='button464')
            button465 = types.InlineKeyboardButton(text="Архитектор-градостроитель", callback_data='butto465')
            button466 = types.InlineKeyboardButton(text="Городской урбанист", callback_data='button466')
            button467 = types.InlineKeyboardButton(text="Конструктор", callback_data='button467')
            button468 = types.InlineKeyboardButton(text="Архитектурный дизайнер", callback_data='button468')
            button469 = types.InlineKeyboardButton(text="Технадзор", callback_data='button469')
            keyboard.row(button462)
            keyboard.row(button463)
            keyboard.row(button464)
            keyboard.row(button465)
            keyboard.row(button466)
            keyboard.row(button467)
            keyboard.row(button468)
            keyboard.row(button469)
            bot.send_message(call.message.chat.id, "Выберите профессию, которая вам больше всего нравится", reply_markup=keyboard)

        if call.data == 'button462':
            bot.send_message(call.message.chat.id, "Дизайнер интерьера -- это специалист, который занимается разработкой эстетически привлекательных, функциональных и удобных интерьерных решений для жилых и коммерческих помещений.")
            bot.send_message(call.message.chat.id, '''Начинающие дизайнеры могут зарабатывать от 20 000–40 000 рублей в месяц.
Через 1–2 года практики доход может выйти на 80 000–120 000 рублей.
Через 3–5 лет — 150 000–250 000 рублей в месяц.''')
        if call.data == 'button463':
            bot.send_message(call.message.chat.id, "Проектировщик фасадов -- это специалист, который создаёт проект наружной стороны зданий в соответствии с пожеланиями заказчика и строительными нормами.")
            bot.send_message(call.message.chat.id, '''Средняя зарплата инженера-проектировщика (в том числе проектировщика фасадов) составляет 85–120 тысяч рублей в месяц.
''')
        if call.data == 'button464':
            bot.send_message(call.message.chat.id, "Ландшафтный архитектор -- это специалист, который разрабатывает проектные решения для благоустройства открытых пространств, таких как парки, скверы, дворы и другие общественные территории.")
            bot.send_message(call.message.chat.id, '''Некоторые показатели заработка в зависимости от уровня специалиста:
Начальный уровень — от 60 000 до 90 000 рублей в месяц.
Средний уровень — от 90 000 до 130 000 рублей в месяц.
Эксперт — от 130 000 до 200 000 рублей в месяц.''')
        if call.data == 'button465':
            bot.send_message(call.message.chat.id, "Архитектор-градостроитель -- это специалист, который создаёт и развивает города. Он проектирует жилые кварталы, общественные пространства, дороги, мосты, промышленные зоны и объекты социальной инфраструктуры")
            bot.send_message(call.message.chat.id, '''Заработок архитектора-градостроителя зависит от региона, уровня опыта и места работы.
Начинающий архитектор-градостроитель: 30 000–45 000 рублей в месяц.
Опытный архитектор-градостроитель: 45 000–70 000 рублей.
Руководящие должности: 70 000–100 000 рублей.''')
        if call.data == 'button466':
            bot.send_message(call.message.chat.id, "Городской урбанист -- это специалист, который занимается планированием и развитием городских пространств. Он разрабатывает проекты, направленные на создание удобной, безопасной и устойчивой городской среды, учитывая транспортные потоки, инфраструктуру, экологию и потребности жителей.")
            bot.send_message(call.message.chat.id, '''Начальный уровень — от 60 000 до 80 000 рублей в месяц (урбанисты без опыта).
Средний уровень — от 90 000 до 120 000 рублей в месяц (опытные специалисты, в крупных городах и на известных проектах эта сумма может быть значительно выше).
Эксперт — от 150 000 до 200 000 рублей в месяц (топовые урбанисты, работающие на высокобюджетных проектах, а иногда и значительно больше).''')
        if call.data == 'button467':
            bot.send_message(call.message.chat.id, " Конструктор строительных конструкций -- это специалист, который занимается проектированием, разработкой и расчётом конструкций для зданий, сооружений.")
            bot.send_message(call.message.chat.id, '''Начальный уровень — от 80 000 до 120 000 рублей в месяц для специалистов без опыта.
Средний уровень — от 120 000 до 180 000 рублей в месяц для опытных специалистов, в крупных городах и на известных проектах эта сумма может быть значительно выше.
Эксперт — от 200 000 до 300 000 рублей в месяц для топовых инженеров-конструкторов зданий, работающих на высокобюджетных проектах.''')
        if call.data == 'button468':
            bot.send_message(call.message.chat.id, "Архитектурный дизайнер -- это специалист в области проектирования и дизайна объектов различного назначения. Он создаёт эстетически привлекательные, эргономичные и функциональные пространства с учётом всех технических и нормативных требований. ")
            bot.send_message(call.message.chat.id, '''В среднем новички-архитекторы-дизайнеры зарабатывают от 40 000 до 50 000 рублей в месяц.
 Более опытные дизайнеры могут рассчитывать на зарплату от 50 000 до 100 000 рублей.
 Специалисты со стажем от 3 лет получают 100 000–150 000 рублей в месяц.''')
        if call.data == 'button469':
            bot.send_message(call.message.chat.id, "Технадзор -- это комплекс мероприятий по контролю качества строительных и монтажных работ, направленный на обеспечение соответствия реализуемого проекта требованиям нормативных документов, технического задания и проектной документации.")
            bot.send_message(call.message.chat.id, '''В России инженер технадзора/по строительному контролю может получать заработную плату от 100 000 до 250 000 рублей в зависимости от уровня квалификации:
минимальный уровень: 100 000–140 000 рублей;
средний уровень: 140 000–185 000 рублей;
повышенный уровень: 185 000–250 000 рублей.''')
    
        #Разработчики ПО
        if call.data == 'button433':
            keyboard = types.InlineKeyboardMarkup()
            button470 = types.InlineKeyboardButton(text="Frontend-разработчик", callback_data='button470')
            button471 = types.InlineKeyboardButton(text="Backend-разработчик", callback_data='button471')
            button472 = types.InlineKeyboardButton(text="Fullstack-разработчик", callback_data='button472')
            button473 = types.InlineKeyboardButton(text="Mobile-разработчик", callback_data='button473')
            button474 = types.InlineKeyboardButton(text="DevOps-инженер", callback_data='button474')
            button475 = types.InlineKeyboardButton(text="Data Scientist", callback_data='button475')
            button476 = types.InlineKeyboardButton(text="Game Developer", callback_data='button476')
            button477 = types.InlineKeyboardButton(text="Тестировщик ПО", callback_data='button477')
            keyboard.row(button470)
            keyboard.row(button471)
            keyboard.row(button472)
            keyboard.row(button473)
            keyboard.row(button474)
            keyboard.row(button475)
            keyboard.row(button476)
            keyboard.row(button477)
            bot.send_message(call.message.chat.id, "Выберите профессию, которая вам больше всего нравится", reply_markup=keyboard)

        if call.data == 'button470':
            bot.send_message(call.message.chat.id, "Frontend-разработчик -- это IT-специалист, отвечающий за клиентскую часть веб-сайтов и приложений, то есть за то, что видит пользователь и с чем он непосредственно взаимодействует.")
            bot.send_message(call.message.chat.id, '''Средние зарплаты по грейдам:
Junior: 50 000 – 100 000 рублей
Middle: 150 000 – 210 000 рублей
Senior: 250 000 – 350 000+ рублей''')
        if call.data == 'button471':
            bot.send_message(call.message.chat.id, "Backend-разработчик -- это IT-специалист, который отвечает за создание и поддержку невидимой для пользователя серверной части веб-сайтов и приложений.")
            bot.send_message(call.message.chat.id, '''Средние зарплаты по грейдам
Стажер: Около 52 000 - 54 000 рублей.
Junior: От 88 000 рублей.
Middle: Примерно 200 000 - 201 000 рублей.
Senior: От 342 000 рублей и выше.''')
        if call.data == 'button472':
            bot.send_message(call.message.chat.id, "Fullstack-разработчик -- это IT-специалист, который обладает знаниями и навыками как во фронтенд-, так и в бэкенд-разработке, что позволяет ему заниматься полным циклом создания веб-приложений или сайтов — от пользовательского интерфейса до серверной логики и баз данных.")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button473':
            bot.send_message(call.message.chat.id, "Mobile-разработчик -- это ")
            bot.send_message(call.message.chat.id, '''В России среднемесячная зарплата фулстек-разработчика в 2025 году составляет от 150 000 до 250 000 рублей, но может значительно варьироваться в зависимости от опыта (Junior, Middle, Senior)
''')
        if call.data == 'button474':
            bot.send_message(call.message.chat.id, "DevOps-инженер -- это IT-специалист, который автоматизирует процессы разработки и эксплуатации программного обеспечения, выступая связующим звеном между разработкой (Dev) и операционной поддержкой (Ops).")
            bot.send_message(call.message.chat.id, '''Опыт и квалификация:
Junior DevOps: от 75 000 до 130 500 рублей (средняя по Москве). 
Middle DevOps: от 150 000 до 280 000 рублей. 
Senior DevOps: от 280 000 рублей и выше, может достигать 450 000–600 000 рублей и более. ''')
        if call.data == 'button475':
            bot.send_message(call.message.chat.id, "Data Scientist -- это специалист, который использует статистику, программирование и машинное обучение для извлечения ценной информации из больших данных с целью решения бизнес-задач, создания прогностических моделей и поддержки принятия обоснованных решений.")
            bot.send_message(call.message.chat.id, '''Зарплата по уровню специалиста (в рублях в месяц)
Junior: 100 000 – 120 000
Middle: 200 000 – 280 000
Senior: от 300 000 до 700 000.''')
        if call.data == 'button476':
            bot.send_message(call.message.chat.id, "Game Developer -- это разработчик программного обеспечения, специализирующийся на разработке видеоигр — процессе и связанных с ним дисциплинах создания видеоигр.")
            bot.send_message(call.message.chat.id, '''Примеры зарплат в России (по данным на 2025 год):
Junior (начальный уровень): от 50 000 до 90 000 рублей в месяц. 
Middle (средний уровень): от 100 000 до 225 000 рублей в месяц. 
Senior (опытный специалист): до 480 000 рублей в месяц и более, в зависимости от проекта и опыта.''')
        if call.data == 'button477':
            bot.send_message(call.message.chat.id, "Тестировщик ПО -- это специалист, который проверяет качество IT-продуктов (сайтов, приложений, сервисов) на наличие ошибок, сбоев и несоответствий требованиям перед их выпуском к пользователям. ")
            bot.send_message(call.message.chat.id, '''Уровень дохода по опыту:
Junior (начинающий): от 50-80 тыс. рублей в месяц, по некоторым данным, может быть от 40-50 тыс. рублей в регионах. 
Middle (средний уровень): от 80-150 тыс. рублей в месяц, с медианой зарплаты около 100-120 тыс. рублей в регионах. 
Senior (опытный): от 150 тыс. до 250 тыс. рублей и выше, с возможностью достигать 380 тыс. рублей в Москве.''')
        
        #Экология
        if call.data == 'button434':
            keyboard = types.InlineKeyboardMarkup()
            button478 = types.InlineKeyboardButton(text="Эколог", callback_data='button478')
            button479 = types.InlineKeyboardButton(text="Биолог", callback_data='button479')
            button480 = types.InlineKeyboardButton(text="Гидролог", callback_data='button480')
            button481 = types.InlineKeyboardButton(text="Климатолог", callback_data='button481')
            button482 = types.InlineKeyboardButton(text="Почвовед", callback_data='butto482')
            button483 = types.InlineKeyboardButton(text="Агроэколог", callback_data='button483')
            button484 = types.InlineKeyboardButton(text="Географ", callback_data='button484')
            button485 = types.InlineKeyboardButton(text="Зелёный инженер", callback_data='button485')
            keyboard.row(button478)
            keyboard.row(button479)
            keyboard.row(button480)
            keyboard.row(button481)
            keyboard.row(button482)
            keyboard.row(button483)
            keyboard.row(button484)
            keyboard.row(button485)
            bot.send_message(call.message.chat.id, "Выберите профессию, которая вам больше всего нравится", reply_markup=keyboard)

        if call.data == 'button478':
            bot.send_message(call.message.chat.id, "Эколог -- это специалист, изучающий взаимоотношения живых организмов друг с другом и с окружающей средой, анализирующий и оценивающий воздействие человека на природу, а также разрабатывающий мероприятия по ее защите и охране.")
            bot.send_message(call.message.chat.id, '''Средняя зарплата эколога в России составляет около 60–70 тысяч рублей в месяц, но диапазон может варьироваться от 40 тысяч рублей для начинающих специалистов до более 120 тысяч для ведущих или главных экологов.
''')
        if call.data == 'button479':
            bot.send_message(call.message.chat.id, "Биолог -- это специалист, который изучает живые организмы, их строение, функции, развитие, происхождение и взаимодействие с окружающей средой, от микроорганизмов до человека.")
            bot.send_message(call.message.chat.id, '''Примеры зарплат в зависимости от опыта и сектора:
Начинающий специалист (0-2 года опыта): от 30 000 до 70 000 рублей в месяц. 
Специалист (3-5 лет опыта): от 70 000 до 120 000 рублей. 
Опытный специалист (6-10 лет опыта): от 120 000 до 180 000 рублей. 
Эксперт (10+ лет опыта): от 180 000 рублей и выше.''')
        if call.data == 'button480':
            bot.send_message(call.message.chat.id, "Гидролог -- это ")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button481':
            bot.send_message(call.message.chat.id, "Климатолог -- это ")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button482':
            bot.send_message(call.message.chat.id, "Почвовед -- это ")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button483':
            bot.send_message(call.message.chat.id, "Агроэколог -- это ")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button484':
            bot.send_message(call.message.chat.id, "Географ -- это ")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button485':
            bot.send_message(call.message.chat.id, "Зелёный инженер -- это ")
            bot.send_message(call.message.chat.id, '''
''')
        #Преподаватели
        if call.data == 'button435':
            keyboard = types.InlineKeyboardMarkup()
            button486 = types.InlineKeyboardButton(text="", callback_data='button486')
            button487 = types.InlineKeyboardButton(text="", callback_data='button487')
            button488 = types.InlineKeyboardButton(text="", callback_data='button488')
            button489 = types.InlineKeyboardButton(text="", callback_data='button489')
            button490 = types.InlineKeyboardButton(text="", callback_data='button490')
            button491 = types.InlineKeyboardButton(text="", callback_data='button491')
            button492 = types.InlineKeyboardButton(text="", callback_data='button492')
            button493 = types.InlineKeyboardButton(text="", callback_data='button493')
            keyboard.row(button486)
            keyboard.row(button487)
            keyboard.row(button488)
            keyboard.row(button489)
            keyboard.row(button490)
            keyboard.row(button491)
            keyboard.row(button492)
            keyboard.row(button493)
            bot.send_message(call.message.chat.id, "Выберите профессию, которая вам больше всего нравится", reply_markup=keyboard)

        if call.data == 'button486':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button487':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button488':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button489':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button490':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button491':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button492':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''
''')
        if call.data == 'button493':
            bot.send_message(call.message.chat.id, "")
            bot.send_message(call.message.chat.id, '''
''')
        
        if call.data == 'button439':
            keyboard = types.InlineKeyboardMarkup()
            button440 = types.InlineKeyboardButton(text="Инженеры", callback_data='button440')
            button441 = types.InlineKeyboardButton(text="Физики", callback_data='button441')
            button442 = types.InlineKeyboardButton(text="Архитекторы", callback_data='button442')
            button443 = types.InlineKeyboardButton(text="Разработчики ПО", callback_data='button443')
            button444 = types.InlineKeyboardButton(text="Экологи", callback_data='button444')
            button445 = types.InlineKeyboardButton(text="Преподаватели", callback_data='button445')
            bt21 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt21")
            keyboard.row(button440)
            keyboard.row(button441)
            keyboard.row(button442)
            keyboard.row(button443)
            keyboard.row(button444)
            keyboard.row(button445)
            keyboard.row(bt21)
            bot.send_message(call.message.chat.id, "Выберите раздел, с которым вы хотите ознакомиться.", reply_markup=keyboard)
            
        if call.data == 'button440':
            bot.send_message(call.message.chat.id, "Инженер -- это  специалист, который применяет научные знания и технические навыки для решения практических задач в различных областях техники и технологий. Основная цель работы — создание, модернизация и эксплуатация технических устройств, сооружений, систем и технологических процессов. ")
        if call.data == 'button441':
            bot.send_message(call.message.chat.id, "Физик -- это учёный, который изучает законы природы и физические явления, исследует свойства материи, энергии и их взаимодействия друг с другом в пространстве и времени. ")
        if call.data == 'button442':
            bot.send_message(call.message.chat.id, "Архитектор -- это специалист, который занимается проектированием зданий и других объектов, а также контролирует процесс строительства.")
        if call.data == 'button443':
            bot.send_message(call.message.chat.id, "Разработчик программного обеспечения (ПО) -- это  специалист в области информационных технологий, который создаёт, тестирует и поддерживает программы и приложения для компьютеров, мобильных устройств и других платформ. Цель — сделать надёжный и удобный продукт, который будет стабильно работать.")
        if call.data == 'button444':
            bot.send_message(call.message.chat.id, "Эколог -- это специалист, который изучает взаимодействие живых организмов с окружающей средой, а также влияние человеческой деятельности на природные экосистемы.")
        if call.data == 'button445':
            bot.send_message(call.message.chat.id, "Преподаватель -- это специалист, осуществляющий обучение студентов, слушателей или курсантов в вузах, колледжах и других образовательных организациях.")
           
           
           
           
           
           
           
           
           
        if call.data == 'button205':
            keyboard = types.InlineKeyboardMarkup()
            button209 = types.InlineKeyboardButton(text="История", callback_data='button209')
            button210 = types.InlineKeyboardButton(text="Философия", callback_data='button2010')
            button211 = types.InlineKeyboardButton(text="Литературоведение", callback_data='button211')
            button212 = types.InlineKeyboardButton(text="Языкознание", callback_data='button212')
            button213 = types.InlineKeyboardButton(text="Искусствоведение", callback_data='button213')
            button214 = types.InlineKeyboardButton(text="Психология", callback_data='button214')
            button215 = types.InlineKeyboardButton(text="Социология", callback_data='button215')
            button216 = types.InlineKeyboardButton(text="Этнография ", callback_data='button216')
            button217 = types.InlineKeyboardButton(text="Антропология", callback_data='button217')
            button218 = types.InlineKeyboardButton(text="Педагогика", callback_data='button218')
            button219 = types.InlineKeyboardButton(text="Ознакомиться🔎", callback_data='button219')
            bt25 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt25")
            keyboard.row(button209)
            keyboard.row(button210)
            keyboard.row(button211)
            keyboard.row(button212)
            keyboard.row(button213)
            keyboard.row(button214)
            keyboard.row(button215)
            keyboard.row(button216)
            keyboard.row(button217)
            keyboard.row(button218)
            keyboard.row(button219)
            keyboard.row(bt25)
            bot.send_message(call.message.chat.id, "Выберите предмет, который вам нравится. Если вы не понимаете значение какого-то предмета, то нажмите на --Ознакомиться--.", reply_markup=keyboard)
            
    #Ознакомиться======================================================================

        if call.data == 'button219':
            keyboard = types.InlineKeyboardMarkup()
            button257 = types.InlineKeyboardButton(text="История", callback_data='button209')
            button258 = types.InlineKeyboardButton(text="Философия", callback_data='button210')
            button259 = types.InlineKeyboardButton(text="Литературоведение", callback_data='button211')
            button260 = types.InlineKeyboardButton(text="Языкознание", callback_data='button212')
            button261 = types.InlineKeyboardButton(text="Искусствоведение", callback_data='button213')
            button262 = types.InlineKeyboardButton(text="Психология", callback_data='button214')
            button263 = types.InlineKeyboardButton(text="Социология", callback_data='button215')
            button264 = types.InlineKeyboardButton(text="Этнография ", callback_data='button216')
            button266 = types.InlineKeyboardButton(text="Антропология", callback_data='button217')
            button265 = types.InlineKeyboardButton(text="Педагогика", callback_data='button218')
            bt22 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt22")
            keyboard.row(button257)
            keyboard.row(button258)
            keyboard.row(button259)
            keyboard.row(button260)
            keyboard.row(button261)
            keyboard.row(button262)
            keyboard.row(button263)
            keyboard.row(button264)
            keyboard.row(button265)
            keyboard.row(button266)
            keyboard.row(bt22)
            bot.send_message(call.message.chat.id, "Нажмите на предмет, с которым вы хотите ознакомиться.", reply_markup=keyboard)
                
                
        if call.data == 'button257':
            bot.send_message(call.message.chat.id, "История -- история занимается изучением прошлого человечества, его развития, изменения обществ, государств, цивилизаций и отдельных личностей. Она помогает понять современные реалии, выявляя причины возникновения тех или иных процессов и ситуаций.")
        if call.data == 'button258':
            bot.send_message(call.message.chat.id, "Философия -- философия ставит перед собой цель исследовать природу бытия, познания, этику, эстетику, политику и другие важнейшие вопросы существования человека. Это наука о мировоззрении, осмыслении мира и поиске смысла жизни.")
        if call.data == 'button259':
            bot.send_message(call.message.chat.id, "Литературоведение -- литературоведение изучает литературу, её формы, жанры, художественное содержание и развитие литературных традиций. Оно также включает теорию литературы, критику и историю литературы.")
        if call.data == 'button260':
            bot.send_message(call.message.chat.id, "Языкознание -- Наука о языках и речи, изучении структуры, функционирования и исторического развития языков. Включает фонетику, грамматику, лексикологию, стилистику и семантику.")
        if call.data == 'button261':
            bot.send_message(call.message.chat.id, "Искусствоведение -- Искусствоведение направлено на изучение искусства, его форм, стилей, видов и особенностей восприятия. Эта область занимается живописью, скульптурой, архитектурой, музыкой, театром и кино.")
        if call.data == 'button262':
            bot.send_message(call.message.chat.id, "Психология -- психология изучает поведение, мышление, эмоции и сознание человека. Выделяются клиническая психология, социальная психология, детская психология, педагогическая психология и многие другие специализированные направления.")
        if call.data == 'button263':
            bot.send_message(call.message.chat.id, "Социология -- изучение общества, социальной структуры, социального поведения и взаимоотношений индивидов внутри коллективов. Объектами изучения являются социальные институты, группы, классы, культура и общество в целом.")
        if call.data == 'button264':
            bot.send_message(call.message.chat.id, "Этнография -- этнография занимается описанием, сравнительным изучением народов, их обычаев, верований, быта и материальной культуры. Её задачей является выявление сходства и различий среди этнических групп.")
        if call.data == 'button265':
            bot.send_message(call.message.chat.id, "Антропология -- антропология рассматривает человеческую сущность, происхождение, физическое строение, развитие и разнообразие культур. Она объединяет биологический и социальный подходы к изучению человека.")
        if call.data == 'button266':
            bot.send_message(call.message.chat.id, "Педагогика -- Педагогика изучает процесс воспитания и обучения, методики преподавания, организацию образовательного процесса и формирование личности ребенка и взрослого.")
        
        
        
            
            
            
            
        if call.data == 'button223':
            keyboard = types.InlineKeyboardMarkup()
            button224 = types.InlineKeyboardButton(text="Природоведение ", callback_data='button224')
            button225 = types.InlineKeyboardButton(text="Биология", callback_data='button225')
            button226 = types.InlineKeyboardButton(text="Химия", callback_data='button226')
            button227 = types.InlineKeyboardButton(text="Физика", callback_data='button227')
            button228 = types.InlineKeyboardButton(text="Астрономия", callback_data='button228')
            button229 = types.InlineKeyboardButton(text="Экология", callback_data='button229')
            button230 = types.InlineKeyboardButton(text="Естествознание ", callback_data='button230')
            button231 = types.InlineKeyboardButton(text="Основы безопасности и защиты Родины ", callback_data='button231')
            button232= types.InlineKeyboardButton(text="Ознакомиться🔎", callback_data='button232')
            bt23 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt23")
            keyboard.row(button224)
            keyboard.row(button225)
            keyboard.row(button226)
            keyboard.row(button227)
            keyboard.row(button228)
            keyboard.row(button229)
            keyboard.row(button230)
            keyboard.row(button231)
            keyboard.row(button232)
            keyboard.row(bt23)
            bot.send_message(call.message.chat.id, "Выберите предмет, который вам нравится. Если вы не понимаете значение какого-то предмета, то нажмите на --Ознакомиться--.", reply_markup=keyboard)
           
           
        if call.data == 'button232':
            keyboard = types.InlineKeyboardMarkup()
            button267 = types.InlineKeyboardButton(text="Природоведение ", callback_data='button224')
            button268 = types.InlineKeyboardButton(text="Биология", callback_data='button225')
            button269 = types.InlineKeyboardButton(text="Химия", callback_data='button226')
            button270 = types.InlineKeyboardButton(text="Физика", callback_data='button227')
            button271 = types.InlineKeyboardButton(text="Астрономия", callback_data='button228')
            button272 = types.InlineKeyboardButton(text="Экология", callback_data='button229')
            button273 = types.InlineKeyboardButton(text="Естествознание ", callback_data='button230')
            button274 = types.InlineKeyboardButton(text="Основы безопасности и защиты Родины", callback_data='button231')
            bt24 = types.InlineKeyboardButton(text="Вернуться 🔙", callback_data="bt24")
            keyboard.row(button267)
            keyboard.row(button268)
            keyboard.row(button269)
            keyboard.row(button270)
            keyboard.row(button271)
            keyboard.row(button272)
            keyboard.row(button273)
            keyboard.row(button274)
            keyboard.row(bt24)
            bot.send_message(call.message.chat.id, "Нажмите на предмет, с которым вы хотите ознакомиться.", reply_markup=keyboard)
            
        if call.data == 'button267':
            bot.send_message(call.message.chat.id, "Природоведение --  совокупность знаний о природе, или естествознание как предмет преподавания.")
        if call.data == 'button268':
            bot.send_message(call.message.chat.id, "Биология -- наука о живых существах и природе, строении живых организмов и их взаимодействии с окружающей средой. Относится к естественным наукам.")
        if call.data == 'button269':
            bot.send_message(call.message.chat.id, "Химия -- это наука о веществах, их строении, свойствах и взаимных превращениях. Также химией называют качественный состав чего-либо, например «химия нефти», «химия крови».")
        if call.data == 'button270':
            bot.send_message(call.message.chat.id, "Физика -- это фундаментальная естественная наука, изучающая общие законы природы, материи и её движения.")
        if call.data == 'button271':
            bot.send_message(call.message.chat.id, "Астрономия -- наука о движении, строении, возникновении и развитии небесных тел, их систем, а также Вселенной в целом. Название произошло от слияния двух слов: ἄστρον — «звезда» и νόμος — «закон».")
        if call.data == 'button272':
            bot.send_message(call.message.chat.id, "Экология -- наука о взаимоотношениях живых организмов и окружающей среды, об обмене веществ и потоках энергии, которые делают возможной жизнь на Земле, и о приспособлениях организмов к изменяющимся условиям существования.")
        if call.data == 'button273':
            bot.send_message(call.message.chat.id, "Естествознание -- это система наук о законах, явлениях и свойствах объектов природы. Включает множество отраслей — естественных наук")
        if call.data == 'button274':
            bot.send_message(call.message.chat.id, "Основы безопасности и защиты Родины -- дисциплина, изучаемая школьниками и студентами образовательных учреждений России, направленная на формирование базовых знаний и практических навыков в области личной и общественной безопасности, а также основ военной подготовки.")
        
            
    
            
            
            
bot.infinity_polling()