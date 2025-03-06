import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

msg_num = 0

@client.event
async def on_ready():
    print("Logged on as", client.user)

@client.event
async def on_message(message):
    global msg_num
    print("$", msg_num, " ", message.content, sep = "")
    msg_num += 1
    if message.author == client.user:
        return
    
    if message.content == ("ping"):
        await message.channel.send("pong")

client.run(os.getenv("TOKEN"))