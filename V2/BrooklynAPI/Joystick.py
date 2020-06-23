
import pygame
 
class Joystick:
    def __init__(self):

        pygame.init()
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
 
 
    def get_number_of_joysticks(self):
        joystick_count = pygame.joystick.get_count()
        return joystick_count
 
    
 
    
    def get_type_of_joystick(self):
        name = joystick.get_name()
        return name
 
    def get_number_of_axis(self):

        axes = joystick.get_numaxes()
        return axes
    def get_axis_vaule(self, axis_number):
        
        axis = joystick.get_axis(axis_number)
        return axis
    def get_num_buttons(self):
 
        buttons = joystick.get_numbuttons()
        return buttons
    
    def get_button(self, buttton_number):
        
            button = joystick.get_button(buttton_number)
            return button
 
        
