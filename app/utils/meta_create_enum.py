from transliterate import translit


def meta_create_enum(l: list):
    for word in l:
        # TODO: возможно стоит добавлять префик 'u' перед строкой: u'текс',
        #  т.к так написано в документации к transliterate
        #  префик делает из строки строку unicode

        # TODO: Можно заменить translit на slugify, он сразу уберет ' из пол. строки, и все-будет-через-тире
        translit_word: str = translit(word, language_code='ru', reversed=True)
        translit_word = translit_word.replace(' ', '_').replace('-', '_')

        # 'ь' - траслитица в ', поэтому не придумал ничего лучше, как просто убрать ' из получившейся строки
        translit_word = translit_word.replace("'", '')

        print(f"{translit_word} = '{word}'")


if __name__ == '__main__':
    # print(slugify('равноапостольный'))
    # print(translit('равноапостольный', language_code='ru', reversed=True))
    #
    # print(translit('равноапостольный', language_code='ru', reversed=True))
    # print(translit('ь', language_code='ru', reversed=True))
    #
    # print(translit("ravnoapostol'nyj", language_code='ru'))
    # print(translit('ravnoapostolnyj', language_code='ru'))
    #
    # print(translit("'", language_code='ru'))

    l: list = [
        'Прмчч. монахи 17 в Индии', 'Мученики 62 иерея и 300 мирян',
        'Собор Пресвятой Богородицы', 'Мученики 14 000 младенцев, от Ирода в Вифлееме убиенные',
        'Собор 70-ти апостолов', 'Собор славных и всехвальных 12-ти апостолов',
        'Собор вселенских учителей и святителей Васи́лия Великого, Григо́рия Богослова и Иоа́нна Златоустого',
        'Святые мученики 1003, в Никомидии пострадавшие', 'Собор всех преподобных отцов, в подвиге просиявших',
    ]

    meta_create_enum(l)
