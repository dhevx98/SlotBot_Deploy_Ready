import telebot
import requests

TOKEN = "ISI_TOKEN_BOT_KAMU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(message, "🎰 Selamat datang di Slot Bot!")

@bot.message_handler(commands=["spin"])
def handle_spin(message):
    result = requests.get("https://your-slot-api.com/spin")  # ganti sesuai backend-mu
    if result.ok:
        data = result.json()
        bot.reply_to(message, f"Hasil Spin Kamu:\n{data['result']}")
    else:
        bot.reply_to(message, "⚠️ Gagal melakukan spin, coba lagi nanti.")

@bot.message_handler(commands=["help"])
def handle_help(message):
    text = (
        "📌 Perintah yang tersedia:\n"
        "/start - Mulai bot\n"
        "/spin - Putar slot\n"
        "/help - Bantuan"
    )
    bot.reply_to(message, text)

bot.polling()
