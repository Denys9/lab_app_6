def reverse_string1(s):
    try:
        return s[::-1]

        x = input("str - ")
        print(reverse_string1(x))
    except Exception as ex:
        print(f'Eror information: {ex}')
