# Copyright (c) 2022 Maged Magdy. All rights reserved.

"""
MAK Currency Bot is a Telegram bot that allows users to convert an amount of one currency to another.
Users can enter a conversion command in the following format: [Amount] [Base] [Target]
The bot makes use of the ExchangeRate-API to retrieve up-to-date exchange rates and perform the conversion.
"""

import telebot
import requests
from decouple import config

# Load the bot token from a private .env file
BOT_TOKEN = config('BOT_TOKEN')

# Create a new bot using the bot token
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def handle_start_command(message):
    """
    Send a welcome message and list of commands when the /start command is received.

    Parameters:
        message (telebot.types.Message): The incoming message.
    """
    # Send a welcome message
    bot.send_message(message.chat.id, "Welcome to MAK Currency bot!")

    # Send instructions on how to use the bot
    bot.send_message(message.chat.id, "Enter the currency in this format: [Amount] [Base] [Target]")
    bot.send_message(message.chat.id, "ex: 200 USD EGP")

    # Send a list of available commands
    bot.send_message(message.chat.id, "You can use the command /help to get a list of available commands.")


@bot.message_handler(commands=["help"])
def handle_help_command(message):
    """
    Send a list of commands and a brief description of each when the /help command is received.

    Parameters:
        message (telebot.types.Message): The incoming message.
    """

    # Send a list of available commands
    bot.send_message(message.chat.id, "Here is a list of available commands:")
    bot.send_message(message.chat.id, "/start - Show a welcome message")
    bot.send_message(message.chat.id, "/help - Show a list of available commands.")
    bot.send_message(message.chat.id, "/currencies - Show a list of currency abbreviations.")
    bot.send_message(message.chat.id, "Convert an amount of one currency to another. "
                                      "Use the format: [Amount] [Base] [Target]")


@bot.message_handler(commands=["currencies"])
def handle_currencies_command(message):
    """
    Send a list of currency abbreviations when the /currencies command is received.

    Parameters:
        message (telebot.types.Message): The incoming message.
    """

    # Send a list of currency abbreviations
    bot.send_message(message.chat.id, "Abbreviations of some famous currencies:")
    bot.send_message(message.chat.id, "United States Dollar: USD\n"
                                      "Euro: EUR\n"
                                      "British Pound: GBP\n"
                                      "Japanese Yen: JPY\n"
                                      "Australian Dollar: AUD\n"
                                      "Canadian Dollar: CAD\n"
                                      "Swiss franc: CHF\n"
                                      "Chinese Yuan: CNY\n"
                                      "Indian Rupee: INR\n"
                                      "South African Rand: ZAR\n"
                                      "Brazilian Real: BRL\n"
                                      "Mexican Peso: MXN\n"
                                      "United Arab Emirates Durham: AED\n"
                                      "Saudi Arabian Riyal: SAR\n"
                                      "Kuwaiti Dinar: KWD\n"
                                      "Qatari Riyal: QAR\n"
                                      "Omani Rial: OMR\n"
                                      "Bahrain Dinar: BHD\n"
                                      "Egyptian Pound: EGP\n"
                                      "Lebanese Pound: LBP")


@bot.message_handler(func=lambda msg: True)
def handle_convert_command(message):
    """
    Convert an amount of one currency to another when the /convert command is received.

    Parameters:
        message (telebot.types.Message): The incoming message.
    """

    # Split the message text into a list of three strings: amount, base currency, and target currency
    my_list = message.text.split()
    if len(my_list) == 3:
        amount = my_list[0]
        base = my_list[1]
        target = my_list[2]

        # Convert the amount to a float
        try:
            amount = float(amount)
        except ValueError:
            bot.send_message(message.chat.id, "Invalid amount. Please enter a valid number.")
            return

        # Convert the currency codes to uppercase
        base = base.upper()
        target = target.upper()

        # Set the API endpoint URL
        api_url = "https://api.exchangerate-api.com/v4/latest/{}".format(base)

        # Make the API request
        try:
            response = requests.get(api_url)
        except requests.exceptions.RequestException as e:
            bot.send_message(message.chat.id, "An error occurred while making the API request: {}".format(e))
            return

        # Get the exchange rate from the API response
        try:
            exchange_rate = response.json()["rates"][target]
        except KeyError:
            bot.send_message(message.chat.id, "Invalid currency code. Please enter a valid currency code.")
            return

        # Calculate the conversion result
        converted_amount = amount * exchange_rate

        # Send the result to the user
        bot.reply_to(message, "{} {} = {} {}".format(amount, base, converted_amount, target))
    else:
        bot.reply_to(message, "Invalid format!")
        bot.send_message(message.chat.id, "Please, enter a valid format like this: 200 USD EGP")


bot.polling()
