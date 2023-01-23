import discord
from discord.ext import commands
import EFTChangesAPI

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(bot.user.name, "로 로그인 함")


@bot.command()
async def 탄약(ctx, *, message):
    search_result = EFTChangesAPI.ammo_search(message)
    await ctx.send(search_result)

token = ""
bot.run(token)
