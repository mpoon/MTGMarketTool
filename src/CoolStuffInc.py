'''
Created on Jul 24, 2010

@author: mpoon
'''

import urllib
import re

URL = 'http://www.coolstuffinc.com/buyList_main.php?pa=vbl&gn=mtg&dp=1'

class CoolStuffInc():
    '''
    classdocs
    '''
    rawHTML = ''

    def __init__(self):
        '''
        Constructor
        '''
        f = urllib.urlopen(URL)
        self.rawHTML = f.read()
    def fetch(self,set):
        
        data = self.rawHTML
        data = data.partition('<b>Bulk Magic</b>')[2]
        data = data.partition('<u>View Buy Cart</u>')[0]
        
        data = re.sub('<[^<]*>|&nbsp;|\\n|\\r|Qty','!',data)
        data = re.sub('!+','!', data)
        dataList = data.split('!')
        
        for x in dataList:
            if x == '' or x == ' ' or x == 'Qty':
                dataList.remove(x)
                
        startindx = 10000000;
        endindx = 0;
        
        for i in xrange(0,len(dataList)):
            if dataList[i] == set:
                if i < startindx:
                    startindx = i
                if i > endindx:
                    endindx = i 
                    
        info  = dataList[startindx+1:endindx+4]
        
        m11 = {}
        
        done = False
        i=0
        while(not done):
            m11[info[i]] = (info[i+4][1:],'CSI')
            i= i + 5
            if(i >= len(info)):
                done = True
        
        return m11
        