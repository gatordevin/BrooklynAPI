class socketJoy:
    def __init__(self):
        self.data = {
                "id": "Logitech Gamepad F310 (STANDARD GAMEPAD Vendor: 046d Product: c21d)",
                "axes": [
                    "0.00",
                    "0.00",
                    "0.00",
                    "0.00"
                ],
                "buttons": [
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False
                ]
                }
        self.axs = self.data["axes"]
        self.btns = self.data["buttons"]
        self.left_y = -float(self.axs[1])
        self.left_x = float(self.axs[0])
        self.right_y = -float(self.axs[3])
        self.right_x = float(self.axs[2])
        self.a = self.btns[0]
        self.b = self.btns[1]
        self.x = self.btns[2]
        self.y = self.btns[3]
        self.left_bumper = self.btns[4]
        self.right_bumper = self.btns[5]
        self.left_trigger = self.btns[6]
        self.right_trigger = self.btns[7]
        self.back = self.btns[8]
        self.start = self.btns[9]
        self.left_joy_btn = self.btns[10]
        self.right_joy_btn = self.btns[11]
        self.dpad_up = self.btns[12]
        self.dpad_down = self.btns[13]
        self.dpad_left = self.btns[14]
        self.dpad_right = self.btns[15]
    def update_data(self, data):
        self.data = data
        self.axs = self.data["axes"]
        self.btns = self.data["buttons"]
        self.left_y = -float(self.axs[1])
        self.left_x = float(self.axs[0])
        self.right_y = -float(self.axs[3])
        self.right_x = float(self.axs[2])
        self.a = self.btns[0]
        self.b = self.btns[1]
        self.x = self.btns[2]
        self.y = self.btns[3]
        self.left_bumper = self.btns[4]
        self.right_bumper = self.btns[5]
        self.left_trigger = self.btns[6]
        self.right_trigger = self.btns[7]
        self.back = self.btns[8]
        self.start = self.btns[9]
        self.left_joy_btn = self.btns[10]
        self.right_joy_btn = self.btns[11]
        self.dpad_up = self.btns[12]
        self.dpad_down = self.btns[13]
        self.dpad_left = self.btns[14]
        self.dpad_right = self.btns[15]