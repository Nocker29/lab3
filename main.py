# # zad1
# A=[1-x for x in range(1,11)]
# print(A)
# B=[4**x for x in range(8)]
# print(B)
# C=[x for x in B if x%2==0]
# print(C)

# # zad3
# zakupy={'Ziemniaki':'kg',
#         'Bułki':'sztuki',
#         'Konserwy':'sztuki',
#         'Jabłka':'kg',
#         'Tabliczka czekolady':'sztuki'
#         }
# lista_sztuki=[key for key,value in zakupy.items() if value.count("sztuki")==1]
# print(lista_sztuki)

# # zad4
# def trojkat_kwadratowy(a,b,c):
#     if (c**2)==(a**2)+(b**2):
#         return 1
#     else:
#         return 0
# print('Podaj dwie przyprostokątne: ')
# a=int(input())
# b=int(input())
# c=int(input('Podaj przeciwprostokątną:\n'))
# if trojkat_kwadratowy(a,b,c)==1:
#     print('Jest to trojkat prostokątny')
# else:
#     print('To nie jest trójkąt prostokątny')