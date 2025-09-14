import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تجيب التوكن من متغير البيئة
TOKEN = os.environ.get("1976445156:AAF8P9cCTq2OGLCpCmtxsFhI9A9GNzhEXfo")

# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا بيك 👋، البوت شغال على Render!")

def main():
    # إنشاء التطبيق
    app = Application.builder().token(TOKEN).build()

    # إضافة أمر /start
    app.add_handler(CommandHandler("start", start))

    # تشغيل البوت (Polling)
    app.run_polling()

if __name__ == "__main__":
    main()