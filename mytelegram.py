from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 1090456
api_hash = 'beb4755795a60f94da87d88c8b62653c'

my_channle_id = 1353575894
target_channel_id = 1320956312

with TelegramClient('session_name', api_id, api_hash) as client:
    @client.on(events.NewMessage())
    async def handler(event):
        sender = await event.get_sender()
        print('received message from {}'.format(sender.id))
        if sender.id == target_channel_id:
            print('forwarding message..')
            await client.send_message(entity = my_channle_id, message = event.message.text)
    client.run_until_disconnected()
