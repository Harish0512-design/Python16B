# 2.Write a function to calculate area and perimeter of a rectangle.

def calculate_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return f'Area : {area}\nPerimeter : {perimeter}'


res = calculate_area_perimeter(40, 20)

print(res)
