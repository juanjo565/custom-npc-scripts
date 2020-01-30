# Tepes (9390217) | San Commerci

if sm.getChr().getLevel() < 10:
    sm.sendSayOkay("You need to be level 10 to job advance.")
if sm.getChar().getLevel() >= 10 and sm.getChr().getJob() == 0:
    sm.sendSendOkay("What job would you like to become?: ")