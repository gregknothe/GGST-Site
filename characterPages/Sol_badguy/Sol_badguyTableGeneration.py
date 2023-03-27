import pandas as pd
import sys
sys.path.append("")
import frameTrapCalc as ft

#Cmd Normals: "6P", "6S", "6H"
#Dust: "5D", "5[D]"
#Ground Specials: "236P","623S","623H","236K","214K","623K","632146H"
#Air Specials: "j623S", "j623H", "j236K", "j236KK", "j214K", "j214[K]"

#charName, moveName, active, recovery, onBlock, level, gatling
'''
ft.firstEntry("Sol_badguy","5P",5,9,-2,1,["5P","2P","6P","236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","5K(1)",1,25,-16,0,["6P", "6S", "6H", "5D", "5[D]", "2D", "236P","623S","623H","236K","214K","623K","632146H", "jump"],"")
ft.addiontalEntry("Sol_badguy","5K(2)",4,25,-16,1,["6P", "6S", "6H", "5D", "5[D]", "2D", "236P","623S","623H","236K","214K","623K","632146H", "jump"],"")
ft.addiontalEntry("Sol_badguy","cS",6,10,3,4,["6P","fS","2S","6S","5H","2H","6H","5D","5[D]","2D","236P","623S","623H","236K","214K","623K","632146H","jump"],"")
ft.addiontalEntry("Sol_badguy","fS",2,13,2,3,["5H", "2H", "236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","5H",4,20,-5,4,["236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","5D",3,26,-15,2,[],"")
ft.addiontalEntry("Sol_badguy","5[D]",3,26,-10,2,[],"")
ft.addiontalEntry("Sol_badguy","2P",4,8,-2,0,["5P","2P","6P","6S","6H","236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","2K",3,11,-2,1,["6P", "6S", "6H", "5D", "5[D]", "2D", "236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","2S",6,15,-7,2,["5H", "2H", "236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","2H",5,31,-17,4,["236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","2D",3,18,-4,3,["236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","6P",5,20,-11,2,["236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","6S",6,20,-9,3,["236P","623S","623H","236K","214K","623K","632146H"],"")
ft.addiontalEntry("Sol_badguy","6H",3,43,-27,4,[],"")
ft.addiontalEntry("Sol_badguy","jP",3,8,-99,0,["jP","j623S", "j623H", "j236K", "j236KK", "j214K", "j214[K]"],"")
ft.addiontalEntry("Sol_badguy","jK",3,20,-99,1,["jD","j623S", "j623H", "j236K", "j236KK", "j214K", "j214[K]"],"")
ft.addiontalEntry("Sol_badguy","jS",3,23,-99,2,["jH","jD","j623S", "j623H", "j236K", "j236KK", "j214K", "j214[K]"],"")
ft.addiontalEntry("Sol_badguy","jH",12,0,-99,2,["jD", "j623S", "j623H", "j236K", "j236KK", "j214K", "j214[K]"],"")
ft.addiontalEntry("Sol_badguy","jD",3,17,-99,3,["j623S", "j623H", "j236K", "j236KK", "j214K", "j214[K]"],"")
ft.addiontalEntry("Sol_badguy","236P",8,54,-10,2,[],"")
ft.addiontalEntry("Sol_badguy","623S",14,28,-28,2,[],"")
ft.addiontalEntry("Sol_badguy","623H",16,29,-26,2,[],"")
ft.addiontalEntry("Sol_badguy","236K",6,15,-7,2,["236K-K"],"")
ft.addiontalEntry("Sol_badguy","236K-K",2,17,-11,2,[],"")
ft.addiontalEntry("Sol_badguy","j236K",6,6,-99,2,["j236K-K"],"")
ft.addiontalEntry("Sol_badguy","j236K-K",2,17,-99,2,[],"")
ft.addiontalEntry("Sol_badguy","214K",7,12,-2,3,[],"")
ft.addiontalEntry("Sol_badguy","j214K",99,18,-99,3,[],"")
ft.addiontalEntry("Sol_badguy","j214[K]",99,18,-99,3,[],"")
ft.addiontalEntry("Sol_badguy","214S",2,32,-17,3,[],"")
ft.addiontalEntry("Sol_badguy","214[S]",8,26,-17,3,[],"")
ft.addiontalEntry("Sol_badguy","41236H",3,16,11,4,[],"")
ft.addiontalEntry("Sol_badguy","632146H",43,41,-44,3,[],"")
'''
df = pd.read_csv("characterPages/Sol_badguy/Sol_badguyDataTable.txt", sep=",")
df.to_html("characterPages/Sol_badguy/Sol_badguyHTML.txt", index=False)

'''
-remove all x > 236K-K and j236K-K except for 236K/j236K
-remove all non-gatling 5K(1)
'''