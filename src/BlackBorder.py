'''
Created on Jul 24, 2010

@author: mpoon
'''

import urllib
import re

class BlackBorder():
    '''
    classdocs
    '''

    URL = 'http://www.blackborder.com/cgi-bin/shopping/longprintablebuylist.cgi'

    rawHTML = ''

    def __init__(self):
        '''
        Constructor
        '''
        f = urllib.urlopen(self.URL)
        self.rawHTML = f.read()
        
    def fetch(self, set):
        if set == 'Magic 2011':
            set = 'Magic 2011 Core Set'
        if set == 'Magic 2010':
            set = 'Magic 2010 Core Set'
        data = self.rawHTML
        data = re.sub('<[^<]*>|&nbsp;|\\n|\\r|\\t|--|\$','!',data)
        data = re.sub('!+','!', data)
        dataList = data.split('!')
        indx = dataList.index(set)
        dataList = dataList[indx:]
        dataList.append('Product')
        dataList.pop(1)
        dataList.pop(1)
        dataList.pop(1)
        indx = dataList.index('Product')
        dataList = dataList[1:indx-2]

        dict = {}
        done = False
        i=0
        while(not done):
            dict[dataList[i]] = (dataList[i+2],'BLB')
            i= i + 3
            if(i >= len(dataList)):
                done = True
        
        
        return dict
    
    
    
    
    
    
    
    
    