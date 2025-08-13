import discord
from discord.ext import commands
import os
from dotenv import load_dotenv



TOKEN = os.getenv("TOKEN")    
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def on_message(message):
  if message.author == bot.user:
        return


  if message.content == "السلام عليكم" :
    await   message.channel.send(f"{message.author.mention}و عليكم السلام و رحمة الله تعالى و بركاته")
  if message.content == "." :
    await   message.channel.send("استغفر الله و اتوب اليه استغفر الله العظيم")
  if message.content == "رابط" :
    await message.channel.send("https://discord.gg/Kjq7DuTBjX")
  if message.content == "تقديم" :
      await message.channel.send("استمارت التقديم :\nالاسم: \nالبلد : \nالعمر: \nمدة التفاعل: \nبماذا ستفيد الادارة: ")
  if message.content == "خط" :
    await message.channel.send("https://i.imgur.com/NL0J4iu")
  if message.content =="شعار" :
    await message.channel.send("https://i.imgur.com/IH3delE.png")  
  if message.content =="باك"  :
    await message.channel.send(f"{message.author.mention}و لكم باك يا لي نورنا زي القمر يا غالي يا انت")
  if message.content =="برب" :
    await message.channel.send(f"{message.author.mention}ربي يسهل ليك")
  if message.content =="استلام" :
    await message.channel.send(f"{message.author.mention}تم استلام تكت من قبل هذا الاداري")
  if message.content =="hi" :
    await message.channel.send("https://images-ext-1.discordapp.net/external/SbAxlTSf9QkQBLf8MEjWyOr7EA2wUQv4jyCYnFmepNY/https/media.tenor.com/b7lPcGXxKpsAAAPo/shut-up-stfu.mp4")
  if message.content =="m" :
    await message.channel.send("@everyone@here ")

  await bot.process_commands(message)


bot.run(TOKEN)
