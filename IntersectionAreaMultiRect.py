from .IsCorrectRect import isCorrectRec 
from itertools import combinations  

def intersectionAreaMultiRec(rectangles):
    #функция нахождения пересечений прямоугольников
    def get_intersection(rects):
        
        #координаты левого нижнего угла (макс)
        x1 = max(rect[0][0] for rect in rects)
        y1 = max(rect[0][1] for rect in rects)
        
        #Правого верхнего(макс)
        x2 = min(rect[1][0] for rect in rects)
        y2 = min(rect[1][1] for rect in rects)
        
        #проверка существования пересечения
        if x1 < x2 and y1 < y2:
            #Возвращаем координаты пересечения
            return [(x1, y1), (x2, y2)]  
        return None  
    
    #площадь прямоугольника, если не существует площадь = 0
    def area(rect):
        if not rect:
            return 0 
        
        #Разность x координат по ширине
        width = rect[1][0] - rect[0][0]  
        #Разность y координат по высоте
        height = rect[1][1] - rect[0][1]  
        #площадь
        return width * height  

    #Хранилище общей площади пересечений
    total_area = 0  
    #Список хранения всех существующих пересечений
    all_intersections = []  
    
    #перебор комбинациий пар прямоугольников
    for combination in combinations(rectangles, 2):
        #Пересечения пары + проверка
        intersection = get_intersection(combination)  
        if intersection:  
            #Добавляем его в список
            all_intersections.append(intersection)  

    #Нахождение общей площади
    for k in range(1, len(all_intersections) + 1):
        #Определение знака
        sign = (-1) ** (k + 1)  
        for combination in combinations(all_intersections, k):
            intersection = get_intersection(combination)  #Пересечение текущей комбинации
            # + или - от общего
            total_area += sign * area(intersection)  

    #Общая площадь
    return total_area 
