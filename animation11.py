from turtle import*
bgcolor('black')
c = ['black','white','black',
     'white','black','white']
for i in range(800):
     color(c[i%6])
     fd(7)
     lt(88)
     fd(i*3)
     circle(10)
     lt(59)
done()
