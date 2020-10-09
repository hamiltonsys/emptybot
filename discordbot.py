from discord.ext import commands
import os
import traceback
import random

# Embed形式
import discord

bot = commands.Bot(command_prefix='$', help_command=HelpCommand())
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
    # bot相手なら無視
    if message.author == bot.user:
        return
    if message.content == 'ローソン':
        await message.channel.send('行け')
    if message.content == 'からあげクン':
        await message.channel.send('食え')
    poops = ['うんこ', 'うんち', 'ウンコ', 'ウンチ', '糞']
    for poop in poops:
        if poop in message.content:
            await message.add_reaction('💩')

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await member.edit(nick='はみるとん')

@bot.event
async def on_guild_remove(member):
    text_channel = member.guild.text_channels[0]
    await text_channel.send(f"{member.name}さんが消えていきました")

@bot.command()
async def ping(ctx):
    await ctx.send('静かにしろ')

@bot.command()
async def alchol(ctx):
    with open("list/alchol.txt") as f:
        alchol_list = [s.strip() for s in f.readlines()]
    await ctx.send(random.choice(alchol_list))

@bot.command()
async def drink(ctx):
    with open("list/drink.txt") as f:
        drink_list = [s.strip() for s in f.readlines()]
    await ctx.send(random.choice(drink_list))

@bot.command()
async def food(ctx):
    with open("list/food.txt") as f:
        food_list = [s.strip() for s in f.readlines()]
    await ctx.send(random.choice(food_list))

@bot.command()
async def konbini(ctx):
    with open("list/konbini.txt") as f:
        konbini_list = [s.strip() for s in f.readlines()]
    await ctx.send(random.choice(konbini_list))

@bot.command()
async def misosoup(ctx):
    with open("list/misosoup.txt") as f:
        misosoup_list = [s.strip() for s in f.readlines()]
    await ctx.send(random.choice(misosoup_list))

@bot.command()
async def shop(ctx):
    with open("list/shop.txt") as f:
        shop_list = [s.strip() for s in f.readlines()]
    await ctx.send(random.choice(shop_list))

@bot.command()
async def tumami(ctx):
    with open("list/tumami.txt") as f:
        tumami_list = [s.strip() for s in f.readlines()]
    await ctx.send(random.choice(tumami_list))

# また今度やる
class HelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super()__init__()
        self.commands_heading = "ガチャ"
        self.command_attrs["alchol"] = "酒ガチャ"
        self.command_attrs["drink"] = "飲み物ガチャ"
        self.command_attrs["food"] = "ごはんガチャ"
        self.command_attrs["konbini"] = "コンビニガチャ "
        self.command_attrs["misosoup"] = "味噌汁の具ガチャ"
        self.command_attrs["shop"] = "ごはんやさんガチャ"
        self.command_attrs["tumami"] = "つまみガチャ"

bot.run(token)
