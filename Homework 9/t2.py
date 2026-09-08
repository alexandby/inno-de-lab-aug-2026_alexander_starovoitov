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
            raise ValueError('The score shouldn t be less than 0!')
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


class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        self.score += 2


class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        return self.score > 0


class Cohort:
    def __init__(self, title: str):
        self.title = title
        self.trainees : list[Trainee] = []

    def add_trainee(self, trainee: Trainee) -> None:
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        return [trainee for trainee in self.trainees if trainee.is_passing()]




# 1. Создаем учащихся разных типов
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

# 2. Создаем группу и добавляем студентов
cohort = Cohort("Python Advanced")
cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)

# 3. Проводим лекцию для всей группы (+1 балл всем)
cohort.conduct_lecture()

# 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла)
hard_trainee.do_homework()

# 5. Выводим список тех, кто проходит курс
passing_students = cohort.get_passing_students()

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
for student in cohort.trainees:
    print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}")

print("\nУспешно зачислены на следующий модуль:")
for student in passing_students:
    print(f"- {student.name} {student.surname}")