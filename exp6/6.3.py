def shorten_number(suffixes, base):
    def shorten(str1):
        bool_1 = False
        bool_2 = isinstance(str1, str)
        if bool_2:
            for i in str1:
                if i.isdigit():
                    bool_1 = True
                else:
                    bool_1 = False
            if bool_1:
                new_string = ''
                if str1 == '1':
                    new_string += '1'
                    new_string += suffixes[0]
                elif int(str1) > int(base) ** len(suffixes):
                    n, m = divmod(int(str1), int(base) ** (len(suffixes) - 1))
                    new_string = str(n)
                    new_string += suffixes[len(suffixes) - 1]
                # elif int(str1) < int(base) ** 1:
                #     print(str1)
                else:
                    for i in range(len(suffixes)):
                        if int(base) ** i < int(str1) < int(base) ** (i + 1):
                            n, m = divmod(int(str1), int(base) ** i)
                            new_string = str(n)
                            new_string += suffixes[i]
                            # new_string = str1[:- 3 * i]
                            # new_string += suffixes[i]
                return new_string
            else:
                return str1
        else:
            return str(str1)

    return shorten