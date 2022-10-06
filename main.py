import turtle as t
t.getcanvas().winfo_toplevel().attributes("-fullscreen", True)
t.colormode(255)
t.speed(0)
t.hideturtle()
def grid():
  def lines(x=20):
    for i in range(x):
      if i == 10:
        pass
      else:
        t.color(10,130,4)
        t.forward(20)
        t.color(50,230,41)
        t.left(90)
        t.forward(200)
        t.backward(400)
        t.forward(200)
        t.right(90)
    t.color(10,130,4)
  t.width(3)
  t.forward(200)
  t.backward(400)
  t.width(1)
  lines()
  t.goto(0,0)
  t.width(3)
  t.left(90)
  t.forward(200)
  t.backward(400)
  t.width(1)
  lines()
  t.goto(0,0)
  t.width(3)
  t.left(90)
  t.forward(200)
  t.backward(400)
  t.width(1)
while  True:
  m = float(input('y = \033[1mm\033[0mx + b    (Slope)\n> '))
  b = float(input('y = mx + \033[1mb\033[0m    (Y-Intercept)\n> '))
  grid()
  t.penup()
  t.width(2)
  t.goto(-200,(m*(-200)+b))
  t.pendown()
  t.color(0,0,0)
  t.goto(200, (m*(200)+b))
  if b == 0 or m == 0:
    x_inter = 0
  else:
    x_inter = (-b)/m
  print(f'Equation: {m}x + {b}\nx-intercept: {x_inter}\ny-intercept: {b}')
  break1 = False
  while break1 == False:
    con = input('Do you want to graph another line? [y, n]\n> ')
    if con == 'y':
      break1 = True
    elif con == 'n':
      exit()
    else:
      print('Invalid option. Try again.')
input('[Enter] to end program')