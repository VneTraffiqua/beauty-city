from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


personal_account_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True
)

st1_kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Записаться'),
            KeyboardButton(text='Личный кабинет'),
        ],
    ],
    resize_keyboard=True
)

st2_kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='В салон...'),
            KeyboardButton(text='На услугу...'),
            KeyboardButton(text='К мастеру...'),
        ],
    ],
    resize_keyboard=True
)
st3_kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ближайший салон'),
            KeyboardButton(text='Выбрать салон из списка...'),
        ],
    ],
    resize_keyboard=True
)
confirm_oder_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подтвердить заказ'),
            KeyboardButton(text='Начать заново')
        ]
    ],
    resize_keyboard=True
)

approval_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Согласен(на)'),
            KeyboardButton(text='Отказ')
        ]
    ],
    resize_keyboard=True
)

confirm_salon_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подтвердить салон'),
            KeyboardButton(text='Выбрать другой салон')
        ]
    ],
    resize_keyboard=True
)

confirm_service_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подтвердить выбор услуги'),
            KeyboardButton(text='Выбрать другую услугу')
        ]
    ],
    resize_keyboard=True
)

confirm_master_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подтвердить выбор мастера'),
            KeyboardButton(text='Выбрать другого мастера')
        ]
    ],
    resize_keyboard=True
)

confirm_slot_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подтвердить время'),
            KeyboardButton(text='Выбрать другое время')
        ]
    ],
    resize_keyboard=True
)

ok_button_request_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='OK', request_location=True),
            KeyboardButton(text='Выбрать салон из списка...')
            
        ]
    ],
    resize_keyboard=True
)

ok_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='OK')
        ]
    ],
    resize_keyboard=True
)

clear_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Понятно')
        ]
    ],
    resize_keyboard=True
)

finish_order_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подтвердить заказ'),
            KeyboardButton(text='Начать сначала')
        ]
    ],
    resize_keyboard=True
)