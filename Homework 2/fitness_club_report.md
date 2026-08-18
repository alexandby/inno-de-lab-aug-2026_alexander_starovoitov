## Часть 1: Выбор Сценария
Для выполнения работы выбран сценарий: **Управление фитнес-клубом** (Вариант 7).

### Цели и задачи системы
* **Автоматизация учета** клиентов и тренерского состава.
* **Организация расписания** групповых занятий клуба.
* **Контроль записи** клиентов на тренировки.
* **Исключение конфликтов** в расписании и переполнения залов.

## Часть 2: Проектирование Базы Данных и Документация

### Идентификация Сущностей и Атрибутов
1. **Trainers (Тренеры)** — Данные об инструкторах, ведущих занятия.
2. **Clients (Клиенты)** — Информация о посетителях клуба.
3. **Classes (Групповые занятия)** — Программа и расписание тренировок.
4. **Enrollments (Запись на тренировки)** — Связующая таблица для реализации связи «многие-ко-многим».

### Спецификация Таблиц (3NF)

#### 1. Таблица: `Trainers`
* **Описание**: Хранит информацию о тренерском составе клуба.
* **Атрибуты**:
  * `TrainerID`: `SERIAL` (PK, NOT NULL) — Уникальный идентификатор тренера.
  * `FirstName`: `VARCHAR(100)` (NOT NULL) — Имя.
  * `LastName`: `VARCHAR(100)` (NOT NULL) — Фамилия.
  * `Specialization`: `VARCHAR(150)` — Направление (например, "Йога", "Кроссфит").
  * `Phone`: `VARCHAR(20)` (UNIQUE, NOT NULL) — Контактный телефон.
* **Ограничения**:
  * `PK_Trainers`: `PRIMARY KEY (TrainerID)`
  * `UQ_Trainer_Phone`: `UNIQUE (Phone)`

#### 2. Таблица: `Clients`
* **Описание**: Содержит персональные данные клиентов фитнес-клуба.
* **Атрибуты**:
  * `ClientID`: `SERIAL` (PK, NOT NULL) — Уникальный номер клиента.
  * `FirstName`: `VARCHAR(100)` (NOT NULL) — Имя.
  * `LastName`: `VARCHAR(100)` (NOT NULL) — Фамилия.
  * `Email`: `VARCHAR(255)` (UNIQUE, NOT NULL) — Электронная почта.
  * `RegistrationDate`: `DATE` (NOT NULL, DEFAULT `CURRENT_DATE`) — Дата регистрации.
* **Ограничения**:
  * `PK_Clients`: `PRIMARY KEY (ClientID)`
  * `UQ_Client_Email`: `UNIQUE (Email)`

#### 3. Таблица: `Classes`
* **Описание**: Описывает проводимые групповые занятия и их расписание.
* **Атрибуты**:
  * `ClassID`: `SERIAL` (PK, NOT NULL) — Идентификатор занятия.
  * `ClassName`: `VARCHAR(150)` (NOT NULL) — Название тренировки.
  * `TrainerID`: `INTEGER` (FK, NOT NULL) — Уникальный ID тренера.
  * `ScheduleTime`: `TIMESTAMP` (NOT NULL) — Дата и время проведения.
  * `MaxCapacity`: `INTEGER` (NOT NULL) — Максимальное количество мест.
* **Ограничения**:
  * `PK_Classes`: `PRIMARY KEY (ClassID)`
  * `FK_Classes_Trainers`: `FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE RESTRICT`
  * `CHK_MaxCapacity`: `CHECK (MaxCapacity > 0 AND MaxCapacity <= 50)`

#### 4. Таблица: `Enrollments`
* **Описание**: Фиксирует запись клиентов на конкретные групповые занятия (Связь Многие-ко-Многим).
* **Атрибуты**:
  * `EnrollmentID`: `SERIAL` (PK, NOT NULL) — Идентификатор записи.
  * `ClientID`: `INTEGER` (FK, NOT NULL) — Уникальный ID клиента.
  * `ClassID`: `INTEGER` (FK, NOT NULL) — Уникальный ID занятия.
  * `EnrollmentDate`: `TIMESTAMP` (NOT NULL, DEFAULT `CURRENT_TIMESTAMP`) — Дата записи.
* **Ограничения**:
  * `PK_Enrollments`: `PRIMARY KEY (EnrollmentID)`
  * `FK_Enrollments_Clients`: `FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE`
  * `FK_Enrollments_Classes`: `FOREIGN KEY (ClassID) REFERENCES Classes(ClassID) ON DELETE CASCADE`
  * `UQ_Client_Class`: `UNIQUE (ClientID, ClassID)`

### Мощность и описание связей
* **Trainers и Classes (Один-ко-Многим)**: Один тренер может вести несколько занятий. Одно занятие ведет один тренер. Связь через `Classes.TrainerID`.
* **Clients и Classes (Многие-ко-Многим)**: Один клиент посещает много занятий. На одном занятии присутствует много клиентов. Реализовано через промежуточную таблицу `Enrollments`.
