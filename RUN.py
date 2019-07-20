# Import so that the bot could function
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import Config

#Determine the bots prefix
bot = commands.Bot(command_prefix = Config.PREFIX)

@bot.event
async def on_ready():
    print("===================================")
    print("Logged in as: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print('Server count:', str(len(bot.servers)))
    print('User Count:',len(set(bot.get_all_members())))
    print("===================================")

@bot.command(pass_context=True)
async def ping(ctx):
    """Check The Bots Response Time"""
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    thedata = (":ping_pong: **Pong.**\nTime: " + str(round((t2 - t1) * 1000)) + "ms")
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    data = discord.Embed(description = thedata, colour=discord.Colour(value = color))
    data.set_footer(text="{} | Requested by: {}".format(Config.BOTNAME, ctx.message.author))
    await bot.say(embed = data)

bot.run(Config.TOKEN)

