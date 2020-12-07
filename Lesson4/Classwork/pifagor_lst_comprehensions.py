# line = list(range(1, 10))
# stolbic = list(range(1, 10))
# ans = []
# a = []
# i = 0
# for i in line:
#     for j in stolbic:
#         a.append(i * j)
#     ans.append(a)
#     a = []
# print(ans)


result_list = [[i*j for i in range(1, 10)] for j in range(1, 10)]
print(result_list)