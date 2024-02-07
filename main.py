from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


bot = TeleBot(
    token="5673977494:AAGMAVB09giqgzwFXbkcKYAyIZkGLjR6s2w",
    parse_mode="html"
)


@bot.message_handler(commands=["start"], chat_types=["private"])
def start(msg):
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)

    reply_markup.add(
        KeyboardButton(text="Профиль"),
        KeyboardButton(text="Заказы"),
    )

    reply_markup.add(
        KeyboardButton(text="Кнопка4"),
    )
    
    reply_markup.add(
        KeyboardButton(text="Кнопка5"),
        KeyboardButton(text="Кнопка6"),
        KeyboardButton(text="Кнопка7"),
        KeyboardButton(text="Кнопка8"),
    )

    bot.send_message(
        chat_id=msg.chat.id,
        text="test",
        reply_markup=reply_markup
    )


@bot.message_handler(chat_types=["private"])
def cmd_start(msg):
    if msg.text == "Профиль":
        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        reply_markup.add(
            KeyboardButton(text="<< Назад"),
            KeyboardButton(text="Дата регистрации"),
        )

        bot.send_message(
            chat_id=msg.chat.id,
            text="Профиль\n\n...",
            reply_markup=reply_markup
        )
        
    elif msg.text == "Заказы":
        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        reply_markup.add(
            KeyboardButton(text="<< Назад"),
            KeyboardButton(text="Ожидающие оплаты"),
        )

        bot.send_message(
            chat_id=msg.chat.id,
            text="Профиль\n\n...",
            reply_markup=reply_markup
        )

    elif msg.text == "<< Назад":
        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)

        reply_markup.add(
            KeyboardButton(text="Профиль"),
            KeyboardButton(text="Заказы"),
        )

        bot.send_message(
            chat_id=msg.chat.id,
            text="test",
            reply_markup=reply_markup
        )

    else:
        bot.send_message(chat_id=msg.chat.id, text="Пожалуйста, используйте одну из кнопок")


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    ...


def main():
    print("Starting polling")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
