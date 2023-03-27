import pandas as pd
import sys
sys.path.append("")
import frameTrapCalc as ft

#Cmd Normals: "6P", "6K", "6H"
#Dust: "5D", "5[D]"
#Ground Specials: "236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"
#Air Specials: "j236S", "j236H", "j623S", "j623H", "j632146H" 

#charName, moveName, active, recovery, onBlock, level, gatling
'''
ft.firstEntry("Ky_Kiske","5P",4,7,-1,0,["5P","2P","6P", "6K", "6H","236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","5K",8,6,-2,1,["6P","6K","6H","5D","5[D]","2D","236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H", "jump"],"")
ft.addiontalEntry("Ky_Kiske","cS",6,10,1,3,["6P","6K","fS","2S","5H","2H","6H","5D","5[D]","2D","236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H", "jump"],"")
ft.addiontalEntry("Ky_Kiske","fS",6,13,-5,2,["5H","2H","236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","5H",6,21,-8,4,["236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","5D",4,25,-15,2,[],"")
ft.addiontalEntry("Ky_Kiske","5[D]",4,25,-10,2,[],"")
ft.addiontalEntry("Ky_Kiske","2P",4,8,-2,0,["5P","2P","6P","6K","6H","236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","2K",4,10,-2,1,["6P", "6K", "6H","5D","5[D]", "2D", "236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","2S",2,20,-9,2,["5H","2H","236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","2H(1)",1,28,-13,3,["236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","2H(2)",4,28,-13,4,["236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","2D",5,17,-8,2,["236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","6P",5,17,-8,2,["236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","6K",2,11,4,3,["236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","6H",4,20,-7,3,["236S","SS-236S","DI-236S","236H","SS-236H","DI-236H" "236K", "SS-236K", "DI-236K", "214K", "SS-214K", "DI-214K", "623S", "DI-623S", "623H", "DI-623H", "214S", "SS-214S", "DI-214S", "632146H", "DI-632146H", "236236P", "SS-236236P", "DI-236236P", "214214H"],"")
ft.addiontalEntry("Ky_Kiske","jP",3,9,-99,0,["jP","j236S", "j236H", "j623S", "j623H", "j632146H"],"")
ft.addiontalEntry("Ky_Kiske","jK",4,8,-99,1,["jD","j236S", "j236H", "j623S", "j623H", "j632146H"],"")
ft.addiontalEntry("Ky_Kiske","jS",3,21,-99,2,["jH","jD","j236S", "j236H", "j623S", "j623H", "j632146H"],"")
ft.addiontalEntry("Ky_Kiske","jH",4,23,-99,2,["jD","j236S", "j236H", "j623S", "j623H", "j632146H"],"")
ft.addiontalEntry("Ky_Kiske","jD",6,15,-99,2,["j236S", "j236H", "j623S", "j623H", "j632146H"],"")
ft.addiontalEntry("Ky_Kiske","236S",99,46,-15,2,[],"")
ft.addiontalEntry("Ky_Kiske","SS-236S",99,46,-15,2,[],"")
ft.addiontalEntry("Ky_Kiske","DI-236S",99,46,-11,2,[],"")
ft.addiontalEntry("Ky_Kiske","236H",99,62,22,4,[],"")
ft.addiontalEntry("Ky_Kiske","SS-236H",99,62,25,4,[],"")
ft.addiontalEntry("Ky_Kiske","DI-236H",99,62,45,4,[],"")
ft.addiontalEntry("Ky_Kiske","236K",3,26,-15,2,[],"")
ft.addiontalEntry("Ky_Kiske","SS-236K",3,26,-10,2,[],"")
ft.addiontalEntry("Ky_Kiske","DI-236K",3,26,-10,2,[],"")
ft.addiontalEntry("Ky_Kiske","214K",11,6,-2,1,[],"The gap is -2f smaller when standing")
ft.addiontalEntry("Ky_Kiske","SS-214K",11,6,5,4,[],"The gap is -2f smaller when standing")
ft.addiontalEntry("Ky_Kiske","DI-214K",6,6,7,4,[],"The gap is -2f smaller when standing")
ft.addiontalEntry("Ky_Kiske","623S",4,43,-33,2,[],"")
ft.addiontalEntry("Ky_Kiske","DI-623S",4,43,-26,4,[],"")
ft.addiontalEntry("Ky_Kiske","623H",8,44,-38,2,[],"")
ft.addiontalEntry("Ky_Kiske","DI-623H",6,39,-22,4,[],"")
ft.addiontalEntry("Ky_Kiske","214S",3,25,-8,3,[],"")
ft.addiontalEntry("Ky_Kiske","SS-214S",3,25,-6,4,[],"")
ft.addiontalEntry("Ky_Kiske","DI-214S",3,25,-6,4,[],"")
ft.addiontalEntry("Ky_Kiske","632146H",2,99,-82,4,[],"")
ft.addiontalEntry("Ky_Kiske","DI-632146H",2,99,-79,4,[],"")
ft.addiontalEntry("Ky_Kiske","236236P",99,32,10,4,[],"")
ft.addiontalEntry("Ky_Kiske","SS-236236P",99,32,26,4,[],"")
ft.addiontalEntry("Ky_Kiske","DI-236236P",99,32,32,4,[],"")
ft.addiontalEntry("Ky_Kiske","214214H",5,25,4,4,[],"")
'''


df = pd.read_csv("characterPages/Ky_Kiske/Ky_KiskeDataTable.txt", sep=",")
df.to_html("characterPages/Ky_Kiske/Ky_KiskeHTML.txt", index=False)

'''
-Anything with jDP or air fireball as the first move
-remove all non-gatling 5H(1)
'''