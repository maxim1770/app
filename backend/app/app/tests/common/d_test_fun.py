if __name__ == '__main__':
    d = {}
    d1 = {'fsdf' : ['fsdf', 'fsdf'], 'fsd11': ['fsdf']}
    d2 = {'fsdf' : ['fsdffsd', 'fsdfsdf'], 'fs22': ['fsdfdsf']}
    for manuscript_code, molitva_books in d1.items():
        if not d.get(manuscript_code):
            d[manuscript_code] = []
        d[manuscript_code] += molitva_books


    for manuscript_code, molitva_books in d2.items():
        if not d.get(manuscript_code):
            d[manuscript_code] = molitva_books
        else:
            d[manuscript_code] += molitva_books

    for molitva_books in d.values():
        molitva_books.append('fsa222222')
    if d:
        print(d)

    print(sorted([423, 3, 34 ]))