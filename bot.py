#Prismatic#3969 BOT

import discord
from discord import Game
from discord import Message
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1JtJr-f0HVB8hLfAELZSJSp2UqI4djMo8ol3CtsMTwlk/edit").sheet1



bot = commands.Bot(command_prefix='?')
#bot.get_all_emojis()
#bot.get_all_emojis

@bot.event
async def on_ready():
	await bot.change_presence(game=Game(name="with Prismatic gang"))
	print("Name and Discriminator: " + bot.user.name + "#" + bot.user.discriminator)
	print("ID: " + bot.user.id)

@bot.event
async def on_member_join(member):
	role = discord.utils.get(member.server.roles, name="Guest")
	await bot.add_roles(member, role)

@bot.event
async def on_message(message):
	if message.content.startswith("** **"):
		#emoji = get(bot.get_all_emojis(), name="a:prismyes:508125853641605150")
		#pNo = get(bot.get_all_emojis(), name=":prismno:508125853641605150")
		await bot.add_reaction(message=message, emoji="prismyes:508125853641605150")
		await bot.add_reaction(message=message, emoji="prismno:508125946226802688")
		#await bot.add_reaction(message=message, emoji=pNo)

	await bot.process_commands(message)

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("Hello! Ping!")

@bot.command(pass_context=True)
async def user_info(ctx, user: discord.Member):
	embed = discord.Embed(title="{}'s User Information".format(user.name), description="Their user info.", color=0x9d00ff)
	embed.add_field(name="Name", value=user.name, inline=True)
	embed.add_field(name="User ID", value=user.id, inline=True)
	embed.add_field(name="Current Status", value=user.status, inline=True)
	embed.add_field(name="Highest Role", value=user.top_role)
	embed.set_thumbnail(url=user.avatar_url)
	embed.set_footer(text="First seen: {}".format(user.joined_at))
	await bot.say(embed=embed)

#@bot.command(pass_context=True)
#async def mute(ctx, user: discord.Member, muteTime):

#	await asyncio.sleep(int(muteTime))
	#user.add_roles("Muted")

@bot.command(pass_context=True)
async def gang_info(ctx):
	GANG_NAME = wks.cell(1, 1).value
	GANG_MEMBERS = wks.cell(8, 13).value
	GANG_UPGRADES = wks.cell(8, 15).value
	GANG_RANK = wks.cell(8, 16).value
	LAST_UPDATE = wks.cell(32, 14).value
	embed = discord.Embed(title="Prismatic Gang Stats", description="The current stats for our gang.", color=0x4286f4)
	embed.add_field(name="Gang Name", value=GANG_NAME, inline=True)
	embed.add_field(name="Gang Members", value=GANG_MEMBERS)
	embed.add_field(name="Gang Upgrades", value=GANG_UPGRADES)
	embed.add_field(name="Gang Rank", value=GANG_RANK)
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	embed.set_footer(text="Last updated: " + LAST_UPDATE)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def total_strikes(ctx):
	TOTAL_STRIKES = wks.cell(8, 14).value
	embed = discord.Embed(title="Total Strikes", description="{}".format(TOTAL_STRIKES), color=0xff0000)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def rapsheet(ctx, user: discord.Member):
	embed = discord.Embed(title="Rapsheet", description="All their punishments.", color=0xff0000)
	embed.set_author(name="{}".format(user.name), icon_url=user.avatar_url)
	embed.add_field(name="Unban", value="No reason.")
	embed.add_field(name="Ban", value="Backstab (2nd time).")
	embed.add_field(name="Kick", value="Backstab.")
	embed.add_field(name="Strike", value="Backstab")
	embed.add_field(name="Demote", value="Raided gang base.")
	embed.add_field(name="Strike", value="Killed gangmate.")
	embed.set_footer(text="Total strikes: 6")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def create_vote(ctx,
	 applicantName, applicationURL):

	#message = message.content.startswith("?create_vote")
	#client_message = bot.get_message(id=message.content.startswith("?create_vote").id,
	#channel="applications")

	embed = discord.Embed(title="Applicant's name", description= "{}".format(applicantName),
	color=0xd3d3d3)
	embed.add_field(name="Application URL", value="{}".format(applicationURL))
	embed.set_footer(text="Applications bot by: Rick Johnson")
	await bot.say("<@&510592602865795102>")
	await bot.say(embed=embed)
	await bot.say("** **")
	await bot.delete_message(ctx.message)

bot.run(os.getenv('TOKEN'))
