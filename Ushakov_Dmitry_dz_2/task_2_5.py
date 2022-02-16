# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
def show_price(items, show_delim=True):
    for price in items:
        price = int(round(price * 100))
        rubles = price // 100
        cents = price % 100
        print(f'{rubles:02d} руб {cents:02d} коп', end=',')
    if show_delim:
        print()


prices = [101.8, 46.51, 31.64, 53.69, 7.63, 3.5, 1.36, 9.6, 15.87, 97, 56.78, 124.6, 32.45, 12.78, 83.84, 26.89, 62.5,
          67.87, 77.77, 34.68]
show_price(prices)
prices.sort()
show_price(prices)
prices_desc = sorted(prices, reverse=True)
show_price(prices_desc)
show_price(show_delim=False, items=prices_desc[4::-1])
