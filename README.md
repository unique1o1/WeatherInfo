# WeatherInfo
A super simple python module to retrieve Weather Info about a certain location (eg. New York, Boston, Kathmandu etc..)


**Installation:**


Linux:


		git clone https://github.com/unique1o1/WeatherInfo
		sudo cp -R WeatherInfo /usr/lib/python3.5/ 

**How to use:**


		from WeatherInfo import *


*Call the constructor to send the location you want and put it in a variable.*


		weather = get_weather('new york')
		weather_info = weather.returnvalue() #weather.returnvalue() returns the weatherinfo
		print(weather_info) 
