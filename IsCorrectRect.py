#Функция isCorrectRect 
def isCorrectRec(rectangles):
    #Перебор элементов rectangles с возвратом rect и index
    for index, rect in enumerate(rectangles, start = 1):
        #Проверяем корректность прямоугольника
        if rect[0][0] >= rect[1][0] or rect[0][1] >= rect[1][1]:
            raise ValueError(f'Некорректный прямоугольник с номером {index}')
    #Если все прямоугольники корректны, функция возвращает True
    return True
