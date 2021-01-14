with open('Inputs/c_many_ingredients.in','r') as file:
    lines = file.readlines()
    numPizzas, num2teams, num3teams, num4teams = map(int,lines[0].split())
    pizzas = []
    for line in lines[1:]:
        line = line.split()
        line[0]=int(line[0])
        pizzas.append(line)


