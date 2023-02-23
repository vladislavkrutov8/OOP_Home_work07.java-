import zoo


def menu():
    print("\n1. Добавить животное \n"
          "2. Удалить животное \n"
          "3. Просмотреть информацию о конкретном животном\n"
          "4. Заставить конкретное животное издать звук\n"
          "5. Просмотреть информацию о всех животных \n"
          "6. Заставить все животные в зоопарке издать звук\n"
          "7. Выйти")
    num = int(input("Выберите пункт меню: "))
    return num


def addAnimalMenu():
    print("\n1. Добавить кота\n"
          "2. Добавить тигра\n"
          "3. Добавить собаку\n"
          "4. Добавить волка\n"
          "5. Добавить курицу\n"
          "6. Добавить аиста\n"
          "7. Выйти")
    num = int(input("Выберите пункт меню: "))
    return num


def deleteAnimalMenu():
    print(f"{len(zoo.Zoo.all)+1} Назад")
    num = int(input("Выберите кого хотите удалить: "))
    return num


def showAnimalMenu():
    print(f"{len(zoo.Zoo.all)+1} Назад")
    num = int(input("Выберите кого хотите посмотреть: "))
    return num


def sayAnimalMenu():
    print(f"{len(zoo.Zoo.all)+1} Назад")
    num = int(input("Выберите кого хотите посмотреть: "))
    return num
