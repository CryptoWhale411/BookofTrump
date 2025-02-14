from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# 🔑 Bot Token from BotFather (Do not share this publicly!)
TOKEN = "8086979687:AAEhY3uvk85PZRvxTqDjG-tFIVrcx9ysvrE"

# 📜 Book of Trump Coin Contract Address
BOOK_OF_TRUMP_TOKEN_ADDRESS = "w1vyfnRXU4jtSeAtdc1MjncioHa92UShMk5HZSe2Siv"

async def start(update: Update, context: CallbackContext):
    """Handles the /start command"""
    await update.message.reply_text(
        "🔥 Welcome to the **Book of Trump Bot**! 🔥\n\n"
        "Use /help to see available commands."
    )

async def help_command(update: Update, context: CallbackContext):
    """Handles the /help command"""
    await update.message.reply_text(
        "📌 Available Commands:\n"
        "- /price → Get the latest price\n"
        "- /buy → Learn how to buy\n"
        "- /contract → Get the token address\n"
        "- /info → Get details about Book of Trump Coin"
    )

async def price(update: Update, context: CallbackContext):
    """Handles the /price command"""
    await update.message.reply_text("📈 The current price of **Book of Trump Coin** is ... (Fetching live data soon!)")

async def buy(update: Update, context: CallbackContext):
    """Handles the /buy command"""
    await update.message.reply_text(
        "🛒 **How to Buy Book of Trump Coin:**\n\n"
        "1️⃣ Buy Solana (SOL) on an exchange like Binance or Coinbase.\n"
        "2️⃣ Transfer SOL to your Solana wallet (Phantom, Solflare, etc.).\n"
        "3️⃣ Use **Raydium or Jupiter** to swap SOL for Book of Trump Coin.\n"
        "4️⃣ Enter the contract address: 📜 `" + BOOK_OF_TRUMP_TOKEN_ADDRESS + "`"
    )

async def contract(update: Update, context: CallbackContext):
    """Handles the /contract command"""
    await update.message.reply_text(f"📜 **Book of Trump Coin Contract Address:**\n`{BOOK_OF_TRUMP_TOKEN_ADDRESS}`")

async def info(update: Update, context: CallbackContext):
    """Handles the /info command"""
    await update.message.reply_text(
        "📖 **Book of Trump Coin** is a meme coin on Solana!\n\n"
        "⚡ **Fast Transactions**\n"
        "🔥 **High Community Engagement**\n"
        "🚀 **Potential Moonshot**\n\n"
        "Stay updated by following our official channels!"
    )

async def handle_message(update: Update, context: CallbackContext):
    """Handles normal text messages"""
    text = update.message.text.lower()
    if "price" in text:
        await price(update, context)
    elif "how to buy" in text:
        await buy(update, context)
    elif "contract" in text:
        await contract(update, context)
    else:
        await update.message.reply_text("🤖 I'm here to help! Try using /help to see available commands.")

# Create the bot application
app = Application.builder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("contract", contract))
app.add_handler(CommandHandler("info", info))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Run the bot
print("✅ Bot is running... Waiting for messages...")
app.run_polling()

