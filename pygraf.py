x = 0.0
y = 0.0

upscale = 5
disp_x = [-upscale*100, -upscale*100]
disp_y = [upscale*100, upscale*100]


import turtle
import math
import time


t = turtle
t.setworldcoordinates(disp_x[0], disp_x[1], disp_y[0], disp_y[1])
t.ht()
t.speed(10)
t.pu()

def screen_conf(title: str="Graph", height: int=500, width:int=500, anim:bool=False):
	"""
    Настройка окна
    :param title: Заголовок окна
    :param height: Высота окна
    :param width: Ширина окна
    :param anim: Включить анимацию отрисовки?
    :return: None
	"""
	sc = t.Screen()
	if not anim: sc.tracer(0)
	sc.setup(height, width)

	t.title(title)


def screen_save():
	"""
	Не закрывать окно и начать отслеживать перемещение.
	:return: None
	"""

	def move(d1:list[int], d2:list[int], size=False):
		global disp_x, disp_y, upscale
		if size: upscale -= d1[0] / 100
		if (upscale > 0) or not size:
			disp_x[0] += d1[0]; disp_x[1] += d1[1]
			disp_y[0] += d2[0]; disp_y[1] += d2[1]
			t.setworldcoordinates(disp_x[0], disp_x[1], disp_y[0], disp_y[1])
		else:
			if size: upscale = 1


	turtle.listen()
	turtle.onkey(lambda: move([-100, -100], [100, 100], True), "9" ) # -, уменьшение
	turtle.onkey(lambda: move([100, 100], [-100, -100], True), "0") # +, приближение
	turtle.onkey(lambda: move([0, 100], [0, 100]), "Up")
	turtle.onkey(lambda: move([0, -100], [0, -100]), "Down")
	turtle.onkey(lambda: move([-100, 0], [-100, 0]), "Left")
	turtle.onkey(lambda: move([100, 0], [100, 0]), "Right")
	turtle.done()

def draw_coord(size:int=500):
	"""
	Отрисовать координатную плоскость
	:param size: Размер
	:return: None
	"""
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
	def __init__(self, equation:str, mult:float|int=1,  x_from:int = -100, x_to:int = 100):
		"""
		График зависимости Y от X
		:param equation: математическое уравнение ('y = ..x..')
		:param mult: домножение каждого значения Y на указанную величину (>=0.0.2)
		:param x_from: Ограничение графика 'слева'
		:param x_to: Ограничение графика 'справа'
		"""
		self.equation = equation
		self.x_from = x_from
		self.x_to = x_to
		self.mult = mult

	def draw(self, color:str="red"):
			"""
			Отрисовать график
			:param color: Цвет
			:return: None
			"""
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
	def __init__(self, data_array:list[int], start_x:int = 0, start_y:int = 0):
		"""
		График значений списка
		:param data_array: список
		:param start_x: Сдвиг по X
		:param start_y: Сдвиг по Y
		"""
		self.da = data_array
		self.start_x = start_x
		self.start_y = start_y
			
		
	def draw(self, color:str="red"):
		"""
		Отрисовать график
		:param color: Цвет
		:return: None
		"""
		if len(self.da) == 0:
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
