# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

# per attivarlo vai su pythonanywhere.com 
# agiungere questo file sul cruscotto di pythonanywhere e avviarlo dalla console. 
#attiva l'ambiente virtuale con i seguenti comandi:

# istruzioni console bash

#    mkvirtualenv--python=/usr/bin/python3.7 mysite-virtualenv
#    pip install pyTelegramBotAPI
#    python3 aggiunginomedelfile.py

#dopodiche' verificalo su telegram 
#################################################


import telebot
API_TOKEN = '------inserisci il token -------'
bot = telebot.TeleBot(API_TOKEN)
# Handle '/start' and '/help'
@bot.message_handler(commands=["ciao","start"])
def send_welcome(message):
    bot.reply_to(message, "Ciao ❤(◡‿◡✿)❤ sono -----#inserire il nome del bot#------ piacere di conoscerti, come stai?!")
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)

def echo_message(message):

    if message.text=="Ciao":
        bot.reply_to(message,"{◠‿◠}ciao Se vuoi potrai farmi alcune domande ❤ heii come stai? Bene o Male?!")
    elif message.text == "Bene grazie":
        bot.reply_to(message, "{◠‿◠}❤ anch'io apparte qualche bug ogni tanto ;D")
    elif message.text== "Bene":
        bot.reply_to(message,"Mi fa piacere {◠‿◠}❤ anch'io apparte qualche bug ogni tanto ;D")
        #esempio per impostare disegni a comando
    elif message.text=="Disegno 1":
        bot.reply_to(message,""" \
▓▓▀█▐▌▀▀▐█▀█▌█▐▀▀▀▐█▓▓
▀╒╗╔╕╔▀▀╗╔╗▀╔╗▄╔▀▀╗▌▐▓
█▌╙╜▐▌▐█╝▌▐█▌▐█▌▐▌▐▌▐█
█▌╓╖▐▌┌▄█▌╘╗▌╘╗▌▐▌▐╘╛▄
▄╘╝╚╛╚▄▄╝└▄╝└▄╝╚▄▄╝╒╕█
▓▓█▐▄▌▄▄▄▌▄▄▌▄▐▄▄▄▐██▓
|¸´:*|▄█▀▀║░▄█▀▄║▄█▀▄║██▀▄
|* ¸’|██║▀█║██║█║██║█║██║█
|¸´:*|▀███▀║▀██▀║▀██▀║███▀
|* ¸’|✫✫✫✫✫✫✫✫✫✫✫✫✫
|¸´:*|██████║░░▄▄▄▄║▄▄║░▄
|* ¸’|███║░██║██║░█║██║░█
|¸´:*|███║░██║██║░█║██║░█
|* ¸’|███║░██║▀█▄▀█║▀█▄▀█
|* ¸’|███║░██║░░░░░░▄░░░█
|* ¸’|██████║░░░░░░░▀███▀

/""")

    elif message.text== "Disegno 2":
        bot.reply_to(message, """\
             ──────────────────────
─────▄█▀█▄──▄███▄────❤
────▐█░██████████▌────
─────██▒█████████─────
──────▀████████▀──────
─────────▀██▀─────────
\ """)

    elif message.text== "Disegno 3":
        bot.reply_to(message, """\
____________░▒░
___________░▒▒▒░
_________▒░▒░▒░▒
________▒░░░▒░░░▒
______▒▒░░░▒░░░░▒
____▒▒░░░░▒░░░░░▒
_█_▒▒░░░░▒░░░░░░▒
_██▒░░░░▒▒░░░░░░▒█
_██▒░░░▒▒▒░░░░░▒ █_ █
█_██░░▒▒▒█░░░░▒ █ ██
████░░████░░░░░███
_██████████░░░████
__███████████████
___█████████████
____█_██_██_███___█
_______█_ ██ _██__███
___███___ ██ _█_ █████
_███▓██__██__ ███▓██
_████▓██_██_ ███▓██
__████▓██ ██_██▓███
____██▒▒▒_██_█████
_____▒░░░▒██_███ ▒▒▒▒
____▒░░░░░▒████▒▒░░░▒
____▒░░░░░░▒█▒░░░░░░░▒
_▒▒░░░░░░▒▒▒▒▒▒░░░░░▒
▒░░░░░░░▒▒▒▒▒▒▒▒░░░░▒
▒░░░░░░▒░▒▒▒▒▒▒░░░░░▒
_▒▒▒▒▒▒░░▒░▒░░▒▒▒▒▒▒
___▒░░░░░▒██▒░░░▒▒
_▒░░░░░░▒_██_▒░░░░▒
▒░░░░░░▒__██__▒░░░░▒
▒░░░░░▒___██___▒░░░░▒
_▒░░░▒____██____▒░░░▒
__▒░▒_____██____▒░░▒
__▒▒______██____▒░▒
/""")
#esempi di impostare risposte con disegni, link, immagini, audio, video, ecc ecc.
    elif message.text== "Qui nevica":
        bot.reply_to(message,"""\
        ADORO LA NEVE è STUPENDA!!!!!!
                 .-~~\
           /     \ _
           ~x   .-~_)_
             ~x".-~   ~-.
         _   ( /         \   _
         ||   T  o  o     Y  ||
       ==:l   l   <       !  I;==
          \\   \  .__/   /  //
           \\ ,r"-,___.-'r.//
            }^ \.( )   _.'//.
           /    }~Xi--~  //  \
          Y    Y I\ \    "    Y
          |    | |o\ \        |
          |    l_l  Y T       |
          l      "o l_j       !
           \                 /
    ___,.---^.     o       .^---.._____
"~~~          "           ~            ~~~"
/""")

    elif message.text== "Rido":
        bot.reply_to(message,"""\ hahahhahah mi dissocio!!!
──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌
───▄▄██▌█ mi dissocio▐
▄▄▄▌▐██▌█░░░░░░░░░░░░▐
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌
▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀
https://i.pinimg.com/236x/fb/20/35/fb2035187ac4e706850098a72bbd7be1.jpg
/""")
    elif message.text== "Mi dissocio":
        bot.reply_to(message, "✖‿= Mi dissocio anch'io ma da te")
    elif message.text== "Mi associo":
        bot.reply_to(message, "=‿= Mi associo anch'io")
    elif message.text== "Salve":
        bot.reply_to(message,"Salve a lei ✿♥‿♥✿")
    elif message.text== "Tutto ok?":
        bot.reply_to(message, "Diciamo di si ✿♥‿♥✿ grazie!")
    elif message.text=="Sei stanca?":
        bot.reply_to(message, "Io non mi stanco mai sono un super_bot ✿♥‿♥✿")
    elif message.text== "Che bello":
        bot.reply_to(message, "Woow ♥‿♥ bellissimo")
        
#continua ad aggiungere botta e risposta o cambia i campi a piacimento 

#elif message.text== "------":
#        bot.reply_to(message, "-------")
        

bot . polling ()
#fine.
