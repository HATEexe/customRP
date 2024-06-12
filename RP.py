from pypresence import Presence
import time
import random
import string
import os
from dotenv import load_dotenv

load_dotenv()

RPC = Presence(os.getenv("TOKEN"))
RPC.connect()

##импорт из .env
img = os.getenv("IMG_1"), os.getenv("IMG_2"), os.getenv("IMG_3")
small = os.getenv("SMALL")
end_nier = os.getenv("END_NIER")
end = os.getenv("END")
reboot_img = os.getenv("REBOOT")

##обычные фразы
quotes = [
    "𝙴𝚁𝚁𝙾𝚁:𝙵𝙸𝙻𝙴_𝙽𝙾𝚃_𝙴𝚇𝙸𝚂𝚃",
    "𝙾𝚗𝚕𝚢 𝚍𝚎𝚊𝚝𝚑 𝚠𝚒𝚕𝚕 𝚖𝚊𝚔𝚎 𝚖𝚎 𝚑𝚊𝚙𝚙𝚢...",
    "       ツ",
    "◥◤◢◣◥◤◢◣◥◤◢◣◥◤◢◣◥◤",
    "𝙰𝙽𝙾𝚃𝙷𝙴𝚁 𝙰𝚁𝙶𝙴𝙼𝙵𝙰𝙽?",
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝙷𝙸 :𝟹",
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝙸 𝙺𝙽𝙾𝚆 𝚄 𝚂𝙴𝙴 𝚃𝙷𝙰𝚃"
]

##фразы при count = 6
glitch = [
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝙸 𝙺𝙽𝙾𝚆 𝚆𝙷𝙰𝚃 𝚄 𝚂𝙰𝚆 𝙸𝚃",
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝚆𝙷𝙰𝚃 𝚆𝙰𝚂 𝚃𝙷𝙰𝚃?",
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝙳𝙸𝙳 𝚈𝙾𝚄 𝚂𝙴𝙴 𝚃𝙷𝙰𝚃?"
]

##фразы при значениях threat
threat_line = [
    "𝚆𝙰𝚁#𝙸𝙽𝙶. 𝚂𝚈𝚂#𝙴𝙼__𝙵#𝙸𝙻𝚄𝚁𝙴",
    "[𝚁𝙴#𝙰𝙲_𝙴𝙳]",
]

loading = "░░░░░░░░░░░░░░░░░░░░░░░░░"

##сохранят 24-х часовой цикл 
timerCount = 86400
timerCount = 10
##при True - запускает отсчет переменной timerCount
endIsNier = False
##случайные ивенты при определнных значениях
threat = 30
##количество иттерций при timerCount = 0
reboot = 0

while True:
    ## 100 итерация перезапуска при timerCount = 0 
    while timerCount <= 0 and reboot <= 100:
        state = ''.join(random.choices(string.digits, k=23))
        print(state)
        if reboot % 4 == 0:
            k = 0
            k += 1
            loading = loading.replace("░", "█", k)
        RPC.update(
            state = "𝙳𝙴𝙲𝙾𝙳𝙸𝙽𝙶: " + state,
            details = loading,
            large_image = end,
            large_text = "𝚃𝙷𝙴 𝙴𝙽𝙳",
            buttons = [
            {"label": "𝚂𝚢𝚜𝚝𝚎𝚖 𝚛𝚎𝚋𝚘𝚘𝚝 ", "url": "https:://"},
            {"label": "𝚒𝚗 𝚙𝚛𝚘𝚐𝚛𝚎𝚜𝚜...", "url": "https:://"}   
            ]
        )
        reboot += 1
        time.sleep(1)
    
        if reboot == 100: 
            RPC.update(
            state = "𝚂𝚈𝚂𝚃𝙴𝙼 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳",
            details = loading,
            large_image = end,
            )
            time.sleep(6)

            ##возврат к изначальным значениям
            timerCount = 86400
            endIsNier = False
            threat = 0
            reboot = 0
            loading = "░░░░░░░░░░░░░░░░░░░░░░░░░"
            print("system restarted")

    count = random.randint(0,9)
    state = random.choice(quotes)
    imageChoice = random.choice(img)

    ##автоматически вызывает мивент glitch 
    if threat == 30:
        count = 6

    if threat >= 10 and threat < 12:
        state = "##########################"
    if threat >= 20:
        state = random.choice(threat_line)
    
    print("-------")
    print("number:", count)

    print("state:", state)
    if imageChoice == os.getenv("IMG_1"):
        print("image: 1232.gif")
    elif imageChoice == os.getenv("IMG_2"):
        print("image: GGV2.png")
    elif imageChoice == os.getenv("IMG_3"):
        print("image: large.gif")
    print("time:", timerCount)
    print("threat level:", threat)

    ##обычное состояние RP
    RPC.update(
        state = state,
        details = "═══════════════════════",
        end = time.time() + 21,
        large_image = imageChoice,
        large_text = "𝚆𝙷𝙰𝚃 𝙳𝙸𝙳 𝚈𝙾𝚄 𝙴𝚇𝙿𝙴𝙲𝚃 𝚃𝙾 𝚂𝙴𝙴 𝙷𝙴𝚁𝙴?",
        small_image = small,
        small_text = "𝚌𝚛𝚎𝚊𝚝𝚎𝚍 𝚘𝚗 𝚙𝚢𝚙𝚛𝚎𝚜𝚎𝚗𝚌𝚎",
        buttons =  [
        {"label": "DEVIL DAGGERS.INFO", "url": "https://devildaggers.info/leaderboard/player/240450"}, 
        {"label": "ELITE STEAM CHARTS", "url": "https://steamcharts.com/app/359320"}
        ],
    )

    time.sleep(2)

    if endIsNier == True:
        timerCount -= 21
    threat += 1

    ##glitch ивент при определнных значениях
    if count == 6 and threat >= 10:
        count = 0
        threat = 0

        print("-------")
        if endIsNier == False:
            print("vir#s_de#ect#d!")

        while count < 80:
            btn1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            btn2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            RPC.update(
                state = "       ",
                end = time.time(),
                large_image = end_nier,
                buttons =  [
                {"label": btn1, "url": "https://"}, 
                {"label": btn2, "url": "https://"}
                ]
            )
            time.sleep(0.03)
            count += 1

        state = random.choice(glitch)
        print(state)
        RPC.update(
            state = state,
            details = "═══════════════════════",
            end = time.time() + timerCount,
            large_image = end,
            large_text = "𝙸 𝙺𝙽𝙾𝚆 𝚆𝙷𝙰𝚃 𝚄 𝚂𝙰𝚆 𝙸𝚃",
            buttons =  [
            {"label": "𝙸 𝙺𝙽𝙾𝚆 𝚆𝙷𝙰𝚃", "url": "https://"}, 
            {"label": "𝚈𝙾𝚄 𝙳𝙸𝙳", "url": "https://"}
            ]
        )
        time.sleep(9)
        endIsNier = True
        print("-------")

        timerCount -= 9
