def complite(name, salary):
    i = 0
    file = open('salary.txt', 'w', encoding='utf-8')
    while i < len(salary):
        name[i] = name[i].capitalize()
        file.write(f'{name[i]} - {salary[i]}\n')
        i += 1
    file.close()

def showme():
    file = open('salary.txt', 'r', encoding='utf-8')
    i = 0
    massnum = []
    massname = []
    while i < len(salary):
        line = file.readline()
        line = line.replace("\n", "")
        line = line.split(' - ')
        massnum.append(line[1])
        massname.append(line[0])
        i += 1
    i = 0
    while i < len(massnum):
        massnum[i] = int(massnum[i])
        massnum[i] = massnum[i] * 0.87
        massname[i] = str(massname[i])
        massname[i] = massname[i].upper()
        i += 1
    file.close()
    return massnum, massname

def print_salary(massnum, massname):
    i = 0
    file = open('newsalary.txt', 'w', encoding='utf-8')
    while i < len(massnum):
        massnum[i] = int(massnum[i])
        if massnum[i] < 500000:
            print(f'{massname[i]} - {massnum[i]}')
            file.write(f'{massname[i]} - {massnum[i]}\n')
        else:
            pass
        i += 1
    file.close()

name = ["ВасиЛИЙ", "Николя", "анастасия", "аЛеНа", "Mary", "Mechaello"]
salary = [20000, 60000, 700000, 45000, 12000, 899000]
name_and_salary = dict(zip(name, salary)) # понятия не имею, зачем этот словарь нужен

complite(name, salary)
massnum, massname = showme()
print_salary(massnum, massname)
