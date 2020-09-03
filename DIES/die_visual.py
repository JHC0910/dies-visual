import pygal

from die import Die


print("Welcome to Two-Dices Simulator!!")

while True:
    print("\nHow many sides do you want?")

    t1 = input()
    t1 = int(t1)
    t2 = input()
    t2 = int(t2)

    if (t1 <=0) or (t2 <=0):
        print("Error!!")
        print("Input again.")
    
        continue
    elif (t1 > 0) and (t2 > 0):  
        while True:
            print("\nHow many times you want??")
            t = input()
            t = int(t)
            if t <= 0:
                print("Error!!")
                print("Input again.")
                continue
            elif t > 0:
                break
        break

die1 = Die(t1)
die2 = Die(t2)

results = []
for times in range(t):
    result = die1.roll() + die2.roll()
    results.append(result)


occupations = []
max_result = die1.num_sides + die2.num_sides

for value in range(2, max_result+1):
    occupation = results.count(value)
    occupations.append(occupation)

labels = []
for i in range(2, max_result+1):
    x = str(i)
    labels.append(x)


hist = pygal.Bar()

hist.title = "Results of rolling two dices" + str(t) + "times"
hist.x_labels = labels
hist.x_title = "Results"
hist.y_title = "Occupations of results"
hist.add("D" + str(t1) + "D" + str(t2), occupations)
hist.render_to_file("die_visual.svg")

