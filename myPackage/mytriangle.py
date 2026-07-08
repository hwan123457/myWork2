import turtle

def draw_square(t, x, y, size=100):
    """
    (x, y) 위치를 시작점으로 정삼각형을 그립니다.

    t    : turtle.Turtle 객체
    x, y : 그림을 그릴 좌표
    size : 정사각형 한 변의 길이
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)

    for _ in range(3):
        t.forward(size)
        t.left(120)