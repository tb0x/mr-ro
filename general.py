import discord
from discord.ext import commands

class General:
    def __init__(self, client):
        self.client = client


#Help Command
    @commands.command(pass_context=True)
    async def help(self,ctx):
        author = ctx.message.author
        embed = discord.Embed(
            color = discord.Color.dark_blue()
        )
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/a/a4/Cute-Ball-Help-icon.png')
        embed.set_author(name='Mr. Robot\'s Command List')
        embed.add_field(name = '.clear', value='Clears old messages in the channel', inline = False)
        embed.add_field(name = '.echo', value='Returns the previous message.', inline = False)
        embed.add_field(name = '.help', value='Helps show the user the commands available for this bot.', inline = False)
        embed.add_field(name = '.idot', value='Calls idot!', inline = False)
        embed.add_field(name = '.join', value='Joins Voice Channel!', inline = False)
        embed.add_field(name = '.leave', value='Leaves Voice Channel!', inline = False)
        embed.add_field(name = '.play', value='Plays song!', inline = False)
        embed.add_field(name = '.pause', value='Pauses song!', inline = False)
        embed.add_field(name = '.stop', value='Stops song!', inline = False)
        embed.add_field(name = '.resume', value='Resumes song!', inline = False)
        embed.add_field(name = '.tts', value = 'Text-to-speech', inline = False)

        await self.client.send_message(author, embed = embed)
        await self.client.say("{}, Check your Direct Messages!".format(ctx.message.author.mention))


#Idot Command
    @commands.command()
    async def idot(self):
        await self.client.say('Ur an idot bud!')


#DDOS Command
    @commands.command()
    async def ddos(self):
        await self.client.say('Say goodbye to ur network')


#Echo Command
    @commands.command()
    async def echo(self, *args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await self.client.say(output)


#Clear Command
    @commands.command(pass_context=True)
    async def clear(self, ctx, amount=100):
        channel = ctx.message.channel 
        messages = []
        async for message in self.client.logs_from(channel, limit=int(amount)):
            messages.append(message)
        await self.client.delete_messages(messages)
        #await client.say('Messages deleted.')


#Text to speech Command
    @commands.command(pass_context = True)
    async def tts(self, ctx):
        messages = ctx.message.content
        await self.client.say(messages[4:], tts = True)

'''
@client.command(pass_context = True)
async def keeble(ctx, member: discord.Member, channel: discord.Channel):

    await client.move_member(member, channel)

'''


def setup(client):
    client.add_cog(General(client))