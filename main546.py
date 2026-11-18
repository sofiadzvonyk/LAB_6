stocks = {
    "FB": 10.75,
    "IBM": 205.55,
    "HPQ": 37.2,
    "AAPL": 612.78,
    "ACME": 45.23,
}
for key, value in sorted(stocks.items(), key=lambda x: x[1]):
    print(value, key)