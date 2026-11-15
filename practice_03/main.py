#Вариант 21
g = (x for x in [1, 2, 3, 4, 5, 6] if x > 1)
print(list(g))


def announce(func):
    def wrapper():
        print("Начинаем")
        result = func()
        print("Готово")
        return result
    return wrapper

@announce
def hello():
    print("Привет!")

hello()
