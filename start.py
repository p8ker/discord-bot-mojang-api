import cards
import disnake
from disnake.ext import commands

#make bot
intents = disnake.Intents.all() 
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Done!")

#command for card minecraft user
@bot.slash_command(description="Card player")
async def card(ctx, name):
    cards.card_name(name)
    await ctx.send(file = disnake.File(f"card.png"))

#command for skin minecraft user
@bot.slash_command(description="Skin player")
async def skin(ctx, name):
    cards.skin_name(name)
    await ctx.send(file = disnake.File(f"skin.png"))

bot.run("TOKEN")
