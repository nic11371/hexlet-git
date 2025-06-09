import requests

url = 'http://31.130.149.237/api/v1/ajax/GetSum'

params = {
    'GiveName': 'JPY',
    'GetName': 'DOGE',
    'Sum': 51284.43,
    'Direction': 1
}

amounts_per_give_currency = {
        "USD": 150, "EUR": 120, "RUB": 20000, "BYN": 50, "JPY": 50000,
        "GBP": 250, "CAD": 1000, "BTC": 0.01, "ETH": 0.5, "SOL": 10,
        "USDT": 150, "ADA": 300, "DOGE": 5000, "XRP": 1000, "BNB": 1,
        "USDC": 150, "TRX": 10000
}

total = 0
count = 0
for give_cur, give_num in amounts_per_give_currency.items():
    for get_cur, get_num in amounts_per_give_currency.items():
        if give_cur == get_cur:
            continue
        params = {
            'GiveName': give_cur,
            'GetName': get_cur,
            'Sum': give_num,
            'Direction': 1
        }
        response = requests.get(url=url, params=params)
        answer = response.json()
        total += answer.get('giveSum')
        count += 1
# print(round(total, 2))
print(count)
print(total)
