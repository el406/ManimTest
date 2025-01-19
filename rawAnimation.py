from manim import *
import numpy as np

class Main(Scene):
    def construct(self):
        epsilon = 1e-6
        proton = Circle()
        proton.set_color(RED)
        polarity = 1
        x_shift = 0
        y_shift = 0
        
        proton.set_fill(RED_A, opacity=0.5)
        electron = Circle()
        electron.set_color(BLUE)
        electron.set_fill(BLUE_A, opacity=0.5)
        proton.scale(.3)
        electron.scale(.1)
        title = Text("The Electrical Field").scale(2)
        subtitle = Text("Visualization of Colombs law").scale(.7).shift(DOWN*1.2)
        self.play(Write(title))
        self.wait(0.01) 
        self.play(Write(subtitle))
        self.wait(1)
        self.play(FadeOut(title,subtitle)) 
        func = lambda pos: pos * 0
        vector_field = ArrowVectorField(func)
        self.play(FadeIn(vector_field))
        self.wait(2)
        self.play(Create(proton))
        self.wait(2)
        func = lambda pos: np.array([polarity*4/(np.square(np.sqrt(np.square(pos[0] - x_shift) + np.square(pos[1] - y_shift)+epsilon))) * (pos[0] - x_shift), 
                                     polarity*4/(np.square(np.sqrt(np.square(pos[0] - x_shift) + np.square(pos[1] - y_shift)+epsilon))) * (pos[1] - y_shift)])                     
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        #shift left and right and up and down
        x_shift = -3
        self.wait(3)
        self.play(proton.animate.shift(LEFT*3),vector_field.animate.become(ArrowVectorField(func)))
        x_shift = 3
        self.wait(1)
        self.play(proton.animate.shift(RIGHT*6),vector_field.animate.become(ArrowVectorField(func)))
        x_shift = 0
        self.wait(1)
        self.play(proton.animate.shift(LEFT*3),vector_field.animate.become(ArrowVectorField(func)))
        
        
        
        
        
        
        
        
        #switch the polarty
        polarity = -1
        self.wait(3)
        self.play(ReplacementTransform(proton,electron))
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait(3)
       
        
        
        