# https://docs.python.org/zh-cn/3.14/

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


for x in range(2, 5):
    if 5 % x == 0:
        print(5, 'equals', x, '*', 5//x)
        break
else:
    # 循环到底未找到一个因数
    print(5, 'is a prime number')


def http_error(status):
    match status:
        case 400 | 401 | 402:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(http_error(402))


# 定义一个表示坐标点的元组（示例）
point = (3, 0)

# 对 point 元组进行结构化模式匹配
match point:
    # 匹配 (0, 0) 这个具体的坐标点（原点）
    case (0, 0):
        print("Origin")
    # 匹配 x=0、y 为任意值的点（Y 轴上的点），y 会捕获对应的值
    case (0, y):
        print(f"Y={y}")
    # 匹配 y=0、x 为任意值的点（X 轴上的点），x 会捕获对应的值
    case (x, 0):
        print(f"X={x}")
    # 匹配任意 (x, y) 元组（非坐标轴上的普通点），x、y 捕获对应值
    case (x, y):
        print(f"X={x}, Y={y}")
    # 通配符，匹配所有非元组的情况（防御性处理）
    case _:
        raise ValueError("Not a point")

from enum import Enum
class Color(Enum):
    """An enumeration."""
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

def fib(n):    # 打印小于 n 的斐波那契数列
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# 现在调用我们刚定义的函数：
fib(2000)


# 列表
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # 从 4 号位开始查找下一个 banana

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()

# del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

# 元组
t = 12345, 54321, 'hello!'
print(t[0])

print(t)

# 元组可以嵌套：
u = t, (1, 2, 3, 4, 5)
print(u)

# 元组是不可变对象：
# t[0] = 88888
# 但它们可以包含可变对象：
v = ([1, 2, 3], [3, 2, 1])
print(v)

# 集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 显示重复项已被移除

'orange' in basket                 # 快速成员检测

'crabgrass' in basket


# 演示针对两个单词中独有的字母进行集合运算

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # a 中独有的字母

print(a - b)                              # 存在于 a 中但不存在于 b 中的字母

print(a | b)                              # 存在于 a 或 b 中或两者中皆有的字母

print(a & b)                              # 同时存在于 a 和 b 中的字母

print(a ^ b)                              # 存在于 a 或 b 中但非两者中皆有的字母

# 字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

print(tel.get('irv'))

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

print('guido' in tel)

print('jack' not in tel)


year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))