import pandas as pd

def scrapeTable(url):
    df = pd.read_html(url)
    return df

def getTable(charName, tableNums = [6,7,8]):
    x = scrapeTable("https://www.dustloop.com/w/GGST/"+charName+"/Frame_Data")
    table = x[tableNums[0]]
    #print(table)
    tableNums.pop(0)
    for y in tableNums:
        #print(x[y])
        table = pd.concat([table, x[y]])
    table = table.reset_index(drop=True)
    table = table.drop(table.loc[table["Input"]=="Input"].index)
    table["Notes"] = table["Invuln"]
    table["Gatling"] = ""
    table["Input"] = table["Input"].str.replace(".","")
    table = table.drop(columns=["Unnamed: 0", "Damage", "Proration", "R.I.S.C. Gain", "R.I.S.C. Loss", "Counter Type", "On-Hit", "Invuln"]).reset_index(drop=True)
    table.to_csv("rawFrameData/"+charName+".txt", sep="/", index=False)
    return

'''
charList = ["Anji_Mito", "Axl_Low", "Baiken", "Bridget", "Chipp_Zanuff", "Faust", "Giovanna", "Goldlewis_Dickinson", "Happy_Chaos", "I-No", "Jack-O", "Ky_Kiske", "May", "Millia_Rage", "Nagoriyuki", "Potemkin", "Ramlethal_Valentine", "Sin_Kiske", "Sol_Badguy", "Testament", "Zato-1"]
tableList = [[6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8] , [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8], [6,7,8]]
for x in range(len(charList)):
    getTable(charList[x], tableList[x])
    print(charList[x]+" updated.")
    
getTable("Leo_Whitefang",[7,8,9,10])
'''