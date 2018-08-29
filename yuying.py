import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pyttsx3
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',}
res =requests.get('http://tianqi.moji.com/',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
temp=soup.find('div',attrs={'class':'wea_weather clearfix'}).em.getText()
weather = soup.find('div', attrs={'class': 'wea_weather clearfix'}).b.getText()
sd = soup.find('div', attrs={'class': 'wea_about clearfix'}).span.getText()
sd_num = re.search(r'\d+', sd).group()
wind = soup.find('div', attrs={'class': 'wea_about clearfix'}).em.getText()
aqi = soup.find('div', attrs={'class': 'wea_alert clearfix'}).em.getText()
aqi_num = re.search(r'\d+', aqi).group()
info = soup.find('div', attrs={'class': 'wea_tips clearfix'}).em.getText()
sd = sd.replace(' ', '百分之').replace('%', '')
aqi = 'aqi' + aqi
 
today = datetime.now().date().strftime('%Y年%m月%d日')
text = '早上好！今天是%s,天气%s,温度%s摄氏度,%s,%s,%s,%s'%(today, weather, temp, sd, wind, aqi, info)
engine=pyttsx3.init()
engine.setProperty('voice','com.apple.speech.synthesis.voice.ting-ting')
engine.say(text)
engine.runAndWait()
