x = 0.0
y = 0.0

upscale = 1.1
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

def float_range(start:int|float, stop:int|float, step:int|float):
	"""
	Аналог range, но только с float как шаг.
	:param start: Начальное значение
	:param stop: Конечное значение
	:param step: Шаг
	:return: None
	"""
	while start < stop:
		yield start
		start += step

def screen_conf(title: str="Graph", width: int=500, height:int=500, anim:bool=False):
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
	sc.setup(width, height)

	t.title(title)

def zoom(scale:int):
	"""
	Увеличить/уменьшить картинку из кода
	:param scale: Размер увеличения. Отрицательное число - уменьшение.
	:return: None
	"""
	if scale > 0:
		for _ in range(scale): move([100, 100], [-100, -100], True)
	elif scale < 0:
		for _ in range(abs(scale)): move([-100, -100], [100, 100], True)

def move(d1:list[int], d2:list[int], size=False):
	global disp_x, disp_y, upscale
	if size: upscale -= (d1[0] / 100)
	if (upscale > 0) or not size:
		disp_x[0] += d1[0]; disp_x[1] += d1[1]
		disp_y[0] += d2[0]; disp_y[1] += d2[1]
		t.setworldcoordinates(disp_x[0], disp_x[1], disp_y[0], disp_y[1])
	else:
		if size: upscale = 1

def screen_save():
	"""
	Не закрывать окно и начать отслеживать перемещение.
	:return: None
	"""

	turtle.listen()
	turtle.onkey(lambda: zoom(-1), "-" ) # -, уменьшение
	turtle.onkey(lambda: zoom(1),  "=") # +, приближение
	turtle.onkey(lambda: move([0,  20], [0,  20]), "Up")
	turtle.onkey(lambda: move([0, -20], [0, -20]), "Down")
	turtle.onkey(lambda: move([-20, 0], [-20, 0]), "Left")
	turtle.onkey(lambda: move([20,  0], [20,  0]), "Right")
	turtle.done()

def draw_coord(size:int=500, sep_step:int|float=10, sep_size:float=0.6):
	"""
	Отрисовать координатную плоскость
	:param sep_size: Размер сечений
	:param sep_step: Шаг сечений
	:param size: Размер
	:return: None
	"""
	ft = ("Arial", 8, "normal")
	small_ft = ("Arial", 6, "normal")

	t.goto(-size, 0)
	t.write(str(-size), font=ft)
	t.pd()
	for x_ in float_range(-size + sep_step, size + sep_step, sep_step):
		t.goto(x_, 0)
		t.goto(x_, sep_size)
		t.goto(x_, -sep_size)
		t.write(x_, font=small_ft)
		t.goto(x_, 0)
	t.pu()
	t.write(str(size), font=ft)

	t.goto(0, -size)
	t.write(str(-size), font=ft)
	t.pd()
	for y_ in float_range(-size + sep_step, size + sep_step, sep_step):
		t.goto(0, y_)
		t.goto(sep_size, y_)
		t.goto(-sep_size, y_)
		t.write(y_, font=small_ft)
		t.goto(0, y_)
	t.pu()
	t.write(str(size), font=ft)

	# y = ... equation graph
class y_plot(object):
	def __init__(self, equation:str, mult:float|int=1,  x_from:int = -100, x_to:int = 100, step:float=0.1):
		"""
		График зависимости Y от X
		:param equation: математическое уравнение ('y = ..x..')
		:param mult: домножение каждого значения Y на указанную величину (>=0.0.2)
		:param x_from: Ограничение графика 'слева'
		:param x_to: Ограничение графика 'справа'
		:param step: Шаг, чем меньше - тем точнее график
		"""
		self.equation = equation
		self.x_from = x_from
		self.x_to = x_to
		self.mult = mult
		self.step = step

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
			raise Exception("[PF] Wrong equation. (use *, /...)")


		for x in float_range(self.x_from, self.x_to, self.step):
			lcls = locals()
			try:
				exec(self.equation, globals(), lcls)
				y = lcls["y"] * self.mult
				if (x >= self.x_from):
					t.goto(x, y)
					t.pd()
				t.goto(x, y)
			except:
				# t.pu()
				print(f"[PF] Failed to find y for x = {x}")
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
			raise Exception("[PF] Data from array not found.")

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
