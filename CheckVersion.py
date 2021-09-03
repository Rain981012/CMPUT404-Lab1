import requests
import urllib.request

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'

def printVersion():
	print("current requests lib version is ",requests.__version__)


def getHomepage():
	page = 'http://google.com/'
	r = requests.get(page)
	print(r)

def DownloadItSelf():
	url = 'https://raw.githubusercontent.com/Rain981012/CMPUT404-Lab1/main/CheckVersion.py'
	r = requests.get(url)

	with open('/Users/wusiyuan/cmput404/CMPUT404-Lab1/Downloadfile.py', 'wb') as f:
		f.write(r.content)

	newf = open('/Users/wusiyuan/cmput404/CMPUT404-Lab1/Downloadfile.py')

	lines = newf.read()

	print(lines)

def main():
	DownloadItSelf()
	printVersion()
	getHomepage()

if __name__ == '__main__':
	main()
