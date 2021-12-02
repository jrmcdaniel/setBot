import discord
import os
from io import BytesIO

from project_helper import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    
    if message.content.lower().startswith('?set'):
      print('Channel: %s' %message.channel.id)

      #bot to send collage to channel
      image=project_sorter(message.channel.id,message.content.lower())
      with BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.channel.send(file=discord.File(fp=image_binary,filename='image.png'))



client.run(os.getenv('BotID'))