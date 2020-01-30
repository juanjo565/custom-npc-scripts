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
if sm.getChr().getLevel() >= 30 and sm.getChr().getJob() == 200:
    magician = sm.sendSayOkay("What would you like to become?: \r\n#L0#Fire/Poison Magician \r\n#L1#Ice/Lightning Magician.")
    if magician == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become an archer?")
        if response:
            sm.jobAdvance(210)
            sm.dispose()
    if magician == 1:
        response = sm.sendAskYesNo("Are you sure you'd like to become an archer?")
        if response:
            sm.jobAdvance(220)
            sm.dispose()
