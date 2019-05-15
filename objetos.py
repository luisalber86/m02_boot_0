import turtle #modulo turtle

tortuguita = turtle.Turtle() #objeto tipo turtle
otraTortuguita = turtle.Turtle()
lentorra = turtle.Turtle()

lentorra.speed(1)
lentorra.right(90)
lentorra.fd(100)

tortuguita.speed(5)
tortuguita.shape('turtle')
tortuguita.fd(50) #fd avanzar

otraTortuguita.speed(5)
otraTortuguita.color('green')
otraTortuguita.shape('square')
otraTortuguita.left(90)
otraTortuguita.fd(50)