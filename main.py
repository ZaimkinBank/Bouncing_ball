import random
import turtle
import time

window = turtle.Screen()
border = turtle.Turtle()
# отрисовка границ
border.up()
border.speed(0)
border.hideturtle()
border.pensize(10)
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)
border.pensize(1)
border.color('red')
border.goto(300, 115)
border.goto(-300, 115)
#

ball = turtle.Turtle()
ball.shape('circle')
ball.up()
ball.goto(0,115) # следовательно высота 400 пикселей
ball.speedY = 0 # начальная вертикальная скороть
grav = 0.251 # ускорение свободного падения
k = 0.64 # теряем 36% энергии
flag = True
ball.speedX = random.randint(-15, 15)
while flag:
    now = time.time()
    ball.speedY = ball.speedY - grav # уравнение v(t)
    ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY) # каждая итерация должна перемещать мячик в указанную координату
    if ball.ycor() + ball.speedY <= -285: # изменяем импульс в момент касания земли
        ball.speedY = -ball.speedY * (k ** 0.5) # домножаем идеальную скорость на коэфицент передачи энергии под корнем
    if ball.xcor() + ball.speedX <= -285 or ball.xcor() + ball.speedX >= 285:  # изменяем импульс в момент касания земли
        ball.speedX = -ball.speedX
    if ball.ycor() + ball.speedY <= -285 and (1 > ball.speedX > -1): #чтобы внизу долго не ждать
        flag = False
    print(time.time() - now)
window.mainloop()  # чтобы не сразу закрывалось
