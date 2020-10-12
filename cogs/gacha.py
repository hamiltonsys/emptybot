from discord.ext import commands
import random

class GachaSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gacha(self, ctx, category, count=1):
        """ガチャができます
        alcohol, drink, food, konbini, misosoup, shop, sweets, tsumami
        数字でいくつか指定できます"""
        with open(f"/app/list/{category}.txt") as f:
            category_contents = [s.strip() for s in f.readlines()]
        if count == 0 or count > 10:
            return await ctx.send("ムチャ言うな")
        for i in range(count):
            await ctx.send(random.choice(category_contents))

    @gacha.error
    async def gacha_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("数字で言って！")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("なんのガチャ？")

def setup(bot):
    bot.add_cog(GachaSystem(bot))
