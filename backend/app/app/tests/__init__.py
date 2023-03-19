from PIL import Image

if __name__ == '__main__':
    im = Image.open(r"C:\Users\MaxDroN\python_projects\data\img\manuscripts\lls\lls-book-rus-5\506.webp")
    print(im)

    im = Image.open(r"C:\Users\MaxDroN\python_projects\data\img\manuscripts\lls\lls-book-rus-6\406.webp")
    print(im)

    # im.save(r"C:\Users\MaxDroN\Desktop\test.png", format='png')

    im = Image.open(r"C:\Users\MaxDroN\python_projects\data\img\manuscripts\rsl\f_37\f-37-430\11.webp")
    print(im.format)
