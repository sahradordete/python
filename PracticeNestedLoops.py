#Create a nested For Loop with the outer loop having 3 items and the inner loop having 5 items.
outer = ['section1', 'section2', 'section3']
inner = [1, 2, 3, 4, 5]

#Print to the screen in groups so the outer loop is grouped with the 5 inner loop items.
for o in outer:
    print(o)
    for i in inner:
        print(i)
    print("\n")
