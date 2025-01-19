from manim import *
import pygame as keylog

keylog.init()

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)

        square = Square()
        
        square.rotate(PI/4)

        self.play(Create(square)) # animate the creation of the square
        
        self.play(square.animate.rotate(3*PI/4))
        self.play(Transform(square, circle)) # interpolate the square into the circle
        self.play(square.animate.set_fill(RED))
        self.play(FadeOut(square)) # fade out animation 