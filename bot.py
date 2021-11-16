import discord
from discord.ext import commands
from discord.commands import Option
import asyncio
import random
import datetime

client=commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print('bot is ready')
    await client.change_presence(activity=discord.Game(name="DM ME FOR SUPPORT"))


@client.event
async def on_message_delete(message):
    if '<@' in message.content:
        gping=discord.Embed(title=f"{message.author.name} Has ghost pinged someone", description=f"{message.content}")
        await message.channel.send(embed=gping)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.guild:
        await message.channel.send("Thank you for sending your concern/question/support. Staff will reply soon so please be patient. Replies should average 1h-1d responses")
        channel = client.get_channel(modmail-channel)
        nocontext=discord.Embed(title=(f"{message.author.name} requires support"), description=(f"{message.content}"))
        await channel.send(embed=nocontext)

@client.slash_command(guild_ids=[---])
async def issuereply(ctx, user: Option(discord.Member, 'the user you wish to reply to', Required=False, Default=None), contekst, messageideee):
    resolv=discord.Embed(title=(f"{user.name}'s case... Resolved by {ctx.author.name}."), description=(contekst))
    await user.send(embed=resolv)
    await ctx.send(embed=resolv)
    msgeeee = await ctx.fetch_message(messageideee)
    await msgeeee.add_reaction("🎉")

@client.slash_command(guild_ids=[---])
@commands.has_role("Staff")
async def gstart(ctx, mins: Option(int, 'How long should the giveaway be!?', Required=False, Default=None), * , prize: Option(str, 'What should the prize be?')):
    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60) 

    embed.add_field(name = "Ends At:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends {mins} mintues from now!")

    my_msg = await ctx.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")



@client.slash_command(guild_ids=[---])
async def rng(ctx, num1: Option(int, "1st number", required=True), num2: Option(int, "2nd number", Required=True)):
    ee=random.randint(num1, num2)
    await ctx.respond(ee)



client.run('TOKEN')
