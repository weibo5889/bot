import discord
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix = "!!")

@client.command()
async def play(ctx, url : str):

    song_three = os.path.isfile("song.mp3")

    try:
        if song_three:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("song is playing")

    
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = "一般")
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
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

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    if voice:
        await voice.disconnect()
        await ctx.send("機器人 離線.....")
    else:
        await ctx.send("The bot is not connected")


if __name__ == "__main__":
    client.run("OTY3NDkzNTM3OTgzNzg3MDE4.YmRGkg.T1IFC4r0JanAihH2kxdef1Z2wC4")
