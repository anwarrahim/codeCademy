# do the task

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:
# task 1
subjects = ["physics", "calculus", "poetry", "history"]
# task 2
grades = [98, 97, 85, 88]

# task 3
gradebook = [["physices", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# task 4
print(gradebook)

# add More subjects
# task 5

gradebook.append(["computer science", 100])
print(gradebook)

# task 6
gradebook.append(["visual arts", 93])
print(gradebook)
# Modify the gradebook

# task 7
gradebook[5][1] += 5
print(gradebook)

# task 8
gradebook[2].remove(85)
print(gradebook)

# task 9
gradebook[2].append("Pass")
print(gradebook)

# create new variable  to combine the two variables
# task 10
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
