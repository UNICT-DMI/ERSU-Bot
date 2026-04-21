"""Constants used throughout the application"""

from typing import Literal

DB_PATH = "data/ERSU_DB.db"

START_CMD_TEXT = (
    "Benvenuto! Questo bot è stato realizzato dagli studenti del Corso di Laurea in Informatica "
    "al fine di fornire uno strumento di supporto per chi usufruisce dei servizi ERSU. "
    "Per scoprire cosa puoi fare usa /help"
)

HELP_CMD_TEXT = (
    "Telegram ERSU Bot\n"
    "📚 /ufficioersu Fornisce informazioni sugli uffici ERSU Catania\n"
    "📬 /report Fornisce la possibilità di poter inviare una segnalazione ai Rappresentanti "
    "ERSU, riguardante qualsiasi disservizio, informazione, dubbi e domande\n"
    "📖 /faq Lista delle risposte alle domande più frequenti sulla borsa di studio"
)

# 🍽 /menu Fornisce il menù per il prossimo pasto Mensa
# ⚙️ /menu_settings Fornisce la possibilità di impostare quando vuoi ricevere
# automaticamente qualche ora prima il menù del prossimo pasto

UFFICIO_ERSU_CMD_TEXT = """ERSU CATANIA
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
📞 095330868"""

ANSWER_TO_REPORT_TEXT = """Non hai risolto? Prenota un *appuntamento telefonico*
da [qui](https://www.ersucatania.it/calendario-ufficio-assegnazione/)"""

FAQ = "📖 FAQ"


MENU_MENSA = "Menù mensa 🍽"
CONTACT_ERSU = "Contatti ERSU 📚"
REPORT = "Segnalazioni Rappresentanti 📬"
HELP = "Help ❔"
MENU_SETTINGS = "Impostazioni Menù Mensa ⚙️"

CROSS = "❌"
CHECK = "✅"
SYMBOLS = [CROSS, CHECK]
EMPTY = 0
USER_EMPTY_SETTINGS = [0] * 14

DAYS = Literal[
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
]
MEALS = Literal["lunch", "dinner"]
VALID_DAYS = (
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
)
VALID_MEALS = ("lunch", "dinner")
DAYS_TRANSLATION = {
    "monday": "Lunedì",
    "tuesday": "Martedì",
    "wednesday": "Mercoledì",
    "thursday": "Giovedì",
    "friday": "Venerdì",
    "saturday": "Sabato",
    "sunday": "Domenica",
}

# callbackquery handler data
DAYS_MEAL_REGEX = (
    r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday)+?_(dinner|lunch)"
)

# correct link format for ERSU news
ERSU_LINK_REGEX = (
    r"(https:\\/\\/www\\.ersucatania\\.it\\/)([a-zA-Z0-9]+)(\\-[a-zA-Z0-9]+)*\\/"
)

# get chat_id from a report message
CHAT_ID_REGEX = r"(id: )([0-9]+)"
