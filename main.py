def rev():
    try:
        x = input("str - ")
        print(x[::-1])
    except Exception as ex:
        print(f'Eror information: {ex}')


rev()
