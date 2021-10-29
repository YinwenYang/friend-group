"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class PersonData:
    def __init__(self, name, age, job, relationship):
        self.name = name
        self.age = age
        self.job = job
        self.relationship = relationship
    
def del_relationship(name1, name2, group):
    del group[name1].relationship[name2]
    del group[name2].relationship[name1] 

def add_person(name, age, job, relationship, group):
    person = PersonData(name, age, job, relationship)
    group[name] = person

def average_age(group):
    ages = []
    for person in group:
        ages.append(group[person].age)
    return sum(ages)/len(ages)




Lifeng = PersonData('Lifeng', 23, 'student', {'Keru':'classmate', 'Yinwen':'friend'})
Yinwen = PersonData('Yinwen', 22, 'student', {'Keru':'partner','Lifeng':'friend'})
Keru = PersonData('Keru', 21, 'student', {'Yinwen':'friend','Lifeng':'classmate'})


my_group = {'Lifeng':Lifeng, 'Keru':Keru, 'Yinwen':Yinwen}

#print(my_group['Lifeng'].relationship)
#del_relationship('Lifeng', 'Keru', my_group)
#print(my_group['Lifeng'].relationship)
#print(my_group)
#add_person('wula', 1, 'job', {'':''}, my_group)
#print(my_group)
#a = average_age(my_group)
#print(a)

print('the maximum age of people in the group is', max(person.age for person in my_group.values()))
print('the average (mean) number of relations among members of the group is', sum(len(person.relationship) for person in my_group.values())/len(my_group))
print('the maximum age of people in the group that have at least one relation is', max(person.age for person in my_group.values() if person.relationship))
print('the maximum age of people in the group that have at least one friend is', max(person.age for person in my_group.values() if 'friend' in person.relationship.values()))
