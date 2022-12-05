# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#


def split_terms(equesion):
    line1=equesion.replace('*','')
    line2=line1.replace(' ','')
    line3=line2[:-2]
    line4=line3.replace('-','+-')
    line5=line4.split('+')
    if line5[0]=='':
        line5.pop(0)
    return line5


def get_dict(list):
    coof={}
    for i in range(len(list)):
        if 'x' not in list[i]:
            a=0
            b=list[i]
        else:
            a=list[i].partition('x')[2]
            b=list[i].partition('x')[0]
            if a=='':
                a=1
            if b=='-':
                b=-1
            if b=='':
                b=1
        coof[int(a)]=int(b)
    return coof


with open('eq1.txt','r') as data1:
    eq1=data1.read()
with open('eq2.txt','r') as data2:
    eq2=data2.read()

dict1=get_dict(split_terms(eq1))
dict2=get_dict(split_terms(eq2))

print(dict1)
print(dict2)

if len(dict1)>=len(dict2):
    length=len(dict1)
else:
    length = len(dict2)

new_dict={}
for v in range(length-1, -1, -1):
    if v in dict1.keys() and v in dict2.keys():
        new_dict[v]=dict1[v]+dict2[v]
    else:
        if v in dict1.keys():
            new_dict[v] = dict1[v]
        elif v in dict2.keys():
            new_dict[v] = dict2[v]

print('Проведено сложение многочленов: ')
print(new_dict)

def get_equasion (dictionary):
    text=''
    for i in range(list(dictionary.keys())[0], -1, -1):
        if i in dictionary.keys():
            if dictionary[i]!=0:
                if i==list(dictionary.keys())[0]:
                    if dictionary[i]==1:
                        text += f'x**{i}'
                    elif dictionary[i]==-1:
                        text += f'-x**{i}'
                    else:
                        text+=f'{dictionary[i]}*x**{i}'
                elif i==1:
                    if dictionary[i] == 1:
                        text += f' +x'
                    elif dictionary[i] == -1:
                        text += f' -x'
                    else:
                        text += f' +{dictionary[i]}*x'
                elif i==0:
                    text+=f' +{dictionary[i]}'
                else:
                    text += f' +{dictionary[i]}*x**{i}'
    final=text.replace('+-','-')
    final=final+' = 0'
    return final

new_equasion=get_equasion(new_dict)

print(new_equasion)

file=open('result.txt','w')
file.write(new_equasion)
file.close()

