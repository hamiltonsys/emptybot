from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_ready():
    print('on_ready')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    #bot相手なら無視
    if message.author == bot.user:
        return
    if message.content == 'ローソン':
        await message.channel.send('行け')
    if message.content == 'からあげクン':
        await message.channel.send('食え')
    poops = ['うんこ', 'うんち' , 'ウンコ' , 'ウンチ', '糞']
    for poop in poops:
        if poop in message.content:
            await message.add_reaction('💩')
            
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await after.edit(nick = 'はみるとん')
async def on_guild_remove(member):
    await message.channel.send(f"{message.author.name}さんが消えていきました")
    


@bot.command()
async def ping(ctx):
    await ctx.send('静かにしろ')
async def alchol(ctx):
    with open("list/alchol.txt") as f:
        alchol_list = [s.strip() for s in f.readlines()]
    await ctx.send(random.choice(alchol_list))
        
bot.run(token)
