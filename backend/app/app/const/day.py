from typing import Final

MONTH_TITLE: Final[dict[int, str]] = {
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря',
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа'
}

DAY_SUNSETS: dict[int, dict[int, tuple[int, int]]] = {
    1: {1: (16, 52), 2: (16, 53), 3: (16, 54), 4: (16, 55), 5: (16, 56), 6: (16, 57), 7: (16, 59), 8: (17, 0),
        9: (17, 1),
        10: (17, 3), 11: (17, 4), 12: (17, 6), 13: (17, 7), 14: (17, 9), 15: (17, 10), 16: (17, 12), 17: (17, 14),
        18: (17, 15), 19: (17, 17), 20: (17, 19), 21: (17, 21), 22: (17, 22), 23: (17, 24), 24: (17, 26), 25: (17, 28),
        26: (17, 30), 27: (17, 32), 28: (17, 33), 29: (17, 35), 30: (17, 37), 31: (17, 39)},
    2: {1: (17, 41), 2: (17, 43), 3: (17, 45), 4: (17, 47), 5: (17, 49), 6: (17, 51), 7: (17, 53), 8: (17, 55),
        9: (17, 57), 10: (17, 59), 11: (18, 1), 12: (18, 3), 13: (18, 5), 14: (18, 7), 15: (18, 9), 16: (18, 11),
        17: (18, 13), 18: (18, 15), 19: (18, 17), 20: (18, 19), 21: (18, 21), 22: (18, 23), 23: (18, 26), 24: (18, 28),
        25: (18, 30), 26: (18, 32), 27: (18, 34), 28: (18, 36), 29: []},
    3: {1: (18, 38), 2: (18, 40), 3: (18, 42), 4: (18, 44), 5: (18, 46), 6: (18, 48), 7: (18, 50), 8: (18, 52),
        9: (18, 54), 10: (18, 56), 11: (18, 58), 12: (19, 0), 13: (19, 2), 14: (19, 4), 15: (19, 6), 16: (19, 9),
        17: (19, 11), 18: (19, 13), 19: (19, 15), 20: (19, 17), 21: (19, 19), 22: (19, 21), 23: (19, 23), 24: (19, 25),
        25: (19, 27), 26: (19, 29), 27: (19, 31), 28: (19, 33), 29: (19, 36), 30: (19, 38), 31: (19, 40)},
    4: {1: (19, 42), 2: (19, 44), 3: (19, 46), 4: (19, 48), 5: (19, 50), 6: (19, 53), 7: (19, 55), 8: (19, 57),
        9: (19, 59), 10: (20, 1), 11: (20, 3), 12: (20, 6), 13: (20, 8), 14: (20, 10), 15: (20, 12), 16: (20, 14),
        17: (20, 17), 18: (20, 19), 19: (20, 21), 20: (20, 23), 21: (20, 26), 22: (20, 28), 23: (20, 30), 24: (20, 32),
        25: (20, 35), 26: (20, 37), 27: (20, 39), 28: (20, 42), 29: (20, 44), 30: (20, 46)},
    5: {1: (20, 49), 2: (20, 51), 3: (20, 53), 4: (20, 56), 5: (20, 58), 6: (21, 0), 7: (21, 3), 8: (21, 5), 9: (21, 7),
        10: (21, 10), 11: (21, 12), 12: (21, 14), 13: (21, 16), 14: (21, 19), 15: (21, 21), 16: (21, 23), 17: (21, 26),
        18: (21, 28), 19: (21, 30), 20: (21, 32), 21: (21, 34), 22: (21, 37), 23: (21, 39), 24: (21, 41), 25: (21, 43),
        26: (21, 45), 27: (21, 47), 28: (21, 49), 29: (21, 51), 30: (21, 53), 31: (21, 55)},
    6: {1: (21, 56), 2: (21, 58), 3: (22, 0), 4: (22, 2), 5: (22, 3), 6: (22, 5), 7: (22, 6), 8: (22, 8), 9: (22, 9),
        10: (22, 10), 11: (22, 12), 12: (22, 13), 13: (22, 14), 14: (22, 15), 15: (22, 15), 16: (22, 16), 17: (22, 17),
        18: (22, 18), 19: (22, 18), 20: (22, 19), 21: (22, 19), 22: (22, 19), 23: (22, 19), 24: (22, 19), 25: (22, 19),
        26: (22, 19), 27: (22, 19), 28: (22, 19), 29: (22, 18), 30: (22, 18)},
    7: {1: (22, 17), 2: (22, 17), 3: (22, 16), 4: (22, 15), 5: (22, 14), 6: (22, 13), 7: (22, 12), 8: (22, 11),
        9: (22, 10), 10: (22, 8), 11: (22, 7), 12: (22, 6), 13: (22, 4), 14: (22, 2), 15: (22, 1), 16: (21, 59),
        17: (21, 57), 18: (21, 56), 19: (21, 54), 20: (21, 52), 21: (21, 50), 22: (21, 48), 23: (21, 46), 24: (21, 44),
        25: (21, 42), 26: (21, 40), 27: (21, 38), 28: (21, 35), 29: (21, 33), 30: (21, 31), 31: (21, 29)},
    8: {1: (21, 26), 2: (21, 24), 3: (21, 22), 4: (21, 19), 5: (21, 17), 6: (21, 14), 7: (21, 12), 8: (21, 9),
        9: (21, 7),
        10: (21, 4), 11: (21, 2), 12: (20, 59), 13: (20, 57), 14: (20, 54), 15: (20, 51), 16: (20, 49), 17: (20, 46),
        18: (20, 44), 19: (20, 41), 20: (20, 38), 21: (20, 36), 22: (20, 33), 23: (20, 30), 24: (20, 28), 25: (20, 25),
        26: (20, 22), 27: (20, 19), 28: (20, 17), 29: (20, 14), 30: (20, 11), 31: (20, 9)},
    9: {1: (20, 6), 2: (20, 3), 3: (20, 0), 4: (19, 58), 5: (19, 55), 6: (19, 52), 7: (19, 49), 8: (19, 47),
        9: (19, 44),
        10: (19, 41), 11: (19, 39), 12: (19, 36), 13: (19, 33), 14: (19, 30), 15: (19, 28), 16: (19, 25), 17: (19, 22),
        18: (19, 19), 19: (19, 17), 20: (19, 14), 21: (19, 11), 22: (19, 9), 23: (19, 6), 24: (19, 3), 25: (19, 1),
        26: (18, 58), 27: (18, 55), 28: (18, 53), 29: (18, 50), 30: (18, 47)},
    10: {1: (18, 45), 2: (18, 42), 3: (18, 40), 4: (18, 37), 5: (18, 34), 6: (18, 32), 7: (18, 29), 8: (18, 27),
         9: (18, 24), 10: (18, 22), 11: (18, 19), 12: (18, 17), 13: (18, 14), 14: (18, 12), 15: (18, 10), 16: (18, 7),
         17: (18, 5), 18: (18, 2), 19: (18, 0), 20: (17, 58), 21: (17, 55), 22: (17, 53), 23: (17, 51), 24: (17, 49),
         25: (17, 46), 26: (17, 44), 27: (17, 42), 28: (17, 40), 29: (17, 38), 30: (17, 36), 31: (17, 34)},
    11: {1: (17, 31), 2: (17, 29), 3: (17, 27), 4: (17, 26), 5: (17, 24), 6: (17, 22), 7: (17, 20), 8: (17, 18),
         9: (17, 16), 10: (17, 14), 11: (17, 13), 12: (17, 11), 13: (17, 9), 14: (17, 8), 15: (17, 6), 16: (17, 5),
         17: (17, 3), 18: (17, 2), 19: (17, 0), 20: (16, 59), 21: (16, 58), 22: (16, 57), 23: (16, 55), 24: (16, 54),
         25: (16, 53), 26: (16, 52), 27: (16, 51), 28: (16, 50), 29: (16, 49), 30: (16, 48)},
    12: {1: (16, 47), 2: (16, 47), 3: (16, 46), 4: (16, 45), 5: (16, 45), 6: (16, 44), 7: (16, 44), 8: (16, 43),
         9: (16, 43), 10: (16, 43), 11: (16, 43), 12: (16, 42), 13: (16, 42), 14: (16, 42), 15: (16, 42), 16: (16, 42),
         17: (16, 42), 18: (16, 43), 19: (16, 43), 20: (16, 43), 21: (16, 44), 22: (16, 44), 23: (16, 45), 24: (16, 45),
         25: (16, 46), 26: (16, 46), 27: (16, 47), 28: (16, 48), 29: (16, 49), 30: (16, 50), 31: (16, 50)}}
