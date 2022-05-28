
# take function as an object
import collections
from functools import reduce


def foo():
    print("foo")


bar = foo
bar()

# take an object as a function


class Greeter:
    def __init__(self, greeting) -> None:
        self.greeting = greeting

    def __call__(self, name) -> str:
        return self.greeting + " " + name


morning = Greeter("good morning")  # create the callable object
print(morning("John"))  # calling the object
# print "good morning John" to the console

# 我们可以调用 morning 对象的原因在于，我们已经在类定义中使用了 __call__ 方法。
# 为了检查对象是否可调用，我们使用内置函数 callable

callable(morning)  # true
callable(145)  # false. int is not callable

# function in dict

mapping = {
    0: foo,
    1: bar
}

mapping[0]()  # call the func returned by dictionary access


# take function as parameter and returned value
# 函数还可以作为其他函数的参数和返回值。
# 接受函数作为输入或返回函数的函数叫做高阶函数，它是函数式编程的重要组成部分

### "高阶函数允许我们对动作执行抽象，而不只是抽象数值" ###

def iterate(list_of_items):
    for item in list_of_items:
        print(item)


def iterate_custom(list_of_items, custom_func):
    for item in list_of_items:
        custom_func(item)


def add(x, y):
    return x + y


def sub(x, y):
    return x-y


def mult(x, y):
    return x * y


def calculator(opcode):
    if opcode == 1:
        return add
    elif opcode == 2:
        return sub
    else:
        return mult


my_calc = calculator(2)  # my_calc is a subtractor
my_calc(5, 4)  # return 5-4 = 1

my_calc = calculator(9)  # my_calc is a multiplier

my_calc(5, 4)  # 5 * 4 = 20

# nested function
# 函数还可以在其他函数内部，这就是「内部函数」。
# 内部函数在创建辅助函数时非常有用，辅助函数即作为子模块来支持主函数的小型可重用函数。


def fib(n):
    def fib_helper(fk1, fk, k):
        if n == k:
            return fk
        else:
            return fib_helper(fk, fk1+fk, k+1)
    if n <= 1:
        return n
    else:
        return fib_helper(0, 1, 1)

# 将该计算从函数主体移到函数参数，这具备非常强大的力量。因为它减少了递归方法中可能出现的冗余计算

# 单表达式函数（Lambda 表达式）


def mult(x, y): return x * y


mult(1, 2)  # return 2

# lambda 函数更加强大和精准，因为我们还可以构建匿名函数（即没有名称的函数）
(lambda x, y: x * y)(9, 10)  # return 90

pre_fill = collections.defaultdict(lambda: (0, 0))

# all dictionary keys and values are set to 0


# Map、Filter 和 Reduce

scores = [3, 4, 5]
modified_scores = list(map(lambda x: 4 * x, scores))

even_scores = list(filter(lambda x: True if (x % 2 == 0) else False, scores))

sum_scores = reduce(lambda x, y: x + y, scores)
