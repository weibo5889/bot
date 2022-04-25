from ast import keyword
from dis import dis, disco
from traceback import format_tb
import darksky
from email import message
from core import CogExtension
from multiprocessing import Event
import discord 
from discord.ext import commands
import random 
import json
import youtube_dl
import os
with open('setting.json', mode= 'r' , encoding="utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="!!")

@bot.event
async def on_ready():
    print(">>我復活拉<<")




@bot.command()
async def delete(ctx):
    message = ctx.message.id
    await message.delete()

@bot.command()

async def tag(ctx):
    await ctx.send(f'嗨{ctx.author.mention}')              
    

@bot.command()
async def 講話(ctx):
    s=random.choice(jdata['s'])
    await ctx.send(s)
@bot.command()
async def 圖片(ctx):
    p=random.choice(jdata['p'])
    pi= discord.File(p)
    await ctx.send(file = pi)




@bot.command()
async def play(ctx, url : str):

    song_three = os.path.isfile("song.mp3")

    try:
        if song_three:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("song is playing")

    
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = "一般")
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    
    # if voice is None or not voice.is_connected():
        

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)

    if voice:
        await voice.disconnect()
        await ctx.send("高歌離席")
    else:
        await ctx.send("阿我就不在")
@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("沒歌你是要我暫停甚麼")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")



@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()

def setup(bot):
    bot.add_cog(bot(bot))


@bot.event
async def on_message(msg):
    
    if ("你媽漂來的") in msg.content :
        
        await msg.delete()
        await msg.channel.send(f'{msg.author.mention}乃滋乃滋')
    if ("妳媽漂來的") in msg.content :
        
        await msg.delete()
        await msg.channel.send(f'{msg.author.mention}乃滋乃滋')
    if ("你媽瞟來的") in msg.content :
        
        await msg.delete()
        await msg.channel.send(f'{msg.author.mention}乃滋乃滋')
    if ("妳媽瞟來的") in msg.content :
        
        await msg.delete()
        await msg.channel.send(f'{msg.author.mention}乃滋乃滋')
    if ("你媽嫖來的") in msg.content :
        
        await msg.delete()
        await msg.channel.send(f'{msg.author.mention}乃滋乃滋')
    if ("妳媽嫖來的") in msg.content :
        
        await msg.delete()
        await msg.channel.send(f'{msg.author.mention}乃滋乃滋')
    

    if ("富士") in msg.content :

        await msg.channel.send(f"{msg.author.mention}Nikon no.1")
    if ("Fujifilm no.1") in msg.content :

        await msg.channel.send(f"{msg.author.mention}Nikon no.1")
    if ("fujifilm no.1") in msg.content :

        await msg.channel.send(f"{msg.author.mention}Nikon no.1")
    if ("奶子") in msg.content :

        await msg.channel.send(f"{msg.author.mention}又怎麼拉美女")
    if ("乃子") in msg.content :

        await msg.channel.send(f"{msg.author.mention}又怎麼拉美女")

    #if msg.author.id == 589472406540648525:

   #     await msg.channel.send(f'{msg.author.mention}Nikon no.1')


  
    await bot.process_commands(msg)
        

bot.run(jdata["TOKEN"])  