from discord.ext import commands
import discord, chalk, asyncio, random, time, datetime
from datetime import datetime

bot = commands.Bot(command_prefix="-", status=discord.Status.idle, activity=discord.Game(name="Starting up..."))
client = discord.Client()

bot.remove_command("help")
@bot.event
async def on_ready():
    print(chalk.green("Ready to go!"))
    print(chalk.blue(f"Serving: {len(bot.guilds)} guilds."))
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Minecraft Helpdesk"))

@bot.command()
async def suggest(ctx, *, suggestion):
    channel = bot.get_channel(548688373250785305)
    embed = discord.Embed(title=f"{suggestion}", colour=discord.Colour(0xf6ff), description=f"Suggested by {ctx.message.author.mention}")
    msg = await channel.send(embed=embed)
    await msg.add_reaction(f"\N{thumbs up sign}")
    await msg.add_reaction("\U0001f44e")

    embed = discord.Embed(title=f"Your suggestion has been saved", colour=discord.Colour(0xf6ff), description=f"View it in {channel.mention}")
    await ctx.channel.send(embed=embed)




@bot.command()
@commands.has_any_role("✱ Staff")
async def bc(ctx, title:str, content:str):
    await ctx.channel.send(f"Saying {title} and {content}")
    embed = discord.Embed(title=f"{title}", colour=discord.Colour(0x4d7), description=f"{content}")
    channel = bot.get_channel(548687445525266442)
    await channel.send(embed=embed)

@bot.command()
@commands.has_any_role("✱ Staff")
async def sbc(ctx, title:str, content:str):
    await ctx.channel.send(f"Saying {title} and {content}")
    embed = discord.Embed(title=f"{title}", colour=discord.Colour(0x4d7), description=f"{content}")
    channel = bot.get_channel(554392245822947332)
    await channel.send(embed=embed)

@bot.command()
async def botver(ctx):
    await ctx.channel.send(f"{discord.__version__}")

bot.launch_time = datetime.utcnow()

@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")






        
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    embed = discord.Embed(title=f"The bots ping is {ping}ms :ping_pong: ", colour=discord.Colour(0x9adc86),)

    await ctx.channel.send(embed=embed)
@bot.command()
async def avatar(ctx, member:discord.User = None):
    if member == None or member == ctx.message.author:
        embed = discord.Embed(title=f"**{ctx.message.author.name}**'s avatar", colour=discord.Colour(0x9adc86))
        avatar = ctx.message.author.avatar_url
    else:
        avatar = member.avatar_url
        embed = discord.Embed(title=f"**{member.name}**'s avatar", colour=discord.Colour(0x9adc86))
    embed.set_image(url=avatar)


    await ctx.channel.send(embed=embed)
@bot.command()
async def embed(ctx, content):
    embed = discord.Embed(title=f"{content}", colour=discord.Colour(0x9adc86))
    await ctx.channel.send(embed=embed)


@bot.command()
async def close(ctx):
    channel = bot.get_channel(ctx.channel.id)
    if channel.category.name == "Tickets":
        await channel.delete()
    else:
        await ctx.channel.send("This is not a ticket...")

@bot.command(aliases=["app", "application"])
async def apply(ctx, *, type = None):
    if type != None:

        num = random.randint(0,999)
        if num < 10:
            num = f"00{num}"
        if num < 100:
            num = f"0{num}"
        guild = ctx.message.guild
        tick = bot.get_channel(554316532763852834)
        channel = await guild.create_text_channel(f"application-{num}", category=tick)
        await channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)

        embed = discord.Embed(title="Your application has been created ", colour=discord.Colour(0xf6ff), description=f"We created a channel for your application in {channel.mention}")
        
        await ctx.channel.send(embed=embed)
        embed = discord.Embed(title=f"{ctx.message.author.name}, We will get right back to you ", colour=discord.Colour(0xff00), description="Your application has been created. We will come right back to you! In the mean time please describe what you can do.")

        embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
        embed.set_author(name=f"{type}")
        embed.set_footer(text=f"Thank you for choosing {ctx.message.guild.name}")
        await channel.send(embed=embed)

    else:
        embed = discord.Embed(title="Please tell us what you want to apply for", colour=discord.Colour(0xf6ff), description="eg. -apply Configuring plugins")

        await ctx.channel.send(embed=embed)


@bot.command()
@commands.has_any_role("✱ Staff")
async def claim(ctx, id:int):
    channel = bot.get_channel(id)
    if channel.category.name == "Tickets":
        await channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True) 
        await ctx.channel.send(f"You have claimed {channel.mention}")
    else:
        await ctx.channel.send("You cant claim this")
#category 554316532763852834
@bot.command(aliases=["tickets", "ticket", "make", "order"])
async def new(ctx, *, type = None):
    if type != None:

        num = random.randint(0,999)
        if num < 10:
            num = f"00{num}"
        if num < 100:
            num = f"0{num}"
        guild = ctx.message.guild
        tick = bot.get_channel(554316532763852834)
        channel = await guild.create_text_channel(f"ticket-{num}", category=tick)
        await channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)

        embed = discord.Embed(title="Your ticket has been created ", colour=discord.Colour(0xf6ff), description=f"We created a channel for your ticket in {channel.mention}")
        
        await ctx.channel.send(embed=embed)
        embed = discord.Embed(title=f"{ctx.message.author.name}, We will get right back to you ", colour=discord.Colour(0xff00), description="Your ticket has been created. We will come right back to you! In the mean time please describe your questions thoroughly.")

        embed.add_field(name="To get faster support check out #prices", value="We will get back to you faster than other custumers", inline=False)

        embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
        embed.set_author(name=f"{type}")
        embed.set_footer(text=f"Thank you for choosing {ctx.message.guild.name}")
        await channel.send(content="<@&548681892401119235>", embed=embed)
        claimchnanel = bot.get_channel(554570404497457172)

        embed = discord.Embed(title=f"New commision to claim", colour=discord.Colour(0xff0004), description=f"{ctx.message.author.name} Just created a ticket")

        embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
        embed.set_author(name=f"{type}", url="https://discordapp.com", icon_url=f"{ctx.message.author.avatar_url}")
        embed.set_footer(text=f"Please claim this commission using -claim {channel.id} ")
        embed.add_field(name=f"ID: {channel.id}", value=f"-claim {channel.id}")
        await claimchnanel.send(content="<@&548681892401119235>", embed=embed)

    else:
        embed = discord.Embed(title="Please tell us what you need", colour=discord.Colour(0xf6ff), description="eg. -new Discord Bot")

        await ctx.channel.send(embed=embed)


@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    mention = member.mention
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"{pronoun} name is {name} and thier id is {member.id}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")


@bot.command()
@commands.has_any_role("✱ Staff")
async def clear(ctx):
    deleted = await ctx.channel.purge(limit=10000)
    embed = discord.Embed(title=f"Cleared all of the messages", colour=discord.Colour(0x9adc86))
    embed.set_footer(text="Message will delete in 10 secs with all other messages sent.")
    await ctx.channel.send(embed=embed)
    await asyncio.sleep(10)
    deleted2 = await ctx.channel.purge(limit=10000)



@bot.command()
@commands.has_any_role("✱ Staff")
async def cr(ctx, id:int, *, name):
    guild = ctx.message.guild

    cat = bot.get_channel(id)
    channel = await guild.create_text_channel(f"{name}", category=cat)

#the token hasnt been removed for security and privacy
