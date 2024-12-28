from .IsCorrectRect import isCorrectRec

class RectCorrectError(Exception):
    pass

#Функция для проверки пересечения прямоугольников
def isCollisionRec(rectangles):
    try:
        #Вызов функции isCorrectRect
        isCorrectRec(rectangles)
    except ValueError as error:
        raise RectCorrectError("1-ый прямоугольник некорректный") from error


    count = len(rectangles)

    for i in range(count):
        for j in range(i + 1, count):
            
            #Координаты первого прямоугольника
            x_left1, y_bottom1 = rectangles[i][0]  #Координаты левого нижнего угла
            x_right1, y_top1 = rectangles[i][1]  #Координаты правого верхнего угла

            #Координаты второго прямоугольника
            x_left2, y_bottom2 = rectangles[j][0]  #Координаты левого нижнего угла
            x_right2, y_top2 = rectangles[j][1]  #Координаты правого верхнего угла

            #Границы возможного пересечения
            intersection_left = max(x_left1, x_left2)
            intersection_top = min(y_top1, y_top2)
            intersection_right = min(x_right1, x_right2)
            intersection_bottom = max(y_bottom1, y_bottom2)

            #Ширина и высота пересечения
            intersection_width = intersection_right - intersection_left
            intersection_height = intersection_top - intersection_bottom

            #Если ширина и высота +, то прямоугольники пересекаются
            if intersection_width > 0 and intersection_height > 0:
                return True  

  
    return False
