from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8079309657:AAGGicXtuP-Vc6j4KPhiQq6kSV0OGH6kehA"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت يعمل الآن! أنا هنا لحماية المجموعة 👮‍♂️")

# حذف الروابط
async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "http" in update.message.text or "t.me/" in update.message.text:
        try:
            await update.message.delete()
        except:
            pass

# رد تلقائي
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "مرحبا" in msg or "هلا" in msg:
        await update.message.reply_text("👋 أهلًا وسهلًا!")
    elif "ادمن" in msg:
        await update.message.reply_text("👮‍♂️ سيتم إبلاغ الأدمن فوراً.")
    elif "قوانين" in msg:
        await update.message.reply_text("📜 قوانين المجموعة:\n1. ممنوع السبام\n2. احترم الجميع\n3. لا تنشر روابط")

# ترحيب بعضو جديد
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        name = member.full_name
        await update.message.reply_text(f"🎉 أهلاً وسهلاً بك {name} في مجموعتنا!")

# main
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, delete_links))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, auto_reply))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    print("🤖 البوت يعمل الآن...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
