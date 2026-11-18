stocks = {
    "FB": 10.75,
    "HPQ": 37.2,
    "ACME": 45.23,
    "IBM": 205.55,
    "AAPL": 612.78
}
n = int(input())
new_stocks = {}
for key, value in stocks.items():
    if value > n:
        new_stocks[key] = value
for key, value in new_stocks.items():
    print(key, value)