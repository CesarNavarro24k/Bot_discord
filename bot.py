import discord
from discord.ext import commands
import requests
import numpy as np
from qutip import *
import time
import aiohttp
import os


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
async def exp(ctx,n1:int, n2: int):
    resultado_exp = n1**n2
    await ctx.send(f"el numero {n1} elevado a la {n2} es {resultado_exp}")
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
import aiohttp
import os

@bot.command()
async def check(ctx, link=None):
    if ctx.message.attachments:  # Manejo de archivos adjuntos
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Guardé la imagen en ./{file_name}")
    elif link:  # Manejo de enlaces proporcionados como argumento
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(link) as response:
                    if response.status == 200:
                        content_disposition = response.headers.get("Content-Disposition", "")
                        file_name = (
                            content_disposition.split("filename=")[-1].strip('"')
                            if "filename=" in content_disposition
                            else os.path.basename(link)
                        )
                        file_path = f"./{file_name}"
                        with open(file_path, "wb") as f:
                            f.write(await response.read())
                        await ctx.send(f"Guardé el archivo del enlace en {file_path}")
                    else:
                        await ctx.send(f"No se pudo descargar el archivo. Estado HTTP: {response.status}")
            except Exception as e:
                await ctx.send(f"Hubo un error al descargar el archivo: {e}")
    else:
        await ctx.send("Por favor, sube una imagen o proporciona un enlace.")

#############################
@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)# esta linea saluda
    await ctx.send("Quieres hablar de fornite o de counter strike? Responde con 'fornite' o 'counter'.")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['counter', 'fornite']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content == 'fornite':
            await ctx.send("""Fortnite es un videojuego del año 2017 desarrollado por la empresa Epic Games lanzado como diferentes paquetes de software que presentan seis diferentes modos de juego, pero que comparten el mismo motor de juego y mecánicas. Fue anunciado en los premios Spike Video Game Awards en 2011.""")
            await ctx.send("""modos de juego-los dos modos de juego principales están configurados para ser títulos gratuitos, aunque actualmente Salvar el mundo está en un acceso anticipado y requiere ser comprado. Ambos juegos se monetizan mediante el uso de V-Bucks (PaVos o Monedas V en español3​), la moneda del juego que también se puede ganar solo a través de Salvar el mundo. Los V-Bucks en Salvar el mundo se pueden usar para comprar piñatas con forma de llamas para obtener una selección aleatoria de artículos. En Battle Royale, los V-Bucks se pueden usar para comprar artículos estéticos como modelos de personajes o similares, o también se puede usar para comprar el pase de batalla, una progresión escalonada de recompensas de personalización para ganar experiencia y completar ciertos objetivos durante el juego, en el curso de una temporada de Battle Royale.""")   
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber sobre otros juegos, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    
    await ctx.send("Quieres saber en que capitulo estamos, responde 'sí' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("capitulo 6 - temporada 1") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas hablar sobre juegos, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    
    await ctx.send("Deseas saber como se celebra en Suiza o Finlandia. Si tu respuesta es Suiza marca 1 o si es Finlandia marca 2")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['1', '2']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response2.content == "1":
            await ctx.send("En Suiza, las celebraciones incluyen...")
        elif response2.content == "2":
            await ctx.send("En Finlandia, las celebraciones incluyen...")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
@bot.command()
async def divide(ctx, left: int, right: int):
    """divide two numbers together."""
    if right == 0:
        await ctx.send("Error: Division por cero no esta definida!")
    else:
        await ctx.send(left / right)
   
bot.run("")
