import discord
from discord.ext import commands
import requests
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


#############################
@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)# esta linea saluda
    await ctx.send("Quieres hablar de la contaminacion?")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content == 'si':
            await ctx.send("""La contaminación ambiental es la presencia de sustancias o elementos dañinos para los seres humanos y los ecosistemas (seres vivos)""")   
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber sobre que es la contaminación, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    
    await ctx.send("Quieres conocer algunos ejemplos de contaminación, responde 'sí' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("1. contaminación del aire") 
            await ctx.send("2. contaminación del suelo") 
            await ctx.send("3. contaminación acustica")
            await ctx.send("4. contaminación termica") 

        else:
            await ctx.send("Está bien, si alguna vez necesitas conocer los tipos de contaminación, me avisas.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    
    await ctx.send("Deseas ver una imagen sobre un ejemplo de contaminación?")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'si']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response2.content == "si":
            with open('conta.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
                picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=picture)
        else:
            await ctx.send("Esta bien!")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

bot.run("")
