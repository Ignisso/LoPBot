import discord
import asyncio
import urllib.request
from datetime import datetime

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)

players = {
    "Ignisso": "<@427135054888697869>",
    "cosmo sin": "<@437319671591600140>",
    "C.Blossom": "<@428968935430553612>",
    "Beastmode": "<@490964640046514188>",
}
async def inGame():
    while True:
        lop = client.get_guild(459472853360967680)
        in_game = lop.get_role(782975800135778334)
        for member in lop.members:
            if member.activities != ():
                #print(member.activities[0].name)
                if member.activities[0].name == "League of Pixels":
                    if in_game not in member.roles:
                        await member.add_roles(in_game)
                        print("+" + member.name)
                elif in_game in member.roles:
                    await member.remove_roles(in_game)
                    print("-" + member.name)
            elif in_game in member.roles:
                    await member.remove_roles(in_game)
                    print("-" + member.name)
        await client.change_presence(activity=discord.Game(name="Discord Users: " + str(client.guilds[0].member_count)))
        await asyncio.sleep(30)

async def leaderboard():
    while True:
        response = urllib.request.urlopen('https://lopdatabase.tk/getscores.php')
        html = response.read()
        text = html.decode()
        lista = text.split('|')
        lop = client.get_guild(459472853360967680)
        channel = lop.get_channel(783030691449012255)
        message = await channel.fetch_message(783050607832334349)
        text = "**Leaderboard**\n\n"
        number = 1
        for i in range(1,33,4):
            text = text + "**#" + str(number) + " "
            number = number + 1
            text = text + lista[i] + " - " + players.get(lista[i],"**Not verified** ") + "**\n"
            text = text + lista[i+1] + " wins - " + str(int(100*int(lista[i+1]) / (int(lista[i+1])+int(lista[i+2])))) + "%\n\n"
        now = datetime.now()
        dt_string = now.strftime("%b-%d-%Y %H:%M:%S")
        text = text + dt_string
        await message.edit(content=text)
        await asyncio.sleep(60)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.loop.create_task(inGame())
    client.loop.create_task(leaderboard())
    x = 1
    while True:
        if x > 100:
            x = x - 50
        else:
            x = x + 1
        await asyncio.sleep(0.5)

client.run('NzgyOTYzOTAzNzM4MDE5ODYw.X8T19Q.oCR5_TM3lFF_lfEx-YgqWokoK0E')
