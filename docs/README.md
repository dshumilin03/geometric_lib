
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## Function description

### Areas

#### Circle
```python
def area(r):
    """Принимает радиус, возвращает площадь окружности"""
    return math.pi * r * r
```
Example:
```python
x = area(5)
x = 78.53982
```

#### Triangle
```python
def area(a, b, c):
    """Принимает 3 стороны, возвращает площадь треугольника"""
    return (a + b + c) / 2
```
Example:
```python
x = area(5, 4, 3)
x = 12
```
#### Square
```python
def area(a):
"""Принимает сторону, возвращает площадь квадрата"""
    return a * a
```
Example:
```python
x = area(4)
x = 16
```

### Perimeters

#### Circle
```python
def perimeter(r):
    """Принимает радиус, возвращает длину окружности"""
    return 2 * math.pi * r
```
Example:
```python
x = perimeter(5)
x = 31.4159
```
#### Triangle
```python
def perimeter(a, b, c):
    """Принимает 3 стороны, возвращает периметр треугольника"""
    return a + b + c
```
Example:
```python
x = perimeter(5, 10, 4)
x = 19
```
#### Square

```python
def perimeter(a):
    """Принимает сторону возвращает периметр квадрата"""
    return 4 * a
```
Example:
```python
x = perimeter(15)
x = 60
```

