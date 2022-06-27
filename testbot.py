from discord.ext import commands
import discord
from random import choice

import asyncio
token = 'token'
client = commands.Bot(command_prefix = '~', case_insensitive = True)

with open('facts.txt') as f:
    fact_list = f.read().split('\n')

'''
Actual Functionality of the bot

<---------------------------------------->

'''

@client.command()
async def fact(ctx):    
    fact = choice(fact_list)
    embed=discord.Embed(title="Fun Facts with FactBot!", url="http://www.youtube.com/watch?v=DLzxrzFCyOs", description=fact, color=0xFF5733)
    await ctx.send(embed=embed)

@client.command(aliases = ['sn1p3'])
async def snipe(ctx):
    embed=discord.Embed(title="Sniped!", url="http://www.youtube.com/watch?v=DLzxrzFCyOs", description=msg, color=0xFF5733)
    await ctx.send(embed = embed)
   

'''
Actual pictures of somewhat relevance
<--------------------------------------------------------------------------->
'''

@client.command(aliases = ['Toppers', 'ToppersTT', 'ToppersTimeTable'])
async def ttt(ctx):
    await ctx.channel.send(file=discord.File('images/new_tt.jpg'))

@client.command(aliases  = ['Exam', 'Schedule'])
async def mock(ctx):
    await ctx.channel.send(file = discord.File('images/toppersexamschedule.png'))

@client.command()
async def tt(ctx):
    await ctx.channel.send(file=discord.File('images/timetablenew.jpeg'))



'''
Pictures for fun :D

<---------------------------------------------------->
'''

@client.command(aliases = ['michael', 'tech'])
async def techsupport(ctx):
    files = ['ajay', 'abhinav', 'ishan', 'shaam']
    import random
    fch = random.choice(files)
    await ctx.channel.send(file=discord.File(f'images/{fch}techsupport.png'))
    white_names = ['Michael', 'Steve', 'Jim', 'Kevin', 'Connor']
    ch = random.choice(white_names)
    companies = ['Amazon', 'Microsoft', 'Facebook', 'Apple', 'Google']
    company = random.choice(companies)
    await ctx.channel.send(f"Hello, this is {ch} from {company}\nHow may I help you?")


@client.command(aliases = ['pal'])
async def weeb(ctx):
    await ctx.channel.send(file=discord.File('images/palpriyansh.png'))

@client.command(aliases = ['vigissatisfied', 'satisfied'])
async def satisfaction(ctx):
    await ctx.channel.send(file=discord.File('images/vignesh_is_satisfied.png'))

@client.command(aliases = ['vig', 'brugnesh', 'lignesh', 'viggie'])
async def vignesh(ctx):
    files = ['vigneshvenkatesh']*15 + ['vignesh']*15 + ['vigneshdonewithlife '] * 10 + ['vigneshmaari'] *3 + ['vigneshmaarimoustache']*3 + ['vigneshstare']*1 + ['vigneshswag']*25 + ['vigraja']*4
    import random
    fch = random.choice(files)
    await ctx.channel.send(file = discord.File(f'images/{fch}.png'))

@client.command(aliases = ['azzer', 'axxer','azar','azhar', 'uzzer'])
async def ashar(ctx):
    await ctx.channel.send(file=discord.File('images/azzer.jpg'))


@client.command(aliases = ['hiranmayi','oshin', 'hiran'])
async def sagar(ctx):
    files = ['annualdaysagar']*5 + ['sag3huh']*30 + ['cs'] * 40 + ['sagar'] *3 + ['sagar+garla']*1 + ['sagarazer']*5 + ['sagarquestioninggaze']*25 + ['sagarsmirk']*10 + ['sagartonguebite']*10
    import random
    fch = random.choice(files)
    await ctx.channel.send(file=discord.File(f'images/{fch}.png'))

@client.command(aliases = ['IncarnationOfNarcissism', 'narcissism', 'god'])
async def ajay(ctx):
    files = ['union']*10 + ['loss']*90 
    import random
    fch = random.choice(files)
    await ctx.channel.send(file=discord.File(f'images/{fch}.png'))

'''
Somewhat meaningful text messages for easy accessibility
<--------------------------------------------------------------------------------->
'''

@client.command(aliases = ['hi', 'hello'])
async def hey(ctx):
    await ctx.send('Are you really trying to talk to a bot?!')

@client.command(pass_context = True, aliases = ['jhoom', 'onlineclass', 'link'])
async def zoom(ctx):
    
    '''
    Gives the zoom link for online class
    '''

    msg = await ctx.channel.send('<https://globalschools.zoom.us/j/99904909013?pwd=OFkzTExyOVF6aTVkMVBzZWNiK0Q3dz09>')
    await asyncio.sleep(10)
    await msg.delete()

@client.command(pass_context = True, aliases = ['jhoom2', 'onlineclass2', 'link2', 'physics', '12B'])
async def zoom2(ctx):
    '''
    Gives the zoom link for online class for 12B
    '''

    msg = await ctx.channel.send('<https://globalschools.zoom.us/j/97813317687?pwd=TWNLSTMzbDByODJCOThTUjRxNk9pdz09>')
    await asyncio.sleep(10)
    await msg.delete()


@client.event
async def on_message_delete(message):
    global msg 
   
    msg2 = str(message.author)+ ' deleted message in '+str(message.channel)+': \n'+str(message.content)
    msg = str(message.author)+ ' deleted message : \n'+str(message.content)
    channel = client.get_channel(807641377419558943)
    await channel.send('```'+msg2+'```')
 


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('~help'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)

