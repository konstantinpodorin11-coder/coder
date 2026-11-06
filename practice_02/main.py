#Вариант 21
def tasks_per_student(tasks, students):
    if students == 0:
        return "На ноль делить нельзя"
    return tasks / students

assert tasks_per_student(100, 25) == 4.0
assert tasks_per_student(100, 0) == "На ноль делить нельзя"
assert tasks_per_student(60, 10) == 6.0

print(sorted(["акт", "задача", "упражнение"], key=lambda word: len(word)))
