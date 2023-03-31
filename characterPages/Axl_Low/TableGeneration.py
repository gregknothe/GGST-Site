import pandas as pd
import sys
sys.path.append("")
import frameTrapCalc as ft

#Cmd Normals: "6P", "6K", "6H"
#Dust: "5D", "5[D]"
#Ground Specials: "[4]6S", "41236H", "214S", "214H", "236236H"
#Air Specials: "j214H", "j236H"
#Rekkas:  "[4]6S-8", "[4]6S-2", "[4]6S-S", "[4]6S-[S]"

#charName, moveName, active, recovery, onBlock, level, gatling
'''
ft.firstEntry("Axl_Low","5P",6,19,-11,2,["6P", "6K", "6H", "[4]6S", "41236H", "214S", "214H", "236236H"],"5P has +3f of blockstun at max range.")
ft.addiontalEntry("Axl_Low","5K",3,11,-2,1,["6P", "6K", "6H", "2D", "5D", "5[D]", "[4]6S", "41236H", "214S", "214H", "236236H", "jump"],"")
ft.addiontalEntry("Axl_Low","cS",6,12,-1,3,["6P", "6K", "fS", "2S", "5H", "2H", "6H", "2D", "5D", "5[D]", "[4]6S", "41236H", "214S", "214H", "236236H", "jump"],"")
ft.addiontalEntry("Axl_Low","fS",3,19,-8,2,["5H", "2H", "[4]6S", "41236H", "214S", "214H", "236236H"],"")
ft.addiontalEntry("Axl_Low","5H",4,19,-4,4,["[4]6S", "41236H", "214S", "214H", "236236H"],"")
ft.addiontalEntry("Axl_Low","5D",6,23,-15,2,[],"")
ft.addiontalEntry("Axl_Low","5[D]",6,23,-10,4,[],"")
ft.addiontalEntry("Axl_Low","2P",4,21,-13,1,["6P", "6K", "6H", "[4]6S", "41236H", "214S", "214H", "236236H"],"2P has +2f of blockstun at max range.")
ft.addiontalEntry("Axl_Low","2K",5,11,-4,1,["2D", "6P", "6K", "6H", "5D", "5[D]", "[4]6S", "41236H", "214S", "214H", "236236H"],"")
ft.addiontalEntry("Axl_Low","2S",10,23,-16,3,["5H", "2H", "[4]6S", "41236H", "214S", "214H", "236236H"],"2S has +2f of blockstun at max range.")
ft.addiontalEntry("Axl_Low","2H",9,26,-18,3,["[4]6S", "41236H", "214S", "214H", "236236H"],"2H has +2f of blockstun at max range.")
ft.addiontalEntry("Axl_Low","2D",6,17,-9,2,["[4]6S", "41236H", "214S", "214H", "236236H"],"")
ft.addiontalEntry("Axl_Low","6P",5,22,-13,2,["[4]6S", "41236H", "214S", "214H", "236236H"],"")
ft.addiontalEntry("Axl_Low","6K",5,25,-13,3,["[4]6S", "41236H", "214S", "214H", "236236H"],"6K has +2f of blockstun at max range.")
ft.addiontalEntry("Axl_Low","6H",9,13,-3,4,[],"")
ft.addiontalEntry("Axl_Low","jP",4,23,-99,1,["j214H", "j236H"],"jP has +2f of blockstun at max range.")
ft.addiontalEntry("Axl_Low","jK",3,16,-99,1,["jD", "j214H", "j236H"],"")
ft.addiontalEntry("Axl_Low","jS",4,18,-99,2,["jH", "jD", "j214H", "j236H"],"jS has +3f of blockstun at max range.")
ft.addiontalEntry("Axl_Low","jH",6,25,-99,2,["jD", "j214H", "j236H"],"jH has +3f of blockstun at max range.")
ft.addiontalEntry("Axl_Low","jD",3,22,-99,3,["j214H", "j236H"],"")
ft.addiontalEntry("Axl_Low","[4]6S",15,29,-19,3,["[4]6S-8", "[4]6S-2", "[4]6S-S", "[4]6S-[S]"],"Gap can be up to -10f at max range.")
ft.addiontalEntry("Axl_Low","[4]6S-8",15,34,-11,3,[],"")
ft.addiontalEntry("Axl_Low","[4]6S-2",36,19,-6,2,[],"")
ft.addiontalEntry("Axl_Low","[4]6S-S",10,24,-3,3,[],"")
ft.addiontalEntry("Axl_Low","[4]6S-[S]",10,24,10,4,[],"")
ft.addiontalEntry("Axl_Low","214S",3,21,3,3,[],"")
ft.addiontalEntry("Axl_Low","214H",12,29,-24,3,[],"")
ft.addiontalEntry("Axl_Low","j214H",9,10,-19,3,[],"")
ft.addiontalEntry("Axl_Low","j236H",10,7,-22,4,[],"")
ft.addiontalEntry("Axl_Low","236236H",45,26,-2,4,[],"")
'''


df = pd.read_csv("characterPages/Axl_Low/Axl_LowDataTable.txt", sep=",")
df.to_html("characterPages/Axl_Low/Axl_LowDataTable.txt", index=False)

'''
-remove all [4]6S followups aside from [4]6S
'''