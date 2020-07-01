
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
 

class InputEvent:

    def __init__(self, key, down):
        self.key = key
        self.down = down
        self.up = not down

 class InputManager:

     def __init__(self):
        self.init_joystick()
        self.buttons = ['up', 'down', 'left', 'right', 'start', 'A', 'B', 'X', 'Y', 'L', 'R']
        self.key_map = {
            K_UP = 'up',
            K_DOWN = 'down',
            K_LEFT = 'left',
            K_RIGHT = 'right',
            K_RETURN = 'start',
e            K_a = 'A',
            K_b = 'B',
            K_x = 'X',
            K_y = 'Y',
            K_l = 'L',
            K_r = 'R'
        }

        self.keys_pressed = {}
        for button in self.buttons:
            self.keys_pressed[button] = False
        self.joystick_config = {}
        self.quit_attempt = False

    def is_pressed(self, button):
        return self.keys_pressed[button]

    def get_events(self):
        events = []
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.quit_attempt = True
            if event.type == KEYDOWN or event.type == KEYUP:
                key_pushed_down = event.type == KEYDOWN
                button = self.key_map.get(event.key)
                if button != None:
                    events.append(InputEvent(button, key_pushed_down))
                    self.keys_pressed[button] = key_pushed_down
                    for button in self.buttons:
                        config = self.joystick_config.get(button)
                        if config != None:
                            if config[0] == 'is_button':
                                pushed = self.joystick.get_button(config[1])
                                if pushed != self.keys_pressed[button]:
                                    events.append(InputEvent(button, pushed))
                                    self.keys_pressed[button] = pushed
                            elif config[0] == 'is_axis':
                                status = self.joystick.get_axis(config[1])
                                if config[2] == 1:
                                    pushed = status > 0.5
                                else:
                                    pushed = status < -0.5
                                if pushed != self.keys_pressed[button]:
                                    events.append(InputEvent(button, pushed))
                                    self.keys_pressed[button] = pushed

        return events

    def is_button_used(self, button_index):
        for button in self.buttons:
            config = self.joystick_config.get(button)
            if config != None and config[0] == 'is_button' and config[1] == button_index:
                return True
        return False

    def configure_button(self, button):
        js = self.joystick

        for button_index in range(js.get_num_buttons()):
            button_pushed = js.get_button(button_index)
            if button_pushed and not self.is_button_used(button_index):
                self.joystick_config[button] = ('is_button', button_index)
                return True

        for axis_index in range(js.get_number_of_axis()):
            axis_status = js.get_axis(axis_index)
            

 



    

        
