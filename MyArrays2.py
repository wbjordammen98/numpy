import numpy as np
"""
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())
print(grades.mean(axis=0))
print(grades.mean(axis=1))

numbers = np.array([1,4,5,9,16,25,36])

print(np.sqrt(numbers))

print(grades[0,1])
print(grades[1])
print(grades[0:2])

print()
print()


print(grades[1,2])
print(grades[[1,3]])
print(grades[1,:])


print(grades)
print(grades[:,1:3])


numbers = np.arange(1,6)
number2 = numbers.view()

print(number2)

numbers[1] *= 20

print(number2)

number2[1] /= 10

numbers2 = numbers[0:3]

print(numbers2)
"""

grades = np.array([[87,96,70],[100,87,90]])
grades2 = np.array([[94,77,90],[100,81,82]])
h_grades = np.hstack((grades,grades2))

print(h_grades)

v_grades = np.vstack((grades,grades2))

print(v_grades)
#print(grades.reshape(1,6))
#print(grades)

raveled = grades.ravel()
#print(raveled)

raveled[5] = 99
#print(grades)


    
