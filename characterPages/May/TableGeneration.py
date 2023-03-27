import pandas as pd
import sys
sys.path.append("")
import frameTrapCalc as ft

#Cmd Normals: "6P", "6K", "3K", "6H"
#Dust: "5D", "5[D]"
#Ground Specials: "[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"
#Air Specials: "j632146H"

#charName, moveName, active, recovery, onBlock, level, gatling

ft.firstEntry("May","5P",3,8,-1,0,["5P", "2P", "6P", "6K", "3K", "6H", "[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","5K",6,11,-5,1,["5D", "5[D]", "2D", "6P", "6K", "3K", "6H", "[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H", "jump"],"")
ft.addiontalEntry("May","cS",6,7,3,3,["fS", "2S", "5H", "2H", "6P", "6K", "3K", "6H", "5D", "5[D]", "2D", "[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H", "jump"],"")
ft.addiontalEntry("May","fS",3,19,-8,2,["5H", "2H", "[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","5H",8,15,-4,4,["[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","5D",3,26,-15,2,[],"")
ft.addiontalEntry("May","5[D]",3,25,-10,4,[],"")
ft.addiontalEntry("May","2P",4,8,-2,0,["5P", "2P", "6P", "6K", "3K", "6H", "[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","2K",4,10,-2,1,["6P", "6K", "3K", "6H" ,"5D", "5[D]", "2D", "[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","2S",3,18,-7,2,["5H", "2H", "[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","2H",13,26,-20,4,["[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","2D",7,17,-7,3,["[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","6P",6,18,-7,3,["[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"")
ft.addiontalEntry("May","6K",5,11,-2,2,[],"")
ft.addiontalEntry("May","3K",9,15,-10,2,[],"")
ft.addiontalEntry("May","6H",6,24,-8,4,["[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"Hits all but Pot/Anji/GL 3 frames after becoming active, so the gap is -3f.")
ft.addiontalEntry("May","6[H]",6,24,8,4,["[4]6S", "[4]6H", "[2]8S", "[2]8H", "623K", "214P", "214K", "236236S", "632146H"],"Hits all but Pot/Anji/GL 3 frames after becoming active, so the gap is -3f.")
ft.addiontalEntry("May","jP",3,12,-99,0,["jP"],"")
ft.addiontalEntry("May","jK",3,12,-99,1,["jD"],"")
ft.addiontalEntry("May","jS",4,15,-99,2,["jH", "jD"],"")
ft.addiontalEntry("May","jH",10,15,-99,3,["jD"],"")
ft.addiontalEntry("May","jD",6,21,-99,4,[],"")
ft.addiontalEntry("May","j2H",99,6,-99,3,[],"")
ft.addiontalEntry("May","[4]6S",9,24,-3,2,[],"")
ft.addiontalEntry("May","[4]6H",9,18,7,4,[],"")
ft.addiontalEntry("May","[2]8S",19,21,0,2,[],"May is airborne on block, add a few frames to the gap if Input2 is not a air button")
ft.addiontalEntry("May","[2]8H",27,19,6,3,[],"May is airborne on block, add a few frames to the gap if Input2 is not a air button")
ft.addiontalEntry("May","214P",6,45,29,2,[],"")
ft.addiontalEntry("May","214K",10,45,29,2,[],"")
ft.addiontalEntry("May","236236S",99,88,-54,4,[],"")
ft.addiontalEntry("May","632146H",44,55,-21,4,[],"")


df = pd.read_csv("characterPages/May/MayDataTable.txt", sep=",")
df.to_html("characterPages/May/MayDataTable.txt", index=False)

'''
-
-
'''