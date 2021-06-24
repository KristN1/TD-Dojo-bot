import discord
import datetime
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed=discord.Embed(color=0x08ccfd)
        embed.add_field(name="Pong", value=f"Latency is `{round(self.client.latency * 1000)}`ms", inline=False)
        embed.set_footer(text=f"© {self.client.user.name}")
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ping(client))