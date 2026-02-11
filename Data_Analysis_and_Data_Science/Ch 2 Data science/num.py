from multiprocessing.connection import wait
from timeit import repeat
from turtle import *
nsides = float(input('Type in the number of side : '))
bgcolor('white')
hideturtle()
repeat(nsides)
forward(50)
left(360.0/nsides)
wait(2)
done()
