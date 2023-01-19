import discord
import MyClient
import EFTChangesAPI

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
token = "MTA2NTY1MTA4MjU3NzA2NDA2Ng.GBnU3F.hAgxDhtSX0OJhXh8Q3SYG-r2k8hX-K7a8RG6rg"
client.run(token)
