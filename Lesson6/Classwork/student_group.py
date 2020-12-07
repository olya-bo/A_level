'''Vvod studentov'''
# student_group = {}
# for _ in range(int(input('how many students are there in the group? '))):
#     student = input('Put name student ')
#     course = input('what courses does the student go to? ').split()
#     student_group[student] = course


student_group = {'Kolya':['Python'],
                 'Petr':['Java', 'FullStack'],
                 'Sonya':['Python'],
                 'Alisa':['FrontEnd'],
                 'Kiril':['Java', 'FrontEnd'],
                 'Tolik':['FrontEnd', 'Python'],
                 'Vasya':['Python', 'FrontEnd', 'FullStack', 'Java'],
                 'Olya': []}

more_than_one = []
not_frontend = []
java_or_python = []
# python_students = []
# java_students = []


for key, value in student_group.items():
    if len(value) > 1:
        more_than_one.append(key)
    if 'FrontEnd' not in value:
        not_frontend.append(key)
    if 'Python' in value or 'Java' in value:
        java_or_python.append(key)
    # if 'Python' in value:
    #     python_students.append(key)
    # if 'Java' in value:
    #     java_students.append(key)

print('2 or more course:', ', '.join(more_than_one))
print('Not FrontEnd:', ', '.join(not_frontend))
print('Java or Python student:', ', '.join(java_or_python))
# print('Python student:', ', '.join(python_students))
# print('Java student:', ', '.join(java_students))

