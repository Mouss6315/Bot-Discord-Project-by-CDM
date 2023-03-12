import discord #importer 
import random #pour tout ce qui est de la génération aléatoires
import PyPDF2 #pour ouvrir les pdf
global_membre_du_salon = ""
client = discord.Client(intents=discord.Intents.all())

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
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/LORENTZ/folder/Chapitre I, La relation progrès technique – croissance au regard de l’histoire - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename))                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/LORENTZ/folder/Chapitre II, Les moteurs thÇoriques de la croissance, Destruction crÇatrice vs. rendements croissants - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/LORENTZ/folder/Chapitre III, A l’aube des théories modernes de la croissance, Le débat sur l’instabilité de la croissance - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 4"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/LORENTZ/folder/Chapitre IV, Progräs technique endogäne dans les modäles de croissance - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )
                    if  element_choisi=="CHAPITRE 5"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/LORENTZ/folder/Chapitre V, Les principes de la croissance cumulative - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 6"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/LORENTZ/folder/Chapitre VI, Destruction crÇatrice endogäne et principes de macroÇconomie Çvolutionniste - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )
                    if  element_choisi=="CHAPITRE 7"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Innovation/LORENTZ/folder/Chapitre VII, Changement technologique endogäne dans la nouvelle thÇorie de la croissance - Cours.pdf"
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
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre I, RÇgression linÇaire - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )                                  


                    if  element_choisi=="CHAPITRE 2"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre II, InterprÇtation des rÇsultats - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 3"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre III, HÇtÇroscÇdasticitÇ et autocorrÇlation - Cours.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 4"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre IV, EndogÇnÇitÇ, Variable instumentale et GMM - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )
                    if  element_choisi=="CHAPITRE 5"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre V, Maximum de vraisemblance - Diapo.pdf"
                        with open(filename, 'rb') as file:
                            await message.channel.send(file=discord.File(file, filename) )

                    if  element_choisi=="CHAPITRE 6"  :
                        filename = "/Users/ilma/Desktop/dossier sans titre/Économétries/Roquebert/Chapitre VI, Variable dÇpendante limitÇe - Diapo.pdf"
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
        
client.run("MTA4MDQ5OTc0NTIyNDY2MzExMA.G8l7N0.4rJ08XTPt6AXoIefeeVFTx62SAIwELQZDbVqYo")
#block événement arriver de qlq dans le serveur  """ 










