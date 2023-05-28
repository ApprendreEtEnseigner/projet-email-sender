# mdp: oihrheneycgihaqj
# Du module email.message importer la classe EmailMessage
#* En utilisant ces modules, il est possible de créer et envoyer des e-mails en Python.
#* EmailMessage est une classe qui permet de construire et manipuler des messages email. 
from email.message import EmailMessage

#* ssl est un module qui fournit des fonctionnalités de sécurité pour les connexions réseau
import ssl

#* smtplib est une bibliothèque Python pour envoyer des courriels à l'aide du protocole SMTP.
import smtplib

email_sender = 'yeroscorpion149@gmail.com' # stocke email de l'expeditaire
email_password = 'oihrheneycgihaqj' # stocke mdp de l'expeditaire
email_recever = 'sayor19488@cutefier.com' # stoke email du receveur
subject = "Dont forget to subscribe" # sujet du message
body = """ 
When you watch a video, please hit subscribe
""" # corps du message

# creer une instance de la classe emailMessage (= un modele)
em = EmailMessage() # em => un message electronique
em['From'] = email_sender # => stocke les infos de email_sender dans l'objet em['From'] de la classe em
em['To'] = email_recever # => stocke les infos de email_recever dans l'objet em['To'] de la classe em
em['subject'] = subject # => stocke les infos de subject dans l'objet em['subject'] de la classe em
em.set_content(body) # =>  La méthode set_content() est appelée sur l’objet em (grand-object = classe) et prend un argument body qui est le contenu du message

"""
? Explication des lignes ci-dessous

? Elle permettent d'envoyer un email sécurisé à partir d'un compte Gmail en utilisant le protocole SMTP (Simple Mail Transfer Protocol).
"""
#* Tout d'abord, un contexte SSL (Secure Sockets Layer) est créé en utilisant la méthode:  ssl.create_default_context(). Ceci est nécessaire pour établir une connexion SSL sécurisée avec le serveur SMTP de Gmail.
context = ssl.create_default_context()

#* Ensuite, une connexion SSL sécurisée est établie avec le serveur SMTP de Gmail en utilisant la classe smtplib.SMTP_SSL. Les paramètres pour établir cette connexion sont: 'smtp.gmail.com' pour le serveur SMTP de Gmail, 465 pour le port SSL par défaut de Gmail, et le contexte SSL créé précédemment.
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    
    # *Après cela, l'utilisateur se connecte à son compte Gmail en utilisant la méthode smtp.login(email_sender, email_password), où email_sender est l'adresse e-mail de l'expéditeur et email_password est leur mot de passe.
    smtp.login(email_sender, email_password) # pour se connecter
    
    #* Enfin, l'e-mail est envoyé en utilisant la méthode smtp.sendmail(email_sender, email_receiver, em.as_string()), où email_sender est l'adresse e-mail de l'expéditeur, email_receiver est l'adresse e-mail du destinataire et em.as_string() est le contenu du message converti en une chaîne de caractères.
    smtp.sendmail(email_sender, email_recever, em.as_string())