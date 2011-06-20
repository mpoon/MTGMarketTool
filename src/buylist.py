'''
Created on Jul 24, 2010

@author: mpoon
'''
import CoolStuffInc
import PandemoniumBooks
import BlackBorder
import ChannelFireball
import StarCityGames
import TrollandToad
import CardKingdom
import urllib
import re

#Stores = ['CardKingdom','PandemoniumBooks','CoolStuffInc','BlackBorder']
Stores = ['CardKingdom','PandemoniumBooks']

SetBuyLists = [['Magic 2011', {}],
        ['Magic 2010', {}], 
        ['Rise of the Eldrazi', {}], 
        ['Worldwake', {}],
        ['Zendikar', {}],
        ['Alara Reborn', {}], 
        ['Conflux', {}], 
        ['Shards of Alara', {}],
        ['Scars of Mirrodin', {}],
        ['Mirrodin Besieged', {}]]

SupportedStores = {
                   'BlackBorder':BlackBorder.BlackBorder,
                   'CardKingdom':CardKingdom.CardKingdom,
                   'ChannelFireball':ChannelFireball.ChannelFireball,
                   'CoolStuffInc':CoolStuffInc.CoolStuffInc,
                   'PandemoniumBooks':PandemoniumBooks.PandemoniumBooks,
                   'StarCityGames':StarCityGames.StarCityGames,
                   'TrollandToad':TrollandToad.TrollandToad,
                   }

def main():
    for store in Stores:
        StoreObj = SupportedStores[store]()
        for set in SetBuyLists:
            updateDict(set[1],StoreObj.fetch(set[0]))
    return SetBuyLists

def updateDict(dOld, dNew):
    for key in dNew:
        if key in dOld:
            dOld[key] = sorted(dOld[key]+ [dNew[key]], key = lambda num: float(num[0]), reverse = True)
        else:
            dOld[key] = [dNew[key]]
            
def updateWithEbay(list):
    for set in list:
        cards = set[1]
        for card in cards.keys():
            words = card.replace(' ', '+')
            URL = 'http://magictraders.com/cgi-bin/query.cgi?list=magic&target='+words+'&field=0&operator=re'
            f = urllib.urlopen(URL)
            html = f.read()
            

if __name__ == '__main__':
    list = main()
    for set in list:
        print set[0]
        stuff = set[1].items()
        
        for item in sorted(stuff, key = lambda alpha: alpha[0]):
            print item
    
    
    
    #list = PandemoniumBooks.PandemoniumBooks()
    #list.fetch()