if sm.getChr().getLevel() < 10:
    sm.sendSayOkay("You need to be level 10 to job advance.")
if sm.getChr().getLevel() >= 10 and sm.getChr().getJob() == 0:
    explorer = sm.sendSayOkay("What job would you like to become?: \r\n#L0#Magician \r\n#L1#Thief. \r\n#L2#Warrior. \r\n#L3#Archer. \r\n#L4#Pirate.")
    if explorer == 0:
        response = sm.sendAskYesNo("Are you sure you'd like to become a magician?")
        if response:
            sm.getChr().setJob(200)
            sm.dispose()
    if explorer == 1:
        sm.sendSayOkay("test")
    if explorer == 2:
        sm.sendSayOkay("test")
    if explorer == 3:
        sm.sendSayOkay("test")
    if explorer == 4:
        sm.sendSayOkay("test")