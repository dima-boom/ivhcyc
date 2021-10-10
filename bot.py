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

  token = "bdf7d0d51edee96551f2d6e0caee66c21a850766bd4a495bfa716403179cd7f7ee15818d781fd2d00b61f"
  authorize = vk_api.VkApi(token=token)
  longpoll = VkLongPoll(authorize)
  for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # ПРОВЕРКА
        reseived_message = event.text.lower()
        sender = event.user_id
        if sender == 558612192:
            if reseived_message == 'начать':
                write_message(sender, "Работает!")
            elif reseived_message[0:4] == '/lii':
                naz = text1(reseived_message)
                ckok = text2(reseived_message)
                requests.post('https://instagram777.ru/api', params={'key': '1356536ce1fe797f8e1ff1b092ef60fe',
                                    'action': 'create', 'service': '131', 'quantity': int(ckok), 'link': str(naz)})
                write_message(sender, 'Всё ок')
            elif reseived_message[0:5] == '/poid':
                naz = text1(reseived_message)
                ckok = text2(reseived_message)
                requests.post('https://instagram777.ru/api', params={'key': '1356536ce1fe797f8e1ff1b092ef60fe',
                                    'action': 'create', 'service': '177', 'quantity': int(ckok), 'link': str(naz)})
                write_message(sender, 'Всё ок')
            elif reseived_message[0:5] == '/proc':
                naz = text1(reseived_message)
                ckok = text2(reseived_message)
                requests.post('https://instagram777.ru/api', params={'key': '1356536ce1fe797f8e1ff1b092ef60fe',
                                    'action': 'create', 'service': '154', 'quantity': int(ckok), 'link': str(naz)})
                write_message(sender, 'Всё ок')

            elif reseived_message[0:4] == '/pod':
                naz = text1(reseived_message)
                ckok = text2(reseived_message)
                requests.post('https://instagram777.ru/api', params={'key': '1356536ce1fe797f8e1ff1b092ef60fe',
                                    'action': 'create', 'service': '350', 'quantity': int(ckok), 'link': str(naz)})
                write_message(sender, 'Всё ок')
            elif reseived_message[0:4] == '/lik':
                naz = text1(reseived_message)
                ckok = text2(reseived_message)
                requests.post('https://instagram777.ru/api', params={'key': '1356536ce1fe797f8e1ff1b092ef60fe',
                                    'action': 'create', 'service': '351', 'quantity': int(ckok), 'link': str(naz)})
                write_message(sender, 'Всё ок')
            elif reseived_message[0:4] == '/rep':
                naz = text1(reseived_message)
                ckok = text2(reseived_message)
                requests.post('https://instagram777.ru/api', params={'key': '1356536ce1fe797f8e1ff1b092ef60fe',
                                    'action': 'create', 'service': '352', 'quantity': int(ckok), 'link': str(naz)})
                write_message(sender, 'Всё ок')
            elif reseived_message[0:5] == '/pood':
                naz = text1(reseived_message)
                ckok = text2(reseived_message)
                requests.post('https://instagram777.ru/api', params={'key': '1356536ce1fe797f8e1ff1b092ef60fe',
                                    'action': 'create', 'service': '400', 'quantity': int(ckok), 'link': str(naz)})
                write_message(sender, 'Всё ок')
            elif reseived_message[0:5] == '/pros':
                naz = text1(reseived_message)
                ckok = text2(reseived_message)
                requests.post('https://instagram777.ru/api', params={'key': '1356536ce1fe797f8e1ff1b092ef60fe',
                                    'action': 'create', 'service': '2191', 'quantity': int(ckok), 'link': str(naz)})
                write_message(sender, 'Всё ок')


except:
  os.system('python bot.py')
