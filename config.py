# Файл config.py с вашими учетными данными и параметрами общения с клиентами

# Ваши учетные данные для подключения к телеграму
api_id = 123456 # Ваш api_id
api_hash = 'abcdef1234567890abcdef1234567890' # Ваш api_hash
phone = '+71234567890' # Ваш номер телефона

# Параметры общения с клиентами

# Тайминг - интервалы времени в секундах, через которые будем отправлять сообщения или звонить клиентам
timing = {
    'text': (10, 20), # Отправляем текстовые сообщения через 10-20 секунд после предыдущего сообщения или звонка
    'voice': (30, 60), # Отправляем голосовые сообщения через 30-60 секунд после предыдущего сообщения или звонка
    'media': (40, 80), # Отправляем медиа сообщения (фото, видео и т.д.) через 40-80 секунд после предыдущего сообщения или звонка
    'call': (120, 180), # Звоним клиентам через 120-180 секунд после предыдущего сообщения или звонка
}

# Режимы звонков и приглашений - параметры, которые определяют, когда и как будем звонить клиентам или приглашать их на канал или группу
call_mode = {
    'enabled': True, # Включен ли режим звонков
    'always': False, # Звонить ли даже если были раньше звонки
    'message': 'Привет, это {name} из компании {company}. Я хотел бы поговорить с вами о нашем новом продукте. Пожалуйста, перезвоните мне по номеру {phone}.' # Сообщение, которое отправляем, если клиент не поднял трубку
}

invite_mode = {
    'enabled': True, # Включен ли режим приглашений
    'channel': '@my_channel', # Ссылка на канал или группу, на которую приглашаем
    'message': 'Приглашаю вас на наш канал {channel}, где вы можете узнать больше о нашем продукте и получить специальные предложения.' # Сообщение, которое отправляем с приглашением
}

# Случайная последовательность высылки сообщений - параметр, который определяет, будем ли мы отправлять сообщения из шаблонов в случайном порядке или в определенном
random_mode = False

# Переменные из нашего профиля, которые будем подставлять в текстовые сообщения
profile = {
    'name': 'Иван', # Ваше имя
    'company': 'ООО "Рога и копыта"', # Название вашей компании
    'website': 'https://rogaikopyta.ru', # Ссылка на ваш сайт
    'catalog': 'https://rogaikopyta.ru/catalog.pdf', # Ссылка на ваш каталог
    'phone': '+71234567890', # Ваш номер телефона
    'email': 'ivan@rogaikopyta.ru' # Ваш адрес электронной почты
}
