entername = input('Введите свое имя: ')

people = {'People':{
        'person1':{'name':'Denis', 'bal':7},
        'person2':{'name':'Pozhar', 'bal':8},
        'person3':{'name':'lexa', 'bal':6},
        'person4':{'name':'Sanya', 'bal':5},
        'person5':{'name':'Sanya2', 'bal':4},
        'person6':{'name':'Oleg', 'bal':3},
        'person7':{'name':'Dimon', 'bal':2},
        }
}    
for personalName in people['People']:
    myPath = people['People']
    if entername == myPath[personalName]['name']:
        if myPath[personalName]['bal'] >= 5:
           print('Поздравляю, вы приняты на работу ')
        else:
            print('Извините вы ненабрали достаточное количество балов')

       