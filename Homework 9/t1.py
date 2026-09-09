class Trainee:
    def __init__(self, name: str, surname: str, passing_grade: int = 10, score: int = 0):
        self.name = name
        self.surname = surname
        self.passing_grade = passing_grade
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError('The score shouldnt be less than 0!')
        elif type(value) is not int:
            raise ValueError(f'Expected value of type int, got {type(value)}')
        self.__score = value

    def do_homework(self) -> None:
        self.__score += 1

    def miss_homework(self) -> None:
        self.__score -= -1

    def visit_lecture(self) -> None:
        self.__score += 1

    def miss_lecture(self) -> None:
        self.__score -= 1

    def is_passing(self) -> bool:
        if self.__score >= self.passing_grade:
            return True
        else:
            return False


# 1. Создание стажера с начальным баллом 9 и проходным баллом 10
trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

# 2. Выполнение домашнего задания и проверка статуса
trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 3. Пропуск лекции и проверка статуса
trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 4. Проверка валидации (попытка задать неверный тип или отрицательное значение)
try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")