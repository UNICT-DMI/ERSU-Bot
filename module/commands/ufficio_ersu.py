# ufficioersu command

from telegram import Update
from telegram.ext import CallbackContext

def ufficio_ersu(update: Update, context: CallbackContext) -> None:
  context.bot.sendMessage(chat_id=update.message.chat_id, text=
"""ERSU CATANIA
📍 Via Etnea, 570
🕑 Orari di ricevimento
Lunedì 09:00 - 12:00
Mercoledì 15:00 - 18:00
Venerdì 09:00 - 12:00
  
📋Prenotazione appuntamento
È possibile prenotare un appuntamento con l'ufficio assegnazione e l'ufficio ristorazione cliccando al seguente link:  
https://www.ersucatania.it/category/calendari-prenotazione/
  
☎️ Contatti
• CENTRALINO
📞 095 7517910

• URP
📞 095 7517940

• ASSEGNAZIONE, BORSE DI STUDIO
📞 0957517935
📞 0957517932
📧 assegnazione@ersucatania.it 
L'ufficio risponde nei seguenti orari
Lunedì, Mercoledì, Venerdì ore 8.00-9.00 e 13.00-14.00;
Martedì e Giovedì ore 8.00-10.00 e 13.00-14.00.

• RISTORAZIONE
📞 0957517917
📧 ristorazione@ersucatania.it

• ATTIVITA' CULTURALI
📞 097517968 
📧 attivitaculturali@ersucatania.it 

• TRASPORTI EXTRAURBANI E ABBONAMENTI TEATRALI 
📞 0957517913
📧 trasportiextraurbani@ersucatania.it

• ERASMUS INCOMING E FORESTERIA  
📞 0957517937  
📧 erasmus@ersucatania.it
📧 foresteria@ersucatania.it 

• COORDINAMENTO CASE 
📧 residenze@ersucatania.it

• RESIDENZA CITTADELLA
📞 095330911
📧 residenza.cittadella@ersucatania.it

• RESIDENZA CENTRO
📞 095504680
📧 residenza.centro@ersucatania.it

• RESIDENZA TOSCANO SCUDERI
📞 095436481

• RESIDENZA VIA VERONA
📞 0957167107

• RESIDENZA SAN MARZANO
📞 095330868""")