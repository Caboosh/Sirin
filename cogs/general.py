import datetime
import discord
from cogs.vitainfo.vitainfo import vitainfopg1
from cogs.vitainfo.vitainfo import vitainfopg2
from botconfig import prefix
from botconfig import since
from discord.ext import commands


class General:
    """General Commands, anyone can use these."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, *, user: discord.User = None):
        """Shows a User's Profile in a nice Embed"""
        author = ctx.author

        if not user:
            user = author

        days_since = (datetime.datetime.utcnow() - since).days
        joined_at = user.joined_at
        since_created = (ctx.message.created_at - user.created_at).days
        since_joined = (ctx.message.created_at - joined_at).days
        user_joined = joined_at.strftime("%d %b %Y %H:%M")
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        voice_state = user.voice

        created_on = "{}\n({} days ago)".format(user_created, since_created)
        joined_on = "{}\n({} days ago)".format(user_joined, since_joined)

        embed = discord.Embed(description="All your User Info in a handy Embed!", colour=discord.Colour(0xb675c7))

        embed.add_field(name="User ID", value=user.id, inline=False)
        embed.add_field(name="Joined Discord on", value=created_on, inline=True)
        embed.add_field(name="Joined this server on", value=joined_on, inline=True)
        if voice_state and voice_state.channel:
            embed.add_field(
                name="Current voice channel",
                value="{0.name} (ID {0.id})".format(voice_state.channel),
                inline=False,
            )
        else:
            embed.add_field(
                name="Current Voice Channel",
                value="None."
            )

        embed.set_footer(
            text="Moderating the server since 1st Nov 2018! ({} days ago!)".format(days_since),
            icon_url=self.bot.user.avatar_url)

        name = str(user)
        name = " ~ ".join((name, user.nick)) if user.nick else name

        if user.avatar:
            avatar = user.avatar_url
            avatar = avatar.replace("webp", "png")
            embed.set_author(name=name, icon_url=avatar)
            embed.set_thumbnail(url=avatar)
        else:
            embed.set_author(name=name)

        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I cant Embed links, can i have the permission?")

    @commands.group(invoke_without_command=True)
    async def echo(self, ctx):
        """Echos an input from the user."""
        await ctx.send("""```python
Usage: {}echo 'Subcommand' 'Word/String/Int to Echo'```""".format(prefix))

    @echo.command()
    async def word(self, ctx, arg):
        await ctx.send(arg)

    @echo.command()
    async def string(self, ctx, *, string: str):
        await ctx.send(string)

    @commands.group(invoke_without_command=True)
    async def vitainfo(self, ctx):
        """Displays some handy info about the Vita homebrew and hacks available."""
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(
            colour=discord.Colour(0xb675c7),
            description=vitainfopg1 )
        embed.add_field(name="PAGE 2", value="{}vitainfo pg2".format(prefix))
        embed.set_author(name="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        embed.set_footer(
            text="Moderating the server since 1st Nov 2018! ({} days ago!)".format(days_since),
            icon_url=self.bot.user.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I cant Embed links, can i have the permission?")

    @vitainfo.command()
    async def pg2(self, ctx):
        """Page 2 of the vita info"""
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(
            colour=discord.Colour(0xb675c7),
            description=vitainfopg2)
        embed.add_field(name="PAGE 1", value="{}vitainfo".format(prefix))
        embed.add_field(name="PAGE 3", value="{}vitainfo pg3".format(prefix))
        embed.set_author(name="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        embed.set_footer(
            text="Moderating the server since 1st Nov 2018! ({} days ago!)".format(days_since),
            icon_url=self.bot.user.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I cant Embed links, can i have the permission?")

def setup(bot):
    bot.add_cog(General(bot))
