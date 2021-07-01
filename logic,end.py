dict1 = {(0, 0): 'siri', (0, 1): 21, (0, 2): 'Data structures',
         (1, 0): 'chinni', (1, 1): 20, (1, 2): 'Machine Learning',
         (2, 0): 'honey', (2, 1):21, (2, 2): 'OOPS with Java'}
for i in range(3):
    for j in range(3):
        a=dict1[i,j]
        print(a,end=" ")
    print()