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

        if message.content.lower()==("!workshop"):            
            nom_expediteur=message.author
            nom_channel=message.guild.get_channel(1080929878116925450)
            #d'abord il faut verifier si la personne n'est pas déja dans le channel cible
            if nom_expediteur.voice and nom_expediteur.voice.channel == nom_channel:
                await message.channel.send("t es deja dedans bg")
                return

            else:
                await nom_expediteur.edit(voice_channel=(nom_channel))
        
        
        
        
        if message.content.startswith("!test"):
            taille_grp= int(message.content.split()[1]) 
            channel_groupe_WK = client.get_channel(1081538537935085609)
            channel_WK1=client.get_channel(1081532679016681502)
            channel_WK2=client.get_channel(1081532791986081833)
            channel_WK3=client.get_channel(1081532679016681502)

            #ont va extraire les noms des users dans le channel qui sert a faire les groupe
            membre_du_salon = channel_groupe_WK.members
            #boucle pour checker si personne est dans le salon pour faire les grp si c le cas stoper la fonction et le dire
            if len(membre_du_salon)==0 :                        
                await message.channel.send("le salon:Groupe work shop est vide, rentrez dedans afin que les groupe sois fait")
                return
            #finds members connected to the channel
            les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
            les_nom_des_salon_vocaux= []
            les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
            les_nom_des_salon_vocaux= []
            #boucle pour ajouter le_nom des salon dans une liste si jamais ont en ajoute une de plus pour gagner du temps
          #  for i in range(1,4):
           #     nom_variable = 'channel_WK' + str(i) # Construire le nom de la variable
            #    pour_l_appeler= globals()[nom_variable]
             #   les_nom_des_salon_vocaux.append(pour_l_appeler)
            nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
            nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
            nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3
            
            Flag2=0
            Flag3=0
            
            #ont va generer les sujet avec chat gpt 
            topics = ['Travel', 'Technology', 'Food', 'Music', 'Sports', 'Fashion', 'Movies', 'Health', 'Politics', 'Education', 'Relationships', 'Work', 'Art', 'Science', 'Finance', 'Religion', 'Culture', 'Environment', 'Cars', 'Literature']
            random.shuffle(topics)
            #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard
            
            for member in membre_du_salon :
                les_nom_des_membre.append(member)
            random.shuffle(les_nom_des_membre)
            
            for member in les_nom_des_membre :
                if nombre_wk1<taille_grp:
                    nombre_wk1+=1 
                    await member.edit(voice_channel=(channel_WK1))                   
                     
                elif nombre_wk2<taille_grp:
                    nombre_wk2+=1
                    await member.edit(voice_channel=(channel_WK2))
                    Flag2=1
                elif nombre_wk3<taille_grp:
                    nombre_wk3+=1             
                    await member.edit(voice_channel=(channel_WK3))
                    Flag3=1
            #buocle pour donner des topics pour les salon 2 et 3 uniquement si ya des gens dedans    
            if Flag2==1  :
                await message.channel.send("work shop 2 your topic is "+topics[1])
                if Flag3==1 :
                    await message.channel.send("work shop 3 your topic is "+topics[2])
            await message.channel.send("work shop 1 your topic is "+topics[0])
        
        
        
        #pour mélanger les groupe 
        if message.content.startswith("!shuffle"):            
            taille_grp= int(message.content.split()[1])
            channel_WK1=client.get_channel(1081532679016681502)
            channel_WK2=client.get_channel(1081532791986081833)
            channel_WK3=client.get_channel(1081532679016681502)
            #sortir les membre de chaque salon
            
            membre_du_salon_WK1 = channel_WK1.members
            membre_du_salon_WK2 = channel_WK2.members
            membre_du_salon_WK3 = channel_WK3.members
            #créer une liste pour stocker les membre
            
            liste_des_membre=[membre_du_salon_WK1,membre_du_salon_WK2,membre_du_salon_WK3]
            #ont mélange pour avoir un ordre déii
            random.shuffle(liste_des_membre)
            #ont réarragne les sujet 
            topics = ['Travel', 'Technology', 'Food', 'Music', 'Sports', 'Fashion', 'Movies', 'Health', 'Politics', 'Education', 'Relationships', 'Work', 'Art', 'Science', 'Finance', 'Religion', 'Culture', 'Environment', 'Cars', 'Literature']
            random.shuffle(topics)
            #ont peut réuttilliser des compteur plutot que la taille des grp 
            nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
            nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
            nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3
            
            Flag2=0
            Flag3=0
            for member in liste_des_membre :
                if nombre_wk1<taille_grp:
                    nombre_wk1+=1 
                    await member.edit(voice_channel=(channel_WK1))                   
                     
                elif nombre_wk2<taille_grp:
                    nombre_wk2+=1
                    await member.edit(voice_channel=(channel_WK2))
                    Flag2=1
                elif nombre_wk3<taille_grp:
                    nombre_wk3+=1             
                    await member.edit(voice_channel=(channel_WK3))
                    Flag3=1
            #buocle pour donner des topics pour les salon 2 et 3 uniquement si ya des gens dedans    
            if Flag2==1  :
                await message.channel.send("work shop 2 your topic is "+topics[1])
                if Flag3==1 :
                    await message.channel.send("work shop 3 your topic is "+topics[2])
            await message.channel.send("work shop 1 your topic is "+topics[0])
client.run("MTA4MDQ5OTc0NTIyNDY2MzExMA.G5mrDZ.TvyTB2NtBMMu2vFKaCWw3S9G9B8LHRd8QDzVJY")
#block événement arriver de qlq dans le serveur





