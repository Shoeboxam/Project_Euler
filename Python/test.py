import urllib
from xml.etree.ElementTree import parse
import webbrowser

a = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = a.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

doc = parse('rt22.xml')
for bus in doc.findall('bus'):
	d = bus.findtext('d')
	lst = float(bus.findtext('lat'))
	
webbrowser.open("http://google.com")
