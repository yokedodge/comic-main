print("Добро пожаловать в опросник!")

student = input("Ученик ли вы? (Да/Нет) ")
if student.upper() == "ДА":
    print("Вы ученик.")
    grade = input("В каком вы классе? ")
    school = input("Из какой вы школы? ")
    print(f"Вы учитесь в {grade} классе школы {school}.")
else:
    print("Вы не ученик.")

predmet = input("Вы будите сдавать экзамены?(Да/Нет)")
if predmet.upper()=="ДА":
    ege=input("Какие прдеметы?")
    print("Поздравляю вы сдаёте",ege,"!")
else:
    print("Вы ничего не сдаёте!")

institution_rating = int(input("Оцените учебное заведение от 1 до 5: "))
if institution_rating<=5:
    print("Спасибо за вашу оценку учебного заведения!")
else:
    print("Вы ввели некректное число!")

print("Спасибо за участие в опросе!")