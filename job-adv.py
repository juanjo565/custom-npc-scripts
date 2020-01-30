# Tepes (9390217) | San Commerci

if sm.getChr().getLevel() < 10:
    sm.sendSayOkay("You need to be level 10 to job advance.")
if sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 0:
    explorer = sm.sendSayOkay("What would you like to become?: \r\n#L0#Magician \r\n#L1#Thief. \r\n#L2#Warrior. \r\n#L3#Archer. \r\n#L4#Pirate.")
    if explorer == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a magician?")
        if response:
            sm.jobAdvance(200)
            sm.dispose()
    if explorer == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become a thief?")
        if response:
            sm.jobAdvance(400)
            sm.dispose()
    if explorer == 2:
        response = sm.sendAskYesNo("Are you sure you'd like to become a warrior?")
        if response:
            sm.jobAdvance(100)
            sm.dispose()
    if explorer == 3:
        response = sm.sendAskYesNo("Are you sure you'd like to become an archer?")
        if response:
            sm.jobAdvance(300)
            sm.dispose()
    if explorer == 4:
        response = sm.sendAskYesNo("Are you sure you'd like to become a pirate?")
        if response:
            sm.jobAdvance(500)
            sm.dispose()
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 200:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 200:
    magician = sm.sendSayOkay("What would you like to become?: \r\n#L0#Fire/Poison Magician \r\n#L1#Ice/Lightning Magician. \r\n#L2#Cleric")
    if magician == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Fire/Poison Magician?")
        if response:
            sm.jobAdvance(210)
            sm.dispose()
    if magician == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Ice/Lightning Magician?")
        if response:
            sm.jobAdvance(220)
            sm.dispose()
    if magician == 2:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Cleric?")
        if response:
            sm.jobAdvance(230)
            sm.dispose()
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 400:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 400:
    thief = sm.sendSayOkay("What would you like to become?: \r\n#L0#Bandit \r\n#L1#Assassin.")
    if thief == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Bandit?")
        if response:
            sm.jobAdvance(420)
            sm.dispose()
    if thief == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Assassin?")
        if response:
            sm.jobAdvance(410)
            sm.dispose()
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 100:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 100:
    warrior = sm.sendSayOkay("What would you like to become?: \r\n#L0#Page \r\n#L1#Fighter. \r\n#L2#Spearman.")
    if warrior == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Page?")
        if response:
            sm.jobAdvance(120)
            sm.dispose()
    if warrior == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Fighter?")
        if response:
            sm.jobAdvance(110)
            sm.dispose()
    if warrior == 2:
        response = sm.sendAskYesNo("Are you sure you'd like to become an Spearman?")
        if response:
            sm.jobAdvance(130)
            sm.dispose()
if 30 > sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 300:
    sm.sendSayOkay("Come back when you're Lv.30")
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 300:
    archer = sm.sendSayOkay("What would you like to become?: \r\n#L0#Hunter \r\n#L1#Crossbowman.")
    if archer == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Hunter?")
        if response:
            sm.jobAdvance(310)
            sm.dispose()
    if archer == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become a Crossbowman?")
        if response:
            sm.jobAdvance(320)
            sm.dispose()