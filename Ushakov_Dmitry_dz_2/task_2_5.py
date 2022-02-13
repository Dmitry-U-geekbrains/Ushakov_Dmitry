def show_prices(items, show_delim=True):
    for price in items:
        price = int(round(price * 100))
        rubles = price // 100
        cents = price % 100
        print(f'{rubles:02d} руб {cents:02d} коп', end=',')
    if show_delim:
        print('*' * 25)


prices = [57.8, 46.51, 97, 56.78, 89.76, 32.45, 12.78, 83.84, 26.89, 67.87, 34.68]
show_prices(prices)
prices.sort()
show_prices(prices)
prices_desc = sorted(prices, reverse=True)
show_prices(prices_desc)
show_prices(show_delim=False, items=prices_desc[4::-1])
