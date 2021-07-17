#https://github.com/danpaquin/coinbasepro-python
#https://docs.pro.coinbase.com/#get-historic-rates
#https://pypi.org/project/coinbasepro/
#https://stackoverflow.com/questions/26266425/typeerror-list-indices-must-be-integers-not-dict


from AccountInfo import api_key, api_secret, api_passphrase
import cbpro
from CalcModules import *
from itertools import islice

#Public Client Functions (just shows general data not specific to your account)
public_client = cbpro.PublicClient()
#print(public_client.get_products())
#print(public_client.get_product_order_book('BTC-USD', level=1))
#print(public_client.get_product_ticker(product_id='ETH-USD'))
#print(public_client.get_time())


#Generate Ticker prices for all CRYPTOS
btcTicker = public_client.get_product_ticker(product_id="BTC-USD")
ethTicker = public_client.get_product_ticker(product_id="ETH-USD")
adaTicker = public_client.get_product_ticker(product_id="ADA-USD")
ltcTicker = public_client.get_product_ticker(product_id="LTC-USD")
#btcTicker = public_client.get_product_ticker(product_id="BTC-USD")
#ethTicker = public_client.get_product_ticker(product_id="BTC-USD")

#Authenticated Client (login using api key)
auth_client = cbpro.AuthenticatedClient(api_key, api_secret, api_passphrase)
#print("")

#####################################################################################################################

#BTC - BITCOIN CRYPTO----------------------------------------
fills_gen_BTC = auth_client.get_fills(product_id="BTC-USD")
#Lists all BTC info on your account
BTC_fills = list(fills_gen_BTC)
#print(BTC_fills)
print("BTC - BITCOIN - ${}".format(btcTicker['price']))
print('')
calc_current_amt(BTC_fills)
calc_fees(BTC_fills)
calc_avg_cost(BTC_fills, btcTicker)

#ETH - ETHEREUM CRYPTO----------------------------------------
fills_gen_ETH = auth_client.get_fills(product_id="ETH-USD")
#Lists all LTC info on your account
ETH_fills = list(fills_gen_ETH)
#print(ETH_fills)
print("ETH - ETHEREUM - ${}".format(ethTicker['price']))
print('')
calc_current_amt(ETH_fills)
calc_fees(ETH_fills)
calc_avg_cost(ETH_fills, ethTicker)

#ADA - CARDANO CRYPTO---------------------------------------
fills_gen_ADA = auth_client.get_fills(product_id="ADA-USD")
#Lists all ADA info on your account
ADA_fills = list(fills_gen_ADA)
#print(ADA_fills)
print("ADA - CARDANO - ${}".format(adaTicker['price']))
print('')
calc_current_amt(ADA_fills)
calc_fees(ADA_fills)
calc_avg_cost(ADA_fills, adaTicker)

#LTC - LITCOIN CRYPTO----------------------------------------
fills_gen_LTC = auth_client.get_fills(product_id="LTC-USD")
#Lists all LTC info on your account
LTC_fills = list(fills_gen_LTC)
#print(LTC_fills)
print("LTC - LITECOIN - ${}".format(ltcTicker['price']))
print('')
calc_current_amt(LTC_fills)
calc_fees(LTC_fills)
calc_avg_cost(LTC_fills, ltcTicker)







'''total = 0
for x in range(len(all_fills)):
    if all_fills[x]['side'] == 'buy':
        print("Bought amount {}".format(all_fills[x]['size']))
        total += float(all_fills[x]['size'])
    elif all_fills[x]['side'] == 'sell':
        print("Sold amoutn {}".format(all_fills[x]['size']))
        total -= float(all_fills[x]['size'])
print(total)

'''





'''

fills_gen = auth_client.get_fills(product_id="DOGE-USD")
# Get all fills (will possibly make multiple HTTP requests)
all_fills = list(fills_gen)
print(all_fills)

'''





'''

Creating a Request
All REST requests must contain the following headers:

CB-ACCESS-KEY The api key as a string.
CB-ACCESS-SIGN The base64-encoded signature (see Signing a Message).
CB-ACCESS-TIMESTAMP A timestamp for your request.
CB-ACCESS-PASSPHRASE The passphrase you specified when creating the API key.
All request bodies should have content type application/json and be valid JSON.


from AccountInfo import api_key, api_secret, api_passphrase

import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

# Create custom authentication for Exchange
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')

        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

#Main method
#connect to the api + get your account information
api_url = 'https://api.pro.coinbase.com/'
auth = CoinbaseExchangeAuth(api_key, api_secret, api_passphrase)
#send get request to coinbase server
request = requests.get(api_url + 'accounts', auth=auth)
print(request.json())
print(request.status_code)

'''

