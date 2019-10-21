import pandas as pd

def Predictions(img):
    userItemData = pd.read_csv('ratings.csv')
    userItemData.head()

    itemList=list(set(userItemData["ItemId"].tolist()))

    userCount=len(set(userItemData["userId"].tolist()))

    itemAffinity= pd.DataFrame(columns=('item1', 'item2', 'score'))
    rowCount=0

    for ind1 in range(len(itemList)):
        item1Users = userItemData[userItemData.ItemId==itemList[ind1]]["userId"].tolist()
        for ind2 in range(ind1, len(itemList)):
            if ( ind1 == ind2):
                continue

            item2Users=userItemData[userItemData.ItemId==itemList[ind2]]["userId"].tolist()
            commonUsers= len(set(item1Users).intersection(set(item2Users)))
            score=commonUsers / userCount
            itemAffinity.loc[rowCount] = [itemList[ind1],itemList[ind2],score]
            rowCount +=1
            itemAffinity.loc[rowCount] = [itemList[ind2],itemList[ind1],score]
            rowCount +=1

    itemAffinity.head()

    dic={5001:"Laptop",5002:"Laptop cover",5005:"Laptop skins",5003:"Mobile",5004:"Mobile Covers",5006:"Earphone",5007:"Ipod Charger",5008:"Ipod",5009:"Laptop Charger",5010:"Mobile Charger"}
    for key, value in dic.items():
        if img == value:
            key1 = key
    searchItem=key1

    recoList=itemAffinity[itemAffinity.item1==searchItem]        [["item2","score"]]        .sort_values("score", ascending=[0])

    recordList=list(recoList["item2"])
    recordList=recordList[:3]
    item_list=[]

    for item in recordList:
        item_list.append(dic[item])

    #print(item_list)

    return item_list
