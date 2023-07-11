x = 0.0
	y = 0.0
	
	
	#код
	import turtle
	import math
	import time
	
	
	
	t = turtle
	t.ht()
	t.speed(10)
	
	t.pu()
	
	def screen_conf(title="Graph", height=500, width=500):
		sc = t.Screen()
		sc.setup(height, width)
		
		t.title(title)
		
	def screen_save():
		turtle.done()
	
	#координатная плоскость
	def draw_coord(size=500):
		ft = ("Arial", 4, "normal")
		
		t.goto(-size, 0)
		t.write(str(-size), font=ft)
		t.pd()
		t.goto(size, 0)
		t.write(str(size), font=ft)
		t.pu()
		
		t.goto(0, -size)
		t.write(str(-size), font=ft)
		t.pd()
		t.goto(0, size)
		t.write(str(size), font=ft)
		t.pu()
	# y = ... equation graph
	class y_plot(object):
		def __init__(self, equation, mult=1,  x_from = -100, x_to = 100):
			self.equation = equation
			self.x_from = x_from
			self.x_to = x_to
			self.mult = mult
		
		
	
			
		def draw(self, color):
			#рисование графика
			t.color(color)
			try:
				exec(self.equation)
			except:
				raise Exception("Wrong equation. (use *, /...)")
			
			
			for x in range(self.x_from, self.x_to):
				lcls = locals()
				exec(self.equation, globals(), lcls)
				y = lcls["y"] * self.mult
				if (x == self.x_from):
					t.goto(x, y)
					t.pd()
				t.goto(x, y)
			t.pu()
	
	#custom graph
	class list_plot(object):
		def __init__(self, data_array, start_x = 0, start_y = 0):
			self.da = data_array
			self.start_x = start_x
			self.start_y = start_y
			
		
		def draw(self, color):
			if (len(self.da) != 0):
				pass
			else:
				raise Exception("Data from array not found.")
			t.pu()
			t.color(color)
			t.goto(self.start_x, self.da[0] + self.start_y)
			t.pd()
			sx = self.start_x
			sy = self.start_y
			for i in range(sx, len(self.da) + sx):
				x = sx + i
				y = self.da[i - sx] + sy
				t.goto(i, y)
			t.pu()
			
		