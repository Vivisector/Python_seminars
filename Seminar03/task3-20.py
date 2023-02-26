#task 20
# "взвешиваем" слова
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

mWord = input('введите слово для «взвешивания» (буквы могут быть русскими или английскими, заглавными или строчными):\n')
le1 = list('AEIOULNSTR')
le2 = list('DG')
le3 = list('BCMP')
le4 = list('FHVWY')
le5 = list('K')
le8 = list('JX')
le10 = list('QZ')

l1 = list('АВЕИНОРСТ')
l2 = list('ДКЛМПУ')
l3 = list('БГЁЬЯ')
l4 = list('ЙЫ')
l5 = list('ЖЗХЦЧ')
l8 = list('ШЭЮ')
l10 = list('ФЩЪ')

l_all=[le1,le2,le3,le4,le5,le8,le10,l1,l2,l3,l4,l5,l8,l10]
weight = 0

for w in range(len(mWord)): #перебор букв в слове
    for i in range(len(l_all)):#перебор списков букв
        for j in range(len(l_all[i])):#перебор букв в списке
            if (mWord[w] == ((l_all[i])[j]).lower()): 
                if i==0:
                    weight = weight + 1
                elif i ==1:
                    weight = weight + 2
                elif i ==2:
                    weight = weight + 3
                elif i ==3:
                    weight = weight + 4
                elif i ==4:
                    weight = weight + 5
                elif i ==5:
                    weight = weight + 8
                elif i ==6:
                    weight = weight + 10
                elif i ==7:
                    weight = weight + 1
                elif i ==8:
                    weight = weight + 2
                elif i ==9:
                    weight = weight + 3
                elif i ==10:
                    weight = weight + 4
                elif i ==11:
                    weight = weight + 5
                elif i ==12:
                    weight = weight + 8
                elif i ==13:
                    weight = weight + 10
print(f"слово '{mWord}' оценивается в {weight} баллов")
