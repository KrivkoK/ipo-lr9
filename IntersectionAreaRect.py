from .IsCorrectRect import isCorrectRec 

def intersectionAreaRect(rectangles):
    #Общая площадь пересечения(хранилище)
    total_area = 0  
    
    #Проверка корректности входных данных
    try:
        #Проверка корректности прямоугольников
        isCorrectRec(rectangles)  
    except ValueError as error:
        raise ValueError("Некорректный прямоугольник: " + str(error))  

    #Получаем количество прямоугольников
    count = len(rectangles)  
    #Проверка наличия пересечений
    has_intersection = False  

    #Перебор пар прямоугольников
    for i in range(count):
        for j in range(i + 1, count):
            #Координаты первого 
            x1, y1 = rectangles[i][0]  #Левый нижний угол
            x2, y2 = rectangles[i][1]  #Правый верхний угол

            #Координаты второго
            x3, y3 = rectangles[j][0]  #Левый нижний угол
            x4, y4 = rectangles[j][1]  #Правый верхний угол

            #Границы пересечения
            overlap_left = max(x1, x3)  #Левая граница пересечения
            overlap_top = min(y2, y4)    #Верхняя граница пересечения
            overlap_right = min(x2, x4)  #Правая граница пересечения
            overlap_bottom = max(y1, y3)  #Нижняя граница пересечения

            #Ширины и высота пересечения
            overlap_width = overlap_right - overlap_left
            overlap_height = overlap_top - overlap_bottom

            #Проверка наличия пересечения
            if overlap_width > 0 and overlap_height > 0:
                #Добавляем площадь пересечения к общей площади
                total_area += overlap_width * overlap_height  
                has_intersection = True  

    if not has_intersection:
        #При отсутствии пересечений return 0
        return 0  

    #Возвращаем общую площадь пересечений
    return total_area  
