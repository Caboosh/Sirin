import datetime
import discord
from botconfig import prefix
from botconfig import since
from discord.ext import commands


class Help:
    '''The Help Cog, Allows users to call help commands and get info on what the commands do.'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(invoke_without_command=True)
    async def help(self, ctx):
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(title="Here is a list of command you can run to make me do things!",
                              colour=discord.Colour(0x60c5b7))
        embed.set_author(name="CPU Green Heart", icon_url=self.bot.user.avatar_url)
        embed.add_field(name="General Commands: ", value="{}help general".format(prefix), inline=False)
        embed.add_field(name="Moderation Commands: ", value="{}help mod".format(prefix), inline=False)
        embed.add_field(name="Admin Commands: ", value="{}help admin".format(prefix), inline=False)
        embed.add_field(name="Cog Management Commands (Owner Only): ", value="{}help cogmgr", inline=False)
        embed.set_footer(
            text="Moderating the server since 1st Nov 2018! ({} days ago!)".format(days_since)
        )

