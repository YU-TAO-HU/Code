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