import turtle
import time
class Setup:
	def __init__(self, screen_width, screen_height, scr_bg_color, scr_title, ch_shape, ch_color, ch_x, ch_y, up, down, left, right):
		self.width = screen_width
		self.height = screen_height
		self.bg_color = scr_bg_color
		self.title = scr_title
		self.ch_shape = ch_shape
		self.ch_color = ch_color
		self.ch_x = ch_x
		self.ch_y = ch_y
		self.wn = None
		self.ch = None
		self.late = None
		self.y = None
		self.x = None
		self.up = up
		self.down = down
		self.left = left
		self.right = right

	def build(self):
		self.wn = turtle.Screen()
		self.wn.title(self.title)
		self.wn.bgcolor(self.bg_color)
		self.wn.setup(self.width, self.height)
		self.wn.tracer(0)

		self.ch = turtle.Turtle()
		self.ch.speed(0)
		self.ch.shape(self.ch_shape)
		self.ch.color(self.ch_color)
		self.ch.penup()
		self.ch.goto(self.ch_x, self.ch_y)
		self.ch.direction = "stop"

	def go_up(self):
		if self.ch.direction != "down":
			self.ch.direction = "up"
	def go_down(self):
                if self.ch.direction != "up":
                        self.ch.direction = "down"
	def go_left(self):
                if self.ch.direction != "right":
                        self.ch.direction = "left"
	def go_right(self):
                if self.ch.direction != "left":
                        self.ch.direction = "right"

	def move(self):
		self.y = self.ch.ycor()
		self.x = self.ch.xcor()
		if self.ch.direction == "up":
			self.ch.sety(self.y + 2)
		if self.ch.direction == "down":
			self.ch.sety(self.y - 2)
		if self.ch.direction == "left":
			self.ch.setx(self.x - 2)
		if self.ch.direction == "right":
			self.ch.setx(self.x + 2)

	def listening(self):
		self.wn.listen()
		self.wn.onkeypress(self.go_up, self.up)
		self.wn.onkeypress(self.go_down, self.down)
		self.wn.onkeypress(self.go_left, self.left)
		self.wn.onkeypress(self.go_right, self.right)

	def update(self):
		self.wn.update()

	def delay(self, secs):
		self.late = time.sleep(secs)

	def wall(self):
		self.y = self.ch.ycor()
		self.x = self.ch.xcor()
		if self.x > self.width / 2 - 20:
			self.ch.goto((self.x - 1), self.y)
			self.ch.direction = "stop"
		elif self.x < (self.width / 2) - self.width + 15:
			self.ch.goto((self.x + 1), self.y)
			self.ch.direction = "stop"
		elif self.y > self.height / 2 - 15:
			self.ch.goto(self.x, (self.y - 1))
			self.ch.direction = "stop"
		elif self.y < (self.height / 2) - self.height + 20:
			self.ch.goto(self.x, (self.y + 1))
			self.ch.direction = "stop"
