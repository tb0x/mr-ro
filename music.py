import discord
import youtube_dl
import asyncio
from discord.ext import commands

players = {}
queues = {}


class Music:
    def __init__(self, client):
        self.client = client

    def check_queue(self, id):
        if queues[id] != []:
            player = queues[id].pop(0)
            players[id] = player
            player.start()


#***Join Command***
    @commands.command(pass_context = True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)

#***Leave Command***
    @commands.command(pass_context = True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        await voice_client.disconnect()

#***Play Command***
    @commands.command(pass_context = True)
    async def play(self, ctx, url):
        server = ctx.message.server 
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after= lambda: self.check_queue(server.id))
        players[server.id] = player
        player.start()

#***Pause Command***
    @commands.command(pass_context = True)
    async def pause(self, ctx):
        id = ctx.message.server.id
        players[id].pause()

#***Stop Command***
    @commands.command(pass_context = True)
    async def skip(self, ctx):
        id = ctx.message.server.id
        players[id].stop()
        await self.client.say('ur song just got skipped bitch.')
#***Resume Command***
    @commands.command(pass_context = True)
    async def resume(self, ctx):
        id = ctx.message.server.id
        players[id].resume()

#***Queue Command***
    @commands.command(pass_context = True)
    async def queue(self, ctx, url):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after = lambda: self.check_queue(server.id))
    
        if server.id in queues:
            queues[server.id].append(player)
        else:
            queues[server.id] = [player]
        await self.client.say('Video queued brother.')


def setup(client):
    client.add_cog(Music(client))