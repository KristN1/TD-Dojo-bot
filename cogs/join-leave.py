import discord
from db_actions import Database
from discord.ext import commands

class JoinLeave(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        Database.remove_elo_user(member.id)

def setup(client):
    client.add_cog(JoinLeave(client))