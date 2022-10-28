import numpy as np

print('zad 81', '\n')

print(np.arange('2020-01-06', '2020-03', dtype='datetime64[D]')[::7], '\n')

print('zad 82', '\n')

A2 = np.array(['001', '002', '003'])
B2 = np.array(['XC', 'YC', 'ZC'])

print(np.char.add(A2, B2), '\n')


print('zad 83', '\n')

A3 = np.array(['1', '2', '3'])

r3 = np.char.zfill(A3, 4)
print(r3, '\n')

print('zad 84', '\n')

A4 = np.array([['PLW CDR 11B TEN', 'AMC LPP'],
              ['CDR PKO KGH', 'CCC QMK']])

r4 =np.char.split(A4, sep=None, maxsplit=None)
print(r4, '\n')

print('zad 85', '\n')

A5 = np.array([['#summer#time#mood'],
              ['#sport#time']])

r5 = np.char.replace(A5, '#', ' ')
rr5 = np.char.strip(r5)

print(rr5, '\n')

print('zad 86', '\n')

A6 = np.array(
    [
        ['#summer#time#mood', '#vibe'],
        ['#sport#time', '#good#time'],
        ['#event#summer', '#fast#move'],
    ]
)


r6 = np.char.count(A6, 'time')

print(r6, '\n')

print('zad 87', '\n')

text = """ALIOR    PLALIOR00045    88 860 000    1 386 216 000    0,891    2,16    14
CCC    PLCCC0000016    27 918 000    1 292 603 400    0,831    5,28    42
CDPROJEKT    PLOPTTC00011    67 348 000    22 864 646 000    14,702    7,39    7
CYFRPLSAT    PLCFRPT00013    275 301 000    6 854 994 900    4,408    1,17    14
DINOPL    PLDINPL00011    47 937 000    8 916 282 000    5,733    9,13    12
JSW    PLJSW0000015    52 636 000    716 902 320    0,461    1,51    24
KGHM    PLKGHM000017    136 410 000    9 881 540 400    6,354    4,78    8
LOTOS    PLLOTOS00025    86 543 000    5 609 717 260    3,607    2,91    16
LPP    PLLPP0000011    1 306 000    7 444 200 000    4,787    1,43    19
MBANK    PLBRE0000012    12 997 000    2 830 746 600    1,820    0,42    24
ORANGEPL    PLTLKPL00017    647 357 000    4 285 503 340    2,756    1,16    13
PEKAO    PLPEKAO00016    176 379 000    9 619 710 660    6,185    5,27    9
PGE    PLPGER000010    796 776 000    3 561 588 720    2,290    2,88    18
PGNIG    PLPGNIG00014    1 624 608 000    6 072 784 704    3,905    1,56    12
PKNORLEN    PLPKN0000018    289 049 000    17 701 360 760    11,382    12,44    8
PKOBP    PLPKO0000016    857 593 000    18 807 014 490    12,093    10,49    9
PLAY    LU1642887738    114 151 000    3 696 209 380    2,377    1,47    16
PZU    PLPZU0000011    568 305 000    17 515 160 100    11,262    6,64    6
SANPL    PLBZ00000044    33 207 000    5 213 499 000    3,352    1,91    18
TAURONPE    PLTAURN00011    1 043 590 000    1 252 308 000    0,805    1,21    33"""

linie7 = text.splitlines()
linie7 = [linia.split('\t') for linia in linie7]

r7 =  np.array(linie7)

print(r7)

print('zad 88', '\n')

np.set_printoptions(linewidth=150)
r8 = np.array([['ALIOR', 'PLALIOR00045', '88 860 000', '1 386 216 000', '0,891', '2,16', '14'],
       ['CCC', 'PLCCC0000016', '27 918 000', '1 292 603 400', '0,831', '5,28', '42'],
       ['CDPROJEKT', 'PLOPTTC00011', '67 348 000', '22 864 646 000', '14,702', '7,39', '7'],
       ['CYFRPLSAT', 'PLCFRPT00013', '275 301 000', '6 854 994 900', '4,408', '1,17', '14'],
       ['DINOPL', 'PLDINPL00011', '47 937 000', '8 916 282 000', '5,733', '9,13', '12'],
       ['JSW', 'PLJSW0000015', '52 636 000', '716 902 320', '0,461', '1,51', '24'],
       ['KGHM', 'PLKGHM000017', '136 410 000', '9 881 540 400', '6,354', '4,78', '8'],
       ['LOTOS', 'PLLOTOS00025', '86 543 000', '5 609 717 260', '3,607', '2,91', '16'],
       ['LPP', 'PLLPP0000011', '1 306 000', '7 444 200 000', '4,787', '1,43', '19'],
       ['MBANK', 'PLBRE0000012', '12 997 000', '2 830 746 600', '1,820', '0,42', '24'],
       ['ORANGEPL', 'PLTLKPL00017', '647 357 000', '4 285 503 340', '2,756', '1,16', '13'],
       ['PEKAO', 'PLPEKAO00016', '176 379 000', '9 619 710 660', '6,185', '5,27', '9'],
       ['PGE', 'PLPGER000010', '796 776 000', '3 561 588 720', '2,290', '2,88', '18'],
       ['PGNIG', 'PLPGNIG00014', '1 624 608 000', '6 072 784 704', '3,905', '1,56', '12'],
       ['PKNORLEN', 'PLPKN0000018', '289 049 000', '17 701 360 760', '11,382', '12,44', '8'],
       ['PKOBP', 'PLPKO0000016', '857 593 000', '18 807 014 490', '12,093', '10,49', '9'],
       ['PLAY', 'LU1642887738', '114 151 000', '3 696 209 380', '2,377', '1,47', '16'],
       ['PZU', 'PLPZU0000011', '568 305 000', '17 515 160 100', '11,262', '6,64', '6'],
       ['SANPL', 'PLBZ00000044', '33 207 000', '5 213 499 000', '3,352', '1,91', '18'],
       ['TAURONPE', 'PLTAURN00011', '1 043 590 000', '1 252 308 000', '0,805', '1,21', '33']], dtype='<U14')

splitowany = np.split(r8, indices_or_sections = [150])
r8 = np.char.replace(r8, " ","")
r8 = np.char.replace(r8, ",",".")


print(splitowany, '\n')
print(r8, '\n')


print('zad 89', '\n')

r9 = np.array([['ALIOR', 'PLALIOR00045', '88860000', '1386216000', '0.891', '2.16', '14'],
       ['CCC', 'PLCCC0000016', '27918000', '1292603400', '0.831', '5.28', '42'],
       ['CDPROJEKT', 'PLOPTTC00011', '67348000', '22864646000', '14.702', '7.39', '7'],
       ['CYFRPLSAT', 'PLCFRPT00013', '275301000', '6854994900', '4.408', '1.17', '14'],
       ['DINOPL', 'PLDINPL00011', '47937000', '8916282000', '5.733', '9.13', '12'],
       ['JSW', 'PLJSW0000015', '52636000', '716902320', '0.461', '1.51', '24'],
       ['KGHM', 'PLKGHM000017', '136410000', '9881540400', '6.354', '4.78', '8'],
       ['LOTOS', 'PLLOTOS00025', '86543000', '5609717260', '3.607', '2.91', '16'],
       ['LPP', 'PLLPP0000011', '1306000', '7444200000', '4.787', '1.43', '19'],
       ['MBANK', 'PLBRE0000012', '12997000', '2830746600', '1.820', '0.42', '24'],
       ['ORANGEPL', 'PLTLKPL00017', '647357000', '4285503340', '2.756', '1.16', '13'],
       ['PEKAO', 'PLPEKAO00016', '176379000', '9619710660', '6.185', '5.27', '9'],
       ['PGE', 'PLPGER000010', '796776000', '3561588720', '2.290', '2.88', '18'],
       ['PGNIG', 'PLPGNIG00014', '1624608000', '6072784704', '3.905', '1.56', '12'],
       ['PKNORLEN', 'PLPKN0000018', '289049000', '17701360760', '11.382', '12.44', '8'],
       ['PKOBP', 'PLPKO0000016', '857593000', '18807014490', '12.093', '10.49', '9'],
       ['PLAY', 'LU1642887738', '114151000', '3696209380', '2.377', '1.47', '16'],
       ['PZU', 'PLPZU0000011', '568305000', '17515160100', '11.262', '6.64', '6'],
       ['SANPL', 'PLBZ00000044', '33207000', '5213499000', '3.352', '1.91', '18'],
       ['TAURONPE', 'PLTAURN00011', '1043590000', '1252308000', '0.805', '1.21', '33']], dtype='<U12')

stocks_startswith_P = r9[np.char.startswith(r9[:, 0], 'P')]

print(stocks_startswith_P, '\n')

print('zad 90', '\n')

np.set_printoptions(linewidth=150)

stocks_startswith_P90 = np.array([['PEKAO', 'PLPEKAO00016', '176379000', '9619710660', '6.185', '5.27', '9'],
       ['PGE', 'PLPGER000010', '796776000', '3561588720', '2.290', '2.88', '18'],
       ['PGNIG', 'PLPGNIG00014', '1624608000', '6072784704', '3.905', '1.56', '12'],
       ['PKNORLEN', 'PLPKN0000018', '289049000', '17701360760', '11.382', '12.44', '8'],
       ['PKOBP', 'PLPKO0000016', '857593000', '18807014490', '12.093', '10.49', '9'],
       ['PLAY', 'LU1642887738', '114151000', '3696209380', '2.377', '1.47', '16'],
       ['PZU', 'PLPZU0000011', '568305000', '17515160100', '11.262', '6.64', '6']], dtype='<U12')



aaa = np.round_(stocks_startswith_P90[:, 4].astype(float).sum(), decimals=2)

print(aaa, '\n')

















result = np.array([['ALIOR', 'PLALIOR00045', '88860000', '1386216000', '0.891', '2.16', '14'],
       ['CCC', 'PLCCC0000016', '27918000', '1292603400', '0.831', '5.28', '42'],
       ['CDPROJEKT', 'PLOPTTC00011', '67348000', '22864646000', '14.702', '7.39', '7'],
       ['CYFRPLSAT', 'PLCFRPT00013', '275301000', '6854994900', '4.408', '1.17', '14'],
       ['DINOPL', 'PLDINPL00011', '47937000', '8916282000', '5.733', '9.13', '12'],
       ['JSW', 'PLJSW0000015', '52636000', '716902320', '0.461', '1.51', '24'],
       ['KGHM', 'PLKGHM000017', '136410000', '9881540400', '6.354', '4.78', '8'],
       ['LOTOS', 'PLLOTOS00025', '86543000', '5609717260', '3.607', '2.91', '16'],
       ['LPP', 'PLLPP0000011', '1306000', '7444200000', '4.787', '1.43', '19'],
       ['MBANK', 'PLBRE0000012', '12997000', '2830746600', '1.820', '0.42', '24'],
       ['ORANGEPL', 'PLTLKPL00017', '647357000', '4285503340', '2.756', '1.16', '13'],
       ['PEKAO', 'PLPEKAO00016', '176379000', '9619710660', '6.185', '5.27', '9'],
       ['PGE', 'PLPGER000010', '796776000', '3561588720', '2.290', '2.88', '18'],
       ['PGNIG', 'PLPGNIG00014', '1624608000', '6072784704', '3.905', '1.56', '12'],
       ['PKNORLEN', 'PLPKN0000018', '289049000', '17701360760', '11.382', '12.44', '8'],
       ['PKOBP', 'PLPKO0000016', '857593000', '18807014490', '12.093', '10.49', '9'],
       ['PLAY', 'LU1642887738', '114151000', '3696209380', '2.377', '1.47', '16'],
       ['PZU', 'PLPZU0000011', '568305000', '17515160100', '11.262', '6.64', '6'],
       ['SANPL', 'PLBZ00000044', '33207000', '5213499000', '3.352', '1.91', '18'],
       ['TAURONPE', 'PLTAURN00011', '1043590000', '1252308000', '0.805', '1.21', '33']], dtype='<U12')




























































































































































































