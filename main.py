import roman

from rsl.rsl304_i.f_304i_206 import pages
print(pages.pages_models)

# to roman
number = int(input('> ')) # 10
print(roman.toRoman(number))

# from roman
number = input('> ') # X
print(roman.fromRoman(number))



# from PyPDF2 import PdfReader, PdfWriter
#
# writer = PdfWriter()
# reader = PdfReader(
#     r"C:\Users\MaxDroN\Desktop\правда\библия\Новый завет\с толкованиями\Евангелие учительное\Евангелие учительное («Патриарший гомилиарий»), лицевое..pdf")
#
# for i in range(10):
#     writer.add_page(reader.pages[i])
#
# writer.add_bookmark("Hello, World", 1)
#
# writer.add_bookmark("3 неделя", 2)
#
# parent = writer.add_bookmark("Евангельские чтения", 5)  # add parent bookmark
# writer.add_bookmark("1 Неделя", 5, parent)  # add child bookmark
# writer.add_bookmark("2 Неделя", 6, parent)  # add child bookmark
# writer.add_bookmark("3 Неделя", 7, parent)  # add child bookmark
#
# output = open('NewGrades.pdf', 'wb')
# writer.write(output)
# output.close()
