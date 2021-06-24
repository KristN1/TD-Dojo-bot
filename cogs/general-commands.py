import datetime
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
            user = ctx.author

        elo = Database.find_elo(user.id)

        if elo != None:
            rolelist = [r.mention for r in user.roles if r != ctx.guild.default_role]
            roles = ", ".join(rolelist)

            bot_name = self.client.user.name
            bot_pfp = self.client.user.avatar_url

            embed=discord.Embed(title=f"User details", description=f"Details of {user.mention}", color=user.top_role.color)
            embed.set_thumbnail(url=user.avatar_url)

            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="Tag", value=f"{user.name}#{user.discriminator}", inline=True)
            embed.add_field(name="Effective name", value=user.nick, inline=True)

            embed.add_field(name="Avatar", value=user.avatar_url, inline=False)

            embed.add_field(name="Elo", value=elo, inline=False)

            embed.add_field(name="Joined at", value=user.joined_at, inline=False)
            embed.add_field(name="roles", value=roles, inline=False)

            embed.set_footer(text=bot_name, icon_url=bot_pfp)
            embed.timestamp = datetime.datetime.now()

            await ctx.send(embed=embed)

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