# MAK Currency Bot
You can use the MAK Currency Bot by following this link: [t.me/MAKengr_bot](https://t.me/MAKengr_bot).  
MAK Currency Bot is a Telegram bot that allows users to convert an amount of one currency to another. 
Users can enter a conversion command in the following format: [Amount] [Base] [Target], 
and the bot will use the ExchangeRate-API to retrieve up-to-date exchange rates and perform the conversion.

## Creating a Bot in Telegram
1. Open a conversation with the [Bot Father](https://telegram.me/botfather).
2. Type /newbot and follow the prompts to create a new bot.
3. The Bot Father will give you a token. Save this token in a .env file. [Go to configuration section](#configuration)

## Installation
Clone the repository:
~~~ 
git clone https://github.com/magedmagdy/mak-currency-bot.git
~~~

## Install the required packages:
To use this bot, you will need to install the following dependencies:

- telebot
- requests
- decouple

You can install these dependencies by running the following command:
~~~ 
pip install -r requirements.txt
~~~

## Configuration
Before you can run the bot, you will need to obtain a bot token from the Telegram Bot Father and add it to a private .env file in the root directory of the project. 
The .env file should contain the following line:

~~~
BOT_TOKEN=your_bot_token
~~~

## Usage
Run the script:
~~~
python main.py
~~~
To use the bot, send it a message in the following format: [Amount] [Base] [Target]. 
For example, to convert 200 US dollars to Egyptian pounds, you would send the message 200 USD EGP.

You can also use the following commands:

- /start - Show a welcome message.
- /help - Show a list of available commands.
- /currencies - Show a list of currency abbreviations.

## Acknowledgments
Here is a sample list of acknowledgements that you can include in your project:

- [ExchangeRate-API](https://www.exchangerate-api.com/) - for providing up-to-date exchange rates.
- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) - for providing an easy-to-use Python wrapper for the Telegram Bot API.
- [Requests](https://github.com/psf/requests) - for simplifying HTTP requests in Python.
- [Decouple](https://github.com/HBNetwork/python-decouple) - for providing a simple way to handle configuration variables in Python.

## Copyright
Copyright (c) 2022 Maged Magdy. All rights reserved.

## Contact 
For any inquiries or questions about the bot, please contact the author at magedmagdy.engr@gmail.com.
