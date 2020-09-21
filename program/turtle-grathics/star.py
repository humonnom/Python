import turtle as t

t.shape('turtle')
t.speed('slowest')

degree = 360/5
len = 100

def draw_star():
	t.forward(len)
	t.right(degree * 2)
	t.forward(len)
	t.left(degree)

i = 0
for i in range(5):
	draw_star()
	i += 1
