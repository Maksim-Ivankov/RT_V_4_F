# import flet as ft
# from variable import *
# from imports import *

# # from xmlrpc.client import DateTime
# # from telethon.sync import TelegramClient
 
# # from telethon.tl.functions.messages import GetDialogsRequest
# # from telethon.tl.types import InputPeerEmpty
# # from telethon.tl.functions.messages import GetHistoryRequest
# # from telethon.tl.types import PeerChannel
 
# # import csv



# class Get_tg_data:
#     def __init__(self):
#         super().__init__()
#         print('------------')
        
#         # api_id = 18377495
#         # api_hash = "a0c785ad0fd3e92e7c131f0a70987987"
#         # phone = "+79991669331"

#         # запуск в потоке получаем тг
#     def did_mount(self):
#         self.running = True # условие запусака потока
#         self.myThread_tg = threading.Thread(target=self.update_data_tg, args=(), daemon=True)
#         self.myThread_tg.start()

#     #то что крутится в потоке - получаем тг данные
#     def update_data_tg(self):
#         while self.running:
#             print('поток')
#             time.sleep(1)
#             # client = TelegramClient(username_tg, api_id_tg, api_hash_id_tg)

#         # client.start()
    
    

# # import json

# # from telethon.sync import TelegramClient
# # from telethon import connection

# # # для корректного переноса времени сообщений в json
# # from datetime import date, datetime

# # # классы для работы с каналами
# # from telethon.tl.functions.channels import GetParticipantsRequest
# # from telethon.tl.types import ChannelParticipantsSearch

# # # класс для работы с сообщениями
# # from telethon.tl.functions.messages import GetHistoryRequest

# # print('Внутри тг')

# # client = TelegramClient(username_tg, api_id_tg, api_hash_id_tg,)

# # client.start()

# # async def dump_all_participants(channel):
# # 	"""Записывает json-файл с информацией о всех участниках канала/чата"""
# # 	offset_user = 0    # номер участника, с которого начинается считывание
# # 	limit_user = 100   # максимальное число записей, передаваемых за один раз

# # 	all_participants = []   # список всех участников канала
# # 	filter_user = ChannelParticipantsSearch('')

# # 	while True:
# # 		participants = await client(GetParticipantsRequest(channel,
# # 			filter_user, offset_user, limit_user, hash=0))
# # 		if not participants.users:
# # 			break
# # 		all_participants.extend(participants.users)
# # 		offset_user += len(participants.users)

# # 	all_users_details = []   # список словарей с интересующими параметрами участников канала

# # 	for participant in all_participants:
# # 		all_users_details.append({"id": participant.id,
# # 			"first_name": participant.first_name,
# # 			"last_name": participant.last_name,
# # 			"user": participant.username,
# # 			"phone": participant.phone,
# # 			"is_bot": participant.bot})

# # 	with open(path_data_user_tg_chat, 'w', encoding='utf8') as outfile:
# # 		json.dump(all_users_details, outfile, ensure_ascii=False)


# # async def dump_all_messages(channel):
# # 	"""Записывает json-файл с информацией о всех сообщениях канала/чата"""
# # 	offset_msg = 0    # номер записи, с которой начинается считывание
# # 	limit_msg = 100   # максимальное число записей, передаваемых за один раз

# # 	all_messages = []   # список всех сообщений
# # 	total_messages = 0
# # 	total_count_limit = 10  # поменяйте это значение, если вам нужны не все сообщения

# # 	class DateTimeEncoder(json.JSONEncoder):
# # 		'''Класс для сериализации записи дат в JSON'''
# # 		def default(self, o):
# # 			if isinstance(o, datetime):
# # 				return o.isoformat()
# # 			if isinstance(o, bytes):
# # 				return list(o)
# # 			return json.JSONEncoder.default(self, o)

# # 	while True:
# # 		history = await client(GetHistoryRequest(
# # 			peer=channel,
# # 			offset_id=offset_msg,
# # 			offset_date=None, add_offset=0,
# # 			limit=limit_msg, max_id=0, min_id=0,
# # 			hash=0))
# # 		if not history.messages:
# # 			break
# # 		messages = history.messages
# # 		for message in messages:
# # 			all_messages.append(message.to_dict())
# # 		offset_msg = messages[len(messages) - 1].id
# # 		total_messages = len(all_messages)
# # 		if total_count_limit != 0 and total_messages >= total_count_limit:
# # 			break

# # 	with open(path_data_message_tg_chat, 'w', encoding='utf8') as outfile:
# # 		 json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)


# # async def main():
# # 	url = 'https://t.me/robo_trade_chat'
# # 	channel = await client.get_entity(url)
# # 	await dump_all_participants(channel)
# # 	await dump_all_messages(channel)


# # with client:
# # 	client.loop.run_until_complete(main())

# # async def dump_all_participants(channel):
# # 	"""Записывает json-файл с информацией о всех участниках канала/чата"""
# # 	offset_user = 0    # номер участника, с которого начинается считывание
# # 	limit_user = 100   # максимальное число записей, передаваемых за один раз

# # 	all_participants = []   # список всех участников канала
# # 	filter_user = ChannelParticipantsSearch('')

# # 	while True:
# # 		participants = await client(GetParticipantsRequest(channel,
# # 			filter_user, offset_user, limit_user, hash=0))
# # 		if not participants.users:
# # 			break
# # 		all_participants.extend(participants.users)
# # 		offset_user += len(participants.users)

# # 	all_users_details = []   # список словарей с интересующими параметрами участников канала

# # 	for participant in all_participants:
# # 		all_users_details.append({"id": participant.id,
# # 			"first_name": participant.first_name,
# # 			"last_name": participant.last_name,
# # 			"user": participant.username,
# # 			"phone": participant.phone,
# # 			"is_bot": participant.bot})

# # 	with open(path_data_user_tg_chat, 'w', encoding='utf8') as outfile:
# # 		json.dump(all_users_details, outfile, ensure_ascii=False)


# # async def dump_all_messages(channel):
# # 	"""Записывает json-файл с информацией о всех сообщениях канала/чата"""
# # 	offset_msg = 0    # номер записи, с которой начинается считывание
# # 	limit_msg = 100   # максимальное число записей, передаваемых за один раз

# # 	all_messages = []   # список всех сообщений
# # 	total_messages = 0
# # 	total_count_limit = 10  # поменяйте это значение, если вам нужны не все сообщения

# # 	class DateTimeEncoder(json.JSONEncoder):
# # 		'''Класс для сериализации записи дат в JSON'''
# # 		def default(self, o):
# # 			if isinstance(o, datetime):
# # 				return o.isoformat()
# # 			if isinstance(o, bytes):
# # 				return list(o)
# # 			return json.JSONEncoder.default(self, o)

# # 	while True:
# # 		history = await client(GetHistoryRequest(
# # 			peer=channel,
# # 			offset_id=offset_msg,
# # 			offset_date=None, add_offset=0,
# # 			limit=limit_msg, max_id=0, min_id=0,
# # 			hash=0))
# # 		if not history.messages:
# # 			break
# # 		messages = history.messages
# # 		for message in messages:
# # 			all_messages.append(message.to_dict())
# # 		offset_msg = messages[len(messages) - 1].id
# # 		total_messages = len(all_messages)
# # 		if total_count_limit != 0 and total_messages >= total_count_limit:
# # 			break

# # 	with open(path_data_message_tg_chat, 'w', encoding='utf8') as outfile:
# # 		 json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)


# # async def main():
# # 	url = 'https://t.me/robo_trade_chat'
# # 	channel = await client.get_entity(url)
# # 	await dump_all_participants(channel)
# # 	await dump_all_messages(channel)


# # with client:
# # 	client.loop.run_until_complete(main())








