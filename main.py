import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)



@bot.event
async def on_ready():
    print(f'бот зашел на сервер {bot.user}')

@bot.command()
async def display(ctx, message):
    await ctx.reply(message)

@bot.command()
async def divide(ctx, first: int, second: int):
    try:
        await ctx.send(first/second)

    except:
        await ctx.send('ОшиБкА')

bot.run('MTEwMjE4MjYwNTg1Nzc1MTEwMA.GUcL5P.Q41bTv5Os7qAoiyi7lXPpLumO_T9CEVVXW9kNE')

