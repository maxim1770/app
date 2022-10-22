# import requests
# from bs4 import BeautifulSoup
#
# HEADERS: dict[str, str] = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
# }
#
# req = requests.get(
#     url='https://azbyka.ru/biblia/?Act.9:20-31',
#     headers=HEADERS
# )
# soup = BeautifulSoup(req.text, "lxml")
#
# tag_div_verse = soup.find('div', {'class': 'crossref-verse', 'data-lang': 'r'})
#
# # zachala_str: str = tag_div_verse.find('span', class_='zachala').text
#
# for div in tag_div_verse.find_previous_siblings('div'):
#     tag_span = div.find('span', class_='zachala')
#     if tag_span:
#         zachala_str: str = tag_span.text
#         break
#
# print(zachala_str)
#
#
# # zachala_str: str = tag_div_verse.find_previous_sibling(
# #     'span',
# #     class_='zachala').text
# #
# # print(zachala_str)
#
#
# # zachala_str: str = tag_div_verse.find_next_sibling('div').find(
# # #     'span',
# # #     class_='zachala').text