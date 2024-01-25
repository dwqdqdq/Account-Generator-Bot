# Commands will be like /generate-disneyplus, free 100% working and netflix for premium users & extreme
# Add It So It Deletes the Line After the Generation
# Made by Star Alts | Revamped Code of HellGen 
# DisneyPlus Command Will have a 2 hour cooldown for free users, 15 minutes for premium and 10 minutes for extreme soon
# Join Our Discord Server for 100% Working Alts

import nextcord, os, random, datetime, asyncio
from nextcord.ext import commands

generator_channel = 5374638235
role_premium_id = 1234567890
role_extreme_id = 9876543210 

disneyplus_cooldowns = {}
netflix_cooldowns = {}

intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents, help_command=None)

server_name = "Star Alts"
server_logo = "https://staralts.xyz"
bot_status = ".gg/staralts"

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing,name=bot_status))
    print("Running")

# Disney Plus Command

@bot.slash_command(name="generate-disneyplus", description="Generate a 100% working Disney Plus account!")
async def gen_disneyplus(inter):
user = inter.user
user_id = inter.user.id
if role_premium_id in [role.id for role in user.roles]:
    cooldown = 600
elif role_extreme_id in [role.id for role in user.roles]:
    cooldown = 300 
else:
    cooldown = 3600

if user_id in disneyplus_cooldowns:
    remaining_cooldown = disneyplus_cooldowns[user_id]
    embed = nextcord.Embed(title="Cooldown", description=f"You still have {remaining_cooldown} seconds remaining.",
                           color=nextcord.Color.red())
    await inter.send(embed=embed, ephemeral=True)
    return

if inter.channel.id != generator_channel:
    embed = nextcord.Embed(title=f"Wrong Channel! Use <#{generator_channel}>", color=nextcord.Color.red())
    await inter.send(embed=embed, ephemeral=True)
    return

stock = "disneyplus.txt"
if stock not in os.listdir("stock//"):
    embed = nextcord.Embed(title="The Disney Plus stock does not exist.", color=nextcord.Color.red())
    await inter.send(embed=embed, ephemeral=True)
    return

with open(f"stock//{stock}") as file:
    lines = file.read().splitlines()
    if len(lines) == 0:
        embed = nextcord.Embed(title="Out of stock!", description="This service is currently out of stock. Please wait.", color=nextcord.Color.red())
        await inter.send(embed=embed, ephemeral=True)
        return

account = random.choice(lines)
combo = account.split(':')
User = combo[0]
Pass = combo[1]
Password = Pass.rstrip()

embed = nextcord.Embed(title="Generated Disney Plus Account", color=nextcord.Color.yellow())
embed.add_field(name="Username:", value=f"```{str(User)}```")
embed.add_field(name="Password:", value=f"```{str(Password)}```")
embed.add_field(name="Combo:", value=f"```{str(User)}:{str(Password)}```", inline=False) 
await user.send(embed=embed)

embed1 = nextcord.Embed(title="✅ Disney Plus Account Generated!", description="> Your 100% working account has been sent to your DMs.", color=nextcord.Color.green())
await inter.send(embed=embed1) 
lines.remove(account)
with open(f"stock//{stock}", "w", encoding='utf-8') as file:
    file.write("\n".join(lines))

disneyplus_cooldowns[user_id] = cooldown
await asyncio.sleep(1)
while disneyplus_cooldowns[user_id] > 0:
    disneyplus_cooldowns[user_id] -= 1
    await asyncio.sleep(1)

del disneyplus_cooldowns[user_id]

# Netflix Command

@bot.slash_command(name="generate-netflix", description="Generate a 100% working Netflix account!")
async def gen_netflix(inter):
user = inter.user
user_id = inter.user.id
if role_premium_id not in [role.id for role in user.roles] and role_extreme_id not in [role.id for role in user.roles]:
    embed = nextcord.Embed(title="Purchase to Access this Command", description="You need <@&{role_extreme_id}> or <@&{role_premium_id}> to use this command.", color=nextcord.Color.red())
    await inter.send(embed=embed, ephemeral=True)
    return

if user_id in netflix_cooldowns:
    remaining_cooldown = netflix_cooldowns[user_id]
    embed = nextcord.Embed(title="Cooldown", description=f"You still have {remaining_cooldown} seconds remaining.",
                           color=nextcord.Color.red())
    await inter.send(embed=embed, ephemeral=True)
    return

if inter.channel.id != generator_channel:
    embed = nextcord.Embed(title=f"Wrong Channel! Use <#{generator_channel}>", color=nextcord.Color.red())
    await inter.send(embed=embed, ephemeral=True)
    return

stock = "netflix.txt"
if stock not in os.listdir("stock//"):
    embed = nextcord.Embed(title="The Netflix stock does not exist.", color=nextcord.Color.red())
    await inter.send(embed=embed, ephemeral=True)
    return

with open(f"stock//{stock}") as file:
    lines = file.read().splitlines()
    if len(lines) == 0:
        embed = nextcord.Embed(title="Out of stock!", description="This service is currently out of stock. Please wait.", color=nextcord.Color.red())
        await inter.send(embed=embed, ephemeral=True)
        return

account = random.choice(lines)
combo = account.split(':')
User = combo[0]
Pass = combo[1]
Password = Pass.rstrip()

embed1 = nextcord.Embed(title="✅ Netflix Account Generated!", description="> These accounts are 99% working as they are all checked before adding it to the generator. If they do not work, open a ticket.", color=nextcord.Color.green())
embed.add_field(name="Username:", value=f"```{str(User)}```")
embed.add_field(name="Password:", value=f"```{str(Password)}```")
embed.add_field(name="Combo:", value=f"```{str(User)}:{str(Password)}```", inline=False) 
await user.send(embed=embed)

embed1 = nextcord.Embed(title="✅ Netflix Account Generated!", description="> Your 100% working account has been sent to your DMs.", color=nextcord.Color.green())
await inter.send(embed=embed1) 
lines.remove(account)
with open(f"stock//{stock}", "w", encoding='utf-8') as file:
    file.write("\n".join(lines))

if role_extreme_id in [role.id for role in user.roles]:
    netflix_cooldowns[user_id] = 300  
elif role_premium_id in [role.id for role in user.roles]:
    netflix_cooldowns[user_id] = 600  

await asyncio.sleep(1)
while netflix_cooldowns[user_id] > 0:
    netflix_cooldowns[user_id] -= 1
    await asyncio.sleep(1)

del netflix_cooldowns[user_id]

# Input Your Bot Token Here 
# Running On Replit Is Not Recommended As You May Get Raided or Nuked

bot.run("Your Token Here")
