try:
    import vk_api, requests, os
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id


    def text1(arg):
        return arg.split()[1]


    def text2(arg):
        return arg.split()[2]


    def write_message(sender, message):
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})



    token = "7aa98252b9c75da21e4937a281364c17711e460f059b5200e4dee90345e6546a24b351d8c69e5c2eaae6e"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            # ПРОВЕРКА
            reseived_message = event.text.lower()
            sender = event.user_id
            if sender == 664033661:
                if reseived_message == 'начать':
                    write_message(sender, "Работает!")
                # ОТПРАВКА ЗАПРОСТА ЧЕРЕЗ ПОТОКИ 
                elif reseived_message[0:4] == '/lik':
                    # ПРИМЕР СООБЩЕНИЯ: \l 79287777777 10
                    sslka = text1(reseived_message)
                    ckok = text2(reseived_message)

                    requests.post('https://instagram777.ru/api', params={'key': '13fbaa7934e4869e63c9378e5142d539',
                                            'action': 'create', 'service': '351', 'quantity': int(ckok), 'link': str(sslka)})
                    
                    write_message(sender, 'Всё ок')
                elif reseived_message[0:4] == '/pod':
                    # ПРИМЕР СООБЩЕНИЯ: \l 79287777777 10
                    sslka = text1(reseived_message)
                    ckok = text2(reseived_message)
                    
                    requests.post('https://instagram777.ru/api', params={'key': '13fbaa7934e4869e63c9378e5142d539',
                                            'action': 'create', 'service': '350', 'quantity': int(ckok), 'link': str(sslka)})

                    write_message(sender, 'Всё ок')
                elif reseived_message[0:4] == '/rep':
                    # ПРИМЕР СООБЩЕНИЯ: \l 79287777777 10
                    sslka = text1(reseived_message)
                    ckok = text2(reseived_message)

                    requests.post('https://instagram777.ru/api', params={'key': '13fbaa7934e4869e63c9378e5142d539',
                                            'action': 'create', 'service': '352', 'quantity': int(ckok), 'link': str(sslka)})
                    
                    write_message(sender, 'Всё ок')
                elif reseived_message[0:5] == '/proc':
                    # ПРИМЕР СООБЩЕНИЯ: \l 79287777777 10
                    sslka = text1(reseived_message)
                    ckok = text2(reseived_message)

                    requests.post('https://instagram777.ru/api', params={'key': '13fbaa7934e4869e63c9378e5142d539',
                                            'action': 'create', 'service': '154', 'quantity': int(ckok), 'link': str(sslka)})
                elif reseived_message[0:5] == '/pros':
                    # ПРИМЕР СООБЩЕНИЯ: \l 79287777777 10
                    sslka = text1(reseived_message)
                    ckok = text2(reseived_message)

                    requests.post('https://instagram777.ru/api', params={'key': '13fbaa7934e4869e63c9378e5142d539',
                                            'action': 'create', 'service': '3191', 'quantity': int(ckok), 'link': str(sslka)})
                    
                    write_message(sender, 'Всё ок')
                elif reseived_message[0:5] == '/pood':
                    # ПРИМЕР СООБЩЕНИЯ: \l 79287777777 10
                    sslka = text1(reseived_message)
                    ckok = text2(reseived_message)

                    requests.post('https://instagram777.ru/api', params={'key': '13fbaa7934e4869e63c9378e5142d539',
                                            'action': 'create', 'service': '404', 'quantity': int(ckok), 'link': str(sslka)})
                    
                    write_message(sender, 'Всё ок')
except:
    os.system('python bot.py')

