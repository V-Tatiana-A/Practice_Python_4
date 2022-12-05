# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import random

pow_K=int(input('Введите натуральную степень k: '))

def create_equasion(pow):
    coef={}
    for i in range(pow+1):
        coef[i]=random.randint(-100,100)
    print('Сформированы коэффициенты:')
    for v in reversed(list(coef.values())):
        print(f'{v}', end=' ')
    print()

    equasion=''
    for j in range(pow, -1,-1):
        if coef[j]!=0:
            if coef[j]==1:
                if j==1:
                    equasion+=f'+ x'
                elif j==0:
                    equasion+=f'+ 1'
                elif j==pow:
                    equasion += f'x**{j}'
                else:
                    equasion+=f' +x**{j}'
            elif coef[j]==-1:
                if j==1:
                    equasion+=f' -x'
                elif j==0:
                    equasion+=f' -1 '
                elif j==pow:
                    equasion += f' -x**{j}'
                else:
                    equasion+=f' -x**{j}'
            else:
                if coef[j]>1:
                    if j==1:
                        equasion+=f' +{coef[j]}*x'
                    elif j==0:
                        equasion+=f' +{coef[j]}'
                    elif j==pow:
                        equasion+=f'{coef[j]}*x**{j}'
                    else:
                        equasion+=f' +{coef[j]}*x**{j}'
                if coef[j]<-1:
                    if j==1:
                        equasion+=f' {coef[j]}*x'
                    elif j==0:
                        equasion+=f' {coef[j]}'
                    elif j == pow:
                        equasion+=f'{coef[j]}*x**{j}'
                    else:
                        equasion+=f' {coef[j]}*x**{j}'

    print(equasion +' = 0')
    return equasion +' = 0'

print('Многочлены для степени k сформированы в файлах eq1 и eq2')

file=open('eq1.txt','w')
file.write(create_equasion(pow_K))
file.close()

file2=open('eq2.txt','w')
file2.write(create_equasion(pow_K))
file2.close()


