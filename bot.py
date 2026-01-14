from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = "8247285398:AAEYtqscBvtqUpbxQbUjDLYLxXe7ewinRBc"

def delete_service_messages(update, context):
    message = update.message
    if (
        message.new_chat_members
        or message.left_chat_member
        or message.group_chat_created
        or message.supergroup_chat_created
    ):
        try:
            context.bot.delete_message(
                chat_id=message.chat_id,
                message_id=message.message_id
            )
        except:
            pass

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.status_update, delete_service_messages))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
