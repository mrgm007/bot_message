from aiogram import types
from dispatcher import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Кнопка 1
inkb1 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text = "ДА🔥", callback_data="text2"))
@dp.message_handler(commands ="start")
async def start(message: types.Message):
    text1 = "Хотите дополнительно заработать от 500 грн в день 💸?"
    await message.answer(text= text1, reply_markup=inkb1)


#Кнопка 2
inkb2 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text = "➡️УЗНАТЬ БОЛЬШЕ", callback_data="text3"))
@dp.callback_query_handler(text="text2")
async def text2_call(callback_text2: types.CallbackQuery):
    text2 = "💰  Мы платим за регистрацию на сайте. Чем больше регистраций вы сможете сделать, тем выше будут заработки."\
"✅ Спокойно можно совмещать с работой, которая есть. Обучение предоставляем."
    await callback_text2.message.answer(text=text2, reply_markup=inkb2)


#Кнопка 3
inkb3 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text = "200", callback_data="text4"),
                                              InlineKeyboardButton(text = "500", callback_data="text4_2"),
                                              InlineKeyboardButton(text = "1000+", callback_data="text4_3"))

@dp.callback_query_handler(text="text3")
async def text3_call(callback_text3: types.CallbackQuery):
    text3 = "🤔Сколько вы хотите дополнительно зарабатывать в день❓"
    await callback_text3.message.answer(text= text3, reply_markup=inkb3)


#Кнопка 4
inkb4 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text = "ДА", callback_data="text5"))
@dp.callback_query_handler(text="text4")
async def text4_call(callback_text4: types.CallbackQuery):
    text4 = "🔥Хотите покажу как на регистрациях заработать 200?"
    await callback_text4.message.answer(text=text4, reply_markup=inkb4)

@dp.callback_query_handler(text="text4_2")
async def text4_call(callback_text4: types.CallbackQuery):
    text4 = "🔥Хотите покажу как на регистрациях заработать 500?"
    await callback_text4.message.answer(text=text4, reply_markup=inkb4)

@dp.callback_query_handler(text="text4_3")
async def text4_call(callback_text4: types.CallbackQuery):
        text4 = "🔥Хотите покажу как на регистрациях заработать 1000+?"
        await callback_text4.message.answer(text=text4, reply_markup=inkb4)



#Кнопка 5
urlkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text = "TElEGRAM", url="https://www.youtube.com/watch?v=BZlcslqMNfA"))
@dp.callback_query_handler(text="text5")
async def text5_call(callback_text5: types.CallbackQuery):
    text5 = "✏️Напишите мне в телеграм  “Хочу заработать”, чтобы я лично смог вам все показать."\
"Нажимайте на кнопку ниже и вас перенаправит на диалог со мной"\
"P.S. Кстати, возьму только 10 человек. ⬇️⬇️⬇️"
    await callback_text5.message.answer(text= text5, reply_markup=urlkb)
