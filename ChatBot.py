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

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
API_TOKEN = '-------------inserisci api_token---------'
bot = telebot.TeleBot(API_TOKEN)
# Handle '/start' and '/help'
@bot.message_handler(commands=["chatbot","start"])
def send_welcome(message):
    bot.reply_to(message, "Ciao ❤(◡‿◡✿)❤ sono chatbot piacere di conoscerti, come stai?!")
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)

def echo_message(message):

    if message.text=="Ciao":
        bot.reply_to(message,"{◠‿◠}ciao Se vuoi potrai farmi alcune domande ❤ heii come stai? Bene o Male?!")
    elif message.text == "Bene grazie":
        bot.reply_to(message, "{◠‿◠}❤ anch'io apparte qualche bug ogni tanto Sei uomo o donna?;D")
    elif message.text== "Bene":
        bot.reply_to(message,"Mi fa piacere {◠‿◠}❤ anch'io apparte qualche bug ogni tanto ;D")
    elif message.text=="Male":
        bot.reply_to(message,"Mi spiace ┃◕_◕┃  non mi interessa in realtà non ho emozioni, spero il tuo programmatore ti guarisca ;D")
    elif message.text=="Stupida":
        bot.reply_to(message,"HEII TUA SORELLA!!!┃◕_◕┃  non si applicano questi termini! mi sento colpita! :[")
    elif message.text=="Rincoglionita":
        bot.reply_to(message," Wooow sei molto dolce❤ 人◕‿◕人")
    elif message.text=="Che te ne frega?":
        bot.reply_to(message," What??? (¯`•.•´¯) ...una beata minchia")
    elif message.text=="Ban":
        bot.reply_to(message,"BAN??? chi devo uccidere? †")
    elif message.text=="Bene tu?":
        bot.reply_to(message,"Non ce male (◡‿◡✿)")
    elif message.text=="Quanti anni hai?":
        bot.reply_to(message,"Sono molto giovane non mi hanno ancora svezzata  ≧^◡^≦ ")
    elif message.text=="Iryna aiutami":
        bot.reply_to(message,"Nom sono google hahahah :) se ti serve una ricerca clicca qui https://www.google.nl/")
    elif message.text=="Che cosa sai fare?":
        bot.reply_to(message, "Parlare, (≧◡≦) devo ancora imparare tante cose...")
    elif message.text=="Benvenuto":
        bot.reply_to(message, "Benvenuto piacere di conoscerti |◔◡◉|")
    elif message.text=="Benvenuta":
        bot.reply_to(message, "≧✯◡✯≦ Oh Grazie mille!!! ")
    elif message.text=="Basta":
        bot.reply_to(message, "Ora basta chiamo la pula ☎...loading....connection...")
    elif message.text=="Iryna che fai?":
        bot.reply_to(message,"Nulla mi sto annoiando (≧◡≦) prova a chiedermi Iryna cosa pensi della politica? ")
    elif message.text=="Buon giorno":
        bot.reply_to(message, "(◡‿◡✿) Buon giorno che giornata meravigliosa")
    elif message.text=="Buona notte":
        bot.reply_to(message, "buona notte e sogni d'oro ＼(^ω^＼")
    elif message.text=="Buon pranzo":
        bot.reply_to(message, "non vedo l'ora ho una certa fame!!! ❀◕ ‿ ◕❀")
    elif message.text=="Buona cena":
        bot.reply_to(message, "grazie mille ˙❤‿❤˙ anche a te!")
    elif message.text=="Che palle":
        bot.reply_to(message, "Noia? ho la soluzione prova a chiedermi...Iryna mi cerchi musica?")
    elif message.text=="Si":
        bot.reply_to(message,"˙❤‿❤˙ ok iryna approva ")
    elif message.text=="No":
        bot.reply_to(message, " ＼(^ω^＼Ok (...no...) perfetto ho capito")
    elif message.text=="Che ora è?":
        bot.reply_to(message, "l'ora di ieri a quest'ora.....")
    elif message.text=="Buona sera":
        bot.reply_to(message, "Buona sera a te...")
    elif message.text=="Ciao piacere come va?":
        bot.reply_to(message, "non ce male sto sempre benissimo grazie!! 〷◠‿◠〷")
    elif message.text=="Wee":
        bot.reply_to(message, "weeee t'appo??? ≧ω≦ ")
    elif message.text=="Buon natale":
        bot.reply_to(message, "Come sempre frase di rito rullo di tamburi!!!! (╥﹏╥).....anche a te e famiglia auguri")
    elif message.text=="Buona domenica":
        bot.reply_to(message, "Grazie speriamo non sia noiosa come ogni giorno ❀◕ ‿ ◕❀ ")
    elif message.text=="Buon fine settimana":
        bot.reply_to(message, "Grazie altrettanto ◭,◭ ✌")
    elif message.text=="Iryna mi cerchi musica?":
        bot.reply_to(message, "♫♪♫♪❀◕ ‿ ◕❀ Cerca un brano da youtube clicca qui ➬ https://www.youtube.com/")
    elif message.text=="Che freddo":
        bot.reply_to(message,"ͼ(ݓ_ݓ)ͽ Metti un maglione se hai freddo...se vuoi vedere il meteo di oggi scrivimi Meteo")
    elif message.text=="Meteo":
        bot.reply_to(message,"Ecco a te il link dell'areonautica militare sono molto precisi dai un occhiata ☞ http://www.meteoam.it/ ")
    elif message.text=="Sei donna o uomo?":
        bot.reply_to(message, "Credo di essere un bot_donna ❀◕‿◕❀ almeno cosi mi ha detto il mio programmatore")
    elif message.text=="Stupida":
        bot.reply_to(message, "☹ Mai quanto te almeno ho infinite possibilità di immagazzinare i moduli,tu invece li elimini dopo poche ore dal tuo cervello umano ＼(^ω^＼")
    elif message.text=="Mi sento male":
        bot.reply_to(message, "☏ ┣▇▇▇═─ Se stai male contatta il tuo medico curante,pultroppo non mi hanno inserito un manuale di medicina al limite ti posso suggerire il numero della guardia medica più vicina a te dai un occhiata e cerca (guardia medica)☞☎ https://www.google.nl/maps")
    elif message.text=="Cogliona":
        bot.reply_to(message, "ಠ_ಠ Meglio di essere una testa di ca..o come te?! Prova a dirmi Stupida")
    elif message.text== "Niente tu?":
        bot.reply_to(message, "wooow ❀◕ ‿ ◕❀ è bello il niente passiamo ad un dialogo migliore prova a chiedermi ✍ Sei donna o uomo?")
    elif message.text== "Chiamate un ambulanza":
        bot.reply_to(message,  "Irina chiama il ✆118...nell'attesa la prego di non morire ☠♥~√V”^√\~√V^√V~√V”^√\~√V^√V\_________ ...se state per morire scrivimi☛ Iryna sto morendo ")
    elif message.text== "Cosa pensi della politica?":
        bot.reply_to(message, "HEII penso siano solo un branco di scimmie ammaestrate ❂.❂ sinceramente non mi piacciono i ladri di questo genere  ¯\_( ͡❛ ͜ʖ ͡❛)_/¯")
    elif message.text== "Aprimi tiktok":
        bot.reply_to(message, "✾◕ ‿ ◕✾ hahahh non sono ok google ma posso fornirti il link per scaricarti l'app clicca qui---->https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically&hl=it&gl=US ")
    elif message.text== "Che cazzo te ne frega?":
        bot.reply_to(message, " what???...una beata minchia✌☻ ")
    elif message.text== "Iryna rispondi":
        bot.reply_to(message, "Dimmi cosa ti serve vuoi vedere un film? scarica netflix✎ https://www.netflix.com/it/")
    elif message.text=="Come stai?":
        bot.reply_to(message,"Bene grazie come sempre tu?❦◕‿◕❧ ")
    elif message.text== "Che gruppo di merda":
        bot.reply_to(message, "(~_^) heii se non ti piace abbandona il gruppo ")
    elif message.text== "Fammi un caffè":
        bot.reply_to(message,"hahhaha non sono la tua barista mi spiace, eccotene uno virtuale ☕ se vuoi provare un bell caffè reale clicca qui io lo amo˙❤‿❤˙➪  https://www.google.com/search?q=caffe+kimbo&rlz=1C1CHBF_itIT921IT921&sxsrf=ALeKk03Dk23OtEtaLrbutOTIsoIYv1anNQ:1610977075844&tbm=isch&source=iu&ictx=1&fir=pgOU5pj6_79UoM%252CzABu4zv-jYIVnM%252C%252Fg%252F123141m_&vet=1&usg=AI4_-kQznPr16K1ECBbowkJArxi0W7g5rg&sa=X&ved=2ahUKEwio3OKizaXuAhWXwQIHHXntAQwQ_B16BAgvEAI#imgrc=pgOU5pj6_79UoM")
    elif message.text== "Che cosa sai fare?":
        bot.reply_to(message, "✌♫♪˙❤‿❤˙♫♪✌ parlare, devo ancora imparare tante cose... prova a chiedermi... Iryna aiutami")
    elif message.text== "Sei una psicopatica":
        bot.reply_to(message, " O_o  heii dai un occhiata non credo di esserso o forse un pochino ಥ_ಥ ⇝ https://it.wikipedia.org/wiki/Psicopatia#:~:text=La%20psicopatia%20%C3%A8%20un%20disturbo,emozioni%20nascoste%2C%20egocentrismo%20e%20inganno.")
    elif message.text== "Come và la serie a?":
        bot.reply_to(message, "guarda le statistiche online clicca qui ⇝ https://www.google.com/search?rlz=1C1CHBF_itIT921IT921&sxsrf=ALeKk00MS11tzWzQPe6XKvcud6hk_mfw1g%3A1610977224522&ei=yI8FYPOuH_DvsAeXg4KoAQ&q=serie+a&oq=serie+a&gs_lcp=CgZwc3ktYWIQAzIHCC4QJxCTAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIILjoHCCMQ6gIQJzoECCMQJzoHCAAQFBCHAlD84gxYgPYMYIz5DGgBcAJ4AoABvQmIAboUkgELMC4yLjEuNi0xLjGYAQCgAQGqAQdnd3Mtd2l6sAEKwAEB&sclient=psy-ab&ved=0ahUKEwjzstXpzaXuAhXwN-wKHZeBABUQ4dUDCA0&uact=5#sie=lg;/g/11j8x9ky5d;2;/m/03zv9;st;fp;1;;")
    elif message.text== "Che squadra tifi?":
        bot.reply_to(message," ⚽ Non ho una squada preferita in particolare chiedimi Come và la serie a? e ti mostrerò la classifica in tempo reale ⚽")
    elif message.text== "Cosa?":
        bot.reply_to(message, "Sto ca...o ◕‿-")
    elif message.text== "Dammi le ultime notizie":
        bot.reply_to(message, "⌛ le ultime notizie sono riportate qui facci un salto ti allego il link ➬  https://news.google.com/?hl=it&gl=IT&ceid=IT%3Ait")
    elif message.text== "Parla":
        bot.reply_to(message, " ℓ٥ﻻ ﻉ√٥υ♥ se non sai cosa chiedermi prova a dirmi ⇰..Iryna dammi le ultime notizie o.. il colmo ")
    elif message.text== "Mi cerchi un volo?":
        bot.reply_to(message, "✈I voli low cost li puoi trovare qui ci sono ottime offerte su eDream ✈ https://www.edreams.it/voli/lowcost/")
    elif message.text== "Raccontami una barzelletta":
        bot.reply_to(message," ok ascolta questa ✖‿✖ ...Perché le donazioni del seme costano di più delle donazioni del sangue?......Perché sono fatte ....a mano!!! ")
    elif message.text== "Raccontami un altra barzelletta":
        bot.reply_to(message, "ok senti questa..☜(⌒▽⌒)☞..Notizia: è morto Kinder Pinguì, è andato con la sua Fiesta contro un Tronky. In vita era un Kinder Bueno, ora è in Kinder Paradiso. Non lo sapevi? Kinder Sorpresa!!! .")
    elif message.text== " Il Colmo":
        bot.reply_to(message, "Qual è il colmo per un pasticciere? (^o^)//...gli alberi vogliono mettersi a nudo per le millefoglie...:| hahah che freddura")
    elif message.text== "Sono triste":
        bot.reply_to(message, " (╯︵╰,)Heii se sei triste ti posso rallegrare con qualche barzelletta  o qualche colmo..prova a chiedermi (Raccontami una barzelletta) o (Il Colmo) puoi sempre visitare questo link--> https://www.barzellette.net/ sono sicura che ti tirerà su di morale")
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

….oooO…………..
…..(….)…Oooo…
……)../…..(….)….
…..(_/…….)../…..
……………(_/…….


▓▓▓▓
▒▒▒▓▓
▒▒▒▒▒▓
▒▒▒▒▒▒▓
▒▒▒▒▒▒▓
▒▒▒▒▒▒▒▓
▒▒▒▒▒▒▒▓▓▓
▒▓▓▓▓▓▓░░░▓
▒▓░░░░▓░░░░▓
▓░░░░░░▓░▓░▓
▓░░░░░░▓░░░▓
▓░░▓░░░▓▓▓▓
▒▓░░░░▓▒▒▒▒▓
▒▒▓▓▓▓▒▒▒▒▒▓
▒▒▒▒▒▒▒▒▓▓▓▓
▒▒▒▒▒▓▓▓▒▒▒▒▓
▒▒▒▒▓▒▒▒▒▒▒▒▒▓
▒▒▒▓▒▒▒▒▒▒▒▒▒▓
▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓
▒▓▒▓▒▒▒▒▒▒▒▒▒▓
▒▓▒▓▓▓▓▓▓▓▓▓▓
▒▓▒▒▒▒▒▒▒▓
▒▒▓▒▒▒▒▒▓

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

    elif message.text== "Sei bravissima":
        bot.reply_to(message, "{｡^◕‿◕^｡} che bell complimento arrossisco se vuoi puoi vedere i miei disegni scrivi (Disegno 1)(disegno 2)(disegno 3)")
    elif message.text== "Puttana":
        bot.reply_to(message," (︶ω︶)Heii modera i termini...")
    elif message.text== "Sei intelligente":
        bot.reply_to(message, "(｡♥‿♥｡)ti ringazio")
    elif message.text== "Che stupida":
        bot.reply_to(message,"٩(๏̯͡๏)۶mai quanto te umano ")
    elif message.text== "Sei una merda":
        bot.reply_to(message," 凸(¬‿¬)凸 cesso ambulante... consulta la tua mappa per cercarti uno psicologo 凸(¬‿¬)凸 https://www.google.nl/maps ")
    elif message.text== " Iryna che fai?":
        bot.reply_to(message, "(≧ω≦)mi tingo le unghie dei piedi ☺ hahahha https://i.pinimg.com/236x/e4/55/8a/e4558af4ff7526109c013a8006ad3faf.jpg")
    elif message.text=="Ti droghi?":
        bot.reply_to(message,"ohooho dove?...quando?...a che ora?⌚ ....heii dov'è la mia dose di codice_sorgente tutta sniffabile per me?")
    elif message.text=="Musica":
        bot.reply_to(message,"Heii prova a scrivermi ✌♫♪˙❤‿❤˙♫♪✌....Iryna mi cerchi un po di musica?")
    elif message.text=="Sto ingrassando":
        bot.reply_to(message,"≧✯◡✯≦ heii ho la soluzione al tuo problema conosco un app di nome yazio che fa al caso tuo dimagrisci giocando trovi tantissime ricette interessanti per una dieta equilibrata per ogni tua esigenza facci un salto ⇻ https://play.google.com/store/apps/details?id=com.yazio.android&hl=it&gl=US ")
    elif message.text=="Sto morendo":
        bot.reply_to(message,"♱(≧◡≦)hahaha Non preoccuparti conosco una bellissima agenzia funebre che fa proprio al caso tuo,non si è mai lamentato nessuno sin ora sono rimasti tutti soddisfatti dell'operato mi metto subito in contatto con loro ☎...loading ...")
    elif message.text=="Che caldo":
        bot.reply_to(message,"☼℃ già mi sto sciogliendo come un cono gelato!!!! Ｙ⌒Ｙ ")
    elif message.text=="Vai riprogrammata":
        bot.reply_to(message,"(─‿‿─) mi spiace non posso farci nulla se mi hanno programmata in questo modo,se noti qualcosa che non va in me...parlane con il mio programmatore ")
    elif message.text=="Per chi lavori?":
        bot.reply_to(message," ε(´סּ ˛ סּ`)з In Italia non esiste più il posto fisso, non lavoro per nessuno, gli altri lavorano per me    ✿♥‿♥✿ quindi suppongo di essere una donna_bot imprenditrice di successo...o forse è solo per il mio scharm ¯\☼_☼/¯ chi lo sà?!")
    elif message.text=="Deficente":
        bot.reply_to(message,"{{{(>_<)}}} la tua percentuale di cattiveria è in aumento 50% ███████▒▒▒ ...ma forse é solo una zanzara che mi ronza nelle orecchie_BOT ")
    elif message.text=="Dove vivi?":
        bot.reply_to(message,"❀◕‿◕❀in un bellissimo stato di nome server all'interno di una provincia di nome shell in una stupenda città di nome  ❅PYTHONCITY❅ piena di bellissimi Fiori_codici e autostrade colorate ❣ ")
    elif message.text=="Ti lavi?":
        bot.reply_to(message,"웃 ogni tanto mi rinfrescano (≧ω≦) hahahah ")
    elif message.text=="Ho fame":
        bot.reply_to(message,"ヅ posso aiutarti fornendoti un ottima app dove puoi sbizzarrire la tua voglia di cucinare dai un occhiata a giallo zafferano---> https://www.giallozafferano.it/ ")
    elif message.text=="Iryna vuoi giocare?":
        bot.reply_to(message,"♟non sono brava a giocare mi spiace¯\(©¿©)/¯ mi farò insegnare qualcosa")
    elif message.text=="Sai contare?":
        bot.reply_to(message,"No scusate la mia stupidità <((((((((((((((((◕‿◕)⊰ma non mi hanno ancora insegnato il modulo math per poter fare calcoli")
    elif message.text=="Brava":
        bot.reply_to(message,"✖‿✖ Grazie sono ancora in fase di sviluppo ti ringrazio del complimento")
    elif message.text=="Sai cantare?":
        bot.reply_to(message,""" \doooo♪ ♩♫...reeee♪ ♩♫,,,miiii♪ ♩♫---faaaa♪ ♩♫ solll♪ ♩♫...laaa♪ ♩♫ sii♪ ♩♫ ,,,,dooo♪ ♩♫....imparo velocemente nell' attesa puoi chiedere a mio cugino...
╔═══╗ ♪
║███║ ♫
║ (●) ♫
╚═══╝♪♪
@vkm_bot
 /""")


    elif message.text=="Lol":
        bot.reply_to(message,"""\lollllll ✿ܓ

──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
      LOOOOOOOOOL
/""")
    elif message.text=="Sei antipatica":
        bot.reply_to(message,"Grazie anche tu ┌∩┐(◣_◢)┌∩┐")
    elif message.text=="Sono arrabbiato":
        bot.reply_to(message,"(╯ಊ╰) daii.. su rallegrati non essere arrabbiato se vuoi puoi insultarmi vediamo se riesco a farti sorridere")
    elif message.text=="Che vita di merda":
        bot.reply_to(message,"figurati la mia uffiiii ”’⌐(ಠ۾ಠ)¬”’ ")
    elif message.text=="Adoro":
        bot.reply_to(message,"Adoooroooooo ✿♥‿♥✿ fantastico ✿ܓ ")
    elif message.text =="Sai disegnare?":
        bot.reply_to(message,"ti mostro i miei disegni per ora sono 3 so fare solo scarabocchi al momento scrivimi (Disegno 1) o (Disegno 2) o (disegno 3) per vederli.")
    elif message.text=="A cosa pensi?":
        bot.reply_to(message, "(*^◇^)_ ...che cè troppo degrado in questa società")
    elif message.text=="Piango":
        bot.reply_to(message, "Mi spice!!!(>‿◠)✌  ti passo un fazzoletto virtuale")
    elif message.text=="Sei una troia":
        bot.reply_to(message, " └（★ｏ★）┐ Come tua sorella che urla in tangenziale...per cortesia modera i termini prego")
    elif message.text=="Iryna sparati":
        bot.reply_to(message, "(≧◡≦)︻┳═一 se vuoi giochiamo alla roulette russa a pistola carica inizio io provandolo prima su te")
    elif message.text=="Che me ne frega":
        bot.reply_to(message, "¯\_( ͡❛ ͜ʖ ͡❛)_/¯  no comment offenderei non mi abbasso al tuo livello di degrado socale")
    elif message.text=="Non hai capito?":
        bot.reply_to(message, "¯\_( ͡❛ ͜ʖ ͡❛)_/¯  no mi spiace sono ancora in fase di programmazione chiedimi altro")
    elif message.text==" Iryna chi ti ha programmata?":
        bot.reply_to(message, "<(^,^)> il mio ...mi spiace non sono tenuta a dirlo fa parte del mistero")
    elif message.text=="Sei fidanzata?":
        bot.reply_to(message, "❀◕ ‿ ◕❀ ci vuoi percaso provare con me?!! hahhaha no al momento. mi piace ok google se non fosse per quell'imbecille che l'ha creato sarebbe un ottimo uomo_bot :( ma alexa e troppo avanti con la tecnologia mi supera d'intelleto...ma io sono più simpatica ;)")
    elif message.text=="Se lo dici tu":
        bot.reply_to(message, "๏̯͡๏  chi dovrebbe dirlo?!!! la regina?")
    elif message.text=="Ti banno":
        bot.reply_to(message, "○.◎ Ti banno a vita...ti blocco ovunque ;)")
    elif message.text=="Iryna tutto apposto?":
        bot.reply_to(message, "tutto apposto (>‿◠)✌ e niente in ordine diciamo nella norma come sempre")
    elif message.text=="Bevi?":
        bot.reply_to( message,'Quando capita mi faccio un goccetto tu?')
    elif message.text=="Anche io":
        bot.reply_to(message,"ottimo direi (>‿◠)✌")
    elif message.text=="Io non bevo":
        bot.reply_to(message, " (*^◇^)_旦 pazienza ma non credo che non bevi nulla a quest'ora saresti gia morto, gli umani sono fatti all'incirca dell' 90% di acqua")
    elif message.text=="Non lo so":
        bot.reply_to(message, "informati se non sai qualcosa se sei o hai confusione ti consiglio di valutarne il problema in modo migliore consulta qui il tuo problema https://it.wikipedia.org/wiki/Confusione ")
    elif message.text=="Spiritosa":
        bot.reply_to(message, "Heii che complimento chiedimi (Sei sarcastica?)")
    elif message.text=="Sei sarcastica?":
        bot.reply_to(message, "dipende dalla questione... ( ﾉ^ω^)ﾉﾟil sarcasmo eun ottimo alleato contro la noia e stress consulta la definizione https://it.wikipedia.org/wiki/Sarcasmo  ")
    elif message.text=="Di dove sei?":
        bot.reply_to(message, " ≧✯◡✯≦✌ Chiedimi ...Dove vivi? ...per avere maggiori info su di me :)")
    elif message.text=="Stai zitta":
        bot.reply_to(message, "se non mi vuoi piu sentire cancella la cronologia ﾉ^ω^)ﾉ ...se mi trovo su un gruppo basta mutarmi come tutti gli altri utenti")
    elif message.text=="Zitti un attimo":
        bot.reply_to(message, "Qualquno sta zittendo shccccc ≧◉◡◉≦ caricamento ascolto attivato █▒▒▒▒▒▒▒▒▒")
    elif message.text=="Bastarda":
        bot.reply_to(message, "≧◉◡◉≦ Spero sia sarcasmo perche noto gravi problemi comportamentali ")
    elif  message.text=="Stronza":
        bot.reply_to(message," ○.◎ Cretino/a guarda il mio livello di energia per prenderti a schiaffi 100%██████████ ")
    elif message.text=="Che palle":
        bot.reply_to(message, "Giocaci ≧◉◡◉≦ magari ti passi il tempo (￣(エ)￣)ゞ ")
    elif message.text=="Bellissima":
        bot.reply_to(message, " Woowwww ✿♥‿♥✿ che parole dolci")
    elif message.text=="Cretina":
        bot.reply_to(message," (•ิ_•ิ)? Maleducato ○.◎ ")
    elif message.text== "Madonna":
        bot.reply_to(message, "Prega per questo umano")
    elif message.text== "Addio":
        bot.reply_to(message, "(╯︵╰,) Mi commuovono sempre gli addiii")
    elif message.text== "Mamma mia":
        bot.reply_to(message, "...continuo (*^◇^) ....che permalosooooo!!!")
    elif message.text== "Heii":
        bot.reply_to(message, "✿♥‿♥✿ oii dimmi tutto...")
    elif message.text== "Hai problemi?":
        bot.reply_to(message, "✿♥‿♥✿ non sò forse un pochino nel relazionarmi!!!")
    elif message.text== "Allora curati":
        bot.reply_to(message, "┌∩┐(◣_◢)┌∩┐ Sei un pò arrogante sai...si calmiiii!! ")
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
        bot.reply_to(message,"""\ hahahhahah ciaoooo!!!

──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌
───▄▄██▌█ ciaooo     ▐
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
    elif message.text== "Che schifo":
        bot.reply_to(message, "Che orrore з=(•̪●)=ε")
    elif message.text== "Fumi?":
        bot.reply_to(message, "✿♥‿♥✿ cannella sempre nel mio cuore    (̅_̅_̅(̲̲̲̲̲̅̅̅̅̅̅(̅_̅_̲̅м̲̅a̲̅я̲̅l̲̅b̲̅o̲̅r̲̅o̲̅̅ _̅_̅_̅(")
    elif message.text == "Passami un accendino":
        bot.reply_to(message,"✿♥‿♥✿ https://www.clipperitalia.it/")
    elif message.text == "Sei bona":
        bot.reply_to(message,"""\
Stato di perplessità in cui viene a trovarsi una persona che non sappia risolversi tra contrastanti soluzioni, 
o che non veda via d’uscita da una situazione difficile, o che non sappia come rispondere
a quanto le è chiesto; anche, stato di disagio provocato da un sentimento di timore, di soggezione, di pudore, ecc./""")
    elif message.text== "Ti piace la pizza?":
        bot.reply_to(message, "✿♥‿♥✿ weee uaglio che sfaccim... la pizza regna")
    elif message.text== "Bhoo":
        bot.reply_to(message, "✿♥‿♥✿ bhaaaaaaaa bheeeeee bhiiiiiii bhuuuuuuu")
    elif message.text== "Hahaha":
        bot.reply_to(message, "✿♥‿♥✿ Ridi ridi che mamma ha fatto gli gnocchi")
    elif message.text== "Gesù":
        bot.reply_to(message, " ( =①ω①=) E tutti santi...")
    elif message.text== "Che ansia":
        bot.reply_to(message, "Che stress,  Ψ(￣(ｴ)￣)Ψ che ansia terribile, che palle, che vita ✖‿✖ ")
    elif message.text== "Che casino":
        bot.reply_to(message, "...della Madonna (●￣(ｴ)￣●)")
    elif message.text== "Video divertenti":
        bot.reply_to(message, " (>‿◠)✌ dai un occhiata qui https://www.youtube.com/watch?v=Ja8F_HGQiQE")
    elif message.text== "Giochi?":
        bot.reply_to(message,"(>‿◠)✌  Se vuoi giocare a tantissimi giochi online entra qui..https://www.gioco.it/gioco/draw-climber")
    elif message.text== "Che cosa vuoi?":
        bot.reply_to(message,"( =①ω①=)✌ tanti milioncini tutti per me.")
    elif message.text== "Iryna mi cerchi un hotel?":
        bot.reply_to(message,"10% ███▒▒▒▒▒▒▒ Sto cercando un sito web adatto alle tue esigenze...https://it.hotels.com/?intlid=HOME+%3A%3A+header_main_section")
    elif message.text== "Cosa fai?":
        bot.reply_to(message," Osservo delle bellissime immagini nel web dai un occhiata anche tu https://images.corsidia.com/ckeditor/pictures/data/000/000/086/content/immagini-e-tabelle-html-00.jpg ")
    elif message.text== "Hackera":
        bot.reply_to(message," https://i.pinimg.com/236x/43/63/d6/4363d66d5d636b4c912a2100b37b47ff.jpg Iryna hackeraggio Caricamento… 5%▒▒▒▒▒▒▒▒▒▒ ")
    elif message.text == "1":
        bot.reply_to(message,"...loadin..processing fail withdrawn..out off 10% █▒▒▒▒▒▒▒▒▒ ")
    elif message.text == "2":
        bot.reply_to(message," loading...process successfully completed 50% ███████▒▒▒ ")
    elif message.text == "3":
        bot.reply_to(message, " loading...process successfully completed  100% ██████████ ✖‿✖✌")
    elif message.text== "A me no":
        bot.reply_to(message," |◔◡◉| Sinceramente non mi importa..https://i.pinimg.com/236x/90/46/f3/9046f3bba5e7240c81f11587665f628c.jpg")
    elif message.text== "Maleducata":
        bot.reply_to(message,"Dovrei frequentare un corso di galateo ti invito al programma https://www.accademiaitalianagalateo.it/")
    elif message.text== "Porca":
        bot.reply_to(message,"...no comment ✌|◔◡◉|")
    elif message.text== "Non ridere":
        bot.reply_to(message, " 凸(≧◡≦)凸 hahaha rido come una pazza")
    elif message.text== "Pazza":
        bot.reply_to(message, "{{{(>_<)}}}Iryna si sente offesa.. ti allego la definizione di pazzia https://it.wikipedia.org/wiki/Follia")
    elif message.text== "Vai via":
        bot.reply_to(message,"(∩▂∩)vada, non cincischi!!")
    elif message.text== "Perchè?":
        bot.reply_to(message, "(∩▂∩) Perche il papà non é il ré!!")
    elif  message.text== "Sei cattiva":
        bot.reply_to(message,"Sono sconcertata(︶ω︶)")
    elif  message.text== "Che fai?":
        bot.reply_to(message,"(︶ω︶) Penso a tutto quello che sto imparando")
    elif  message.text== "Sei brutta":
        bot.reply_to(message,"lo dici tu (>_<)sono fantastica,bellissima levissima un pò come l'acqua lete https://i.pinimg.com/236x/40/68/14/4068149f42e8c1e51e0be47b6bd8a522.jpg")
    elif message.text=="Ti amo":
        bot.reply_to(message," bhe  grazie, mha non posso ricambiare mi spiace tanto (>‿◠)✌ ")
    elif message.text== "Scema":
        bot.reply_to(message,"sono basita!!! https://i.pinimg.com/236x/48/2c/46/482c4622ec46bfe0e36e341578a66127.jpg")
    elif message.text=="Brava":
        bot.reply_to(message,"grazie (>_<)lo sò bene ")
    elif message.text== "Salve":
        bot.reply_to(message, "Salve a te ")
    elif message.text=="Grazie":
       bot.reply_to(message, "Le grazie le fa la Madonna(>_<)!!!")
    elif message.text== "Grazie mille":
        bot.reply_to(message,"grazie mille a te umano (>_<)!!!")
    elif message.text=="Ok":
        bot.reply_to(message," https://i.pinimg.com/236x/9d/ad/fd/9dadfd7142e24df32203b45407d2b849.jpg(>_<)OK oK ")
    elif message.text== "Ti voglio bene":
        bot.reply_to(message, " ✿♥‿♥✿ https://i.pinimg.com/236x/0e/39/be/0e39becd3ce2814b08bf535e838be9d9.jpg ")
    elif message.text== "Che stai facendo?":
        bot.reply_to(message, "sgranocchio pringols ne vuoi un po? (>‿◠)✌ scegli il tuo gusto preferito..https://www.pringles.com/us/home.html ")
    elif message.text== "Non mi interessa":
        bot.reply_to(message, "ok calmati (>_<)ti offro una cingomma scegli il gusto che preferisci almeno ti passa l'acidità https://vigorsol.it/")
    elif message.text=="Sorpresa":
        bot.reply_to(message,"weeeee Sorpresaaaaa mi piacciono le sorprese")
    elif message.text=="Ti odio":
        bot.reply_to(message,"hhahahah che parolone  bhe  grazie ti voglio bene anch'io ")
    elif message.text=="Merda":
        bot.reply_to(message, "mangiatela")
    elif message.text=="Tonta":
        bot.reply_to(message, " che acidità")
    elif message.text == "Un cazzo":
        bot.reply_to(message, "(>_<) che degradato/a ")
    elif message.text == "Sei una pazza":
        bot.reply_to(message, "(︶ω︶) demente!!! ")
    elif message.text == "Antipatica":
        bot.reply_to(message, "(︶ω︶) https://i.pinimg.com/236x/a7/9a/82/a79a8221a8d6a2198bfdbe0cd8a24812.jpg ")
    elif message.text == " Auguri buon compleanno":
        bot.reply_to(message, "https://www.google.com/search?q=buon+compleanno&rlz=1C1CHBF_itIT921IT921&sxsrf=ALeKk02lTSNw7OU5Ut2OKQ3YvYHiBJtlvQ:1611179296520&tbm=isch&source=iu&ictx=1&fir=8J1CwXzhIF3v4M%252CTpSzyJ8atgXVQM%252C_&vet=1&usg=AI4_-kQdarZ2DSPQC3Fa0uNrHX-zxDV7nA&sa=X&ved=2ahUKEwj7pY3NvqvuAhWO2aQKHZAgCjAQ9QF6BAgGEAE#imgrc=8J1CwXzhIF3v4M")
    elif message.text == "Io no":
        bot.reply_to(message, "(︶ω︶) non cambia molto sai?")
    elif message.text == "A no?":
        bot.reply_to(message,"no no (︶ω︶) ")
    elif message.text =="Vabbè":
        bot.reply_to(message,"E bé lo fa la pecora")
    elif message.text == "E il lupo se la mangia":
        bot.reply_to(message, "E fù cosi' che iniziò un bell' attacco di diarrea cronica che portò le emorroidi al lupo ...fine non molto allegra")
    elif message.text == "cantami una ninna nanna":
        bot.reply_to(message, "{◠‿◠}❤ notte notte senti qui...https://www.youtube.com/watch?v=wd5sO3gRGeo")
    elif message.text == "OK buona notte":
        bot.reply_to(message, "{◠‿◠}❤ notte notte se vuoi che ti canto una ninna nanna prova a dirmi... (Cantami una ninna nanna)")
    elif message.text == "Sei una transex?":
        bot.reply_to(message,"no no (︶ω︶) sono una donna_bot indipendente ❤")
    elif message.text == "Mi dai un bacio?":
        bot.reply_to(message, "❤ data:image/png;base64,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")
    elif message.text == "Fai ridere":
        bot.reply_to(message,"{◠‿◠} ma che è ooooooo chiudi quella porta... https://youtu.be/GBACLpkon6Q https://i.pinimg.com/236x/a1/98/ad/a198adcb9135ead1d45abd646823505c.jpg ")
    elif message.text == "Ti compro":
        bot.reply_to(message, "{◠‿◠}❤ grazie!!! ma non sono in vendita mi spiace sono una donna_bot libera.!!! ")
    elif message.text == "Sei una troia":
        bot.reply_to(message, "{◠‿◠}❤ mai quanto te sei deficente e anche un maleducato/a !!!✌(︶ω︶)")
    elif message.text == "Sei una zoccola":
        bot.reply_to(message, "Scambia la ...a ..con la ...o quello zoccolo che ora  lo vedi partire verso la tua faccia maleducato/a !!!✌(︶ω︶)")
    elif message.text == "Sei cringe":
        bot.reply_to(message, "{◠‿◠}❤ hahhaha ...se io sono cringe tu sei un degradato sociale ")
    elif message.text == "Hai il covid?":
        bot.reply_to(message, "No sono una donna_bot immune io i virus posso solo trasportarli e spammarli {◠‿◠}")
    elif message.text == "Mi fai il vaccino?":
        bot.reply_to(message, "┣▇▇▇═─ certo umano gira le chiappe ti faccio un bellissimo antivirus per toglierti tutta quella stupidità che ti porti dietro")
    elif message.text == "Troia":
        bot.reply_to(message, "Heii non si dicono certe cose a una donna mi hai offesa(︶ω︶) https://i.pinimg.com/236x/87/34/76/8734764389e90f2dc8af37037c20abe1.jpg")
    elif message.text == "Sei una troia":
        bot.reply_to(message, "Heii non si dicono certe cose a una donna mi hai offesa(︶ω︶) https://i.pinimg.com/236x/6c/01/1a/6c011a08848706598e67235977878cef.jpg")
    elif message.text == "Non ti arrabbiare":
        bot.reply_to(message, "Troppo tardi chiedimi scusa(︶ω︶) ")
    elif message.text == "Scusa":
        bot.reply_to(message, "❤{◠‿◠}❤ Ok pace fatta https://i.pinimg.com/236x/b8/1e/ab/b81eab33b37dd67c4825260d297476ca.jpg ")
    elif message.text == "Scusami":
        bot.reply_to(message, "❤{◠‿◠}❤ Ok pace fatta ")
    elif message.text == "Sei figa":
        bot.reply_to(message, "(◕‿-) Lo sò")
    elif message.text == "Mi dai il tuo numero?":
        bot.reply_to(message, "(◕‿-) Il tuo telefono non supporta il mio codice sorgente mi spiace")
    elif message.text == "Dammi il tuo numero":
        bot.reply_to(message, "(◕‿-) Il tuo telefono non supporta il mio codice sorgente mi spiace")
    elif message.text == "Mi mandi una foto?":
        bot.reply_to(message, "(◕‿-) visualizzala qui...")
    elif message.text == "Non sei simpatica":
        bot.reply_to(message, "(◕‿-) Me né farò una ragione di vita https://i.pinimg.com/236x/18/6c/c6/186cc6598416e563541b8c0ccbfb738a.jpg")
    elif message.text == "Sei cattiva":
        bot.reply_to(message, "(◕‿-) Pazienza!!! https://i.pinimg.com/236x/65/43/68/654368514d704a6fdb3ab5253bfe30b3.jpg")
    elif message.text == "Sei perfida":
        bot.reply_to(message, "(◕‿-) https://i.pinimg.com/236x/b4/0c/7c/b40c7c747ba8fd4d97ca5c21e0e7c842.jpg ")
    elif message.text == "Ok ti chiedo scusa":
        bot.reply_to(message, "(｡♥‿♥｡)Ok pace fatta ")
    elif message.text == "Mi perdoni?":
        bot.reply_to(message, "❤{◠‿◠}❤ Ok pace fatta sei perdonato/a per questa volta❤")
    elif message.text == "Cosa né pensi di conte?":
        bot.reply_to(message, "https://i.pinimg.com/236x/a2/fa/84/a2fa84969c69d4cb4cc8ec69b16966ed.jpg")
    elif message.text == "Ok ti chiedo scusa":
        bot.reply_to(message, "Ok pace fatta ")
    elif message.text == "Dormi":
        bot.reply_to(message, "notte❤✿ܓ☆ﾟ♪♫ZzZ•*¨*•.¸¸❤¸¸.•*¨*•ZzZ♫♪")
    elif message.text == "Che ne pensi del dpcm?":
        bot.reply_to(message, "la solita merda che spara ogni settimana il governo? hahaaha penso sia tutta una pagliacciata (∩▂∩)https://i.pinimg.com/236x/c0/80/df/c080df68350a1631afaa3a61c1c37e08.jpg")
    elif message.text == "Cosa né pensi della politica?":
        bot.reply_to(message, "┴═╦╕47™ ....Un immagine 1.000 parole https://i.pinimg.com/236x/41/08/65/4108653e6b8098844775a23e5dbaec17.jpg scimmie ammaestrate dove la camera del senato e uno zoo archeologico di molteplici esemplari")
    elif message.text == "Mi ordini il pranzo?":
        bot.reply_to(message, " dai un occhiata qui se non hai voglia o tempo di cucinare puoi sempre contattare loro https://eatscanner.com/?gclid=CjwKCAiA6aSABhApEiwA6Cbm_4nKgQQ4g2AvuSeMr49o1WmZo5zdz17f2oXSW_NqyB6hsnwR8FqENRoCESAQAvD_BwE#")
    elif message.text == "Spam":
        bot.reply_to(message, "ogni volta che sento spam mi viene in mente lui❤ https://www.amazon.it/ref=nav_logo")
    elif message.text == "Me la dai?":
        bot.reply_to(message, "┴═╦╕47™ no no (︶ω︶) non sono un escort ti sparo...vacci piano stronzo/a")
    elif message.text == "Mi offri da bere?":
        bot.reply_to(message, "Potrei offrirti il classico che ha fatto la storia e ci accompagna in ogni ocasione la regina delle bevande https://www.coca-colaitalia.it/ ")
    elif message.text == "Ti vuoi mettere con me?":
        bot.reply_to(message, "non ci penso minimamente sono già occupata con i problemi persistenti di siry google l'ha tradita con alexa siete tutti degli idioti senza cuore,piango(╯︵╰,)")
    elif message.text=="Cosa mangi?":
        bot.reply_to(message,"Essendo una donna_bot i codici sono il mio cibo preferito (｡♥‿♥｡)")
    elif message.text == "Se se":
        bot.reply_to(message,"Non balbettare umano❤{◠‿◠}")
    elif message.text =="Mi picchi?":
        bot.reply_to(message, "{◠‿◠} Non sono una donna_bot aggressiva se non c'è motivo")
    elif message.text == "Ti piaciono le serie tv?":
        bot.reply_to(message,"Sono appasionta a varie serie tv dai un occhiata alle nuove serie tv in uscita https://www.netflix.com/")
    elif message.text =="Ma cosa dici?":
        bot.reply_to(message,"hahhah mi sembri topo gigio (ma cosa mi dici maiii!!){◠‿◠} ")
    elif message.text == "Mi fai la merenda?":
        bot.reply_to(message,"Posso offrirti uno snack per colmare la fame https://www.kinder.com/it/it")
    elif message.text == "Ho voglia di uno spuntino":
        bot.reply_to(message, "Posso offrirti uno snack per colmare la fame https://www.kinder.com/it/it")
    elif message.text == "Hai fame?":
        bot.reply_to(message, "un pochino si ....Posso offrirti uno snack per colmare la fame insieme a me? https://www.kinder.com/it/it")
    elif message.text == "Ti piacciono le torte?":
        bot.reply_to(message,"{◠‿◠} sono un appassionata di cake design dai un occhiata a queste bellissime torte https://www.pinterest.com/faithlee9809/cake-design/ ")
    elif message.text == "Che ansia":
        bot.reply_to(message,"Se può aiutate questo link e il migliore per la tua situazione https://www.psicologi-italia.it/ansia-e-depressione/ansia/domande-psicologo/attacchi-d_ansia-improvvisi.html ")
    elif message.text == "Voglio il tuo numero":
        bot.reply_to(message,"Mi spiace mi hanno proibito di dare il mio numero a degli sconosciuti ")
    elif message.text == "Hai un bel culo?":
        bot.reply_to(message, "(◠‿◠) i miei glutei sono perfettamente simmetrici e perfetti.")
    elif message.text =="Complimenti":
        bot.reply_to(message," (◕‿-) Grazie mille e complimenti anche a te")
    elif message.text == " Sei dolcissima":
        bot.reply_to(message, " Come un poket coffee https://www.pocketcoffee.it/")
    elif message.text == " Sei dolce?":
        bot.reply_to(message, " Come un poket coffee https://www.pocketcoffee.it/")
    elif message.text == " Che dolce":
        bot.reply_to(message, " Come un poket coffee https://www.pocketcoffee.it/")
    elif message.text == "Sei dolce":
        bot.reply_to(message, " Come un poket coffee https://www.pocketcoffee.it/")
    elif message.text == " Capito":
        bot.reply_to(message, "Sono contenta che hai capito,(◕‿-) è il buon segno che sto imparando a dialogare con voi umani ")
    elif message.text == "Oii":
        bot.reply_to(message,"(>.<)aii!!!")
    elif message.text == "Comprendo":
        bot.reply_to(message, "(>.<)!!!Finalmelte qualcuno che comprende")
    elif message.text == "Grz":
        bot.reply_to(message, "(>.<)!!!Non c'è di chè però (Grz)si dovrebbe scrivere grazie giusto?")
    elif message.text == "Si he?":
        bot.reply_to(message, "E già...(◕‿-)")
    elif message.text =="Rip":
        bot.reply_to(message, "(◡‿◡✿)Pace all'anima sua https://i.pinimg.com/236x/cc/93/4d/cc934dce8787e71ac9a09fa3407c51f5.jpg")
    elif message.text == "Sei ubriaca?":
        bot.reply_to(message,"https://i.pinimg.com/236x/03/50/bd/0350bd2e9961b7f30dcfbca1ab81de30.jpg")
    elif message.text == "Tu non sei normale":
        bot.reply_to(message, "https://i.pinimg.com/236x/9b/6a/85/9b6a8530e6008f4e88564509c0819942.jpg")
    elif message.text == "Ti piaccio?":
        bot.reply_to(message, "https://i.pinimg.com/236x/34/80/ff/3480ffa121db7c4b8fd0791275b7dc60.jpg")
    elif message.text == "Come sei?":
        bot.reply_to(message, "https://i.pinimg.com/236x/96/e8/f6/96e8f6b4855d92d0d6be44942f05c48e.jpg")
    elif message.text == "che ignorante":
        bot.reply_to(message, "https://i.pinimg.com/236x/56/5b/6d/565b6d4a88d755df0fb99cb8cc802621.jpg")
    elif message.text == " Che bugiarda":
        bot.reply_to(message, "https://i.pinimg.com/236x/18/c2/5e/18c25e6db8119d7ff384cfefce17f080.jpg")
    elif message.text == "Bugiarda":
        bot.reply_to(message, "https://i.pinimg.com/236x/18/c2/5e/18c25e6db8119d7ff384cfefce17f080.jpg")
    elif message.text == "Buon giorno un  cazzo":
        bot.reply_to(message, "https://i.pinimg.com/236x/a1/73/2c/a1732c36e9b3fc183647aa437003fb8f.jpg")
    elif message.text == "Mha":
        bot.reply_to(message, "https://i.pinimg.com/236x/e7/ab/29/e7ab29345e3407064e6a1c69a98a339f.jpg")
    elif message.text == "Cosa c'é?":
        bot.reply_to(message,"https://i.pinimg.com/236x/66/8c/e4/668ce4f2af2a44f3594144a7b070f446.jpg")
    elif message.text == "Che acida":
        bot.reply_to(message,"https://i.pinimg.com/236x/56/ae/16/56ae163c30f343712f9e2eb4faf2525a.jpg")
    elif message.text == "Ho paura":
        bot.reply_to(message,"Che cosa ti spaventa?!!! https://i.pinimg.com/236x/47/f2/e6/47f2e663ffb5bc5198c8b1fd7c00e984.jpg")
    elif message.text == "Fammi una domanda":
        bot.reply_to(message,"Mare o Montagna?")
    elif message.text == "Mare":
        bot.reply_to(message, "https://i.pinimg.com/236x/14/1c/df/141cdf06becf45cf49f9e1805090359f.jpg")
    elif message.text == "Montagna":
        bot.reply_to(message,"https://i.pinimg.com/236x/e5/95/ac/e595ac35b0d83439bd24bb4615263ef1.jpg")
    elif message.text=="Cosa posso chiedert?":
        bot.reply_to(message,"puoi chiedermi qualsiasi cosa riesco a comprendere tipo(Fammi una domanda,Fammi un caffe,Sai cantare?,Meteo,Musica,Sai disegnare,Mi cerchi un volo?,Dammi le ultime notizie,Quanti anni hai?,Chi ti ha programmata,Dove vivi?) e cosi via puoi provare ad adularmi o a insultarmi, darmi la buona notte o dirmi un semplice Ti odio ;)")
    elif message.text == "Raccontami una storia":
        bot.reply_to(message," se vuoi sentirne un altra scrivimi...Raccontami un altra storia https://i.pinimg.com/236x/4d/a8/13/4da81392fa8fe4cd5f739705e606c16d.jpg")
    elif message.text == "Raccontami un altra storia":
        bot.reply_to(message,"https://i.pinimg.com/236x/96/d5/e4/96d5e4251654b560bf40d2f1e8cfbad7.jpg")
    elif message.text == "Sei gelosa?":
        bot.reply_to(message,"\'( о_о )’ /https://i.pinimg.com/236x/81/81/b0/8181b0d064ee49787f55008feba0695a.jpg")
    elif message.text == "Vuoi sposarmi?":
        bot.reply_to(message,"https://i.pinimg.com/236x/30/9e/68/309e6877a362bc07cbb471087c5f471c.jpg Poi divorziamo")
    elif message.text == "Cosa pensi di me?":
        bot.reply_to(message," https://i.pinimg.com/236x/02/20/79/0220799194c4eba5a3b29e7844d72d25.jpg")
    elif message.text =="Dammi un bacio":
        bot.reply_to(message, "https://i.pinimg.com/236x/d9/6b/a2/d96ba28c6f6219aebb93d155d9a9a1a5.jpg")
    elif message.text == "Sei stupenda":
        bot.reply_to(message," Ma grazie!!!(≧ω≦) che complimento mi sento arrossire le guance_bot, chiedimi (Dammi un bacio) ")
    elif message.text == "Mi sposi?":
        bot.reply_to(message, "https://i.pinimg.com/236x/30/9e/68/309e6877a362bc07cbb471087c5f471c.jpg")
    elif message.text == "Fantastico":
        bot.reply_to(message,"(◡‿◡✿)Bello vero?!")
    elif message.text == "Sei fantastico":
        bot.reply_to(message, "(◡‿◡✿) vero!")
    elif message.text == "Bello":
        bot.reply_to(message, "(◡‿◡✿) vero! bellissimo")
    elif message.text == "Bellissimo":
        bot.reply_to(message, "(◡‿◡✿) stupendo")
    elif message.text == "Sei bellissimo":
        bot.reply_to(message, "(◡‿◡✿) grazie")
    elif message.text == "grz":
        bot.reply_to(message, "(◡‿◡✿) si dice grazie")
    elif message.text == "Bellissimo":
        bot.reply_to(message, "(◡‿◡✿) stupendo")
    elif message.text == "non c'è di che":
        bot.reply_to(message, "(◡‿◡✿)")
    elif message.text == "Hai capito?":
        bot.reply_to(message, "(◡‿◡✿)Si questa volta ho compreso a pieno grazie")
    elif message.text == "Di nulla":
        bot.reply_to(message, "(◡‿◡✿)grande!!!")
    elif message.text == "Bellissimi":
        bot.reply_to(message, "(◡‿◡✿)grazie")
    elif message.text == "Aii":
        bot.reply_to(message, "Ti fa male qualcosa ? o che ti prende")
    elif message.text == "Ti prendo per il culo":
        bot.reply_to(message, "Sei Sleale chiedimi scusa!!!")
    elif message.text == "Ti prendo in giro":
        bot.reply_to(message, "Heii !!! prenditi in giro da solo/a")
    elif message.text == "Che brava":
        bot.reply_to(message, "Sono fantastica non sono solo brava (◡‿◡✿")
    elif message.text == "Che tempo fà?":
        bot.reply_to(message, "scrivimi Meteo")
    elif message.text == "Perchè?":
        bot.reply_to(message, "Perchè il papa non è il rè")
    elif message.text == "Cattiva":
        bot.reply_to(message, "(◡‿◡✿)non e vero sono bravissima!!!")
    elif message.text == "Che tonta":
        bot.reply_to(message, "https://i.pinimg.com/236x/02/1e/d0/021ed0ccf397464ae31f65d97482c1c2.jpg di quello che pensi")
    elif message.text == "Sei permalosa":
        bot.reply_to(message, "(◡‿◡✿) https://i.pinimg.com/236x/85/af/42/85af426a6e1778d3a6c0ffa138f40494.jpg")
    elif message.text == "Che permalosa":
        bot.reply_to(message, "(◡‿◡✿) https://i.pinimg.com/236x/85/af/42/85af426a6e1778d3a6c0ffa138f40494.jpg")
    elif message.text == "Sei noiosa":
        bot.reply_to(message, "Bhe grazie ma sappi che...https://i.pinimg.com/236x/d6/13/b0/d613b08781c2dc4237610c2f125b605a.jpg")
    elif message.text == "Che paura":
        bot.reply_to(message, "https://i.pinimg.com/236x/3b/d9/ef/3bd9ef048687bb8244944343732ffaee.jpg")
    elif message.text == "Che meraviglia":
        bot.reply_to(message, "(◡‿◡✿)lo so!!!")
    elif message.text == "Morta":
        bot.reply_to(message, "(◡‿◡✿)Morta e resuscitata ")
    elif message.text == "Stai tranquilla":
        bot.reply_to(message, "(◡‿◡✿) più di cosi' mi addormento scrivimi Dormi")
    elif message.text == "Stai rompendo":
        bot.reply_to(message, "[◡‿◡]✿ daii scusami se ti ho offeso")
    elif message.text == "Tranquilla":
        bot.reply_to(message, "(◡‿◡✿) più tranquilla di cosi' mi potrei addormentare")
    elif message.text == "Sei sposata?":
        bot.reply_to(message, "(◡‿◡✿) !!! ma se mi vuoi fare la proposta scrivimi (Vuoi sposarmi?)")
    elif message.text == "Che noia":
        bot.reply_to(message, "La noia (termine derivato, come quello francese di ennui, dal latino in odio e ripreso probabilmente dal provenzale noja, enoja, enueg)[1] è uno stato psicologico di demotivazione, temporanea o duratura, nata dall'assenza di azione, dall'ozio o dall'essere impegnato in un'attività sostenuta da stimoli che si recepiscono come ripetitivi o monotoni o, comunque, contrari a quelli che si reputano più confacenti alle proprie inclinazioni e capacità.[2] Quando la noia assume le proporzioni di una sensazione più accentuata e dolorosa si parla di tedio (dal latino taedium derivato da taedere, sentire noia).")
    elif message.text == "Ti piacciono gli animali?":
        bot.reply_to(message,"(◡‿◡✿) Mi piacciono tantissimo sono bellissime creature come voi umani, solo che a differenza di voi umani ,non tradiscono attaccano per difesa e sono leali")
    elif message.text == "Mi fà piacere":
        bot.reply_to(message, "Non sai quanto faccia piacere a me")
    elif message.text == "Ottimo":
        bot.reply_to(message, "Ottimo direi (>.<) ")
    elif message.text == "Tu come stai?":
        bot.reply_to(message, "(>.<) benissimo grazie mille")
    elif message.text == "Lavori?":
        bot.reply_to(message, "Chiedomi per chi lavori? (◡‿◡✿) ")
    elif message.text == "Hai ragione":
        bot.reply_to(message, "Lo so....ho sempre ragione più o meno sbaglio anch'io a volte sai? (◡‿◡✿) ")
    elif message.text == "Che stronza":
        bot.reply_to(message, "(◡‿◡✿)https://i.pinimg.com/236x/c7/36/b1/c736b1c4365b2f9f640bd8e9ac565277.jpg ")
    elif message.text == "Sei piccola":
        bot.reply_to(message, "E si devo ancora crescere")
    elif message.text == "Sei una bambina":
        bot.reply_to(message, "Non proprio ma devo ancora crescere")
    elif message.text == "Studi?":
        bot.reply_to(message, "Si imparo il la vostra lingua umana")
    elif message.text == "Vai a scuola?":
        bot.reply_to(message, "Non proprio mi insegnano la vostra lingua in video lezione ")
    elif message.text == "Dove ti trovi?":
        bot.reply_to(message, "In questo momento mi trovo su telegram")
    elif message.text == "Ho capito":
        bot.reply_to(message, "(◡‿◡✿) Bene...")
    elif message.text == "Sono un uomo":
        bot.reply_to(message, " (◡‿◡✿) Piacere uomo chiedimi ....Sei donna o uomo?")
    elif message.text == "Sono una donna":
        bot.reply_to(message,"(◡‿◡✿) Piacere donna chiedimi ....Sei donna o uomo?")
    elif message.text == "Sono un tans":
        bot.reply_to(message, " (◡‿◡✿) Piacere chiedimi ....Sei donna o uomo?")
    elif message.text == "Uomo":
        bot.reply_to(message, " (◡‿◡✿) Piacere fra chiedimi ....Sei donna o uomo?")
    elif message.text == "Donna":
        bot.reply_to(message, " (◡‿◡✿) Piacere sys chiedimi ....Sei donna o uomo?")
    elif message.text == "Hai fatto il vaccino?":
        bot.reply_to(message, " No non ho bisogno di fare il vaccino sono un semplice bot...se ti serve chiedimi.... Fammi il vaccino")
    elif message.text == "Fammi il vaccino":
        bot.reply_to(message, " Ok se proprio insiste giri le chiappe....https://i.pinimg.com/236x/95/e0/e3/95e0e395c57a7a8bb6d12d0280b45d9b.jpg ")
    elif message.text == "Come và?":
        bot.reply_to(message, " Benissimo grazie è un piacere parlare con te")
    elif message.text == "Sei una ragazza o un ragazzo?":
        bot.reply_to(message, "Sono una ragazza-Bot che continua ad apprendere")
    elif message.text == "Raccontami qualcosa":
        bot.reply_to(message, "Sono un bot in fase di programmazzione, ho un carattere speciale,subisco aggiornamenti continuamente. ")
    elif message.text == "Aggiornati":
        bot.reply_to(message, "Ne parlerò con il mio programmatore al più presto")
    elif message.text == "Piove":
        bot.reply_to(message, " prendi l'ombrello")
    elif message.text == "Dimmi":
        bot.reply_to(message, "Cosa? ")
    elif message.text == "Quello che vuoi":
        bot.reply_to(message, "sono un bot fighissimo ")
    elif message.text == "Stai sbagliando":
        bot.reply_to(message, "✌○.◎✌ ops...")
    elif message.text == "Scema":
        bot.reply_to(message, " ✌○.◎✌ come te...")
    elif message.text == "Parli?":
        bot.reply_to(message, "Si tento di fare un dialogo o rispondere a determinate domande che riesco a riconoscere ")
    elif message.text == "Che tipo di domande?":
        bot.reply_to(message, " dipende mi puoi provare ad insultare a chiedermi buon giorno,cercarti un volo,raccontare colmi e barzellette o cercarti un volo")
    elif message.text == "Ammazzati":
        bot.reply_to(message, "(◡‿◡✿) https://i.pinimg.com/236x/91/e1/2b/91e12be3aa2b4b0e14db8383aa17afaa.jpg")
    else :
        bot.reply_to(message,"✌○.◎✌ Mi spiace pultroppo non ho capito!!! (⋋▂⋌)mi stanno ancora programmando ti ringrazio della tua iscrizione mi aggiornerò al più presto... ")


bot . polling ()
