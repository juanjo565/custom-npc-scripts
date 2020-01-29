answer = sm.sendNext("Pick a category: \r\n#L0#Magician Equips. \r\n#L1#Thief Equips. \r\n#L2#Warrior Equips. \r\n#L3#Archer Equips. \r\n#L4#Pirate Equips. \r\n#L5#Common Equips. \r\n#L6#ETC.")


if answer == 0:
	MagicianEquips = sm.sendSayOkay("\r\n#L0#Magician Shoes. \r\n#L1#Magician Overalls. \r\n#L2#Magician Gloves.\r\n#L3#Magician Hats. \r\n#L4#Magician Shields. \r\n#L5#Magician Wands. \r\n#L6#Magician Medals. \r\n#L7#Magician Face. \r\n#L8#Magician Cape.\r\n#L9#Magician Top. \r\n#L10#Magician Bottom. \r\n#L11#Magician ETC. \r\n#L12#Magician Staves.")
	if MagicianEquips == 0:
		sm.openShop(2080004) #replace with right shop id
	if MagicianEquips == 1:
		sm.openShop()
	if MagicianEquips == 2:
		sm.openShop()
	if MagicianEquips == 3:
		sm.openShop()
	if MagicianEquips == 4:
		sm.openShop()
	if MagicianEquips == 5:
		sm.openShop()
	if MagicianEquips == 6:
		sm.openShop()
	if MagicianEquips == 7:
		sm.openShop()
	if MagicianEquips == 9:
		sm.openShop()
	if MagicianEquips == 10:
		sm.openShop()
	if MagicianEquips == 11:
		sm.openShop()
elif answer == 1:
	#same for other jobs