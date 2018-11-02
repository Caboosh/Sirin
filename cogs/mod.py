import datetime
import asyncio
import aiohttp
import discord
from discord.ext import commands
import botconfig

class  mod ():
    """Practical commands for administrators and moderators"""

    def  __init__ ( self , bot ):
        self .bot = bot

    @ commands.command(aliases = [ ' prune ' ], hidden=True)
    @ commands.has_permissions(ban_members=True)
    @ commands.bot_has_permissions(manage_messages=True)
    async  def  purge ( self , ctx , * limit ):
        """Delete multiple messages at once (MOD ONLY)
        Example:
        -----------
        : purge 100
        """
        try :
            limit =  int (limit [ 0 ])
        except  IndexError :
            limit =  1
        deleted =  0
        while limit >=  1 :
            cap =  min (limit, 100 )
            deleted +=  len (await ctx.channel.purge ( limit = cap, before = ctx.message))
            limit -= cap
        tmp =  await ctx.send (' **: put_litter_in_its_place: ** { deleted } messages deleted ' )
        await asyncio.sleep ( 15 )
        await tmp.delete ()
        await ctx.message.delete ()

    @ commands.command ( hidden = True )
    @ commands.has_permissions ( kick_members  =  True )
    @ commands.bot_has_permissions ( kick_members  =  True )
    async  def  kick ( self , ctx , member : discord.Member =  None , * reason ):
        """ Kicks a member with a reason (MOD ONLY)
        Example:
        -----------
        : kick @ Der-Eddy # 6508
        """
        if member is  not  None :
            if reason:
                reason =  '  ' .join (reason)
            else :
                reason =  None
            await member.kick ( reason = reason)
        else :
            await ctx.send ( ' **: no_entry: ** No user specified! ' )

    @ commands.command ( hidden = True )
    @ commands.has_permissions ( ban_members  =  True )
    @ commands.bot_has_permissions ( ban_members  =  True )
    async  def  ban ( self , ctx , member : discord.Member = None , * reason ):
        """ Bans a member with a reason (MOD ONLY)
        Example:
        -----------
        : ban @ Der-Eddy # 6508
        """
        if member is  not  None :
            if reason:
                reason =  '  ' .join (reason)
            else :
                reason =  None
            await member.ban ( reason = reason)
        else :
            await ctx.send ( ' **: no_entry: ** No user specified! ' )

    @ commands.command ( hidden = True )
    @ commands.has_permissions ( ban_members  =  True )
    @ commands.bot_has_permissions ( ban_members  =  True )
    async  def  unban ( self , ctx , user : int = None , * reason ):
        """ Explodes a member with a reason (MOD ONLY)
        The user ID must be specified, name + discriminator is not enough
        Example:
        -----------
        : unban 102815825781596160
        """
        user = discord.User ( id = user)
        if user is  not  None :
            if reason:
                reason =  '  ' .join (reason)
            else :
                reason =  None
            await ctx.guild.unban (user, reason = reason)
        else :
            await ctx.send ( ' **: no_entry: ** No user specified! ' )

    @ commands.command ( hidden = True )
    @ commands.has_permissions ( kick_members  =  True )
    @ commands.bot_has_permissions ( ban_members  =  True )
    async  def  bans ( self , ctx ):
        """ Lists currently banned users (MOD ONLY) """
        users =  await ctx.guild.bans ()
        if  len (users) >  0 :
            msg =  f ' ` { " ID " : 21 } { " name " : 25 } reason \ n '
            for entry in users:
                userID = entry.user.id
                userName =  str (entry.user)
                if entry.user.bot:
                    username =  ' 🤖 '  + userName # : robot: emoji
                reason =  str (entry.reason) # Could be None
                msg + =  f ' { userID : <21 } { userName : 25 } { reason } \ n '
            embed = discord.Embed ( color = 0x e74c3c ) # Red
            embed.set_thumbnail ( url = ctx.guild.icon_url)
            embed.set_footer ( text = f ' server: { ctx.guild.name } ' )
            embed.add_field ( name = ' Ranks ' , value = msg +  ' ` ' , inline = True )
            await ctx.send ( embed = embed)
        else :
            await ctx.send ( ' **: negative_squared_cross_mark: ** There are no banned users! ' )

    @ commands.command ( alias = [ ' clearreactions ' ], hidden = True )
    @ commands.has_permissions ( manage_messages  =  True )
    @ commands.bot_has_permissions ( manage_messages  =  True )
    async  def  removereactions ( self , ctx , messageid : str ):
        """ Removes all emoji reactions from a message (MOD ONLY)
        Example:
        -----------
        : removereactions 247386709505867776
        """
        message =  await ctx.channel.get_message (messageid)
        if message:
            await message.clear_reactions ()
        else :
            await ctx.send ( ' **: x: ** Could not find a message with this ID! ' )

    @ commands.command ( hidden = True )
    async  def  permissions ( self , ctx ):
        """ Lists all rights of the bot """
        permissions = ctx.channel.permissions_for (ctx.me)

        embed = discord.Embed ( title = ' : customs: Permissions ' , color = 0x 3498db ) # Blue
        embed.add_field ( name = ' server ' , value = ctx.guild)
        embed.add_field ( name = ' Channel ' , value = ctx.channel, inline = False )

        for item, valueBool in permissions:
            if valueBool ==  True :
                value =  ' : white_check_mark: '
            else :
                value =  ' : x: '
            embed.add_field ( name = item, value = value)

        embed.timestamp = datetime.datetime.utcnow ()
        await ctx.send ( embed = embed)

    @ commands.command ( hidden = True )
    async  def  hierarchy ( self , ctx ):
        """ Lists the role hierarchy of the current server to """
        msg =  f ' server role hierarchy ** { ctx.guild } **: \ n \ n '
        roleDict = {}

        for role in ctx.guild.roles:
            if role.is_default ():
                roleDict [role.position] =  ' everyone '
            else :
                roleDict [role.position] = role.name

        for role in  sorted (roleDict.items (), reverse = True ):
            msg + = role [ 1 ] +  ' \ n '
        await ctx.send (msg)

    @ commands.command ( hidden = True , alies = [ ' setrole ' , ' sr ' ])
    @ commands.has_permissions ( manage_roles  =  True )
    @ commands.bot_has_permissions ( manage_roles  =  True )
    async  def  setrank ( self , ctx , member : discord.Member = None , * rankName : str ):
        """ Gives a rank to a user
        Example:
        -----------
        : setrole @ Der-Eddy # 6508 Member
        """
        rank = discord.utils.get (ctx.guild.roles, name = '  ' .join (rankName))
        if member is  not  None :
            await member.add_roles (rank)
            await ctx.send ( f ' : white_check_mark: Role ** { rank.name } ** has been distributed to ** { member.name } ** ' )
        else :
            await ctx.send ( ' : no_entry: You must specify a user! ' )

    @ commands.command ( pass_context = True , hidden = True , alies = [ ' rmrole ' , ' removerole ' , ' removerank ' ])
    @ commands.has_permissions ( manage_roles  =  True )
    @ commands.bot_has_permissions ( manage_roles  =  True )
    async  def  rmrank ( self , ctx , member : discord.Member = None , * rankName : str ):
        """ Removes a rank from a user
        Example:
        -----------
        : rmrole @ Der-Eddy # 6508 Member
        """
        rank = discord.utils.get (ctx.guild.roles, name = '  ' .join (rankName))
        if member is  not  None :
            await member.remove_roles (rank)
            await ctx.send ( f ' : white_check_mark: Role ** { rank.name } ** has been removed from ** { member.name } ** ' )
        else :
            await ctx.send ( ' : no_entry: You must specify a user! ' )


def  setup ( bot ):
    bot.add_cog (mod (bot))