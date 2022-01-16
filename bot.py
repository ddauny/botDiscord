import discord
from discord.ext import commands
from discord import client
from youtube_dl import yt

print("il bot si sta avviando")
token = 'OTMyMjU5NTg4NzI2NzQ3MTk2.YeQYZg.obTFR4-WzEJ6E-k9y9LtZBO7Fwg'
cmds = ['1help: restituisce la lista dei comandi disponibili\n', 'secondo comando\n']
str_help = "```Ecco la lista dei comandi disponibili:\n"

client = commands.Bot(command_prefix="1")

@client.event
async def on_ready():
    print(client.user, "è ora online")


@client.event
async def on_message(message):     
    s = message.content.split() #vettore con i campi dei comandi
    if s[0] == "1help":
        await lista_comandi(message, str_help)
    elif s[0] == "1play":
        await play(message, s[1])
    elif s[0] == "1leave":
        await leave(message)
    

@client.command()
async def play(ctx, url_: str):
    vc = discord.utils.get(ctx.guild.voice_channels, id=ctx.author.voice.channel.id)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await vc.connect()
    #if not voice.is_playing():
     #   voice.resume() 
        

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voice.disconnect()


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('Il bot non sta riproducendo')


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    





async def lista_comandi(message, s):
    for i in range(len(cmds)):
        s = s + cmds[i]
    s = s + "```" 
    await message.channel.send(s)


client.run(token)