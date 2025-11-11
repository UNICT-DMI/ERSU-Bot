# Telegram ERSU-Bot
A Telegram Bot for UNICT students aided at helping students find informations about ERSU services.

## How does it works?
This bot allows you to get straight to your telegram chat:
- the menu for the next meal
- informations about ERSU's offices

Send **'/start'** to start it, **'/help'** to see a list of commands.
Please note that the commands and their answers are in Italian.

---

## How to create a Telegram bot and get its token
To start testing this bot you need to get a Telegram Bot's token:
- Go to Telegram and search for @BotFather
- Start it using `/start`
- Create a new bot using the `/newbot` command
- Give it a name and a tag (the tag must end with `bot`)
- Now copy the token it gives you

## Requirements
- Pip3
- Python3

## Docker-compose

To run properly this project via docker compose you can copy `config/settings.yaml.dist` into `config/settings.yaml` and `data/ERSU_DB.db.dist` into `data/ERSU_DB.db` and launch the project via the following command:

```bash
docker compose up
```


## Testing with Docker-Compose
To test the bot with docker compose on Windows follow these steps:
1) Clone the repository
2) Copy the existing `config/settings.yaml.dist` and rename it into `config/settings.yaml`
3) In `token` add your Telegram bot's token
4) Open the terminal on the cloned repository and run ```docker build -t ersubot .``` to build the new image
5) Next run ```docker run -v "/c/Users/your/absolute/path/ERSU-Bot/config/settings.yaml":"/ersubot/config/settings.yaml" ersubot```

To test it with Linux follow the steps above to the point 4) and:

5) Run ```$ docker run -v "/home/your/absolute/path/ERSU-Bot/config/settings.yaml":"/ersubot/config/settings.yaml" ersubot```


## Testing live
To test the bot directly on your machine follow these steps:
1) Clone this repository
2) Copy the existing `config/settings.yaml.dist` and rename it into `config/settings.yaml`
3) In `token` add your Telegram bot's token
4) Run `$ python main.py` to start the bot

## Credits
- [Pierpaolo Pecoraio](https://github.com/Pierpaolo791)
- [Davide Carnemolla](https://github.com/daxcpp)
- [Stefano Borzì](https://github.com/Helias)
- [Ernesto Casablanca](https://github.com/TendTo)
- [Damiano Coppola](https://github.com/DefEnge)
- [Leonardo Mirabella](https://github.com/infra-blue)
