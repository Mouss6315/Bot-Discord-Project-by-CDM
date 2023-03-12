import discord #importer 
import random #pour tout ce qui est de la génération aléatoires
import PyPDF2 #pour ouvrir les pdf
global_membre_du_salon = ""
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
#ajouter global --- nom variable puis definir objet

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

        if message.content.lower()==("!ban"):            
            nom_expediteur=message.author
            nom_channel=message.guild.get_channel(1080929878116925450)
            #d'abord il faut verifier si la personne n'est pas déja dans le channel cible
            if nom_expediteur.voice and nom_expediteur.voice.channel == nom_channel:
                await message.channel.send("t es deja dedans bg")
                return

            else:
                await nom_expediteur.edit(voice_channel=(nom_channel))

        ###### pour trouvez les cours pour chaque matieres et l'ouvrir en PDF


        ###fonction qui va pemettre de faire plus vite l'enchainement qui permet de mettre une liste avec les choix
        ##il faut definir liste de choix avant 


        # commande pour  allez vite envoyer le cour apres que la matiére a été choisi

       

        if message.content.startswith('!MasterAPE'):
            liste_elements = ['Innovation', 'C et I','Économétrie','politique éco','Firmes et marchées']

            liste_str = ""
            for i, element in enumerate(liste_elements):
                liste_str += f"{i+1}. {element}\n"

        # Envoyer la liste 
            await message.channel.send(f"Choisissez une matiere en envoyant le numéro associer:\n{liste_str}")

            def check(msg):
            # Vérifier que  message vien de l'utilisateur  envoyé 
            # et est un chiffre compris entre 1 et le nombre d'éléments dans la liste
                return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

            try:
                # Attendre la réponse de l'utilisateur
                choix = await client.wait_for('message', check=check, timeout=30)
                element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

            # au ca ou il aurais pris trop de temps a choisir le bonne élément
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")




            if element_choisi=="Innovation" : 
                #cour des agr
                liste_elements = ["PENIN","LORENTZ"]
                liste_str = ""
                for i, element in enumerate(liste_elements):
                    liste_str += f"{i+1}. {element}\n"


                await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                def check(msg):

                    return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                try:

                    choix = await client.wait_for('message', check=check, timeout=30)
                    element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                    await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

                #### au ca ou il aurais pris trop de temps a choisir le bonne élément
                except asyncio.TimeoutError:
                    await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")






                if element_choisi=="PENIN" : 
                    #                
                    liste_elements = ["CHAPITRE 1","CHAPITRE 2","CHAPITRE 3","CHAPITRE 4","CHAPITRE 5","CHAPITRE 6","CHAPITRE 7"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="CHAPITRE 1"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/PENIN/Chapitre I, Mesurer l'innovation et la connaissance - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "//Users/ilma/Desktop/dossier sans titre/Innovation/PENIN/Chapitre II, L’économie des externalités de connaissances - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/PENIN/Chapitre III, L'économie de la science - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 4"  :
                        filename = "//Users/ilma/Desktop/dossier sans titre/Innovation/PENIN/Chapitre IV, L’économie de l’open source, au-delà du logiciel - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )
                    if  element_choisi=="CHAPITRE 5"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/PENIN/Chapitre V, Innovation et structures de marché - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 6"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/PENIN/Chapitre VI, L'économie des externalités de réseau - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )
                    if  element_choisi=="CHAPITRE 7"  :
                        filename = "//Users/ilma/Desktop/dossier sans titre/Innovation/PENIN/Chapitre VII, Introduction à l’économie évolutionnaire et questionnements autour de la rationalité - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )        



# il faut 4 tab
                if element_choisi=="LORENTZ" : 
                    #                
                    liste_elements = ["CHAPITRE 1","CHAPITRE 2","CHAPITRE 3","CHAPITRE 4","CHAPITRE 5","CHAPITRE 6","CHAPITRE 7"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="CHAPITRE 1"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre I, RÇgression linÇaire - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename))                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre II, InterprÇtation des rÇsultats - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre III, HÇtÇroscÇdasticitÇ et autocorrÇlation - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 4"  :
                        filename = "Chapitre IV, EndogÇnÇitÇ, Variable instumentale et GMM - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )
                    if  element_choisi=="CHAPITRE 5"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/LORENTZ/folder/Chapitre V, Les principes de la croissance cumulative - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 6"  :
                        filename = "Chapitre VI, Destruction crÇatrice endogäne et principes de macroÇconomie Çvolutionniste - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )
                    if  element_choisi=="CHAPITRE 7"  :
                        filename = "Chapitre VII, Changement technologique endogäne dans la nouvelle thÇorie de la croissance - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )    


            if element_choisi=="C et I" : 
                #cour des agr
                liste_elements = ["Risque et incertain","théorie des contrats"]
                liste_str = ""
                for i, element in enumerate(liste_elements):
                    liste_str += f"{i+1}. {element}\n"


                await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                def check(msg):

                    return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                try:

                    choix = await client.wait_for('message', check=check, timeout=30)
                    element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                    await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

                #### au ca ou il aurais pris trop de temps a choisir le bonne élément
                except asyncio.TimeoutError:
                    await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")    







                if element_choisi=="théorie des contrats" : 
                    #                
                    liste_elements = ["CHAPITRE 1","CHAPITRE 2","CHAPITRE 3"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="CHAPITRE 1"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/C et I /UE3 - Comportements et incitations/Contrats et information/Chapitre I, Le modäle de rÇfÇrence, Les modäles principal-agents - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/C et I /UE3 - Comportements et incitations/Contrats et information/Chapitre II, L'alÇa moral - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/C et I /UE3 - Comportements et incitations/Contrats et information/Chapitre III, La sÇlection contraire - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )





# il faut 4 tab
                if element_choisi=="Risque et incertain" : 
                    #                
                    liste_elements = ["CHAPITRE 1","CHAPITRE 2","CHAPITRE 3"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="CHAPITRE 1"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/C et I /UE3 - Comportements et incitations/Risque et incertain/Chapitre I, L'utilitÇ espÇrÇe - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/C et I /UE3 - Comportements et incitations/Risque et incertain/Chapitre II, Risque et aversion au risque - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/C et I /UE3 - Comportements et incitations/Risque et incertain/Chapitre_3.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )



            if element_choisi=="Économétrie" :        
                #cour des agr
                liste_elements = ["ROQUEBERT"]
                liste_str = ""
                for i, element in enumerate(liste_elements):
                    liste_str += f"{i+1}. {element}\n"


                await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                def check(msg):

                    return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                try:

                    choix = await client.wait_for('message', check=check, timeout=30)
                    element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                    await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

                #### au ca ou il aurais pris trop de temps a choisir le bonne élément
                except asyncio.TimeoutError:
                    await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")






                if element_choisi=="ROQUEBERT" : 
                    #                
                    liste_elements = ["CHAPITRE 1","CHAPITRE 2","CHAPITRE 3","CHAPITRE 4","CHAPITRE 5","CHAPITRE 6"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="CHAPITRE 1"  :
                        filename = "/Users/ilma/Desktop/COUR M1 SE S1/Économétries/Roquebert/Chapitre I, RÇgression linÇaire - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/COUR M1 SE S1/Économétries/Roquebert/Chapitre II, InterprÇtation des rÇsultats - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/COUR M1 SE S1/Économétries/Roquebert/Chapitre III, HÇtÇroscÇdasticitÇ et autocorrÇlation - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 4"  :
                        filename = "/Users/ilma/Desktop/COUR M1 SE S1/Économétries/Roquebert/Chapitre IV, EndogÇnÇitÇ, Variable instumentale et GMM - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )
                    if  element_choisi=="CHAPITRE 5"  :
                        filename = "/Users/ilma/Desktop/COUR M1 SE S1/Économétries/Roquebert/Chapitre V, Maximum de vraisemblance - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 6"  :
                        filename = "/Users/ilma/Desktop/COUR M1 SE S1/Économétries/Roquebert/Chapitre VI, Variable dÇpendante limitÇe - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )


            if element_choisi=="politique éco" : 
                #cour des agr
                liste_elements = ["SIDIROPOULOS","BARBIER"]
                liste_str = ""
                for i, element in enumerate(liste_elements):
                    liste_str += f"{i+1}. {element}\n"


                await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                def check(msg):

                    return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                try:

                    choix = await client.wait_for('message', check=check, timeout=30)
                    element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                    await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

                #### au ca ou il aurais pris trop de temps a choisir le bonne élément
                except asyncio.TimeoutError:
                    await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")






                if element_choisi=="BARBIER" : 
                    #                
                    liste_elements = ["CHAPITRE 1","CHAPITRE 2","CHAPITRE 3"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="CHAPITRE 1"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Politique éco/UE1 - Politiques économiques, activité et emploi/Finances publiques et politique budgÇtaire/Chapitre I, Comprendre les comportements budgÇtaires - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Politique éco/UE1 - Politiques économiques, activité et emploi/Finances publiques et politique budgÇtaire/Chapitre II, Evaluer l'efficacitÇ des politiques budgÇtaires - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Politique éco/UE1 - Politiques économiques, activité et emploi/Finances publiques et politique budgÇtaire/Chapitre III, Les questions budgÇtaires en union monÇtaire - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )





# il faut 4 tab
                if element_choisi=="SIDIROPOULOS" : 
                    #                
                    liste_elements = ["CHAPITRE 1","CHAPITRE 2","CHAPITRE 3"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="CHAPITRE 1"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Politique éco/UE1 - Politiques économiques, activité et emploi/Politique monÇtaire/Chapitre I, Le cadre institutionnel de la politique monÇtaire, AutoritÇs monÇtaires, objectifs et canaux de transmission - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename))                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Politique éco/UE1 - Politiques économiques, activité et emploi/Politique monÇtaire/Chapitre II, La politique monÇtaire dite conventionnelle de la Banque Centrale, L'action de la BCE avant la crise financiäre de 2007 - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Politique éco/UE1 - Politiques économiques, activité et emploi/Politique monétaire/Chapitre III, Les politiques monétaires non-conventionnelles, Mise en œuvre de la politique monétaire post-crise des Banques Centrales - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )


            if element_choisi=="Firmes et marchées" : 
                #cour des agr
                liste_elements = ["MARET","UMBHAUER"]
                liste_str = ""
                for i, element in enumerate(liste_elements):
                    liste_str += f"{i+1}. {element}\n"


                await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                def check(msg):

                    return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                try:

                    choix = await client.wait_for('message', check=check, timeout=30)
                    element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                    await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

                #### au ca ou il aurais pris trop de temps a choisir le bonne élément
                except asyncio.TimeoutError:
                    await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")






                if element_choisi=="MARET" : 
                    #                
                    liste_elements = ["CHAPITRE 1","CHAPITRE 2","CHAPITRE 3"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="CHAPITRE 1"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Firme et marchées/UE4 - Firmes et marchés/Economie industrielle/Chapitre I, DiffÇrenciation des produits - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Firme et marchées/UE4 - Firmes et marchés/Economie industrielle/Chapitre II, EntrÇe sur un marchÇ et stratÇgies d'investissement - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Firme et marchées/UE4 - Firmes et marchés/Economie industrielle/Chapitre III, CoopÇration en R&D et externalitÇs - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )





# il faut 4 tab
                if element_choisi=="UMBHAUER" : 
                    #                
                    liste_elements = ["Cour manuscrit"]
                    liste_str = ""
                    for i, element in enumerate(liste_elements):
                        liste_str += f"{i+1}. {element}\n"


                    await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

                    def check(msg):

                        return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

                    try:

                        choix = await client.wait_for('message', check=check, timeout=30)
                        element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                        await message.channel.send(f"Vous avez choisi le  {element_choisi}")                          
                    except asyncio.TimeoutError:
                        await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")

                    if  element_choisi=="Cour manuscrit"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre I, RÇgression linÇaire - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename))                                  
        if message.content.startswith("!test"):
            guild_id = message.guild.id
            guild = client.get_guild(guild_id)
            channel = discord.utils.get(guild.channels, name="Work shop 1")
            print(channel)
        
        ### pour faire les work shop avec des sujet de conversation 
        if message.content.startswith("!wk"):
            guild_id = message.guild.id
            guild = client.get_guild(guild_id)
            channel_groupe_WK = discord.utils.get(guild.channels, name="Groupe Work shop")
            channel_WK1 = discord.utils.get(guild.channels, name="Work shop 1")
            channel_WK2 = discord.utils.get(guild.channels, name="Work shop 2")
            channel_WK3 = discord.utils.get(guild.channels, name="Work shop 3")
            taille_grp= int(message.content.split()[1]) 
            
            liste_elements = ["Allemands","Anglais","Espagnole"]
            liste_str = ""
            for i, element in enumerate(liste_elements):
                liste_str += f"{i+1}. {element}\n"


            await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

            def check(msg):

                return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

            try:

                choix = await client.wait_for('message', check=check, timeout=30)
                element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

            #### au ca ou il aurais pris trop de temps a choisir le bonne élément
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")
            
            if element_choisi=="Anglais" :
                #ont va extraire les noms des users dans le channel qui sert a faire les groupe
                global global_membre_du_salon1 
                global_membre_du_salon1 = channel_groupe_WK.members
                #boucle pour checker si personne est dans le salon pour faire les grp si c le cas stoper la fonction et le dire
                if len(global_membre_du_salon1)==0 :                        
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

                for member in global_membre_du_salon1 :
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
                await message.channel.send("work shop 1 your topic is "+topics[0])
                if Flag2==1  :
                    await message.channel.send("work shop 2 your topic is "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("work shop 3 your topic is "+topics[2])


            if element_choisi=="Allemands" :
                #ont va extraire les noms des users dans le channel qui sert a faire les groupe
                global global_membre_du_salon2 
                global_membre_du_salon2 = channel_groupe_WK.members
                
                #boucle pour checker si personne est dans le salon pour faire les grp si c le cas stoper la fonction et le dire
                if len(global_membre_du_salon2)==0 :                        
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
                topics = ["Das Wetter", "Die Arbeit", "Familie und Freunde", "Hobbys und Interessen", "Reisen", "Essen und Trinken", "Musik und Filme", "Sport", "Haustiere", "Sprachen und Kultur", "Technologie und Innovation", "Politik und Gesellschaft", "Geschichte und Traditionen", "Bildung und Karriere", "Gesundheit und Fitness", "Mode und Schönheit", "Kunst und Literatur", "Umwelt und Nachhaltigkeit", "Religion und Spiritualität", "Liebe und Beziehungen"]


                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in global_membre_du_salon2 :
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
                await message.channel.send("Arbeitsgruppe 1, dein Thema ist "+topics[0])
                if Flag2==1  :
                    await message.channel.send("Arbeitsgruppe 2, dein Thema ists "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("Arbeitsgruppe 3, dein Thema ist"+topics[2])

            if element_choisi=="Espagnole":
                #ont va extraire les noms des users dans le channel qui sert a faire les groupe
                global global_membre_du_salon3 
                global_membre_du_salon3 = channel_groupe_WK.members
                
                #boucle pour checker si personne est dans le salon pour faire les grp si c le cas stoper la fonction et le dire
                if len(global_membre_du_salon3)==0 :                        
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
                topics = ["El clima", "El trabajo", "Familia y amigos", "Pasatiempos e intereses", "Viajes", "Comida y bebida", "Música y películas", "Deportes", "Mascotas", "Idiomas y cultura", "Tecnología e innovación", "Política y sociedad", "Historia y tradiciones", "Educación y carrera profesional", "Salud y bienestar", "Moda y belleza", "Arte y literatura", "Medio ambiente y sostenibilidad", "Religión y espirit"]



                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in global_membre_du_salon3 :
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
                await message.channel.send("Grupo de trabajo 1, tu tema es "+topics[0])
                if Flag2==1  :
                    await message.channel.send("Grupo de trabajo 2, tu tema es "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("Grupo de trabajo 3, tu tema es"+topics[2])
        
        
        #pour mélanger les groupe FONCTIONNE PAS arrive pas a récuperre le bom des membre des groupe et les mettre dans la
        #une liste car liste pas attribut edit (truc pour changer salon vocale)
        if message.content.startswith("!shuffle"):            
            taille_grp= int(message.content.split()[1])
            guild_id = message.guild.id
            guild = client.get_guild(guild_id)
            channel_groupe_WK = discord.utils.get(guild.channels, name="Groupe Work shop")
            channel_WK1 = discord.utils.get(guild.channels, name="Work shop 1")
            channel_WK2 = discord.utils.get(guild.channels, name="Work shop 2")
            channel_WK3 = discord.utils.get(guild.channels, name="Work shop 3")
            liste_elements = ["Allemands","Anglais","Espagnole"]
            ### boucle pour verifier d'ou tirée le nom des salon 
            if  'global_membre_du_salon1' in globals(): 
                nom_passe_partout=global_membre_du_salon1
            elif 'global_membre_du_salon2' in globals():  
                nom_passe_partout=global_membre_du_salon2
            elif 'global_membre_du_salon3' in globals(): 
                nom_passe_partout=global_membre_du_salon3  
            
            
            
            
            
            liste_str = ""
            for i, element in enumerate(liste_elements):
                liste_str += f"{i+1}. {element}\n"


            await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

            def check(msg):

                return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

            try:

                choix = await client.wait_for('message', check=check, timeout=30)
                element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

            #### au ca ou il aurais pris trop de temps a choisir le bonne élément
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")
            
            #sortir les membre de chaque salon


            #ont mélange pour avoir un ordre déii
            if element_choisi=="Anglais":
                
                random.shuffle(nom_passe_partout)
                #ont réarragne les sujet 
                topics = ['Travel', 'Technology', 'Food', 'Music', 'Sports', 'Fashion', 'Movies', 'Health', 'Politics', 'Education', 'Relationships', 'Work', 'Art', 'Science', 'Finance', 'Religion', 'Culture', 'Environment', 'Cars', 'Literature']
                random.shuffle(topics)
                #ont peut réuttilliser des compteur plutot que la taille des grp 
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0
                for member in nom_passe_partout :
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
                await message.channel.send("work shop 1 your topic is "+topics[0])
                if Flag2==1  :
                    await message.channel.send("work shop 2 your topic is "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("work shop 3 your topic is "+topics[2])
            
            if element_choisi=="Allemands" :
                random.shuffle(nom_passe_partout)
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0

                #ont va generer les sujet avec chat gpt 
                topics = ["Das Wetter", "Die Arbeit", "Familie und Freunde", "Hobbys und Interessen", "Reisen", "Essen und Trinken", "Musik und Filme", "Sport", "Haustiere", "Sprachen und Kultur", "Technologie und Innovation", "Politik und Gesellschaft", "Geschichte und Traditionen", "Bildung und Karriere", "Gesundheit und Fitness", "Mode und Schönheit", "Kunst und Literatur", "Umwelt und Nachhaltigkeit", "Religion und Spiritualität", "Liebe und Beziehungen"]


                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in nom_passe_partout :
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
                await message.channel.send("Arbeitsgruppe 1, dein Thema ist "+topics[0])
                if Flag2==1  :
                    await message.channel.send("Arbeitsgruppe 2, dein Thema ists "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("Arbeitsgruppe 3, dein Thema ist"+topics[2])
            if element_choisi=="Espagnole" :
                random.shuffle(nom_passe_partout)
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0

                #ont va generer les sujet avec chat gpt 
                topics = ["El clima", "El trabajo", "Familia y amigos", "Pasatiempos e intereses", "Viajes", "Comida y bebida", "Música y películas", "Deportes", "Mascotas", "Idiomas y cultura", "Tecnología e innovación", "Política y sociedad", "Historia y tradiciones", "Educación y carrera profesional", "Salud y bienestar", "Moda y belleza", "Arte y literatura", "Medio ambiente y sostenibilidad", "Religión y espirit"]



                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in nom_passe_partout :
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
                await message.channel.send("Grupo de trabajo 1, tu tema es "+topics[0])
                if Flag2==1  :
                    await message.channel.send("Grupo de trabajo 2, tu tema es "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("Grupo de trabajo 3, tu tema es"+topics[2])

                        
                        
            
        
        if message.content.startswith("!Salon"):
            guild_id = message.guild.id
            guild = client.get_guild(guild_id)
            group_workshop_name = 'Groupe Work shop'
            workshop1_name1 = 'Work shop 1'
            workshop1_name2 = 'Work shop 2'
            workshop1_name3 = 'Work shop 3'
            await guild.create_voice_channel(group_workshop_name)
            await guild.create_voice_channel(workshop1_name1)
            await guild.create_voice_channel(workshop1_name2)    
            await guild.create_voice_channel(workshop1_name3)     
                
                
                
                
                
                
                
                
                
                
                
                
                
client.run("MTA4MDQ5OTc0NTIyNDY2MzExMA.G5mrDZ.TvyTB2NtBMMu2vFKaCWw3S9G9B8LHRd8QDzVJY")
#block événement arriver de qlq dans le serveur  """ 








