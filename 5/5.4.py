#!/usr/bin/env python3

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
num_list_rev=num_list[::-1]
word_list_rev=word_list[::-1]

innum=input('Введите число:')
inword=input('Введите слово:')


outnum=num_list_rev.index(int(innum))
outword=word_list_rev.index(inword)
countnum=str(num_list_rev).count(',')+1
countword=str(word_list_rev).count(',')+1


print(num_list)
print(word_list)

print('Индекс последнего вхождения для {} равен {}'.format(innum,(countnum-outnum)))
print('Индекс последнего вхождения для {} равен {}'.format(inword,(countword-outword)))

