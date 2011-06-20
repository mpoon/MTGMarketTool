'''
Created on Jul 24, 2010

@author: mpoon
'''
import urllib
import re

URL = 'http://www.pandemoniumbooks.com/?cont=buylist'

class PandemoniumBooks():
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
        
        
    def GetName(self):
        return 'Pandemonium Books'
        
    def fetch(self, set):
        
        data = self.rawHTML
        data = data.partition('<p>Viewing all cards on the buylist:</p>')[2]
        data = data.partition('<i>Site design and content &copy;2009 Pandemonium Books & Games.</i>')[0]
        data = re.sub('<[^<]*>|&nbsp;|\\n|\\r|\\t|--|\$','!',data)
        data = re.sub('Demon of Deaths Gate','Demon of Death\'s Gate',data)
        data = re.sub('Gaeas Revenge','Gaea\'s Revenge', data)
        data = re.sub('!+','!', data)
        dataList = data.split('!')
        
        for x in dataList:
            if x == '' or x == '    ' or x == '    <':
                dataList.remove(x)

        startindx = 10000000;
        endindx = 0;
        
        for i in xrange(0,len(dataList)):
            if dataList[i] == set:
                if i < startindx:
                    startindx = i
                if i > endindx:
                    endindx = i 
                    
        info  = dataList[startindx-1:endindx+4]
        
        m11 = {}
        
        done = False
        i=0
        while(not done):
            m11[info[i]] = (info[i+4],'PAN')
            i= i + 5
            if(i >= len(info)):
                done = True
        
        return m11