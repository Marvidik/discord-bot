import os
import discord
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("USER_TOKEN")  # Your Discord user token
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))  # Channel ID in your own server

if not TOKEN or not TARGET_CHANNEL_ID:
    print("❌ Missing USER_TOKEN or TARGET_CHANNEL_ID in .env file")
    exit(1)

# Self-bot client
bot = discord.Client()  # discord.py-self uses this

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (Self-Bot Connected)")

async def send_to_target_channel(message):
    """Send a message to the target channel in your server."""
    try:
        channel = await bot.fetch_channel(TARGET_CHANNEL_ID)
        await channel.send(message)
        print(f"✅ Sent to target channel: {message}")
    except Exception as e:
        print(f"❌ Failed to send message: {e}")

@bot.event
async def on_member_join(member):
    alert = (
        f"🔔 New member joined {member.guild.name}\n"
        f"👤 Username: {member}\n"
        f"🆔 ID: {member.id}"
    )

    await send_to_target_channel(alert)

# @bot.event
# async def on_member_remove(member):
#     alert = (
#         f"❌ **Member Left**\n"
#         f"Server: {member.guild.name}\n"
#         f"User: {member}"
#     )
#     await send_to_target_channel(alert)


from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "✅ Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Start Flask in a new thread
threading.Thread(target=run).start()

bot.run(TOKEN)
