from win10toast import ToastNotifier
import robin_stocks.robinhood as r
from PIL import Image

filename = "doge.png"
img = Image.open(filename)
img.save('doge.ico')
file_name = 'doge.ico'

#Login -> SMS Verification
r.login("*******","*****")


#print(r.get_crypto_info("DOGE"))
print(r.get_crypto_quote("DOGE"))
robinDict = (r.get_crypto_quote("DOGE"))

markPrice= robinDict['mark_price']
highPrice = robinDict['high_price']
lowprice = robinDict['low_price']


# create an object to ToastNotifier class
x = ToastNotifier()

x.show_toast("DogeCoin Notification","Dogecoin Current: "+ markPrice + " " +"Dogecoin High Price: " + highPrice + " " +"DogeCoin Low Price: " +lowprice, icon_path=file_name, duration=30, threaded=True)

#Can automate this using task scheduler