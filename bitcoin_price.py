import requests
r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#print(r.json()['bpi'])
#print(r.json()['bpi']['USD'])
rate_dollar=r.json()['bpi']['USD']['rate']
print("The bitcoin costs $",rate_dollar)
api_key='58d4ab78c86ec7880130c91597fc194d'
endpnt='http://data.fixer.io/api/latest?access_key='+api_key
r=requests.get(endpnt)
v=(r.json()['rates']['INR'])
print('And ',float(rate_dollar.replace(",",""))*float(v),'INR')
