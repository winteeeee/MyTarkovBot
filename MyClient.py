import discord
from discord.ext import commands
import EFTChangesAPI

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(bot.user.name, "로 로그인 함")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("[오류] 알 수 없는 명령어. 올바른 명령어를 입력해주세요")


@bot.command()
async def 탄약(ctx, *, message):
    print("[", ctx.message.guild.name, "]", "[", ctx.message.channel, "] [", ctx.message.author, "] ", "탄약 명령어 호출함")
    search_result = EFTChangesAPI.ammo_search(message)
    await ctx.send(search_result)


@탄약.error
async def 탄약_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("[오류] 잘못된 명령어. 검색어를 입력해주세요")


@bot.command()
async def 지도(ctx, *, message):
    print("[", ctx.message.guild.name, "]", "[", ctx.message.channel, "] [", ctx.message.author, "] ", "지도 명령어 호출함")
    if message == "공장":
        await ctx.send(file=discord.File("data/공장_지도.png"))
    elif message == "나들목":
        await ctx.send(file=discord.File("data/나들목_내부_지도.png"))
        await ctx.send(file=discord.File("data/나들목_외부_지도.png"))
    elif message == "등대":
        await ctx.send(file=discord.File("data/등대_지도.png"))
    elif message == "리저브":
        await ctx.send(file=discord.File("data/리저브_지도.png"))
        await ctx.send(file=discord.File("data/리저브_지하_지도.png"))
    elif message == "삼림":
        await ctx.send(file=discord.File("data/삼림_지도.png"))
    elif message == "세관":
        await ctx.send(file=discord.File("data/세관_지도.png"))
    elif message == "연구소":
        await ctx.send(file=discord.File("data/연구소_1층_지도.png"))
        await ctx.send(file=discord.File("data/연구소_2층_지도.png"))
        await ctx.send(file=discord.File("data/연구소_지하_지도.png"))
    elif message == "해안선":
        await ctx.send(file=discord.File("data/해안선_지도.png"))
    elif message == "타르코프시내":
        await ctx.send(file=discord.File("data/타르코프_시내_지도.png"))


@지도.error
async def 지도_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("[오류] 잘못된 명령어. 검색어를 입력해주세요")


token = ""
bot.run(token)
