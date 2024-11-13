import discord
from discord.ext import commands
import requests
import Settings
import numpy as np
from qutip import *
import time
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def test(ctx,*arg):
    respuesta = " ".join(arg)
    await ctx.send(respuesta)
@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")
##################################################################
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
##################################################################
@bot.event
async def on_ready():
    print(f"Estamos dentro! {bot.user}")
@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)
################################################################################################
@bot.command()
async def suma(ctx,n1:int,n2:int):
    """Esta función suma dos números enteros y devuelve el resultado."""
    resultado = n1 + n2
    await ctx.send(f"La suma de {n1} y {n2} es {resultado}")
@bot.command()
async def resta(ctx,n1:int,n2:int):
    """Esta función suma dos números enteros y devuelve el resultado."""
    resultado1 = n1 - n2
    await ctx.send(f"La resta de {n1} y {n2} es {resultado1}")
@bot.command()
async def raiz(ctx,n1:int):
    """Esta función suma dos números enteros y devuelve el resultado."""
    resultado2 = np.sqrt(n1)
    await ctx.send(f"La raiz cuadrada de {n1} {resultado2}")
@bot.command()
async def ket0(ctx):
    """Esta función suma dos números enteros y devuelve el resultado."""
    ket0 = basis(2,0)
    await ctx.send(f"El ket0 es {ket0}")
@bot.command()
async def ket1(ctx):
    """Esta función suma dos números enteros y devuelve el resultado."""
    ket1 = basis(2,1)
    await ctx.send(f"El ket1 es {ket1}")
@bot.command()
async def funciones(ctx):
    """Esta función suma dos números enteros y devuelve el resultado."""
    await ctx.send(f"Tengo varias funciones, aqí te voy a comentar algunas de ellas")
    time.sleep(1)
    await ctx.send(f"1.Tengo una funcion que envia pokemones, para utilizarla debes llamarla !poke pikachu(es un ejemplo)")
    time.sleep(1)
    await ctx.send(f"2.Tengo unas funciones que envian imagenes de perros y de patos")
    time.sleep(1)
    await ctx.send(f"3.Tengo una función que realiza sumas, la llamas !suma 2 3(te da el resultado)")
    time.sleep(1)
    await ctx.send(f"4.Tengo una función que realiza restas, la llamas !resta 2 3(te da el resultado)")
    time.sleep(1)
    await ctx.send(f"5.Tengo una función que realiza raices cuadradas, la llamas !raiz 2 (te da el resultado)")
    time.sleep(1)
    await ctx.send(f"6.Tengo una función que te muestra el ket0, la llama !ket0")
    time.sleep(1)
    await ctx.send(f"7.Tengo una función que te muestra el ket1, la llama !ket1")
bot.run(Settings.TOKEN )
