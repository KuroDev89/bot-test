import discord
from discord.ext import commands

import datetime

import random

bot=commands.Bot(command_prefix="!", description='This is a test bot for discord')

#probando conexión
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#suma de valores
@bot.command()
async def sum(ctx,num1:int,num2:int):
    await ctx.send(num1+num2)

#saludo random
@bot.command()
async def hola(ctx):
    saludos=['hola','holiwi','que pasa culeao?', 'aloha', 'llegó el lechero']
    await ctx.send(random.choice(saludos))

#estadísticas del servidor
@bot.command()
async def stat(ctx):
    embed=discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum is simply dummy text of the printing and typesetting industry.", timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.blue())
    embed.add_field(name="Server creado el ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Creador del server ", value=f"{ctx.guild.owner}")
    await ctx.send(embed=embed)

#bot transmitiendo
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Gameplays", url="https://www.twitch.tv/kurodogames"))
    print ('My bot is online')

bot.run('NzQ5ODAxOTY4NDUyNTAxNjY1.X0xRfw.FirdVQ2TJ-PLUBkCTTCq7VnH9Jg')