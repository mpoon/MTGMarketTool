'''
Created on Jul 24, 2010

@author: mpoon
'''

import urllib
import re

class StarCityGames():
    '''
    classdocs
    '''
    rawHTML = ''
    URL = 'http://sales.starcitygames.com/buylist/'
    
    def __init__(self):
        '''
        Constructor
        '''
        f = urllib.urlopen(self.URL)
        self.rawHTML = f.read()
        
    def fetch(self, set):
        data = self.rawHTML
        data = data.partition('Following these instructions allows us to process your sell order as quickly and efficiently as possible. Thank you for selling to StarCityGames.com!')[2]
        data = data.partition('<br />StarCityGames.com<br />')[0]
        data = re.sub('<[^<]*>|&nbsp;|&nbsp|\\n|\\r|\\t|--|\$','!',data)
        data = re.sub('!+','!', data)
        print data
        dataList = data.split('!')
        return {}