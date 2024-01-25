# Commands will be like /generate-disneyplus, free 100% working and netflix for premium users & extreme
# Add It So It Deletes the Line After the Generation

import nextcord, os, random, datetime, asyncio
from nextcord.ext import commands

generator_channel = 5374638235 # Channel ID here

disneyplus_cooldowns = {}

intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents, help_command=None)

server_name = "ENTER YOUR SERVER NAME HERE"
server_logo = "ENTER YOUR SERVER'S LOGO LINK HERE"
server_status = ".gg/staralts"

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing,name=server_status))
    print("Running")

# Disney Plus Command

@bot.slash_command(name="generate-disneyplus", description="Generate a 100% working Disney Plus account!")
async def gen_disneyplus(inter):
user = inter.user
user_id = inter.user.id
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

disneyplus_cooldowns[user_id] = 30
await asyncio.sleep(1)
while disneyplus_cooldowns[user_id] > 0:
    disneyplus_cooldowns[user_id] -= 1
    await asyncio.sleep(1)

del disneyplus_cooldowns[user_id]

@bot.slash_command(name="stock", description="View free stock!")
async def freestock(inter: nextcord.Interaction):   
    embed = nextcord.Embed(title="Account Stock", color=nextcord.Color.green(), timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=server_name, icon_url=server_logo)
    embed.set_thumbnail(url=server_logo)
    embed.description = ""
    for filename in os.listdir("freestock/"):
        with open(f"freestock/{filename}") as f: 
            amount = len(f.read().splitlines())
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") 
            embed.description += f"* **{name}**: `{amount}`\n"
    await inter.send(embed=embed, ephemeral=True)

bot.run("Your Token Here")
