import pandas as pd
import sys
sys.path.append("")
import frameTrapCalc as ft

#Cmd Normals: "6P", "6K", "6H"
#Dust: "5D", "5[D]"
#Ground Specials: "236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"
#Air Specials: "j236P", "j236K", "j623S", "j214P", "j632146H"
#Rekkas:  "236S-236S", "236S-236K", "236S-236S-236K" 

#charName, moveName, active, recovery, onBlock, level, gatling

ft.firstEntry("Chipp_Zanuff","5P",2,10,-2,0,["5P", "2P", "6P", "6K", "6H", "236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","5K",5,8,-3,0,["5K", "2K", "2D", "6P", "6K", "6H", "5D", "5[D]", "236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P", "jump"],"")
ft.addiontalEntry("Chipp_Zanuff","cS",6,10,1,3,["fS", "2S", "5H", "2H", "2D", "5D", "5[D]", "6P", "6K", "6H", "236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P", "jump"],"")
ft.addiontalEntry("Chipp_Zanuff","fS",2,20,-8,2,["5H", "2H", "236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","5H",7,16,-4,4,["236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","5D",5,24,-15,2,[],"")
ft.addiontalEntry("Chipp_Zanuff","5[D]",5,24,-10,4,[],"")
ft.addiontalEntry("Chipp_Zanuff","2P",2,10,-2,0,["5P", "2P", "6P", "6K", "6H", "236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","2K",4,8,-2,0,["6P", "6K", "6H", "2D", "5D", "5[D]", "236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","2S",4,17,-7,2,["5H", "2H", "236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","2H",9,24,-14,4,["236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","2D",2,19,-7,2,["236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","6P",5,25,-16,3,["236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","6K",5,9,-2,1,[],"")
ft.addiontalEntry("Chipp_Zanuff","6H",6,18,-5,4,["236P", "236K", "623S", "236H", "236S", "63214S", "632146H", "236236P"],"")
ft.addiontalEntry("Chipp_Zanuff","jP",4,8,-99,0,["jP", "j2K", "j236P", "j236K", "j623S", "j214P", "j632146H"],"")
ft.addiontalEntry("Chipp_Zanuff","jK",7,8,-99,1,["j2K", "jD", "j236P", "j236K", "j623S", "j214P", "j632146H"],"")
ft.addiontalEntry("Chipp_Zanuff","jS",4,18,-99,2,["jH", "jD", "j236P", "j236K", "j623S", "j214P", "j632146H"],"")
ft.addiontalEntry("Chipp_Zanuff","jH",12,17,-99,2,["jD", "j236P", "j236K", "j623S", "j214P", "j632146H"],"")
ft.addiontalEntry("Chipp_Zanuff","jD",4,22,-99,2,["j236P", "j236K", "j623S", "j214P", "j632146H"],"")
ft.addiontalEntry("Chipp_Zanuff","j2K",1,0,-99,1,[],"")
ft.addiontalEntry("Chipp_Zanuff","236P",3,19,-4,1,[],"")
ft.addiontalEntry("Chipp_Zanuff","j236P",3,33,-99,1,[],"")
ft.addiontalEntry("Chipp_Zanuff","236K",3,17,-2,1,[],"")
ft.addiontalEntry("Chipp_Zanuff","623S",20,23,-27,2,[],"")
ft.addiontalEntry("Chipp_Zanuff","236H",7,42,9,2,[],"")
ft.addiontalEntry("Chipp_Zanuff","236S",5,16,-4,3,["236S-236S", "236S-236K"],"")
ft.addiontalEntry("Chipp_Zanuff","236S-236S",2,21,-6,3,["236S-236S-236K"],"")
ft.addiontalEntry("Chipp_Zanuff","236S-236K",6,20,-9,3,[],"")
ft.addiontalEntry("Chipp_Zanuff","236236P",99,-99,-20,0,[],"")
ft.rekkaDeletion("Chipp_Zanuff", "236S", ["236S-236S", "236S-236K"])
#Its not deleting the valeus
'''

df = pd.read_csv("characterPages/Chipp_Zanuff/Chipp_ZanuffDataTable.txt", sep=",")
df.to_html("characterPages/Chipp_Zanuff/Chipp_ZanuffDataTable.txt", index=False)

-deal with rekkas
'''