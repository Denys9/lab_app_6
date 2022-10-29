def str():
    try:
        text = input('str - ')
        sym = input('sym - ')
        print(f'count = { text.count(sym)}')
    except Exception as ex:
        print(f'Eror information: {ex}')

str()