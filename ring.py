from  turtle import*
from  colorsys  import*
speed(0)
bgcolor("black")
tracer(1)
h = 0
for i in range(75):
    color(hsv_to_rgb(h,1,1))
    h  +=0.014
    left(3)
    forward(1)
    
    for j in  range(2):
      circle(100)
      
hideturtle()
done()
