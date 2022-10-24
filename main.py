import turtle as t
t.getcanvas().winfo_toplevel().attributes("-fullscreen", True)
t.colormode(255)
t.speed(0)
t.hideturtle()
def grid():
  t.colormode(255)
  t.speed(0)
  t.hideturtle()
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
grid()
cont = True
while cont:
  eq_type = input('What type of equation would you like to graph?\n[1] Linear Equation (Form: y = mx + b)\n[2] Quadratic Equation (Form: y = ax² + bx + c)\n> ')
  if eq_type == '1':
    m = float(input('y = \033[1mm\033[0mx + b    (Slope)\n> '))
    b = float(input('y = mx + \033[1mb\033[0m    (Y-Intercept)\n> '))
    t.penup()
    t.width(2)
    t.goto(-200, (m *(-200) + b))
    t.pendown()
    t.color(0,0,0)
    t.goto(200, (m * (200) + b))
    if b == 0 or m == 0:
      x_inter = 0
    else:
      x_inter = (-b)/m
    print(f'Equation: {m}x + {b}\nx-intercept: {x_inter}\ny-intercept: {b}\n')
    cont1 = input('Would you like to graph another equation? [y, n]\n> ')
    if cont1 == 'y':
      scr_clr = input('Would you like to keep the current graphs or remove them? [y, n]')
      if scr_clr == 'y':
        t.Screen().clear()
        t.Screen().reset()
      elif scr_clr == 'n':
        pass        
    else:
      cont=False
  elif eq_type == '2':
    while True:
      a = input('y = \033[1ma\033[0mx² + bx + c    (Coefficient of x²)\n> ')
      try:
        a = float(a)
        break
      except:
        input('Invalid input. Please try again. \n[Enter] to continue')
    while True:
      b = input('y = ax² + \033[1mb\033[0mx + c    (Coefficient of x)\n> ')
      try:
        b = float(b)
        break
      except:
        input('Invalid input. Please try again. \n[Enter] to continue')
    while True:
      c = input('y = ax² + bx + \033[1mc\033[0m    (Y-Intercept)\n> ')
      try:
        c = float(c)
        break
      except:
        input('Invalid input. Please try again. \n[Enter] to continue')
    t.color(0, 0, 0)
    for x in range(-2000, 2000, 1):
      x /= 10
      y = a * (x ** 2) + b * x + c
      if y >= -200 and y <= 200:
        t.penup()
        t.goto(x, y)
        t.dot(2)
        print(x, y)
      else:
        pass
    x_val = (-b) / (2 * a)
    y_val = a * (x_val ** 2) + b * x_val + c
    if a > 0:
      minormax = f'Minimum: ({x_val}, {y_val})'
    elif a < 0:
      minormax = f'Maximum: ({x_val}, {y_val})'
    x_inter1 = str(((-b) + (b ** 2 + (-4) * a * c) ** 0.5) / (2 * a))
    cmplx = x_inter1.find('j') + 1
    if cmplx:
      cmplx -= 1
      x_inter1 = x_inter1.replace('j', '\033[1mi\033[0m')
    x_inter2 = str(((-b) - (b ** 2 + (-4) * a * c) ** 0.5) / (2 * a))
    cmplx = x_inter2.find('j') + 1
    if cmplx:
      cmplx -= 1
      new_x_inter2 = x_inter2.replace('j', '\033[1mi\033[0m')
      x_inter2 = f'{new_x_inter2}\n(The \033[1mi\033[0m is a complex number (√(-1)))'
    print(f'Equation: {a}x² + {b}x + {c}\nRoots: {x_inter1}, and {x_inter2}\ny-intercept: {c}\n{minormax}')
    cont1 = input('Would you like to graph another equation? [y, n]\n> ')
    if cont1 == 'y':
      scr_clr = input('Would you like to keep the current graphs or remove them? [y, n]')
      if scr_clr == 'y':
        t.Screen().clear()
        t.Screen().reset()
        grid()
      elif scr_clr == 'n':
        pass        
    else:
      cont=False
  else:
    input('Invalid input. Please try again. \n[Enter] to continue')
