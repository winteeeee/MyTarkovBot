import asyncio
from datetime import datetime
import discord
from discord.ext import commands
import EFTChangesAPI
from bs4 import BeautifulSoup
from selenium import webdriver

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), bot.user.name, "로 로그인 함")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("[오류] 알 수 없는 명령어. 올바른 명령어를 입력해주세요")


@bot.command()
async def 탄약(ctx, *, message):
    print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), "[", ctx.message.guild.name, "]", "[", ctx.message.channel, "] [", ctx.message.author, "] ", "탄약 명령어 호출함")
    search_result = EFTChangesAPI.ammo_search(message)
    await ctx.send(search_result)


@탄약.error
async def 탄약_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("[오류] 잘못된 명령어. 검색어를 입력해주세요")


@bot.command()
async def 지도(ctx, *, message):
    print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"),"[", ctx.message.guild.name, "]", "[", ctx.message.channel, "] [", ctx.message.author, "] ", "지도 명령어 호출함")
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


@bot.command()
async def 가격(ctx, *, message):
    print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"),"[", ctx.message.guild.name, "]", "[", ctx.message.channel, "] [", ctx.message.author, "] ", "가격 명령어 호출함")
    loop = asyncio.get_event_loop()
    path = "resource/chromedriver.exe"
    driver = webdriver.Chrome(path)

    await loop.run_in_executor(None, driver.get, "https://tarkov-market.com/")
    element = driver.find_element_by_css_selector("""#__layout > div > div > div.page-content > div.w-100 > div.search > input[type=text]""")
    element.send_keys(message)

    await asyncio.sleep(1.5)
    soup = await loop.run_in_executor(None, BeautifulSoup, driver.page_source, 'html.parser')

    if len(soup.find(class_="cards-list").text) > 100:
        if soup.find(class_="minus"):
            await ctx.send("플리마켓에 올릴 수 없는 상품입니다.")

        else:
            price = soup.select_one("#__layout > div > div > div.page-content > div.w-100 > div.cards-list > div > div.body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text
            await ctx.send(message + " : " + price)

    else:
        await ctx.send("[오류] 아이템이 존재하지 않습니다.")

    await loop.run_in_executor(None, driver.close)


@가격.error
async def 가격_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("[오류] 잘못된 명령어. 검색어를 입력해주세요")


@bot.command()
async def 검색(ctx, *, message):
    print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"),"[", ctx.message.guild.name, "]", "[", ctx.message.channel, "] [", ctx.message.author, "] ", "검색 명령어 호출함")
    loop = asyncio.get_event_loop()
    path = "resource/chromedriver.exe"
    driver = webdriver.Chrome(path)

    await loop.run_in_executor(None, driver.get, "https://escapefromtarkov.fandom.com/wiki/Escape_from_Tarkov_Wiki")
    search_button = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/header/div/div[3]/a[1]")
    search_button.click()

    await asyncio.sleep(1)
    search_bar = driver.find_element_by_xpath("/html/body/div[10]/div/form/input")
    search_bar.send_keys(message)

    await asyncio.sleep(1)
    soup = await loop.run_in_executor(None, BeautifulSoup, driver.page_source, 'html.parser')

    if soup.find(class_="wds-list wds-is-linked SearchResults-module_results__k8itn") is not None:
        link = soup.select_one("body > div.search-modal > div > ul > li:nth-child(1) > a")["href"]
        await ctx.send(link)
    else:
        await ctx.send("[오류] 항목이 존재하지 않습니다.")

    await loop.run_in_executor(None, driver.close)


@검색.error
async def 검색_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("[오류] 잘못된 명령어. 검색어를 입력해주세요")


token = ""
bot.run(token)
