import urllib.request
#import urllib.parse

import re

class get_weather():
    def __init__(self,city_name):
        #x = re.search(' ', city_name)
        #city_name=input("enter the location")
        
        x=re.search(' ',city_name)
        if(x != None):

            pos = x.start()

            city_name = city_name[0:pos] + '-' + city_name[pos+1:]


        url = 'http://www.weather-forecast.com/locations/' + city_name + '/forecasts/latest'
        try:

            datas = urllib.request.urlopen(url).read()
            data = datas.decode('utf-8')
        except IOError as e:
            print('error reading :',e)
        #print(data)

        starting_text = re.search('span class="phrase">', data)
        start = starting_text.end()


        ending_text = re.search('</span></span></span></p><div class="forecast-cont">',data)
        end = ending_text.start()

        self.WeatherReport = data[start:end]
        self.WeatherReport=re.sub('&deg;',' degree ', self.WeatherReport)
    
    def returnvalue(self):
        return self.WeatherReport





def main():
  
   weather=get_weather()

if __name__=="__main__":main()
