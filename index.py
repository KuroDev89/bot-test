import discord
from discord.ext import commands

import datetime

import random

from urllib import parse, request #permite realizar peticiones a una url de internet
import re #expersiones regulares

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
    embed.add_field(name="Server creado el ", value=f"{ctx.guild.created_at}") #la f le da el formato de salida que se desea
    embed.add_field(name="Creador del server ", value=f"{ctx.guild.owner}")
    embed.set_thumbnail(url="https://www.kurodo.games/img/logo.png")
    await ctx.send(embed=embed)

#buscar video en youtube.com
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall(
        r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])




#bot transmitiendo
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Gameplays", url="https://www.twitch.tv/kurodogames"))
    print ('My bot is online')

bot.run('') #Retirar TOKEN AL SUBIR#