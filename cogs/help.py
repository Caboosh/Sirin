import datetime
import discord
from botconfig import prefix
from botconfig import since
from discord.ext import commands


class Help:
    '''The Help Cog, Allows users to call help commands and get info on what the commands do.'''

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(title="Here is a list of commands you can run to make me do things!",
                              colour=discord.Colour(0x60c5b7))
        embed.set_author(name="CPU Green Heart", icon_url=self.bot.user.avatar_url)
        embed.add_field(name="General Commands: ", value="{}help general".format(prefix), inline=False)
        embed.add_field(name="Moderation Commands: ", value="{}help mod".format(prefix), inline=False)
        embed.add_field(name="Admin Commands: ", value="{}help admin".format(prefix), inline=False)
        embed.add_field(name="Cog Management Commands (Owner Only): ", value="{}help cogmgr".format(prefix), inline=False)
        embed.set_footer(
            text="Moderating the server since 1st Nov 2018! ({} days ago!)".format(days_since),
            icon_url=self.bot.user.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I cant Embed links, can i have the permission?")

    @help.command()
    async def general(self, ctx):
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(title="Here is a list of commands you can run to make me do things!",
                              colour=discord.Colour(0x60c5b7))

        embed.set_author(name="CPU Green Heart", icon_url=self.bot.user.avatar_url)
        embed.add_field(name="{}profile".format(prefix), value="Shows you your Discord Info.", inline=False)
        embed.add_field(name="{}info".format(prefix), value="Shows you Info about me.", inline=False)
        embed.add_field(name="{}ping".format(prefix), value="Pings me to show my latency, in 0.x s", inline=False)
        embed.add_field(name="{}vitainfo".format(prefix), value="Embed with some essential homebrews for the Vita.", inline=False)
        embed.add_field(name="{}echo <word|string>".format(prefix), value="Echo's a word or string and makes me say it!", inline=False)
        embed.set_footer(
            text="Moderating the server since 1st Nov 2018! ({} days ago!)".format(days_since),
            icon_url=self.bot.user.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I cant Embed links, can i have the permission?")


def setup(bot):
    bot.add_cog(Help(bot))


