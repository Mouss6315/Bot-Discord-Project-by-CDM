import discord
import random
import openai
client = discord.Client(intents=discord.Intents.all())
openai.api_key="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"
#pour afficher message quand il est pret
@client.event
async def on_ready():
        print("le bot fonctionne il est pret")
#fonction pour utiliser chat_gpt
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
#l argument ici dois etre la questions que ont veut posser a chat gpt


#block événement message

@client.event
async def on_message(message):
        id_serveur=1079374243122401410
        id_role=1080806266181517393
        ####### les jeux ######
        if message.content.startswith("!dé"):
            cmb_il_devine =int(message.content.split()[1])
            cmb_le_bot_joue=random.randint(1,6)
            check=str(cmb_le_bot_joue) #convertis en texte pour pouvoir le mettre dans le .send
            if cmb_il_devine!=cmb_le_bot_joue :
                await message.channel.send(check +  "  bien essayer peut etre la prochaine fois" ) #ce truc accepte comme
            elif cmb_il_devine==cmb_le_bot_joue :
                id_expediteur=message.author.id
                guild = client.get_guild(id_serveur)
                role = guild.get_role(id_role)
                user = guild.get_member(id_expediteur)
                await user.add_roles(role)
                await message.channel.send(check +  "   ta eu de la chance mais bien jouer")    #IL FAUT METTRE PLUS POUR



        if message.content.startswith("!jesuis"):
            son_id=str(message.author.id)
            await message.channel.send(son_id)
        if  message.content.startswith("!effacer") :
            number= int(message.content.split()[1])
            message= await message.channel.history(limit=number+1).flatten()
            for each_message in message: #recupere message met les dans list message et suprime dans boucle for
                 await each_message.delete()

        
        
        
        
        
        
client.run("MTA4MDQ5OTc0NTIyNDY2MzExMA.G5mrDZ.TvyTB2NtBMMu2vFKaCWw3S9G9B8LHRd8QDzVJY")
#block événement arriver de qlq dans le serveur





