import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def hola(ctx):
    mensaje = (
        'Hola, soy un bot ayudando al medio ambiente. ¿En qué te ayudo hoy?\n'
        'estos son los comandos: catastrofes, cuidar, tips, info \n'
    )
    await ctx.send(mensaje)

@bot.command()
async def catastrofes(ctx):
    mensaje = (
        "Las catástrofes ambientales suelen ser causadas por factores como: \n"
        "- Deforestación \n"
        "- Contaminación del agua y aire \n"
        "- Cambio climático debido a emisiones de gases de efecto invernadero \n"
        "- Manejo inadecuado de residuos \n"
        "\nPara reducirlas, podemos: \n"
        "- Reducir, reutilizar y reciclar \n"
        "- Apostar por energías renovables \n"
        "- Proteger los bosques y los ecosistemas \n"
        "- Usar transporte sostenible"
    )
    await ctx.send(mensaje)

@bot.command()
async def cuidar(ctx):
    mensaje = (
        "Podemos cuidar el medio ambiente siguiendo estos consejos: \n"
        "- Ahorrar agua y energía \n"
        "- Consumir productos locales y sostenibles \n"
        "- Plantar árboles \n"
        "- Evitar plásticos de un solo uso \n"
        "- Participar en actividades de limpieza comunitaria \n"
        "- Educar a otros sobre la importancia de proteger nuestro planeta"
    )
    await ctx.send(mensaje)

@bot.command()
async def tips(ctx):
    consejos = [
        "Desconecta los aparatos electrónicos que no estés usando.",
        "Usa bombillas LED para ahorrar energía.",
        "Elige transporte público, bicicleta o camina siempre que sea posible.",
        "Compra ropa y productos hechos de materiales reciclados.",
        "Evita imprimir documentos innecesariamente.",
        "Usa bolsas reutilizables en lugar de plásticas."
    ]
    await ctx.send(random.choice(consejos))

@bot.command()
async def info(ctx):
    mensaje = (
        "Soy un bot creado para promover la concienciación ambiental. ¿Quieres saber cómo puedes ayudar al planeta? \n"
        "Escribe: \n"
        "- !catastrofes para aprender sobre las causas de los desastres ambientales y cómo prevenirlos. \n"
        "- !cuidar para descubrir formas de cuidar el medio ambiente. \n"
        "- !tips para obtener consejos rápidos y prácticos."
    )
    await ctx.send(mensaje)

bot.run("tu token")
