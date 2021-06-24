from itertools import count
from operator import itemgetter
import discord
from db_actions import Database
from discord.ext import commands

class GeneralCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def register(self, ctx, ign):
        Database.add_elo_user(ctx.author.id, ign)
        await ctx.send(f"You have been registered with ign **{ign}**")

    @commands.command()
    async def profile(self, ctx, user : discord.Member = None):
        if user == None:
            user_id = ctx.author.id
            elo = Database.find_elo(ctx.author.id)
        else:
            user_id = (user.id)
            elo = Database.find_elo(user.id)

        if elo != None:
            await ctx.send(f"ELO of <@{user_id}> is `{elo}`")
        else:
            await ctx.send(f"{ctx.author.mention} is not registered, they can register with `.register`")
    

    @commands.command(aliases=['glb'])
    async def globalleaderboard(self, ctx):
        leaderboard = Database.get_global_leaderboard()

        counter = 1
        leaderboard_users = ""

        for user in leaderboard:
            print(user)
            leaderboard_users = f"{leaderboard_users}\n<@{user[0]}> - `{user[2]}`"
            if counter == 20:
                break
            
            counter += 1

        print(leaderboard_users)
        embed=discord.Embed(title="Global Leaderboard", description=f"Here you can see 20 people with the highest ELO ranking\n{leaderboard_users}", color=0xff9705)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(GeneralCommands(client))