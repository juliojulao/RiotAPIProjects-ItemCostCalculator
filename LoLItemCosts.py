import json
import requests

def printItems(items_list):
    for k,v in items_list.items():
        print(v,k)

def purchasableItems(item_dict):
    result = dict()
    for k,v in item_dict["data"].items():
        if v["gold"]["total"] > 0:
            result[v["name"].lower()] = k
    return result
        
def getTotalCost(item_list, item_dict):
    print("\nWhat items do you want to buy?")
    check_items = []
    cost = 0
    while True:
        item = input()
        if not item:
            break
        else:
            check_items.append(item.lower().strip())
    print(check_items)
    for i in check_items:
        if i in item_list:
            print("{}: {}".format(i,item_dict["data"][item_list[i]]["gold"]["total"]))
            cost += item_dict["data"][item_list[i]]["gold"]["total"]
    print("\nTotal cost: {}".format(cost))

def requestItems(patchVersion):
    response = requests.get("http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/item.json".format(patchVersion))
    return response.json()



def main():
    patchVersion = "10.16.1"
    items = requestItems(patchVersion)
    purchasable_items = purchasableItems(items)
    getTotalCost(purchasable_items, items)


if __name__ == "__main__":
    main()
