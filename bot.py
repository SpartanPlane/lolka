import discord
from discord.ext import commands

TOKEN = 'NzM3MDE2MTQ5NTU2MDY4NDAy.Xx3Nxw.7ufaMQaIDNbSl8EMRb5u6PFTKQw'
bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True) #разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент

bot.run(TOKEN) #Алексей не гей, он покермен





