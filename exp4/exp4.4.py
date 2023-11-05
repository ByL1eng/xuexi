stock = {
            '1': 4,
            '2': 10,
            '3': 1,
            '4': 5 }
def fillable(stock, merch, n):
    merch = 10
    n = 9
    if stock.get(merch, 0) >= n:
        return True
    else:
        return False
print(fillable(stock,'1',2))