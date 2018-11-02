from typing import Optional
import discord
from discord.ext import commands

class ModLog():

    def __init__(self, bot):
        self.bot = bot


    @commands.group
    @commands.has_permissions(manage_guild=True)
    async def modlogset(self, ctx):
        """Manage my Modlog Settings."""
        pass

    @modlogset.command()
    @commands.guild_only()
    async def modlog(self, ctx, channel: discord.TextChannel = None):
        """Set a Channel for me to log Mod Actions.

        Omit <channel> To Turn Of Mod Logging.
        """
        guild = ctx.guild
        if channel:
            if channel.permissions_for(guild.me).send_messages:
                await modlog.set_modlog_channel(guild, channel)
                await ctx.send("Mod Events weill be sent to {channel}".format(channel=channel.mention))