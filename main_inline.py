from telebot import TeleBot
from telebot.types import (
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


bot = TeleBot(
    token="5673977494:AAGMAVB09giqgzwFXbkcKYAyIZkGLjR6s2w",
    parse_mode="html"
)


start_counter = dict()


@bot.message_handler(commands=["start"], chat_types=["private"])
def start(msg):
    global start_counter

    start_counter[msg.from_user.id] = start_counter.get(msg.from_user.id, 0) + 1

    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)

    reply_markup.add(
        KeyboardButton(text="Профиль"),
        KeyboardButton(text="Заказы"),
    )

    bot.send_message(
        chat_id=msg.chat.id,
        text="Приветствуем, ваш ID = " + str(msg.from_user.id) + " ID нашего чата: " + str(msg.chat.id),
        reply_markup=reply_markup
    )


@bot.message_handler(chat_types=["private"])
def cmd_start(msg):
    if msg.text == "Профиль":
        inline_markup = InlineKeyboardMarkup(row_width=4)

        inline_markup.add(
            InlineKeyboardButton(text="Заказы", callback_data="profile-orders"),
        )

        bot.send_message(
            chat_id=msg.chat.id,
            text="Профиль",
            reply_markup=inline_markup
        )
        
    elif msg.text == "Заказы":
        ...

    else:
        bot.send_message(chat_id=msg.chat.id, text="Пожалуйста, используйте одну из кнопок")


@bot.callback_query_handler(func=lambda call: True)
def callback(call: CallbackQuery):
    if call.data == "profile-orders":
        inline_markup = InlineKeyboardMarkup(row_width=1)

        inline_markup.add(
            InlineKeyboardButton(text="История заказов", callback_data="profile-orders-history"),
            InlineKeyboardButton(text="<< Назад", callback_data="profile"),
        )

        user_counter = start_counter.get(call.message.chat.id, 0)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"Заказы: {user_counter}",
            reply_markup=inline_markup
        )

    elif call.data == "profile":
        ...

    elif call.data == "profile-orders-history":
        ...

    else:
        bot.send_message(chat_id=call.message.chat.id, text="Пожалуйста, используйте одну из кнопок")


def main():
    print("Starting polling")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
