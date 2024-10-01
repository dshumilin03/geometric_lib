# Project calculates area and perimeter for several shapes
## Available shapes
- rectangle
- circle
- square

## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Function description

### Areas

#### Circle
```
def area(r):
    ```Принимает радиус, возвращает площадь круга```
    return math.pi * r * r
```
Example:
```
x = area(5)
x = 78.53982
```

#### Rectangle
```
def area(a, b):
    ```Получаем длину и ширину, возвращаем площадь прямоугольника```
    return a * b
```
Example:
```
x = area(5, 4)
x = 20
```
#### Square
```
def area(a):
    ```Получаем длину стороны, возвращаем площадь квадрата```
    return a * a
```
Example:
```
x = area(4)
x = 16
```

### Perimeters

#### Circle
```
def perimeter(r):
        ```Принимает радиус, возвращает периметр круга```
    return 2 * math.pi * r
```
Example:
```
x = perimeter(5)
x = 31.
```
#### Rectangle

```def perimeter(a, b):
    ```получаем длину и ширину, возвращаем периметр прямоугольника```
    return (a + b)
```
Example:
```
x = perimeter(5, 10)
x = 15
```
#### Square

```
def perimeter(a):
    ```Получаем длину стороны, возвращаем периметр квадрата```
    return 4 * a
```
Example:
```
x = perimeter(15)
x = 60
```
## Changes
```6aa991a6a15ce1db592f0767e7e15c45560e66b0 added commentaries for circle.py functions```

```a1509037672a51c8e737aa17356d1b4b5fbfa398 added commentaries for rectangle.py functions```

```70eb7a36c987e4606098943fbb8119e70661498c added commentaries for square.py functions```
