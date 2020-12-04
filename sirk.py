import os

import asyncio

import discord

from discord.ext import commands, menus

import json

##CONFIG
tokenFile = "json/config.json"
with open(tokenFile) as f:
    data = json.load(f)
token = data['TOKEN']

prefixFile = "json/tools.json"
with open(prefixFile) as f:
    data = json.load(f)
prefixes = data['PREFIXES']

intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("^"), intents=intents, allowed_mentions=discord.AllowedMentions(users=True, roles=False, everyone=False))
# Might Wanna look at this: command_prefix=commands.when_mentioned_or(prefixes)

bot.owner_ids = {542405601255489537}
#bot.remove_command('help')

os.environ["JISHAKU_NO_UNDERSCORE"] = "True"

# also 
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
os.environ["JISHAKU_HIDE"] = "True"


@bot.event
async def on_ready():
    print('{0.user} is up and running'.format(bot))
    await bot.change_presence(status=discord.Status.idle)
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.content.endswith('<@!751447995270168586>'):
        embed = discord.Embed(title="Sirk Bot", description="Hey there :wave: Seems like you mentioned me.\n\nMy prefixes are: `@Sirk ` and `^`\nIf you would like to see my commands type `[prefix]help`", color=0x2F3136)
        await message.channel.send(embed=embed)
    if message.content.endswith('<@751447995270168586>'):
        embed = discord.Embed(title="Sirk Bot", description="Hey there :wave: Seems like you mentioned me.\n\nMy prefixes are: `@Sirk ` and `^`\nIf you would like to see my commands type `[prefix]help`", color=0x2F3136)
        await message.channel.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.load_extension("jishaku")

#16003
bot.run(token)
