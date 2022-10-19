# ERSU-Bot
A Telegram Bot for UNICT students aided at helping students find informations about ERSU services.

## How does it work?

##Requirements
-Pip3
-Python3

## docker-compose
```yaml
version: '2'
services:
  ersu-bot:
    container_name:ersubot
    image: ghcr.io/unict-dmi/ersubot:master
    volumes:
      - <your-settings.yaml>:/app/config/settings.yaml
    restart: unless-stopped
```

##How to create a Telegram bot and get its token
To start testing this bot you need to get a Telegram Bot's token:
- Go to Telegram and search for @BotFather
- Start it using `/start`
- Create a new bot using the `/newbot`command
- Give it a name and a tag (the tag must end with `bot`)
- Now copy the token it gives you

##Testing with docker compose
To test the bot with docker compose on windows follow these steps:
1) Clone the repository
2) Copy the existing `config/settings.yaml.dist` and rename it into `config/settings.yaml`
3) In `token` add your Telegram bot's token
4) Open terminal on the cloned repository and run ```docker build -t ersubot .``` to build the new image
5) Next run ```docker run -v "/c/Users/your/absolute/path/ERSU-Bot/config/settings.yaml":"/ersubot/config/settings.yaml" ersubot```

To test it with Linux follow the steps above to the point 4):
5) Run ```docker run -v "/home/your/absolute/path/ERSU-Bot/config/settings.yaml":"/ersubot/config/settings.yaml" ersubot```


## Testing live
To test the bot follow these steps:
- Clone this repository
- Create `config/settings.yaml` (or copy the existing `config/settings.yaml.dist` and rename it into `config/settings.yaml`)
- Insert your Telegram Bot Token inside the file
- Run `main.py` to start the bot

## Credits
