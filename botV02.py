# Work with Python 3.6
import discord
#import discord.voice_client
import time
import random
from discord.ext import commands

client = discord.Client()
TOKEN=     #token goes here
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself

    if message.author == client.user:
        return

    if (message.content.startswith('dogo') or message.content.startswith('woof') or message.content.startswith("oof")):
      print(str(message.content))
      print(str(message.author))
      print("_________")
      f = open(str(time.gmtime())+".txt", "w+")
      f.write(str(message.content)+"\n"+str(message.author)+"\n ___________")
      f.close()

    if message.content.startswith('dogo hello'):
        msg = 'hello @'+str(message.author)
        channel = message.channel
        await channel.send(msg)

    if message.content.startswith('dogo spam'):
        channel = message.channel
        #msg=message.content
       # i=1
        await channel.send("illegal command please fuck off")
        #while (i<10):
        #    await channel.send(message.content[9:len(msg)])
        #    i=i+1
        #    time.sleep(0.5)

    if message.content.startswith("dogo help") or message.content.startswith("dogo commands"):
        channel = message.channel
        await channel.send('prefix: dogo \n commends: \n dogo i have food- posts a gif related to food \n dogo are you really a dog- answers with yes\n dogo who is a good dogo- answers with "me!"\n "dogo lick" or "dogo no lick"- answers woth lick\n dogo echo - echos messages content\n "dogo pet" or "dogo i pet you"- gif of a peted dog\n "woof" or "dogo woof" - answers with a woof gif \n cute dogo- answers with a cute dogo gif \n dogo fight - a fight betwen dogo and the author \n oof - respones with oof and gmc time (without dogo prefix!) \n dogo time - responses with gmc time \n bot is still in dev and runs on some randome hardwere please be nice to dogo \n ho btw the messages are being loged so no braking dogo!')

    if message.content.startswith('dogo echo'):
        channel =message.channel
        msg=message.content
        #await commands.bot(";").delete_message(message)
        lengh=len(msg)
        await channel.send(msg[10:lengh])

    if message.content.startswith("dogo i have food"):
        channel = message.channel
        await channel.send("https://tenor.com/R6ms.gif")

    if message.content.startswith("dogo are you really a dog"):
            channel = message.channel
            await channel.send("yes, i am a real dog")

    if message.content.startswith("who is a good dogo"):
        channel = message.channel
        await channel.send("me!")

    if (message.content.startswith("dogo lick") or message.content.startswith("dogo no lick")):
        channel = message.channel
        await channel.send("lick ")
    if (message.content.startswith("dogo pet") or message.content.startswith("dogo i pet you")):
        channel = message.channel
        await channel.send("thanks for the pet \n https://tenor.com/GtJ6.gif")
    if (message.content.startswith("dogo woof") or message.content.startswith("woof")):
        channel = message.channel
        await channel.send("https://tenor.com/RGLA.gif")
    if (message.content.startswith("cute dogo")):
        channel = message.channel
        await channel.send("https://tenor.com/vklV.gif")
    if (message.content.startswith("dogo fight")):
        ans=random.randint(1,3)
        channel = message.channel
        if (ans==1):
            await channel.send("dogo wins")
        if (ans==2):
            await channel.send(str(message.author)+" wins")
        if ans==3:
            await channel.send("its a tie")
    if (message.content.startswith('dogo time')):
        channel=message.channel
        await channel.send(str(time.asctime(time.gmtime())))
    if message.content.startswith("oof"):
        channel=message.channel
        await channel.send("oof happened at: GTC- "+str(time.asctime(time.gmtime())))

    if message.content.startswith("WTF"):
        channel=message.channel
        await channel.send("https://tenor.com/view/ew-disgust-gif-3671470")

    if message.content.startswith("kill") or message.content.startswith("dogo kill"):
        channel=message.channel
        await channel.send("https://media.giphy.com/media/26vUN6gcoBuBbO6ic/giphy.gif")
    



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 #   await client.change_presence(name="with its booms day")

client.run(TOKEN)
