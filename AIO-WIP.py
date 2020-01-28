answer = sm.sendNext("Pick a category: \r\n#L0#Magician Equips. \r\n#L1#Thief Equips. \r\n#L2#Warrior Equips. \r\n#L3#Archer Equips. \r\n#L4#Pirate Equips. \r\n#L5#Common Equips. \r\n#L6#ETC.")


if answer == 0:
	MagicianEqupips = sm.sendSayOkay("\r\n#L0#Magician Shoes. \r\n#L1#Magician Overalls. \r\n#L2#Magician Gloves.")
	if MagicianEqupips == 0:
		sm.openShop(2080004) 
	if MagicianEqupips == 1:
		sm.sendSayOkay("test2.")

elif answer == 1:
	sm.sendSayOkay("Warrior Equips: ")
