import discord
from discord.ext import commands

TOKEN = '***'
client = commands.Bot(command_prefix = '.')
client.remove_command('help')
extensions = ['music', 'general']

@client.event 
async def on_ready():
    #Game Status
    await client.change_presence(game=discord.Game(name='hackerman'))
    print('Mr Robot is ready!')

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} can not be loaded. [{}]'.format(extension, error))

#EVENTS

#*** New Member Role Assignment ***
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='buds')
    await client.add_roles(member, role)

#*** Monitors who joins a channel or leaves it ***
@client.event
async def on_voice_state_update(before, after):
    await client.send_message(client.get_channel('315316561273683978'),  'Someone has joined or left voice chat!', tts = True) 


client.run(TOKEN)
