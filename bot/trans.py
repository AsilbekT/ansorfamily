from .models import BotUsers

def t(word, message=None, user=None) -> object:
    """

    :rtype: object
    """
    if message is not None:
        userModel = BotUsers.objects.get(user_id=message['from']['id'])
        lang = userModel.lang
    elif user is not None:
        userModel = user
        lang = userModel.lang
    else:
        lang = 'uz'

    words_uz = {
        "Paketlar narxi" : "Qadoqlash narxi π¦",
        'qabul_qilindi': "Sizning buyurtmangiz qabul qilindiβ",
        'phone_number_warning': "β Iltimos, telefon raqamingizni quyidagi formatda (+998990000000) yoki telegramdagi telefon nomerni ulashish tugmasi orqali kiritin", 
        'Branches': "πͺ Bizning filiallarimiz",
        'Branch ni tanglang': "Filiallarimizdan birini tanlang",
        "yolda": "Sizni buyurtmangiz yo'ldaπ",
        "yetqazib_berildi": "Sizning buyurtmangiz yetkazib berildi. Bizga sizning fikringiz kerak. Iltimos izoh qoldiringπ",
        "Menular": "Menular",
        "Bizni karta raqamimiz": "Bizni karta raqamimiz",
        "Davom etish": "Davom etish π",
        "To'lash turini kiriting": "π° To'lash turini kiriting",
        "Manzilingizni kiriting": "Geolokatsiyani kiriting",
        "Narxi": "Narxi",
        'Tarkibi': 'Tarkibi',
        'orqaga': 'π Orqaga',
        "Naqt pul": "π΅ Naqt pul",
        'Azimov Tohir': 'Azimov Tohir',
        "Karta orqali to'lash": "π³ Karta orqali to'lash",
        "Iltimos manzilingizni yozib qoldiring": "Iltimos manzilingizni yozib qoldiring yoki izoh qoldiring",
        "asosiy oynaga qaytish": "β Asosiy oynaga qaytish",
        "Joylashuvni jo'natish": "π Geolokatsiya",
        "dastavka": "π Yetkazib berish",
        "olib ketaman": "ππ» Olib ketaman",
        "Buyurtmani o'zingiz olib ketasizmi yoki etkazib berishsinmi": "Buyurtmani o'zingiz olib ketasizmi ππ» yoki etkazib berishsinmi π",
        "quyidagilardan birini tanlang": "Quyidagilardan birini tanlang",
        'contact': "π² Telefon raqam yuborish",
        "Mobil raqamingizni kiriting": "Telefon raqamingizni quyidagi tarzda π yuboring yoki kiriting: +998 ** *** ****",
        "Ismingizni kiriting": "Ism, familiyangizni kiriting",
        'Familyangizni kiriting': "Familyangizni kiriting",
        'Register': "β Ro'yxatdan o'tish / Π Π΅Π³ΠΈΡΡΡΠ°ΡΠΈΡ",
        'uz til': "πΊπΏ O'zbekcha",
        'ru til': "π·πΊ Π ΡΡΡΠΊΠΈΠΉ",
        'Tilni tanlang uz/ru': "Tilni tanlang: / ΠΡΠ±Π΅ΡΠΈΡΠ΅ ΡΠ·ΡΠΊ",
        'welcome': "Xush kelibsiz",
        "Buyurtma qilish": "π Buyurtma qilish",
        "Mening buyurtmalarim": "π Mening buyurtmalarim",
        "Telefon orqali aloqa": "π Telefon orqali aloqa",
        "Sozlash": "β Sozlash",
        "Ansor oilasi": "π¨βπ©βπ§βπ¦ Aksiyalar",
        'savatcha': 'π Savatcha',
        'Savatcha': 'π₯ Savatcha',
        "O'zbekcha": "πΊπΏ O'zbekcha",
        "Ruscha": "π·πΊ Ruscha",
        "ΠΠΈΡΡΡ": 'π ΠΠΈΡΡΡ',
        "Fast food": "π Fast food",
        "Π‘ΡΠΏΡ (ΠΏΠ΅ΡΠ²ΠΎΠ΅ Π±Π»ΡΠ΄ΠΎ)": "π² Π‘ΡΠΏΡ (ΠΏΠ΅ΡΠ²ΠΎΠ΅ Π±Π»ΡΠ΄ΠΎ)",
        "Π‘Π°Π»Π°ΡΡ": "π₯ Π‘Π°Π»Π°ΡΡ",
        "Π’ΡΡΠ΅ΡΠΊΠ°Ρ ΠΊΡΡΠ½Ρ": "π Π’ΡΡΠ΅ΡΠΊΠ°Ρ ΠΊΡΡΠ½Ρ",
        "ΠΠ²ΡΠΎΠΏΠ΅ΠΉΡΠΊΠ°Ρ ΠΊΡΡΠ½Ρ": "π₯ ΠΠ²ΡΠΎΠΏΠ΅ΠΉΡΠΊΠ°Ρ ΠΊΡΡΠ½Ρ",
        "ΠΠ°Π²ΡΡΠ°ΠΊΠΈ": "π? ΠΠ°Π²ΡΡΠ°ΠΊΠΈ",
        "ΠΠ΅ΡΠ΅ΡΡΡ": "π° ΠΠ΅ΡΠ΅ΡΡΡ",
        "Barcha menular": "π Barcha menular",
        "Telefon": "πTelefon",
        "Til": "Til πΊπΏ π·πΊ",
        "checkout": "Davom etamizmiπ",
        "Savatni bo'shatish": "π Savatni bo'shatish",
        "Biz bilan bog'laning": "Biz bilan bog'laning",
        "Menuni tanlang": "Menyuni tanlang",
        "Barcha Menularni Korish": "Barcha Menyularni Korish",
        "Mahsulot narxi": "Mahsulot narxi",
        "Yetkazib berish narxi": "Yetkazib berish narxi",
        "Jami": "Jami",
        "feedback_done": "β Sizning izohingiz qabul qilindi",
        "so'm": "UZS",
        "narxi": "Narxi",
        "ta": "ta",

        "ΠΡΡΡΡΠ°Ρ Π΄ΠΎΡΡΠ°Π²ΠΊΠ°": "Tez yetkazib berildi π",
        "ΠΠ΅ΠΆΠ»ΠΈΠ²ΡΠΉ ΠΊΡΡΡΠ΅Ρ": "Muloyim kurerπ€",
        "ΠΠΏΠ΅ΡΠ°ΡΠΎΡ ΠΌΠΎΠ»ΠΎΠ΄Π΅Ρ": "Yaxshi operatorπ",
        "ΠΠ΅Π»ΠΈΠΊΠΎΠ»Π΅ΠΏΠ½ΡΠΉ Π²ΠΊΡΡ": "Ajoyib ta'm π",
        "savatchada": "Savatchada",
        "Eltish vaqti": "β³ Eltish vaqti",
        "Hali hech narsa yo'q": "Hali hech narsa yo'q",
        'Botimizdan foydalanganingiz uchun rahmat': 'Botimizdan foydalanganiz uchun rahmat, xodimlarimiz tez orada siz bilan boglanishadi',
        "Yangi mahsulot qo'shish": "π Yangi mahsulot qo'shish"

    }

    words_ru = {
        "Paketlar narxi" : "Π£ΠΏΠ°ΠΊΠΎΠ²ΠΊΠ° π¦",
        'qabul_qilindi': "ΠΠ°Ρ Π·Π°ΠΊΠ°Π· ΡΡΠΏΠ΅ΡΠ½ΠΎ ΠΏΡΠΈΠ½ΡΡβ",
        'phone_number_warning': "β ΠΠΎΠΆΠ°Π»ΡΠΉΡΡΠ°, Π²Π²Π΅Π΄ΠΈΡΠ΅ ΡΠ²ΠΎΠΉ Π½ΠΎΠΌΠ΅Ρ ΡΠ΅Π»Π΅ΡΠΎΠ½Π° Π² Π²ΠΈΠ΄Π΅ (+998990000000) ΠΈΠ»ΠΈ ΡΠ΅ΡΠ΅Π· ΠΊΠ½ΠΎΠΏΠΊΡ ΠΏΠΎΠ΄Π΅Π»ΠΈΡΡΡΡ Π½ΠΎΠΌΠ΅ΡΠΎΠΌ ΡΠ΅Π»Π΅ΡΠΎΠ½Π° Π² Telegram", 
        'Branches': "πͺ ΠΠ°ΡΠΈ ΡΠΈΠ»ΠΈΠ°Π»Ρ",
        'Branch ni tanglang': "ΠΡΠ±Π΅ΡΠΈΡΠ΅ Π½Π°ΡΠΈ ΡΠΈΠ»ΠΈΠ°Π»Ρ",
        "feedback_done": "β ΠΠ°Ρ ΠΎΡΠ·ΡΠ² Π±ΡΠ» ΠΏΡΠΈΠ½ΡΡ",
        "yolda": "ΠΠ°Ρ Π·Π°ΠΊΠ°Π· ΡΠΆΠ΅ Π² ΠΏΡΡΠΈπ",
        "qabul_qilindi": "Π‘ΠΏΠ°ΡΠΈΠ±ΠΎ, Π²Π°Ρ Π·Π°ΠΊΠ°Π· ΠΏΠΎΠ΄ΡΠ²Π΅ΡΠΆΠ΄Π΅Π½. ΠΠ½ Π±ΡΠ΄Π΅Ρ Π΄ΠΎΡΡΠ°Π²Π»Π΅Π½ Π² ΡΠ΅ΡΠ΅Π½ΠΈΠ΅ 45 ΠΌΠΈΠ½ΡΡ Π΅ΡΠ»ΠΈ Π²Ρ Π½Π°ΡΠΎΠ΄ΠΈΡΠ΅ΡΡ ΠΏΠΎ Π³ΠΎΡΠΎΠ΄Ρ Π€Π΅ΡΠ³Π°Π½Ρ.",
        "yetqazib_berildi": "ΠΠ°Ρ Π·Π°ΠΊΠ°Π· Π±ΡΠ» Π΄ΠΎΡΡΠ°Π²Π»Π΅Π½. ΠΠ°ΠΌ Π²Π°ΠΆΠ½ΠΎ Π²Π°ΡΠ΅ ΠΌΠ½Π΅Π½ΠΈΠ΅. ΠΠΎΠΆΠ°Π»ΡΠΉΡΡΠ° ΠΎΡΡΠ°Π²ΡΡΠ΅ ΡΠ²ΠΎΠΉ ΠΎΡΠ·ΡΠ²π",
        "Menular": "ΠΠ΅Π½Ρ",
        'orqaga': 'π ΠΠ°Π·Π°Π΄',
        "Kechirasiz hozir bu maxsulot yo'q": "ΠΠ·Π²ΠΈΠ½ΠΈΡΠ΅, ΡΡΠΎΡ ΠΏΡΠΎΠ΄ΡΠΊΡ ΡΠ΅ΠΉΡΠ°Ρ Π½Π΅Π΄ΠΎΡΡΡΠΏΠ΅Π½",
        "Bizni karta raqamimiz": 'ΠΠΎΠΌΠ΅Ρ Π½Π°ΡΠ΅ΠΉ ΠΊΠ°ΡΡΡ',
        "Manzilingizni kiriting": "ΠΠ²Π΅Π΄ΠΈΡΠ΅ Π³Π΅ΠΎΠ»ΠΎΠΊΠ°ΡΠΈΡ",
        "To'lash turini kiriting": "π° ΠΡΠ±Π΅ΡΠΈΡΠ΅ ΡΠΏΠΎΡΠΎΠ± ΠΎΠΏΠ»Π°ΡΡ",
        "Davom etish": "ΠΡΠΎΠ΄ΠΎΠ»ΠΆΠΈΡΡ π",
        "Narxi": "Π¦Π΅Π½Π°",
        "Tarkibi": "Π‘ΠΎΡΡΠ°Π²",
        "Naqt pul": "π΅ ΠΠ°Π»ΠΈΡΠ½ΡΠ΅",
        "Karta orqali to'lash": "π³ ΠΠΏΠ»Π°ΡΠ° ΠΊΠ°ΡΡΠΎΠΉ",
        "Iltimos manzilingizni yozib qoldiring": "ΠΠ°ΠΏΠΈΡΠΈΡΠ΅ ΡΠ²ΠΎΠΉ Π°Π΄ΡΠ΅Ρ Π»ΠΈΠ±ΠΎ ΠΎΡΡΠ°Π²ΡΡΠ΅ ΠΊΠΎΠΌΠΌΠ΅Π½ΡΠ°ΡΠΈΠΈ ΠΊ Π·Π°ΠΊΠ°Π·Ρ",
        "asosiy oynaga qaytish": "βοΈ ΠΠ΅ΡΠ½ΡΡΡΡΡ Π² Π³Π»Π°Π²Π½ΠΎΠ΅ ΠΎΠΊΠ½ΠΎ",
        "Joylashuvni jo'natish": "π ΠΠ΅ΠΎΠ»ΠΎΠΊΠ°ΡΠΈΡ",
        "dastavka": "π ΠΠΎΡΡΠ°Π²ΠΊΠ°",
        "olib ketaman": "ππ» Π‘Π°ΠΌΠΎΠ²ΡΠ²ΠΎΠ·",
        "Buyurtmani o'zingiz olib ketasizmi yoki etkazib berishsinmi": "ΠΠ°Π±Π΅ΡΠ΅ΡΠ΅ ΡΠ²ΠΎΠΉ Π·Π°ΠΊΠ°Π· ΡΠ°ΠΌΠΎΡΡΠΎΡΡΠ΅Π»ΡΠ½ΠΎ ππ» ΠΈΠ»ΠΈ Π²ΡΠ±Π΅ΡΠΈΡΠ΅ Π΄ΠΎΡΡΠ°Π²ΠΊΡ π",
        "quyidagilardan birini tanlang": 'ΠΡΠ±Π΅ΡΠΈΡΠ΅ ΠΎΠ΄ΠΈΠ½ ΠΈΠ· ΡΠ»Π΅Π΄ΡΡΡΠΈΡ',
        'contact': "π² ΠΡΠΏΡΠ°Π²ΡΡΠ΅ ΡΠ²ΠΎΠΉ Π½ΠΎΠΌΠ΅Ρ ΡΠ΅Π»Π΅ΡΠΎΠ½Π°",
        "Mobil raqamingizni kiriting": "ΠΡΠΏΡΠ°Π²ΡΡΠ΅ ΠΈΠ»ΠΈ Π²Π²Π΅Π΄ΠΈΡΠ΅ ΡΠ²ΠΎΠΉ Π½ΠΎΠΌΠ΅Ρ ΡΠ΅Π»Π΅ΡΠΎΠ½Π° π  Π² Π²ΠΈΠ΄Π΅: +998 ** *** ****",
        "Ismingizni kiriting": 'ΠΠ²Π΅Π΄ΠΈΡΠ΅ Π²Π°ΡΠ΅ ΠΈΠΌΡ ΠΈ ΡΠ°ΠΌΠΈΠ»ΠΈΡ',
        'Familyangizni kiriting': 'ΠΠ²Π΅Π΄ΠΈΡΠ΅ Π²Π°ΡΡ ΡΠ°ΠΌΠΈΠ»ΠΈΡ',
        'Tilni tanlang uz/ru': "Tilni tanlang: / ΠΡΠ±Π΅ΡΠΈΡΠ΅ ΡΠ·ΡΠΊ",
        "Buyurtma qilish": "π ΠΠ°ΠΊΠ°Π·Π°ΡΡ",
        'welcome': "Xush kelibsiz ru",
        "ΠΠΈΡΡΡ": 'π ΠΠΈΡΡΡ',
        "Fast food": "π Fast food",
        "Π‘ΡΠΏΡ (ΠΏΠ΅ΡΠ²ΠΎΠ΅ Π±Π»ΡΠ΄ΠΎ)": "π² Π‘ΡΠΏΡ (ΠΏΠ΅ΡΠ²ΠΎΠ΅ Π±Π»ΡΠ΄ΠΎ)",
        "Π‘Π°Π»Π°ΡΡ": "π₯ Π‘Π°Π»Π°ΡΡ",
        "Π’ΡΡΠ΅ΡΠΊΠ°Ρ ΠΊΡΡΠ½Ρ": "π Π’ΡΡΠ΅ΡΠΊΠ°Ρ ΠΊΡΡΠ½Ρ",
        "ΠΠ²ΡΠΎΠΏΠ΅ΠΉΡΠΊΠ°Ρ ΠΊΡΡΠ½Ρ": "π₯ ΠΠ²ΡΠΎΠΏΠ΅ΠΉΡΠΊΠ°Ρ ΠΊΡΡΠ½Ρ",
        "ΠΠ°Π²ΡΡΠ°ΠΊΠΈ": "π? ΠΠ°Π²ΡΡΠ°ΠΊΠΈ",
        "ΠΠ΅ΡΠ΅ΡΡΡ": "π° ΠΠ΅ΡΠ΅ΡΡΡ",
        'Muloqot tili': 'Π―Π·ΡΠΊ ΠΎΠ±ΡΠ΅Π½ΠΈΡ',
        'Telefon nomer': 'Π’Π΅Π»Π΅ΡΠΎΠ½Π½ΡΠΉ Π½ΠΎΠΌΠ΅Ρ',
        'Ruscha': "π·πΊ Π ΡΡΡΠΊΠΈΠΉ",
        "O'zbekcha": "πΊπΏ Π£Π·Π±Π΅ΠΊΡΠΊΠΈΠΉ",
        "Telefon": "πΠ’Π΅Π»Π΅ΡΠΎΠ½",
        "Til": "Π―Π·ΡΠΊ πΊπΏ π·πΊ",
        "Mening buyurtmalarim": "π ΠΠΎΠΈ Π·Π°ΠΊΠ°Π·Ρ",
        "Telefon orqali aloqa": "π Π’Π΅Π»Π΅ΡΠΎΠ½Π½Π°Ρ ΡΠ²ΡΠ·Ρ",
        "Sozlash": "β ΠΠ°ΡΡΡΠΎΠΉΠΊΠΈ",
        "Ansor oilasi": "π¨βπ©βπ§βπ¦ ΠΠΊΡΠΈΠΈ",
        'savatcha': 'ΠΠΎΡΠ·ΠΈΠ½Π°',
        'Savatcha': 'π₯ ΠΠΎΡΠ·ΠΈΠ½Π°',
        "Barcha menular": "π ΠΡΠΎΡΠΌΠΎΡΡΠ΅ΡΡ ΠΌΠ΅Π½Ρ",
        "Savatni bo'shatish": "π ΠΡΠΈΡΡΠΈΡΡ ΠΊΠΎΡΠ·ΠΈΠ½Ρ",
        "checkout": "ΠΡΠΎΠ΄ΠΎΠ»ΠΆΠΈΠΌπ",
        "Biz bilan bog'laning": "Π‘Π²ΡΠΆΠΈΡΠ΅ΡΡ Ρ Π½Π°ΠΌΠΈ",
        "Menuni tanlang": "ΠΡΠ±Π΅ΡΠΈΡΠ΅ ΠΌΠ΅Π½Ρ",
        "Barcha Menularni Korish": "ΠΡΠΎΡΠΌΠΎΡΡΠ΅ΡΡ Π²ΡΠ΅ ΠΌΠ΅Π½Ρ",
        "Mahsulot narxi": "Π¦Π΅Π½Π° ΠΏΡΠΎΠ΄ΡΠΊΡΠ°",
        "Yetkazib berish narxi": "Π‘ΡΠΎΠΈΠΌΠΎΡΡΡ Π΄ΠΎΡΡΠ°Π²ΠΊΠΈ",
        "Jami": "ΠΡΠ΅",
        "savatchada": "Π ΠΊΠΎΡΠ·ΠΈΠ½Π΅",
        "Eltish vaqti": "β³ Π‘ΡΠΎΠΊ ΠΏΠΎΡΡΠ°Π²ΠΊΠΈ",
        "so'm": "UZS",
        'ta': ' ',
        "narxi": "Π¦Π΅Π½Π°",
        "ΠΡΡΡΡΠ°Ρ Π΄ΠΎΡΡΠ°Π²ΠΊΠ°": "ΠΡΡΡΡΠ°Ρ Π΄ΠΎΡΡΠ°Π²ΠΊΠ° π",
        "ΠΠ΅ΠΆΠ»ΠΈΠ²ΡΠΉ ΠΊΡΡΡΠ΅Ρ": "ΠΠ΅ΠΆΠ»ΠΈΠ²ΡΠΉ ΠΊΡΡΡΠ΅Ρ π€",
        "ΠΠΏΠ΅ΡΠ°ΡΠΎΡ ΠΌΠΎΠ»ΠΎΠ΄Π΅Ρ": "ΠΠΏΠ΅ΡΠ°ΡΠΎΡ ΠΌΠΎΠ»ΠΎΠ΄Π΅Ρ π",
        "ΠΠ΅Π»ΠΈΠΊΠΎΠ»Π΅ΠΏΠ½ΡΠΉ Π²ΠΊΡΡ": "ΠΠ΅Π»ΠΈΠΊΠΎΠ»Π΅ΠΏΠ½ΡΠΉ Π²ΠΊΡΡ π",
        'Azimov Tohir': 'ΠΠ·ΠΈΠΌΠΎΠ² Π’ΠΎΡΠΈΡ',
        "Hali hech narsa yo'q": "ΠΠΎΠΊΠ° Π½ΠΈΡΠ΅Π³ΠΎ",
        "nima boldi": "ΠΠΏΠΈΡΠΈΡΠ΅ ΡΡΠΎ ΡΠ»ΡΡΠΈΠ»ΠΎΡΡ?(Text)",
        'Botimizdan foydalanganingiz uchun rahmat': 'Π‘ΠΏΠ°ΡΠΈΠ±ΠΎ Π·Π° ΠΈΡΠΏΠΎΠ»ΡΠ·ΠΎΠ²Π°Π½ΠΈΠ΅ Π½Π°ΡΠ΅Π³ΠΎ Π±ΠΎΡΠ°, Π½Π°ΡΠΈ ΡΠΎΡΡΡΠ΄Π½ΠΈΠΊΠΈ ΡΠΊΠΎΡΠΎ Ρ Π²Π°ΠΌΠΈ ΡΠ²ΡΠΆΡΡΡΡ',
        "Yangi mahsulot qo'shish": "π ΠΠΎΠ±Π°Π²ΠΈΡΡ Π½ΠΎΠ²ΡΠΉ ΡΠΎΠ²Π°Ρ"
    }
    if lang == 'ru':
        if word in words_ru.keys():
            return words_ru[word]
        else:
            return word

    if lang == 'uz':
        if word in words_uz.keys():
            return words_uz[word]
        else:
            return word
