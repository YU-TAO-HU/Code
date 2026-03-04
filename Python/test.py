test = "Hello World "
print(test)

print(test + test)

# 创建示例多项集
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# 策略：迭代一个副本
for user, status in users.copy().items():
    print(f"User: {user}, Status: {status}")
    if status == 'inactive':
        del users[user]

# 策略：创建一个新多项集
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])


for x in range(2, 10):
    pass
    print(x)
    # if 3 % x == 0:
    #     print(3, 'equals', x, '*', 3//x)
    #     break
else:
    # 循环到底未找到一个因数
    print(3, 'is a prime number')
