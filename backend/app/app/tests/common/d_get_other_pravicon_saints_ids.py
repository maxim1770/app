import logging

import requests
from bs4 import Tag
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from app import crud
from app.create.prepare.icon import __collect

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

from sqlalchemy.orm import Session
from app.api import deps

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    session: requests.Session = next(deps.get_session())

    # saints = db.execute(
    #     sa.select(models.Saint).join(models.SaintsHolidays).join(models.Holiday).join(models.HolidayCategory)
    #     .filter(
    #         (models.HolidayCategory.title == enums.HolidayCategoryTitle.den_pamjati)
    #     )).scalars().all()
    # pravicon_saints_ids = get_pravicon_saints_ids(session, saints=saints)
    # logging.warning(pravicon_saints_ids)
    # logging.error([tuple_[1] for tuple_ in pravicon_saints_ids])

    pravicon_saints_ids = [1072, 1144, 1802, 1335, 1547, 2780, 1008, 1282, 2795, 2158, 1926, 2849, 1704, 2844, 2635,
                           1355, 3079, 1684, 1745,
                           1032, 2087, 2212, 2744, 3158, 2843, 2428, 1694, 1249, 1611, 3171, 2014, 3170, 1456, 1749,
                           2868, 2681, 2820, 1792,
                           3189, 2059, 1469, 2152, 1888, 2702, 2636, 3186, 1631, 2351, 3173, 2688, 2685, 2742, 1150,
                           1413, 3134, 1148, 1658,
                           3169, 1420, 2524, 2882, 1981, 2301, 2825, 2289, 2358, 2826, 1278, 1896, 1904, 1905, 2028,
                           1871, 1774, 1294, 1155,
                           2972, 3131, 2307, 2514, 2511, 2513, 2666, 1270, 2151, 1030, 2390, 1726, 2437, 2516, 2013,
                           2629, 1365, 2294, 1835,
                           3096, 2604, 1109, 2613, 2445, 1515, 3150, 1580, 2575, 1362, 2762, 2435, 1099, 1131, 1858,
                           2653, 1859, 2054, 3066,
                           2663, 3161, 1077, 2504, 1015, 1186, 1302, 2073, 1974, 3045, 1500, 1582, 1139, 2582, 1228,
                           1963, 3172, 1609, 2577,
                           2296, 2946, 1092, 2305, 1259, 2964, 2936, 2842, 2476, 2469, 1911, 1460, 1557, 1875, 1607,
                           2094, 2091, 3039, 3110,
                           2587, 2632, 2496, 1739, 2519, 3129, 1199, 2990, 1783, 2885, 1715, 1317, 1240, 4009, 1575,
                           1573, 2077, 2651, 1002,
                           2733, 2712, 2388, 2330, 2807, 2396, 1855, 3105, 1218, 1230, 1307, 2315, 2331, 2329, 4050,
                           1731, 2338, 1057, 2234,
                           1944, 1514, 2479, 2238, 3088, 1811, 1813, 1830, 2794, 2074, 2562, 1467, 3180, 2657, 1203,
                           2770, 2286, 1457, 3080,
                           2424, 1693, 1017, 2067, 2599, 2680, 3073, 3064, 2223, 1040, 3165, 1668, 2258, 1049, 1299,
                           2737, 1094, 1794, 2978,
                           2743, 2761, 2999, 1385, 2512, 2126, 3108, 1685, 1235, 2076, 3098, 1272, 1727, 1522, 1521,
                           1605, 1380, 2189, 2190,
                           2637, 3135, 1796, 2941, 1734, 2943, 2895, 2824, 1101, 1419, 2661, 2848, 1252, 1088, 1118,
                           2319, 2159, 1916, 1412,
                           1853, 3174, 1382, 2064, 2576, 2573, 1821, 2058, 1393, 2416, 1717, 1329, 1673, 2034, 2036,
                           2037, 2367, 1740, 1541,
                           3000, 2525, 2029, 2731, 3084, 1720, 2441, 4115, 1510, 1606, 1336, 1210, 1373, 1967, 1396,
                           1828, 3275, 1279, 2809,
                           1837, 1062, 1932, 1100, 1159, 2346, 3068, 1442, 2816, 4137, 1771, 2883, 1381, 2959, 1543,
                           2960, 2166, 1661, 2679,
                           2321, 1520, 1290, 3086, 2692, 1136, 2049, 1363, 2475, 2581, 1261, 3202, 2904, 2078, 2973,
                           2483, 2797, 1550, 1104,
                           2646, 2273, 2072, 2070, 1318, 3060, 1751, 2206, 2208, 1650, 1408, 1993, 2468, 1752, 2648,
                           2529, 3137, 1968, 3139,
                           3136, 3138, 2530, 1878, 1773, 3094, 1797, 1800, 1635, 2533, 2457, 2443, 1664, 1663, 2155,
                           2157, 1096, 2995, 2881,
                           1368, 1265, 2957, 2489, 1777, 2254, 1814, 3002, 3005, 2276, 2647, 2442, 1544, 2449, 2089,
                           2988, 1707, 1059, 3035,
                           1645, 2830, 2394, 2710, 2704, 2083, 1844, 1400, 1165, 1178, 3054, 1288, 2256, 2917, 2153,
                           3052, 1225, 1242, 2141,
                           1551, 3246, 1080, 2953, 2100, 1312, 2359, 1781, 1962, 2654, 2650, 1239, 3196, 2736, 2318,
                           2482, 2668, 2660, 2000,
                           2630, 2110, 2859, 1935, 1683, 2961, 1227, 1710, 1655, 2722, 2723, 2439, 1782, 1574, 1577,
                           2420, 1699, 3247, 2383,
                           2451, 1130, 1972, 2385, 1189, 1031, 2057, 2111, 1719, 2980, 1066, 1206, 1107, 3199, 3031,
                           2144, 1498, 1965, 4053,
                           2018, 1492, 1375, 2497, 1003, 2938, 1207, 1054, 1885, 2004, 1145, 1914, 2477, 2615, 2008,
                           1009, 2348, 1823, 2071,
                           1775, 1882, 1612, 1153, 1071, 2452, 1016, 1232, 1583, 1760, 1709, 1129, 2384, 3053, 2444,
                           2088, 2142, 3164, 3140,
                           2084, 2336, 1688, 1829, 2323, 3023, 1013, 2450, 2453, 2583, 1555, 1842, 2302, 1345, 1434,
                           2934, 2933, 2048, 3017,
                           2819, 1662, 3120, 1036, 3119, 3077, 2035, 1179, 2233, 2738, 1187, 1979, 2713, 1233, 2114,
                           2163, 2371, 2378, 1595,
                           1470, 4041, 4042, 1482, 3190, 1438, 1593, 1338, 1311, 1691, 1692, 1825, 1046, 1051, 2493,
                           1526, 2768, 2132, 1418,
                           1856, 1615, 1484, 1839, 1087, 2043, 1200, 4142, 3102, 1548, 2401, 2118, 1808, 2175, 1286,
                           2506, 3117, 1826, 1827,
                           2945, 2540, 2215, 1601, 1083, 2718, 1314, 1780, 1197, 1487, 1789, 2178, 2413, 1819, 2002,
                           1166, 3147, 1281, 1246,
                           2140, 3001, 2172, 2932, 2134, 2602, 2447, 1681, 1677, 2356, 2612, 3163, 2264, 1241, 2732,
                           3194, 3103, 2836, 1700,
                           1493, 1695, 1838, 2740, 1053, 1379, 1672, 1680, 2380, 3132, 1964, 3128, 2361, 1801, 2969,
                           1678, 2117, 1346, 1081,
                           1443, 2040, 2835, 1028, 2204, 1370, 1666, 3185, 1343, 2644, 2362, 1843, 3184, 2638, 2096,
                           1404, 1816, 2120, 1679,
                           1809, 1779, 1047, 1488, 3082, 3257, 1689, 3193, 1613, 1973, 2871, 2677, 1052, 3107, 2282,
                           2016, 1350, 2374, 2160,
                           1851, 2756, 2399, 1960, 1216, 1933, 1713, 2221, 3115, 1647, 2923, 1640, 1167, 1341, 4083,
                           2996, 2311, 1134, 1441,
                           2676, 3029, 2191, 2466, 3056, 2101, 2303, 2174, 2033, 2625, 1634, 2411, 1234, 1415, 2017,
                           1558, 1725, 2354, 2823,
                           2081, 2038, 1254, 2097, 1854, 1954, 2709, 3034, 2861, 1530, 2220, 1603, 1991, 2674, 2203,
                           2098, 1085, 3016, 1807,
                           1803, 1806, 2669, 2197, 2218, 1342, 1596, 3024, 2249, 2877, 3037, 3065, 1398, 3182, 1198,
                           1798, 2850, 2734, 1035,
                           1065, 2495, 3111, 1152, 1660, 2459, 1737, 2299, 1182, 3018, 1012, 1994, 2252, 2414, 3070,
                           1356, 1756, 2438, 2631,
                           3109, 2912, 1659, 2340, 2510, 2991, 1157, 1902, 2965, 1074, 3198, 1082, 3011, 2440, 2406,
                           2597, 2463, 1618, 2998,
                           2409, 2350, 1237, 1334, 3020, 2751, 1793, 1602, 1884, 2419, 2755, 2979, 1192, 2181, 2987,
                           2833, 3106, 1883, 1025,
                           2372, 2027, 2517, 1799, 2603, 2745, 1716, 1432, 2967, 1581, 2829, 1014, 2789, 1353, 2364,
                           3118, 2353, 2913, 1042,
                           3244, 3245, 2192, 3127, 3047, 1041, 2047, 3191, 1007, 2339, 2804, 1211, 3121, 1275, 2312,
                           2093, 1702, 1171, 4117,
                           2757, 1895, 1411, 1921, 1629, 1617, 2752, 2787, 1481, 2274, 1236, 1724, 2347, 1862, 2397,
                           1938, 1636, 1698, 1250,
                           1274, 1483, 3155, 2240, 2594, 1795, 2788, 3167, 2803, 1284, 1033, 3015, 2775, 1133, 2122,
                           2879, 1194, 2878, 1787,
                           2183]

    icons_saints: list[Tag] = __collect.collect_icons_saints(session)
    for icon_saint in icons_saints:
        pravicon_saint_id: int = __collect.collect_pravicon_saint_id(icon_saint)
        if pravicon_saint_id in pravicon_saints_ids:
            continue

        logging.info(icon_saint.text)


