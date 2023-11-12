def find_outlier(integers):
    even_count = 0
    odd_count = 0
    even = None
    odd = None
    for value in integers:
        if value % 2 == 0:
            if even is None:
                even = value
            if odd_count > 1:
                return value
            even_count += 1
            if even_count > 1 and odd is not None:
                return odd 
        else:
            if odd is None:
                odd = value
            if even_count > 1:
                return value
            odd_count += 1
            if odd_count > 1 and even is not None:
                return even 