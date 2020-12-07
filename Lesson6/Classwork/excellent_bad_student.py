'''Variant 1'''
# students = {'Petrov Petr':[7, 9, 8], 'Yaroslavich Yaroslav':[2, 5, 9], 'Ivanov Ivan':[7, 9, 8], 'Sidorov Petr':[2, 5, 9], 'Alexandov Alex':[6, 7, 9]}
#
# print(min(students, key=lambda x: sum(students.get(x))/len(students.get(x))))
# print(max(students, key=lambda x: sum(students.get(x))/len(students.get(x))))

'''Variant 2'''
students = {'Petrov Petr':[7, 9, 8], 'Yaroslavich Yaroslav':[2, 5, 9], 'Ivanov Ivan':[7, 9, 8], 'Sidorov Petr':[2, 5, 9], 'Alexandov Alex':[6, 7, 9]}

mean_student = {}
for key, value in students.items():
    res = (sum(value)) / len(value)
    if res not in mean_student:
        mean_student[res] = [key]
    else:
        mean_student[res] += [key]
print('Bad student', ', '.join(mean_student[min(mean_student)]), 'with score', min(mean_student))
print('Excellent student', ', '.join(mean_student[max(mean_student)]), 'with score', max(mean_student))