# ==============================================================================
# description     :Optimization models for teaching purposes
# author          :Roberto Pinto
# date            :2022.03.22
# version         :1.0
# notes           :This software is meant for teaching purpose only and it is provided as-is under the GPL license.
#                  The models are inspired by the book Watson, M., Lewis, S., Cacioppi, P., Jayaraman, J. (2013)
#                  Supply Chain Network Design, Pearson. 
#                  http://networkdesignbook.com/
#                  All the data has been taken from the book.
#                  The software is provided as-is, with no guarantee by the author.
# ==============================================================================

# Data
from data_structures import Warehouse, Customer

warehouses = {5: ('Anápolis', 'Anápolis', 'Brazil', -16.32, -48.96),
 19: ('Belém', 'Belém', 'Brazil', -1.44, -48.5),
 22: ('Betim', 'Betim', 'Brazil', -19.97, -44.19),
 32: ('Campina Grande', 'Campina Grande', 'Brazil', -7.23, -35.88),
 34: ('Campo Grande', 'Campo Grande', 'Brazil', -20.45, -54.63),
 38: ('Cariacica', 'Cariacica', 'Brazil', -20.23, -40.37),
 40: ('Cascavel', 'Cascavel', 'Brazil', -24.96, -53.46),
 43: ('Caxias do Sul', 'Caxias do Sul', 'Brazil', -29.18, -51.17),
 49: ('Cuiabá', 'Cuiabá', 'Brazil', -15.61, -56.09),
 94: ('Juiz de Fora', 'Juiz de Fora', 'Brazil', -21.75, -43.36),
 103: ('Maceió', 'Maceió', 'Brazil', -9.65, -35.75),
 105: ('Manaus', 'Manaus', 'Brazil', -3.12, -60.02),
 113: ('Montes Claros', 'Montes Claros', 'Brazil', -16.72, -43.86),
 115: ('Natal', 'Natal', 'Brazil', -5.8, -35.22),
 125: ('Palmas', 'Palmas', 'Brazil', -10.27, -48.31),
 137: ('Piracicaba', 'Piracicaba', 'Brazil', -22.71, -47.64),
 139: ('Ponta Grossa', 'Ponta Grossa', 'Brazil', -25.09, -50.16),
 142: ('Porto Velho', 'Porto Velho', 'Brazil', -8.76, -63.91),
 147: ('Recife', 'Recife', 'Brazil', -8.08, -34.92),
 157: ('Salvador', 'Salvador', 'Brazil', -12.97, -38.5),
 160: ('Santa Maria', 'Santa Maria', 'Brazil', -29.69, -53.83),
 164: ('Santos', 'Santos', 'Brazil', -23.95, -46.33),
 170: ('São José do Rio Preto', 'São José do Rio Preto', 'Brazil', -20.8, -49.39),
 189: ('Teresina', 'Teresina', 'Brazil', -5.1, -42.8),
 193: ('Uberlândia', 'Uberlândia', 'Brazil', -18.9, -48.28)}

customers = {1: ('São Paulo Region', 'São Paulo Region', 'Brazil', -23.53, -46.63),
 2: ('Rio de Janeiro Region',
  'Rio de Janeiro Region',
  'Brazil',
  -22.91,
  -43.2),
 3: ('Minas Gerais Region', 'Minas Gerais Region', 'Brazil', -19.92, -43.94),
 4: ('Bahia Region', 'Bahia Region', 'Brazil', -12.97, -38.5),
 5: ('Paraná Region', 'Paraná Region', 'Brazil', -25.42, -49.29),
 6: ('Rio Grande do Sul Region',
  'Rio Grande do Sul Region',
  'Brazil',
  -30.04,
  -51.22),
 7: ('Pernambuco Region', 'Pernambuco Region', 'Brazil', -8.08, -34.92),
 8: ('Ceará Region', 'Ceará Region', 'Brazil', -3.78, -38.59),
 9: ('Santa Catarina Region',
  'Santa Catarina Region',
  'Brazil',
  -26.32,
  -48.84),
 10: ('Pará Region', 'Pará Region', 'Brazil', -1.44, -48.5),
 11: ('Goiás Region', 'Goiás Region', 'Brazil', -16.72, -49.26),
 12: ('Distrito Federal Region',
  'Distrito Federal Region',
  'Brazil',
  -15.78,
  -47.91),
 13: ('Espírito Santo Region',
  'Espírito Santo Region',
  'Brazil',
  -20.13,
  -40.32),
 14: ('Amazonas Region', 'Amazonas Region', 'Brazil', -3.12, -60.02),
 15: ('Maranhão Region', 'Maranhão Region', 'Brazil', -2.5, -44.3),
 16: ('Alagoas Region', 'Alagoas Region', 'Brazil', -9.65, -35.75),
 17: ('Rio Grande do Norte Region',
  'Rio Grande do Norte Region',
  'Brazil',
  -5.8,
  -35.22),
 18: ('Paraíba Region', 'Paraíba Region', 'Brazil', -7.12, -34.86),
 19: ('Mato Grosso Region', 'Mato Grosso Region', 'Brazil', -15.61, -56.09),
 20: ('Mato Grosso do Sul Region',
  'Mato Grosso do Sul Region',
  'Brazil',
  -20.45,
  -54.63),
 21: ('Piauí Region', 'Piauí Region', 'Brazil', -5.1, -42.8),
 22: ('Sergipe Region', 'Sergipe Region', 'Brazil', -10.91, -37.07),
 23: ('Amapá Region', 'Amapá Region', 'Brazil', 0.04, -51.05),
 24: ('Rondônia Region', 'Rondônia Region', 'Brazil', -8.76, -63.91),
 25: ('Acre Region', 'Acre Region', 'Brazil', -9.98, -67.82)}

customer_demands = {1: 29029226,
 2: 13370786,
 3: 8663076,
 4: 5899854,
 5: 4947330,
 6: 4912164,
 7: 3921090,
 8: 3579449,
 9: 2657192,
 10: 2597519,
 11: 2559855,
 12: 2551909,
 13: 1896478,
 14: 1865277,
 15: 1383837,
 16: 1330514,
 17: 1239777,
 18: 1230034,
 19: 1184391,
 20: 1010989,
 21: 980832,
 22: 735616,
 23: 440064,
 24: 340522,
 25: 338812}


distance = {(5, 1): 979.29,
 (5, 2): 1109.1599999999999,
 (5, 3): 776.88,
 (5, 4): 1385.28,
 (5, 5): 1184.04,
 (5, 6): 1804.1399999999999,
 (5, 7): 2079.0899999999997,
 (5, 8): 2100.15,
 (5, 9): 1299.87,
 (5, 10): 1935.1799999999998,
 (5, 11): 64.35,
 (5, 12): 148.59,
 (5, 13): 1175.85,
 (5, 14): 2223.0,
 (5, 15): 1893.06,
 (5, 16): 1883.6999999999998,
 (5, 17): 2220.66,
 (5, 18): 2155.14,
 (5, 19): 896.2199999999999,
 (5, 20): 882.18,
 (5, 21): 1656.7199999999998,
 (5, 22): 1657.8899999999999,
 (5, 23): 2143.44,
 (5, 24): 2135.25,
 (5, 25): 2523.69,
 (19, 1): 2881.71,
 (19, 2): 2870.0099999999998,
 (19, 3): 2471.04,
 (19, 4): 1976.1299999999999,
 (19, 5): 3119.22,
 (19, 6): 3733.47,
 (19, 7): 1958.58,
 (19, 8): 1322.1,
 (19, 9): 3235.0499999999997,
 (19, 10): 0.0,
 (19, 11): 1988.9999999999998,
 (19, 12): 1866.1499999999999,
 (19, 13): 2643.0299999999997,
 (19, 14): 1512.81,
 (19, 15): 562.77,
 (19, 16): 1963.26,
 (19, 17): 1813.5,
 (19, 18): 1915.29,
 (19, 19): 2083.77,
 (19, 20): 2591.5499999999997,
 (19, 21): 879.8399999999999,
 (19, 22): 1921.1399999999999,
 (19, 23): 383.76,
 (19, 24): 2208.96,
 (19, 25): 2731.95,
 (22, 1): 548.73,
 (22, 2): 400.14,
 (22, 3): 31.589999999999996,
 (22, 4): 1153.62,
 (22, 5): 936.0,
 (22, 6): 1547.9099999999999,
 (22, 7): 1936.35,
 (22, 8): 2220.66,
 (22, 9): 994.4999999999999,
 (22, 10): 2471.04,
 (22, 11): 754.65,
 (22, 12): 712.53,
 (22, 13): 472.67999999999995,
 (22, 14): 2971.7999999999997,
 (22, 15): 2270.97,
 (22, 16): 1709.37,
 (22, 17): 2163.33,
 (22, 18): 2042.82,
 (22, 19): 1577.1599999999999,
 (22, 20): 1275.3,
 (22, 21): 1941.03,
 (22, 22): 1476.54,
 (22, 23): 2743.6499999999996,
 (22, 24): 2874.6899999999996,
 (22, 25): 3233.8799999999997,
 (32, 1): 2508.48,
 (32, 2): 2234.7,
 (32, 3): 1937.52,
 (32, 4): 817.8299999999999,
 (32, 5): 2891.0699999999997,
 (32, 6): 3506.49,
 (32, 7): 166.14,
 (32, 8): 569.79,
 (32, 9): 2954.25,
 (32, 10): 1800.6299999999999,
 (32, 11): 2100.15,
 (32, 12): 1891.8899999999999,
 (32, 13): 1767.87,
 (32, 14): 3169.5299999999997,
 (32, 15): 1251.8999999999999,
 (32, 16): 314.72999999999996,
 (32, 17): 204.75,
 (32, 18): 132.20999999999998,
 (32, 19): 2793.96,
 (32, 20): 2919.1499999999996,
 (32, 21): 936.0,
 (32, 22): 501.92999999999995,
 (32, 23): 2182.0499999999997,
 (32, 24): 3612.9599999999996,
 (32, 25): 4119.57,
 (34, 1): 1043.6399999999999,
 (34, 2): 1416.87,
 (34, 3): 1305.72,
 (34, 4): 2228.85,
 (34, 5): 909.0899999999999,
 (34, 6): 1309.23,
 (34, 7): 2953.08,
 (34, 8): 2969.46,
 (34, 9): 1029.6,
 (34, 10): 2591.5499999999997,
 (34, 11): 820.17,
 (34, 12): 1028.4299999999998,
 (34, 13): 1744.4699999999998,
 (34, 14): 2354.04,
 (34, 15): 2675.79,
 (34, 16): 2750.6699999999996,
 (34, 17): 3102.8399999999997,
 (34, 18): 3032.64,
 (34, 19): 654.03,
 (34, 20): 0.0,
 (34, 21): 2493.27,
 (34, 22): 2520.18,
 (34, 23): 2702.7,
 (34, 24): 1915.29,
 (34, 25): 2139.93,
 (38, 1): 868.14,
 (38, 2): 487.89,
 (38, 3): 437.58,
 (38, 4): 972.27,
 (38, 5): 1263.6,
 (38, 6): 1802.9699999999998,
 (38, 7): 1722.2399999999998,
 (38, 8): 2150.46,
 (38, 9): 1283.49,
 (38, 10): 2652.39,
 (38, 11): 1187.55,
 (38, 12): 1096.29,
 (38, 13): 14.04,
 (38, 14): 3339.18,
 (38, 15): 2358.72,
 (38, 16): 1492.9199999999998,
 (38, 17): 1985.4899999999998,
 (38, 18): 1840.4099999999999,
 (38, 19): 2033.4599999999998,
 (38, 20): 1737.4499999999998,
 (38, 21): 1991.34,
 (38, 22): 1279.98,
 (38, 23): 2964.7799999999997,
 (38, 24): 3309.93,
 (38, 25): 3686.6699999999996,
 (40, 1): 830.6999999999999,
 (40, 2): 1247.22,
 (40, 3): 1317.4199999999998,
 (40, 4): 2406.69,
 (40, 5): 493.73999999999995,
 (40, 6): 709.02,
 (40, 7): 3178.89,
 (40, 8): 3322.7999999999997,
 (40, 9): 569.79,
 (40, 10): 3120.39,
 (40, 11): 1186.3799999999999,
 (40, 12): 1371.24,
 (40, 13): 1696.5,
 (40, 14): 2955.4199999999996,
 (40, 15): 3137.9399999999996,
 (40, 16): 2958.93,
 (40, 17): 3371.9399999999996,
 (40, 18): 3274.83,
 (40, 19): 1256.58,
 (40, 20): 602.55,
 (40, 21): 2903.9399999999996,
 (40, 22): 2723.7599999999998,
 (40, 23): 3264.2999999999997,
 (40, 24): 2472.21,
 (40, 25): 2633.6699999999996,
 (43, 1): 904.41,
 (43, 2): 1236.6899999999998,
 (43, 3): 1475.37,
 (43, 4): 2603.25,
 (43, 5): 534.6899999999999,
 (43, 6): 112.32,
 (43, 7): 3385.98,
 (43, 8): 3648.06,
 (43, 9): 458.64,
 (43, 10): 3621.1499999999996,
 (43, 11): 1635.6599999999999,
 (43, 12): 1785.4199999999998,
 (43, 13): 1738.62,
 (43, 14): 3560.31,
 (43, 15): 3570.8399999999997,
 (43, 16): 3157.83,
 (43, 17): 3616.47,
 (43, 18): 3494.79,
 (43, 19): 1860.3,
 (43, 20): 1206.27,
 (43, 21): 3295.89,
 (43, 22): 2927.3399999999997,
 (43, 23): 3798.99,
 (43, 24): 3075.93,
 (43, 25): 3213.99,
 (49, 1): 1549.08,
 (49, 2): 1842.75,
 (49, 3): 1604.07,
 (49, 4): 2241.72,
 (49, 5): 1519.83,
 (49, 6): 1964.4299999999998,
 (49, 7): 2862.99,
 (49, 8): 2715.5699999999997,
 (49, 9): 1646.1899999999998,
 (49, 10): 2083.77,
 (49, 11): 864.63,
 (49, 12): 1023.7499999999999,
 (49, 13): 2036.9699999999998,
 (49, 14): 1700.01,
 (49, 15): 2276.8199999999997,
 (49, 16): 2692.1699999999996,
 (49, 17): 2951.91,
 (49, 18): 2919.1499999999996,
 (49, 19): 0.0,
 (49, 20): 654.03,
 (49, 21): 2178.54,
 (49, 22): 2481.5699999999997,
 (49, 23): 2135.25,
 (49, 24): 1333.8,
 (49, 25): 1656.7199999999998,
 (94, 1): 455.13,
 (94, 2): 152.1,
 (94, 3): 248.04,
 (94, 4): 1290.51,
 (94, 5): 851.76,
 (94, 6): 1415.6999999999998,
 (94, 7): 2067.39,
 (94, 8): 2412.54,
 (94, 9): 881.01,
 (94, 10): 2719.08,
 (94, 11): 975.78,
 (94, 12): 957.06,
 (94, 13): 424.71,
 (94, 14): 3208.14,
 (94, 15): 2504.97,
 (94, 16): 1838.07,
 (94, 17): 2313.0899999999997,
 (94, 18): 2180.8799999999997,
 (94, 19): 1758.51,
 (94, 20): 1377.09,
 (94, 21): 2165.67,
 (94, 22): 1612.26,
 (94, 23): 2996.37,
 (94, 24): 3074.7599999999998,
 (94, 25): 3412.89,
 (103, 1): 2254.5899999999997,
 (103, 2): 1957.4099999999999,
 (103, 3): 1684.8,
 (103, 4): 555.75,
 (103, 5): 2645.37,
 (103, 6): 3247.9199999999996,
 (103, 7): 230.48999999999998,
 (103, 8): 847.0799999999999,
 (103, 9): 2700.3599999999997,
 (103, 10): 1963.26,
 (103, 11): 1939.86,
 (103, 12): 1735.11,
 (103, 13): 1477.7099999999998,
 (103, 14): 3246.75,
 (103, 15): 1443.78,
 (103, 16): 0.0,
 (103, 17): 505.43999999999994,
 (103, 18): 348.65999999999997,
 (103, 19): 2692.1699999999996,
 (103, 20): 2750.6699999999996,
 (103, 21): 1084.59,
 (103, 22): 235.17,
 (103, 23): 2347.02,
 (103, 24): 3614.1299999999997,
 (103, 25): 4106.7,
 (105, 1): 3142.62,
 (105, 2): 3332.16,
 (105, 3): 2988.18,
 (105, 4): 3047.85,
 (105, 5): 3194.1,
 (105, 6): 3663.27,
 (105, 7): 3309.93,
 (105, 8): 2782.2599999999998,
 (105, 9): 3322.7999999999997,
 (105, 10): 1512.81,
 (105, 11): 2239.3799999999997,
 (105, 12): 2260.44,
 (105, 13): 3335.6699999999996,
 (105, 14): 0.0,
 (105, 15): 2042.82,
 (105, 16): 3246.75,
 (105, 17): 3232.7099999999996,
 (105, 18): 3298.23,
 (105, 19): 1700.01,
 (105, 20): 2354.04,
 (105, 21): 2247.5699999999997,
 (105, 22): 3127.41,
 (105, 23): 1235.52,
 (105, 24): 889.1999999999999,
 (105, 25): 1345.5,
 (113, 1): 947.6999999999999,
 (113, 2): 808.4699999999999,
 (113, 3): 416.52,
 (113, 4): 831.87,
 (113, 5): 1308.06,
 (113, 6): 1939.86,
 (113, 7): 1595.8799999999999,
 (113, 8): 1811.1599999999999,
 (113, 9): 1385.28,
 (113, 10): 2073.24,
 (113, 11): 672.75,
 (113, 12): 519.48,
 (113, 13): 622.4399999999999,
 (113, 14): 2717.91,
 (113, 15): 1849.77,
 (113, 16): 1377.09,
 (113, 17): 1795.9499999999998,
 (113, 18): 1692.99,
 (113, 19): 1533.87,
 (113, 20): 1412.1899999999998,
 (113, 21): 1516.32,
 (113, 22): 1141.9199999999998,
 (113, 23): 2365.74,
 (113, 24): 2742.48,
 (113, 25): 3151.98,
 (115, 1): 2710.89,
 (115, 2): 2439.45,
 (115, 3): 2141.1,
 (115, 4): 1022.5799999999999,
 (115, 5): 3093.48,
 (115, 6): 3710.0699999999997,
 (115, 7): 298.34999999999997,
 (115, 8): 508.95,
 (115, 9): 3157.83,
 (115, 10): 1813.5,
 (115, 11): 2282.67,
 (115, 12): 2074.41,
 (115, 13): 1971.4499999999998,
 (115, 14): 3232.7099999999996,
 (115, 15): 1253.07,
 (115, 16): 505.43999999999994,
 (115, 17): 0.0,
 (115, 18): 177.83999999999997,
 (115, 19): 2951.91,
 (115, 20): 3102.8399999999997,
 (115, 21): 985.14,
 (115, 22): 705.51,
 (115, 23): 2190.24,
 (115, 24): 3718.2599999999998,
 (115, 25): 4230.719999999999,
 (125, 1): 1736.28,
 (125, 2): 1762.02,
 (125, 3): 1368.8999999999999,
 (125, 4): 1297.53,
 (125, 5): 1973.79,
 (125, 6): 2593.89,
 (125, 7): 1742.1299999999999,
 (125, 8): 1510.4699999999998,
 (125, 9): 2087.2799999999997,
 (125, 10): 1147.77,
 (125, 11): 847.0799999999999,
 (125, 12): 718.38,
 (125, 13): 1626.3,
 (125, 14): 1773.7199999999998,
 (125, 15): 1134.8999999999999,
 (125, 16): 1609.9199999999998,
 (125, 17): 1781.9099999999999,
 (125, 18): 1776.06,
 (125, 19): 1205.1,
 (125, 20): 1542.06,
 (125, 21): 976.9499999999999,
 (125, 22): 1439.1,
 (125, 23): 1386.4499999999998,
 (125, 24): 2010.06,
 (125, 25): 2496.7799999999997,
 (137, 1): 161.45999999999998,
 (137, 2): 532.35,
 (137, 3): 576.81,
 (137, 4): 1696.5,
 (137, 5): 403.65,
 (137, 6): 1040.1299999999999,
 (137, 7): 2478.06,
 (137, 8): 2712.06,
 (137, 9): 490.22999999999996,
 (137, 10): 2767.0499999999997,
 (137, 11): 803.79,
 (137, 12): 902.0699999999999,
 (137, 13): 946.53,
 (137, 14): 2985.8399999999997,
 (137, 15): 2660.58,
 (137, 16): 2252.25,
 (137, 17): 2694.5099999999998,
 (137, 18): 2582.19,
 (137, 19): 1387.62,
 (137, 20): 895.05,
 (137, 21): 2369.25,
 (137, 22): 2018.2499999999998,
 (137, 23): 2989.35,
 (137, 24): 2721.4199999999996,
 (137, 25): 3006.8999999999996,
 (139, 1): 464.48999999999995,
 (139, 2): 873.9899999999999,
 (139, 3): 1005.03,
 (139, 4): 2127.06,
 (139, 5): 111.14999999999999,
 (139, 6): 655.1999999999999,
 (139, 7): 2908.62,
 (139, 8): 3125.0699999999997,
 (139, 9): 222.29999999999998,
 (139, 10): 3081.7799999999997,
 (139, 11): 1093.95,
 (139, 12): 1241.37,
 (139, 13): 1344.33,
 (139, 14): 3111.0299999999997,
 (139, 15): 3026.79,
 (139, 16): 2682.81,
 (139, 17): 3122.73,
 (139, 18): 3011.58,
 (139, 19): 1428.57,
 (139, 20): 806.13,
 (139, 21): 2756.52,
 (139, 22): 2448.81,
 (139, 23): 3268.98,
 (139, 24): 2721.4199999999996,
 (139, 25): 2934.3599999999997,
 (142, 1): 2882.8799999999997,
 (142, 2): 3169.5299999999997,
 (142, 3): 2899.2599999999998,
 (142, 4): 3287.7,
 (142, 5): 2820.87,
 (142, 6): 3168.3599999999997,
 (142, 7): 3728.79,
 (142, 8): 3334.5,
 (142, 9): 2943.72,
 (142, 10): 2208.96,
 (142, 11): 2124.72,
 (142, 12): 2226.5099999999998,
 (142, 13): 3311.1,
 (142, 14): 889.1999999999999,
 (142, 15): 2662.9199999999996,
 (142, 16): 3614.1299999999997,
 (142, 17): 3718.2599999999998,
 (142, 18): 3745.1699999999996,
 (142, 19): 1333.8,
 (142, 20): 1915.29,
 (142, 21): 2764.71,
 (142, 22): 3447.99,
 (142, 23): 2020.59,
 (142, 24): 0.0,
 (142, 25): 526.5,
 (147, 1): 2482.74,
 (147, 2): 2187.9,
 (147, 3): 1912.9499999999998,
 (147, 4): 782.7299999999999,
 (147, 5): 2872.35,
 (147, 6): 3477.24,
 (147, 7): 0.0,
 (147, 8): 733.5899999999999,
 (147, 9): 2928.5099999999998,
 (147, 10): 1958.58,
 (147, 11): 2137.5899999999997,
 (147, 12): 1930.4999999999998,
 (147, 13): 1707.03,
 (147, 14): 3309.93,
 (147, 15): 1414.53,
 (147, 16): 230.48999999999998,
 (147, 17): 298.34999999999997,
 (147, 18): 125.19,
 (147, 19): 2862.99,
 (147, 20): 2953.08,
 (147, 21): 1089.27,
 (147, 22): 459.80999999999995,
 (147, 23): 2341.17,
 (147, 24): 3728.79,
 (147, 25): 4229.55,
 (157, 1): 1700.01,
 (157, 2): 1416.87,
 (157, 3): 1129.05,
 (157, 4): 0.0,
 (157, 5): 2089.62,
 (157, 6): 2695.68,
 (157, 7): 782.7299999999999,
 (157, 8): 1194.57,
 (157, 9): 2145.7799999999997,
 (157, 10): 1976.1299999999999,
 (157, 11): 1436.76,
 (157, 12): 1240.1999999999998,
 (157, 13): 958.2299999999999,
 (157, 14): 3047.85,
 (157, 15): 1552.59,
 (157, 16): 555.75,
 (157, 17): 1022.5799999999999,
 (157, 18): 891.54,
 (157, 19): 2241.72,
 (157, 20): 2228.85,
 (157, 21): 1161.81,
 (157, 22): 324.09,
 (157, 23): 2340.0,
 (157, 24): 3287.7,
 (157, 25): 3753.3599999999997,
 (160, 1): 1158.3,
 (160, 2): 1518.6599999999999,
 (160, 3): 1723.4099999999999,
 (160, 4): 2851.29,
 (160, 5): 762.8399999999999,
 (160, 6): 297.18,
 (160, 7): 3635.1899999999996,
 (160, 8): 3855.1499999999996,
 (160, 9): 720.7199999999999,
 (160, 10): 3731.1299999999997,
 (160, 11): 1771.3799999999999,
 (160, 12): 1942.1999999999998,
 (160, 13): 2017.08,
 (160, 14): 3536.91,
 (160, 15): 3725.2799999999997,
 (160, 16): 3408.2099999999996,
 (160, 17): 3853.9799999999996,
 (160, 18): 3739.3199999999997,
 (160, 19): 1849.77,
 (160, 20): 1205.1,
 (160, 21): 3471.39,
 (160, 22): 3175.3799999999997,
 (160, 23): 3880.89,
 (160, 24): 2984.6699999999996,
 (160, 25): 3074.7599999999998,
 (164, 1): 65.52,
 (164, 2): 396.63,
 (164, 3): 597.87,
 (164, 4): 1722.2399999999998,
 (164, 5): 398.96999999999997,
 (164, 6): 973.4399999999999,
 (164, 7): 2504.97,
 (164, 8): 2796.2999999999997,
 (164, 9): 427.04999999999995,
 (164, 10): 2939.04,
 (164, 11): 1005.03,
 (164, 12): 1079.9099999999999,
 (164, 13): 877.5,
 (164, 14): 3206.97,
 (164, 15): 2799.81,
 (164, 16): 2275.6499999999996,
 (164, 17): 2737.7999999999997,
 (164, 18): 2613.7799999999997,
 (164, 19): 1611.09,
 (164, 20): 1097.46,
 (164, 21): 2489.7599999999998,
 (164, 22): 2046.33,
 (164, 23): 3175.3799999999997,
 (164, 24): 2944.89,
 (164, 25): 3223.35,
 (170, 1): 486.71999999999997,
 (170, 2): 795.5999999999999,
 (170, 3): 673.92,
 (170, 4): 1692.99,
 (170, 5): 600.2099999999999,
 (170, 6): 1220.31,
 (170, 7): 2457.0,
 (170, 8): 2600.91,
 (170, 9): 720.7199999999999,
 (170, 10): 2519.0099999999998,
 (170, 11): 531.18,
 (170, 12): 677.43,
 (170, 13): 1107.99,
 (170, 14): 2662.9199999999996,
 (170, 15): 2465.19,
 (170, 16): 2239.3799999999997,
 (170, 17): 2644.2,
 (170, 18): 2550.6,
 (170, 19): 1067.04,
 (170, 20): 638.8199999999999,
 (170, 21): 2204.2799999999997,
 (170, 22): 2004.2099999999998,
 (170, 23): 2717.91,
 (170, 24): 2400.8399999999997,
 (170, 25): 2700.3599999999997,
 (189, 1): 2444.1299999999997,
 (189, 2): 2315.43,
 (189, 3): 1931.6699999999998,
 (189, 4): 1161.81,
 (189, 5): 2762.37,
 (189, 6): 3402.3599999999997,
 (189, 7): 1089.27,
 (189, 8): 572.13,
 (189, 9): 2859.48,
 (189, 10): 879.8399999999999,
 (189, 11): 1719.8999999999999,
 (189, 12): 1533.87,
 (189, 13): 1978.4699999999998,
 (189, 14): 2247.5699999999997,
 (189, 15): 389.60999999999996,
 (189, 16): 1084.59,
 (189, 17): 985.14,
 (189, 18): 1058.85,
 (189, 19): 2178.54,
 (189, 20): 2493.27,
 (189, 21): 0.0,
 (189, 22): 1055.34,
 (189, 23): 1262.4299999999998,
 (189, 24): 2764.71,
 (189, 25): 3285.3599999999997,
 (193, 1): 634.14,
 (193, 2): 807.3,
 (193, 3): 548.73,
 (193, 4): 1444.9499999999998,
 (193, 5): 856.4399999999999,
 (193, 6): 1489.4099999999999,
 (193, 7): 2196.0899999999997,
 (193, 8): 2318.94,
 (193, 9): 966.42,
 (193, 10): 2269.7999999999997,
 (193, 11): 307.71,
 (193, 12): 408.33,
 (193, 13): 988.65,
 (193, 14): 2536.56,
 (193, 15): 2191.41,
 (193, 16): 1983.1499999999999,
 (193, 17): 2373.93,
 (193, 18): 2285.0099999999998,
 (193, 19): 1060.02,
 (193, 20): 802.62,
 (193, 21): 1923.4799999999998,
 (193, 22): 1749.1499999999999,
 (193, 23): 2487.42,
 (193, 24): 2370.42,
 (193, 25): 2716.74}

# Accounting for circuity factor
#distance = {(w, c): distance[w, c] * 1.17 for w in warehouses.keys() for c in customers.keys()}


# Convert data using standard nametuple

for k, value in warehouses.items():
    warehouses[k] = Warehouse(name=value[0],
                              city=value[1],
                              state=value[2],
                              zipcode=None,
                              latitude=value[3],
                              longitude=value[4],
                              capacity=None,
                              fixed_cost=None)

for k, value in customers.items():
    customers[k] = Customer(name=value[0],
                            city=value[1],
                            state=value[2],
                            zipcode=None,
                            latitude=value[3],
                            longitude=value[4],
                            demand=customer_demands[k])

