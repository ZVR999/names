# python names.py

#Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def dicReader(dic):
    dstr = ''
    for x in range(0,len(dic)):
        dstr += dic[x]['first_name']+' '+dic[x]['last_name']+'\n'
    print dstr
dicReader(students)

#Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def letsGo(maindic):
    for dic in maindic:
        counter = 0
        print dic 
        for x in maindic[dic]:
            counter += 1
            first = x['first_name'].upper()
            last = x['last_name'].upper()
            length = str(len(x['first_name'])+len(x['last_name']))
            print "{} - {} {} - {}".format(counter,first,last,length)
letsGo(users)