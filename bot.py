import os

from pyrogram import Client, filters, enums
from pyrogram.types import Message

import cohere

from db import db

# Cohere API Key
CORAL_KEY= os.environ['CORAL_KEY']
# Telegram Auth API ID
API_ID = os.environ['API_ID']
# Telegram Auth API HASH
API_HASH = os.environ['API_HASH']
# Telegram Bot API TOKEN generated from @botfather
BOT_TOKEN = os.environ['BOT_TOKEN']


# Edit this to your needs
custom_message = "This is an automated response using Ai-ChatBot, My Master is currently away if in case i replied wrongly i apologise, when my master comes back he'll message you back Thanks :)"

# Initialize the client
app = Client("my_business_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

co = cohere.Client(CORAL_KEY)

@app.on_bot_business_message(filters.incoming & filters.text)
async def start(client: Client, message: Message):
    await message.reply_chat_action(enums.ChatAction.TYPING)

    user_id = message.from_user.id

    chat_history = db.get_chat_history(user_id)
    
    prompt = message.text

    db.add_chat_history(user_id, {"role": "USER", "message": prompt})

    response = co.chat(
            chat_history=chat_history,
            model='command-r-plus',
            message=prompt,
            temperature=0.3,
            connectors=[{
                "id": "web-search",
                "options": {
                    "site": "wikipedia.com"
                }
            }],
            prompt_truncation="AUTO"
        )
    
    db.add_chat_history(user_id, {"role": "CHATBOT", "message": response.text})
    
    await message.reply_text(f"{response.text}\n\n{custom_message}")

if __name__ == "__main__":
    app.run()
