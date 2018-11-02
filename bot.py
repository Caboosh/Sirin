import logging
import sys
import traceback
import discord
from discord.ext import commands
from botconfig import token
from botconfig import prefix
from botconfig import botdesc
from botconfig import owner


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix=prefix, description=botdesc, dm_help=False, owner_id=owner)
bot.remove_command("help")

initial_extensions = [
    'cogs.admin',
    'cogs.help',
    'cogs.cogmgr',
    'cogs.general'

]

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

# Set On Ready Status, Print Details into Console and Set Presence to allow Visual that Bot is Running.
@bot.event
async def on_ready():
    print('=======================')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('=======================')
    print('Bot Owner: {}' .format(bot.owner_id))
    await bot.change_presence(game=discord.Game(name='Moderating The Discord', type=0))


bot.run(token, bot=True, reconnect=True)
