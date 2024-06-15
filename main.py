from pypresence import Presence
import time
import random
import string
import os
from dotenv import load_dotenv

load_dotenv()

RPC = Presence(os.getenv("TOKEN"))
RPC.connect()

img = [
    os.getenv("IMG_1"), 
    os.getenv("IMG_2"), 
    os.getenv("IMG_3")
]
    
small = os.getenv("SMALL")
end_nier = os.getenv("END_NIER")
end = os.getenv("END")

onStart = """
┏━━━━━━━━━━━━━━━━━━━━━━━━┓     
 system is up and running
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
        """

logsUp = "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
logsBottom = "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"

##обычные фразы
quotes = [
    "𝙴𝚁𝚁𝙾𝚁:𝙵𝙸𝙻𝙴_𝙽𝙾𝚃_𝙴𝚇𝙸𝚂𝚃",
    "       ツ",
    "◥◤◢◣◥◤◢◣◥◤◢◣◥◤◢◣◥◤",
    "𝙰𝙽𝙾𝚃𝙷𝙴𝚁 𝙰𝚁𝙶𝙴𝙼𝙵𝙰𝙽?",
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝙷𝙸 :𝟹",
    "      ◥◣◢◤"
]

##фразы при count = 6
glitch = [
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝙸 𝙺𝙽𝙾𝚆 𝚆𝙷𝙰𝚃 𝚄 𝚂𝙰𝚆 𝙸𝚃",
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝚆𝙷𝙰𝚃 𝚆𝙰𝚂 𝚃𝙷𝙰𝚃?",
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝙳𝙸𝙳 𝚈𝙾𝚄 𝚂𝙴𝙴 𝚃𝙷𝙰𝚃?",
    "[𝚁𝙴𝙳𝙰𝙲𝚃𝙴𝙳]: 𝙸 𝚂𝙴𝙴 𝚈𝙾𝚄",
]

##фразы при значениях threat
threat_line = [
    "𝚆𝙰𝚁#𝙸𝙽𝙶: 𝚂𝚈𝚂#𝙴𝙼__𝙵#𝙸𝙻𝚄𝚁𝙴",
    "[𝚁𝙴#𝙰𝙲_𝙴𝙳]",
    "𝚅𝙸𝚁#𝚂_𝙳𝙴#𝙴𝙲𝚃#𝙳!",
    "𝙲𝚁𝙸##𝙲𝙰𝙻_𝙴𝚁##𝚁_𝙳𝙴𝚃$𝙲?𝙴𝙳",
    "𝙰𝙽𝟶𝙼𝙰𝙻# 𝙳𝙴𝚃__?𝙲𝚃?𝙳"
]

loading = "░░░░░░░░░░░░░░░░░░░░░"
details = "═════════════════════"

##время в секундах. часовой цикл 
timerCount = 3601
##при True - запускает отсчет переменной timerCount
endIsNier = False
##случайные ивенты при определнных значениях
threat = 0
##количество иттерций при timerCount = 0
reboot = 0

##вывод ивента "загрузки" при первой итерации
first = True
prevImg = random.choice(img)
prevState = random.choice(quotes)

while True:
    ##ивент "загрузки" 
    if first == True:
        i = 0
        while i <= 81:
            if i % 4 == 0:
                k = 0
                k += 1
                loading = loading.replace("░", "█", k)

            RPC.update(
                state = "𝙻𝙾𝙰𝙳𝙸𝙽𝙶... 𝙿𝙻𝙴𝙰𝚂𝙴, 𝚆𝙰𝙸𝚃",
                details = loading,
                large_image = os.getenv("IMG_3"), 
            )

            timeRandom = random.uniform(0.0, 1.0)
            time.sleep(timeRandom)

            i += 1
 
        RPC.update(
        state = "     𝚆𝙴𝙻𝙲𝙾𝙼𝙴",
        details = loading,
        large_image = small,
        )
        time.sleep(7)
        
        loading = "░░░░░░░░░░░░░░░░░░░░"
        first = False
        print(onStart)

    ##последние 10 минут
    while timerCount < 600 and timerCount > 0:
        RPC.update(
            details = details,
            state = "   𝚃𝙷𝙴 𝚃𝙸𝙼𝙴 𝙷𝙰𝚂 𝙲𝙾𝙼𝙴",
            end = time.time() + timerCount,
            large_image = end,
        )
        time.sleep(timerCount)
        timerCount = 0
        print (timerCount)
    
    ## 100 итераций перезапуска при timerCount = 0 
    while timerCount <= 0 and reboot <= 81:
        state = ''.join(random.choices(string.digits, k=18))
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
            {"label": "𝚂𝚢𝚜𝚝𝚎𝚖 𝚛𝚎𝚋𝚘𝚘𝚝", "url": "https:://"},
            {"label": "𝚒𝚗 𝚙𝚛𝚘𝚐𝚛𝚎𝚜𝚜...", "url": "https:://"}   
            ]
        )
        reboot += 1
        time.sleep(0.7)
    
        if reboot == 81: 
            RPC.update(
            state = "   𝚂𝚈𝚂𝚃𝙴𝙼 𝚁𝙴𝚂𝚃𝙾𝚁𝙴𝙳 ",
            details = loading,
            large_image = small,
            )
            time.sleep(4.5)

            RPC.update(
            state = "     𝚆𝙴𝙻𝙲𝙾𝙼𝙴",
            details = loading,
            large_image = small,
            )
            time.sleep(2.5)

            ##возврат к изначальным значениям
            timerCount = 3601
            endIsNier = False
            threat = 0
            reboot = 0
            loading = "░░░░░░░░░░░░░░░░░░░░"
            details = "═════════════════════"
            print("system restarted")

    count = random.randint(0,9)
    state = random.choice(quotes)
    imageChoice = random.choice(img)
    
    if count == 9 and threat >= 10:
        print("loading. please, wait")

        i = 0
        while i <= 81:
            if i % 4 == 0:
                k = 0
                k += 1
                loading = loading.replace("░", "█", k)

            RPC.update(
                state = "𝙻𝙾𝙰𝙳𝙸𝙽𝙶... 𝙿𝙻𝙴𝙰𝚂𝙴, 𝚆𝙰𝙸𝚃",
                details = loading,
                large_image = os.getenv("IMG_3"), 
            )

            timeRandom = random.uniform(0.0, 1.0)
            time.sleep(timeRandom)

            i += 1
    
        loading = "░░░░░░░░░░░░░░░░░░░░"
    
    while imageChoice == prevImg:
        imageChoice = random.choice(img)

    while state == prevState:
        state = random.choice(quotes)

    ##автоматически вызывает ивент glitch
    if threat >= 10:
        state = random.choice(threat_line)

    if threat == 20:
        count = 6

    print(logsUp)
    print(" number:", count)
    print(" state:", state)

    if imageChoice == os.getenv("IMG_1"):
        print(" image: 1232.gif")
    elif imageChoice == os.getenv("IMG_2"):
        print(" image: GGV2.png")
    elif imageChoice == os.getenv("IMG_3"):
        print(" image: large.gif")
        
    print(" time:", timerCount)
    print(" threat level:", threat)
    print(logsBottom)

    ##обычное состояние RP
    RPC.update(
        state = state,
        details = details,
        large_image = imageChoice,
        large_text = "𝚆𝙷𝙰𝚃 𝙳𝙸𝙳 𝚈𝙾𝚄 𝙴𝚇𝙿𝙴𝙲𝚃 𝚃𝙾 𝚂𝙴𝙴 𝙷𝙴𝚁𝙴?",
        small_image = small,
        small_text = "𝚌𝚛𝚎𝚊𝚝𝚎𝚍 𝚘𝚗 𝚙𝚢𝚙𝚛𝚎𝚜𝚎𝚗𝚌𝚎",
        buttons =  [
        {"label": "DEVIL DAGGERS.INFO", "url": "https://devildaggers.info/leaderboard/player/240450"}, 
        {"label": "ELITE STEAM CHARTS", "url": "https://steamcharts.com/app/359320"}
        ],
    )
    prevImg = imageChoice
    prevState = state

    time.sleep(21)

    threat += 1

    if endIsNier == True:
        timerCount -= 21

    ##glitch ивент при определнных значениях
    if count == 6:
        count = 0
        threat = 0

        if endIsNier == False:
            print("""
---------- 
vir#s_de#ect#d! 
----------
            """)
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
            details = details,
            end = time.time() + timerCount,
            large_image = end,
            large_text = "𝙸 𝙺𝙽𝙾𝚆 𝚆𝙷𝙰𝚃 𝚄 𝚂𝙰𝚆 𝙸𝚃",
            buttons =  [
            {"label": "𝙸 𝙺𝙽𝙾𝚆 𝚆𝙷𝙰𝚃", "url": "https://"}, 
            {"label": "𝚈𝙾𝚄 𝙳𝙸𝙳", "url": "https://"}
            ]
        )
        time.sleep(11)
        endIsNier = True

        timerCount -= 60
    