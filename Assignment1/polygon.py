import math
def polygon_perimeter(points):
    perimeter = 0
    n = len(points) 
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # wrap to the first point at the end
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimeter += distance
    
    return perimeter
n = int(input("Enter number of vertices: "))
points = []
print("Enter the coordinates (x y) one by one:")
for i in range(n):
    x, y = map(float, input(f"Vertex {i+1}: ").split())
    points.append((x, y))
print("Perimeter of the polygon:", polygon_perimeter(points))
