prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for prices_key, prices_value in prices.items():
    print(prices_key)
    print("price: ", prices_value)
    for stock_key, stock_value in stock.items():
        if prices_key == stock_key:
            print("stock: ", stock_value)
    print()

