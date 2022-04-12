import discord, os, requests, random, string, asyncio
from discord.ext import commands
from keep_alive import keep_alive
from colorama import Fore, Style

def Clear():
os.system('cls')

Clear()
token = ""
Prefix = "$"

client = discord.Client()
client = commands.Bot(command_prefix=prefix,self_bot=True)

@client.event
async def on_ready():
Clear()
print(f"Dank Memer AutoFarmV1\nDo {prefix}auto_ON To Start Bot\n\n")

@client.command(name='auto_ON', aliases=['on'])
async def auto_ON(ctx):
await ctx.message.delete()
count = 0
while True:
try:
count += 1
await ctx.send('pls beg', delete_after=0.4)
await asyncio.sleep(1.5)
await ctx.send('pls fish', delete_after=0.4)
await ctx.send('pls hunt', delete_after=0.4)
awate ctx.send('pls dig', delete_after=0.4)
print (f'{Fore.BLUE}[DANK MEMER] {Fore.GREEN}Beg number: {count} sent'Fore.RESET)
await asyncio.sleep(35)
exept Exeption as e:
print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

keep_alive()
client.run(token,bot=False)
