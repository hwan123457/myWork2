import turtle

from mytriangle import draw_triangle
from mycircle import draw_circle
from mysquare import draw_square

# ---------- 화면 설정 ----------
screen = turtle.Screen()
screen.title("클릭한 위치에 도형 그리기")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)

last_pos = {"x": 0, "y": 0}


def on_click(x, y):
    last_pos["x"] = x
    last_pos["y"] = y

def on_right_click(x, y):
    t.clear()

def on_key_square():
    draw_square(t, last_pos["x"], last_pos["y"])

def on_key_triangle():
    draw_triangle(t, last_pos["x"], last_pos["y"])

def on_key_circle():
    draw_circle(t, last_pos["x"], last_pos["y"])


screen.onclick(on_click, btn=1)        # 왼쪽 클릭 -> 위치 저장
screen.onclick(on_right_click, btn=3)  # 오른쪽 클릭 -> 화면 지우기

screen.onkey(on_key_square, "a")
screen.onkey(on_key_triangle, "b")
screen.onkey(on_key_circle, "c")
screen.listen()  # 키보드 입력을 받으려면 반드시 필요


screen.mainloop()