import selfcord
import json

# Load the config file
with open('config.json') as f:
    config = json.load(f)

class MyClient(selfcord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # only respond to ourselves
        if message.author.id not in config["target_user_ids"]:
            return

        await message.channel.send(config["responding_message"])

client = MyClient()
client.run(config["host_token"])