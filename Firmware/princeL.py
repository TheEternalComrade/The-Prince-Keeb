# main.py
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide


keyboard = KMKKeyboard()


split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT, data_pin=board.GP0, data_pin2=board.GP1 )

keyboard.modules.append(split)

keyboard.row_pins = (board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    # Base Layer
    [
        #COL GP2		COL GP2	    COL GP4	    COL GP5    COL GP6  COL GP7

        KC.TILDE,		KC.N1,		KC.N2,		KC.N3,		KC.N4,		KC.N5,		
        KC.TAB,			KC.Q,		KC.W,		KC.E,		KC.R,		KC.T,				
        KC.Escape,		KC.A,		KC.S,		KC.D,		KC.F,		KC.G,		
        KC.LCTRL,		KC.Z,		KC.X,		KC.C,		KC.V,		KC.B,		

                                                KC.LShift,  KC.Backspace,KC.SPACE
     ],
]
