'''
Created on Jul 24, 2010

@author: mpoon
'''

import urllib
import re

URL1 = 'http://www.cardkingdom.com/purchasing/mtg_singles?filter[category_id]='
URL2 = '&filter[name]=&filter[rarity]='

setID = {
         'Magic 2011':2847,
         'Magic 2010':2789,
         'Rise of the Eldrazi':2843,
         'Zendikar':2826,
         'Worldwake':2840,
         'Alara Reborn':2385,
         'Conflux':2783,
         'Shards of Alara':2660,
         'Scars of Mirrodin':2852,
         'Mirrodin Besieged':2859
         }

class CardKingdom():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def GetName(self):
        return 'Card Kingdom'
    
    def fetch(self, set):
        f = urllib.urlopen(URL1 + str(setID[set]) + URL2)
        data = f.read()
        data = data.partition('<form action=/sellcart/add method=post>')[2]
        data = data.partition('<p class="pagination">')[0];
        data = re.sub('<[^<]*>|&nbsp;|\\n|\\r|\\t|--|\$|\s\s+','!',data)
        data = re.sub('!+','!', data)
        dataList = data.split('!')
        for x in dataList:
            if x == '':
                dataList.remove(x)
        dataList = dataList[6:]        
        
        m11 = {}
        
        done = False
        i=0
        while(not done):
            m11[dataList[i]] = (dataList[i+3],'CKD')
            i= i + 5
            if(i >= len(dataList)):
                done = True
        
        return m11
        
        
        
        
        
        
        
        
        
        