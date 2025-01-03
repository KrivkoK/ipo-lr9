from collision.IsCorrectRect import isCorrectRec
from collision.IsCollisionRect import isCollisionRec
from collision.IntersectionAreaRect import intersectionAreaRec
from collision.IntersectionAreaMultiRect import intersectionAreaMultiRec

def main():
    #Запускаем бесконечный цикл для взаимодействия с пользователем
    while True:
        #Запрашиваем у пользователя выбор операции
        number = int(input("Выбор: 1 - intersectionAreaRect , 2 - isCorrectRect , 3 - isCollisionRect , 4 - intersectionAreaMultiRect , 5 - Выход: "))

        #Опция 1: Вычисление площади пересечения двух прямоугольников
        if number == 1:
            print("Введите координаты двух прямоугольников:")
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            
            #Создаем список из двух прямоугольников, используя введенные координаты
            rectangles = [((x1, y1), (x2, y2)), ((x3, y3), (x4, y4))]
            
            #Вычисляем площадь пересечения прямоугольников
            area = intersectionAreaRec(rectangles)
            print(f"Площадь пересечения: {area}")

        #Опция 2: Проверка корректности прямоугольника
        elif number == 2:
            rectangles = []
            print("Введите координаты прямоугольника:")
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            #Добавляем введенные координаты в список
            rectangles.append([(x1, y1), (x2, y2)])
            try:
                #Проверяем корректность прямоугольника
                if isCorrectRec(rectangles):
                    print("Прямоугольник корректен.")
                else:
                    print("Прямоугольник некорректен.")
            except ValueError as e:
                #Обрабатываем ошибку, если прямоугольник некорректен
                print(f"Ошибка: {e}")

        #Опция 3: Проверка столкновения двух прямоугольников
        elif number == 3:
            print("Введите координаты двух прямоугольников:")
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            
            #Создаем список из двух прямоугольников
            rectangles = [((x1, y1), (x2, y2)), ((x3, y3), (x4, y4))]
            #Проверяем, пересекаются ли два прямоугольника
            collision = isCollisionRec(rectangles)
            if collision:
                print("Прямоугольники пересекаются.")
            else:
                print("Прямоугольники не пересекаются.")

        #Опция 4: Вычисление площади пересечения множества прямоугольников
        elif number == 4:
            n = int(input("Количество прямоугольников: "))
            rectangles = []
            for i in range(n):
                print(f"Прямоугольник {i + 1}:")
                x1 = float(input('Введите x1: '))
                y1 = float(input('Введите y1: '))
                x2 = float(input('Введите x2: '))
                y2 = float(input('Введите y2: '))
                # Добавляем каждый введенный прямоугольник в список
                rectangles.append([(x1, y1), (x2, y2)])
            
            try:
                #Вычисляем площадь пересечения всех введенных прямоугольников
                area_multi = intersectionAreaMultiRec(rectangles)
                print(f"Площадь пересечения всех прямоугольников: {area_multi}")
            except ValueError as e:
                #Обрабатываем ошибку, если что-то пошло не так
                print(f"Ошибка: {e}")

        #Опция 5: Выход из программы
        elif number == 5:
            print("Выход")
            break
        
        #Обработка некорректного ввода
        else:
           print(f"Вы ввели {number}. Чтобы продолжить, введите число от 1 до 5.")

#Запускаем главную функцию
main()
