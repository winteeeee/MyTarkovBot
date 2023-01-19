import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(self.user, "로 로그인 함")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '타르코프':
            await message.channel.send('망겜')

        print("[", message.guild.name, "]", "[", message.channel, "] [", message.author, "] ", message.content)
