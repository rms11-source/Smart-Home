from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TITLES_FEEL = { "INLINE_BUTTON_GOOD": '🥰', "INLINE_BUTTON_OK": '👌', "INLINE_BUTTON_BAD": '😨'}

CALLBACK_BUTTON_GOOD = "callback_button_good"
CALLBACK_BUTTON_OK = "callback_button_OK"
CALLBACK_BUTTON_BAD = "callback_button_bad"

def get_inline_keyboard_health():
    keyboard = [
        [
            InlineKeyboardButton(TITLES_FEEL["INLINE_BUTTON_GOOD"], callback_data = CALLBACK_BUTTON_GOOD),
            InlineKeyboardButton(TITLES_FEEL["INLINE_BUTTON_OK"], callback_data = CALLBACK_BUTTON_OK),
            InlineKeyboardButton(TITLES_FEEL["INLINE_BUTTON_BAD"], callback_data = CALLBACK_BUTTON_BAD),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

TITLES_CONFIRM = { "INLINE_BUTTON_SEND": "Send data", "INLINE_BUTTON_DISCARD": "Discard"}

CALLBACK_BUTTON_SEND = "callback_button_send"
CALLBACK_BUTTON_DISCARD = "callback_button_discard"

def get_inline_keyboard_confirm():
    keyboard = [
        [
            InlineKeyboardButton(TITLES_CONFIRM["INLINE_BUTTON_SEND"], callback_data = CALLBACK_BUTTON_SEND),
            InlineKeyboardButton(TITLES_CONFIRM["INLINE_BUTTON_DISCARD"], callback_data = CALLBACK_BUTTON_DISCARD),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)