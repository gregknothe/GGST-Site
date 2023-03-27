import pandas as pd

def frameTrapCalc(charName, moveName, active, recovery, onBlock, level, gatling, note=""):
    blockStun = [9,11,13,16,18]
    frameData = pd.read_csv("cleanedFrameData/"+charName+".txt", sep="/")
    ft, sit, imgString, noteList = [], [], [], []
    for x in range(len(frameData["Input"])):
        if (frameData["Input"][x] in gatling) and ("j" not in moveName) and ("j" not in frameData["Input"]):
        #B -G-> B
            ft.append(blockStun[level]-frameData["Startup"][x])
            sit.append("Ground Gatling")
            #print(frameData["Input"][x]+": B -G-> B")
        elif (frameData["Input"][x] not in gatling) and ("j" not in moveName) and ("j" not in frameData["Input"][x]):
        #B -X-> B
            ft.append(onBlock - frameData["Startup"][x])
            sit.append("Ground Non-Gatling")
            #print(frameData["Input"][x]+": B -X-> B")
        elif (frameData["Input"][x] in gatling) and ("j" in moveName) and ("j" in frameData["Input"][x]):
        #jB -G-> jB
            ft.append(blockStun[level]-frameData["Startup"][x])
            sit.append("Air Gatling")
            #print(frameData["Input"][x]+": jB -G-> jB")
        elif (frameData["Input"][x] not in gatling) and ("j" in moveName) and ("j" in frameData["Input"][x]):
        #jB -X-> jB
            ft.append(blockStun[level]-active-recovery-frameData["Startup"][x])
            sit.append("Air Non-Gatling")
            #print(frameData["Input"][x]+": jB -X-> jB")
        elif ("jump" in gatling) and ("j" not in moveName) and ("j" in frameData["Input"][x]):
        #B -G-> jB
            if charName in ["Nagoriyuki", "Goldlewis_Dickinson", "Potemkin"]:
                ft.append(blockStun[level]-5-frameData["Startup"][x])
            else:
                ft.append(blockStun[level]-4-frameData["Startup"][x])
            sit.append("Ground Jump Cancel")
            #print(frameData["Input"][x]+": B -G-> jB")
        elif ("jump" not in gatling) and ("j" not in moveName) and ("j" in frameData["Input"][x]):
        #B -X-> jB
            if charName in ["Nagoriyuki", "Goldlewis_Dickinson", "Potemkin"]:
                ft.append(onBlock-5-frameData["Startup"][x])
            else:
                ft.append(onBlock-4-frameData["Startup"][x])
            sit.append("Ground Non-Jump Cancel")
            #print(frameData["Input"][x]+": B -X-> jB")      
        else:
        #jB -> B
            if ("Until" in str(recovery)):
                landingRecovery = int(recovery.split("+")[1])
                ft.append(blockStun[level] - landingRecovery - frameData["Startup"][x])
                #print(frameData["Input"][x]+": jB -L-> B")
            else:
                ft.append(blockStun[level]-frameData["Startup"][x])
                #print(frameData["Input"][x]+": jB -N-> B")
            sit.append("Jump-in")
    #print(frameData["Input"])
    #print(ft)
        imgString.append("<img src='"+frameData["Input"][x]+".png'></img>")
        print("----framedata: "+str(frameData["Notes"][x]))
        print("----note: "+note)
        if (frameData["Notes"][x] == "nan") and (note == ""):
            noteList.append("nan")
        elif (frameData["Notes"][x] == "nan") and (note != ""):
            noteList.append(note)
        elif (frameData["Notes"][x] != "nan") and (note != ""):
            noteList.append(note + " <br> " + str(frameData["Notes"][x]))
            noteList[x] = noteList[x].split(" <br> nan")[0]
        else: 
            noteList.append(frameData["Notes"][x])
        print(noteList[x])
    ft = [str(int(x * -1))+"f" for x in ft]
    firstMove = [moveName] * len(frameData["Input"])
    firstImg = ["<img src='"+moveName+".png'></img>"] * len(frameData["Input"])
    df = pd.DataFrame(data={"Input1": firstMove, "IMG1": firstImg, "Input2": frameData["Input"], "IMG2": imgString, "Gap": ft, "Situation": sit, "Note": noteList}) 
    return df

def firstEntry(charName, moveName, active, recovery, onBlock, level, gatling, note):
    df = frameTrapCalc(charName, moveName, active, recovery, onBlock, level, gatling, note)
    df.to_csv("characterPages/"+charName+"/"+charName+"DataTable.txt", sep=",", index=False)
    print("Initial table generated")
    return 

def addiontalEntry(charName, moveName, active, recovery, onBlock, level, gatling, note):
    df = pd.read_csv("characterPages/"+charName+"/"+charName+"DataTable.txt", sep=",")
    ft = frameTrapCalc(charName, moveName, active, recovery, onBlock, level, gatling, note)
    df = pd.concat([df,ft])
    df.to_csv("characterPages/"+charName+"/"+charName+"DataTable.txt", sep=",", index=False)
    print(moveName+" has been added to "+charName+"'s table")
    return 



#print(frameTrapCalc("Sol_Badguy","5P",1,-2,5,9,["5P","2P","6P","236P","623S","623H","236K","214K","623K","632146H"]))
#print(frameTrapCalc("Sol_Badguy","cS",4,3,6,10,["6P","fS","2S","6S","5H","2H","6H","5D","5[D]","2D","236P","623S","623H","236K","214K","623K","632146H","jump"]))
#print(frameTrapCalc("Sol_Badguy","jK",1,-99,3,20,["jD","j623S","j623H","j236K","j214K","j214[K]"]))

#print("jump" in ["jump","j236H"])

#print(("jump" in ["5P","2P","6P","236P","623S","623H","236K","214K","623K","632146H"]) and ("j" not in "5P") and ("j" in "jP"))

#x = frameTrapCalc("Sol_Badguy","2D",3,-4,3,18,["236P","623S","623H","236K","214K","623K","632146H"])
#x.to_html("Sol_Badguy_2D.txt", index=False)
#print(x)