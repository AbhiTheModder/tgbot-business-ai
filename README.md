# Telegram Business Chatbot

**NOTE:** Telegram Business is a feature available to users of telegram premium only

- If you're a telegram premium user and want to use this without hosting yourself you can use this bot [@LimitBreakerBot](https://t.me/LimitBreakerBot) which is currently running on it, but i can't gurantee you until when it'll be running :D

## Features

- Cohere Coral Command-R-Plus AI integration for advanced natural language processing and chatbot responses.
- New Telegram Business Chatbot feature to reply to users on your behalf.
- Python-based implementation using the Pyrogram (Pyrofork) library for Telegram bot development.
- Chat history support for each individual user, enabling personalized and context-aware responses.

## Requirements

- Python 3.6 or higher
- Pyrogram (Pyrofork) library
- Cohere Coral Command-R-Plus AI API key

## Installation

1. Install the required libraries:

```
pip install -r requirements.txt
```

2. Fill in the following necessary variabkes in `app.py` with your actual values:

- `API_ID`: Your Telegram API ID.
- `API_HASH` : Your Telegram API Hash.
- `BOT_TOKEN` : Your Telegram Bot Token Obtained from @BotFather.
- `CORAL_KEY` : Your Cohere Coral Command-R-Plus AI API key ( You can find your api key [here](https://dashboard.cohere.com/api-keys) ).

3. Run the bot:

```
python bot.py
```

## Credits

- [Pyrofok](https://github.com/Mayuri-Chan/pyrofork)
- [Cohere Coral](https://cohere.com)
- [Telegram Bot API](https://core.telegram.org/bots)
