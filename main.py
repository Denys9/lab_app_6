def str():
    try:
        text = input('str - ')
        word = input('word - ')
        print(f'count = { text.count(word)}')
    except Exception as ex:
        print(f'Eror information: {ex}')


str()