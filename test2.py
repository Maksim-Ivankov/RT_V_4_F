
# "ЭТО РАБОТАЕТ!!!!!!! НО НЕ В FLASK"
# api_id_tg = '29054097'
# api_hash_id_tg = 'ed0af3e9cb2fb29e47631254716cae92'
# username_tg = 'maksimivankov'
# chat = 'https://t.me/robo_trade_chat'

# from telethon import TelegramClient, events, sync

# client = TelegramClient('session_name', api_id_tg, api_hash_id_tg)
# client.start()
# channel_username = 'robo_trade_chat'# your channel
# for message in client.get_messages(channel_username, limit=10):
#     if message.message:
#         # print(f'{message.from_id.user_id} - {message.message}')
#         print(f'{client.get_entity(message.from_id.user_id).first_name} - {message.message}')
# # print(client.get_messages(channel_username, limit=10))



# parser = argparse.ArgumentParser(description="Extracts Telegram history.")
# parser.add_argument("29054097",
#                     help="something like ../tg/bin/telegram-cli")
# parser.add_argument("ed0af3e9cb2fb29e47631254716cae92",
#                     help="something like ../tg/tg-server.pub")
# parser.add_argument("maksimivankov")
# parser.add_argument("lollololo.csv",
#                     help="CSV file where to save the messages",
#                     default="history.csv")
# parser.add_argument("10",
#                     type=int,
#                     help="Maximum number of messages to retrieve.",
#                     default=MIN_MESSAGES)
# args = parser.parse_args()

# args.telegram_binary = 29054097
# args.telegram_key = 'ed0af3e9cb2fb29e47631254716cae92'
# args.contact_name = 'maksimivankov'

# if __name__ == '__main__':
#     download_history(
#         args.telegram_binary, args.telegram_key,
#         args.contact_name, args.csv_output_filename,
#         args.min_messages
#     )



















