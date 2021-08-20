import collections


class ChainMap:
    def __init__(self, dict1, dict2):
        self.res = collections.ChainMap(dict1, dict2)

    def printChainmap(self):
        print(self.res.maps, '\n')

    def getkeys(self):
        return (f"keys = {list(self.res.keys())}")

    def getValues(self):
        return (f"Values = {list(self.res.values())}") 

    

if __name__ == "__main__":
    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day1': 'Thu'}
    cm = ChainMap(dict1, dict2)
    cm.printChainmap()
    print("\n",cm.getkeys())
    print("\n",cm.getValues())
    print("Check if value in chain map: ", ('day3' in cm.res))
