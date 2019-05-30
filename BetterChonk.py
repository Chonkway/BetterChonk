import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event #A list of automatic responses, like "easter eggs" of sorts, based on specific text being located in a message,
async def on_message(message):
    if message.author == client.user:
        return
    file = discord.File("/home/chonkway/Desktop/BetterChonk/luigi.jpg", filename="luigi.jpg")

    if 'luigi' in message.content:
        await message.channel.send("Did someone say luigi?", file=file)
    if 'Luigi' in message.content:
        await message.channel.send("Did someone say luigi?", file=file)

    if 'Jah' in message.content:
        await message.channel.send('Oh? On Jah?')
    if 'jah' in message.content:
        await message.channel.send('Oh? On Jah?')
    if '583009958380175362' in message.content:
        await message.channel.send("Ping me one more time and I'm going to open that asshole of yours so wide I'll be able to crawl inside")
    if '208645171145998336' in message.content:
        await message.channel.send("Don't ping Davis, he's getting his beauty rest.")

client.run('BOT_TOKEN')
