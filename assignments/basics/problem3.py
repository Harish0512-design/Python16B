# 3. Write a function to calculate area and circumference of a circle.


def calc_area_circumference(radius):
    area = round(3.14 * radius * radius, 2)
    circumference = 2 * 3.14 * radius
    return f"Area of circle: {area}\nCircumference of circle: {circumference} "


res = calc_area_circumference(3)
print(res)
