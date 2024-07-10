grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
johny_key = sum(grades[0])/len(grades[0])
bilbo_key = sum(grades[1])/len(grades[1])
steve_key = sum(grades[2])/len(grades[2])
khendrik_key = sum(grades[3])/len(grades[3])
aaron_key = sum(grades[4])/len(grades[4])
average = {'Johnny:' : johny_key, 'Bilbo:' : bilbo_key, 'Steve:': steve_key, 'Khendrik:':khendrik_key, 'Aaron:': aaron_key}
print(average)


