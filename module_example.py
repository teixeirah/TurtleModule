from turtle_module import Setup
s = Setup(600, 600, "pink", "Turtle_Setup_Class", "circle", "black", 0, 0, "w", "s", "a", "d")
s.build()
while True:
	s.update()
	s.listening()
	s.wall()
	s.move()
	s.delay(0.005)
