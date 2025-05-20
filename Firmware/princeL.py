# main.py
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()
keyboard.modules.append(Layers())


split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT, data_pin=board.GP0, data_pin2=board.GP1 )

keyboard.modules.append(split)

keyboard.row_pins = (board.GP13, board.GP12, board.GP11, board.GP10, board.GP9)
keyboard.col_pins = (board.GP29, board.GP28, board.GP27, board.GP26, board.GP15, board.GP14)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

lower = KC.MO(2)
blank = KC.NO
glass = KC.TRNS

keyboard.keymap = [
    # Base Layer
    [
        #COL GP29		COL GP28    COL GP27    COL GP26    COL GP15    COL GP14

        KC.TILDE,		KC.N1,		KC.N2,		KC.N3,		KC.N4,		KC.N5,		
        KC.TAB,			KC.Q,		KC.W,		KC.E,		KC.R,		KC.T,				
        KC.Escape,		KC.A,		KC.S,		KC.D,		KC.F,		KC.G,		
        KC.LCTRL,		KC.Z,		KC.X,		KC.C,		KC.V,		KC.B,		

                                                KC.LShift,  KC.BSPC,    lower
     ],

     # Raise Layer
    [
        #COL GP29		COL GP28    COL GP27    COL GP26    COL GP15    COL GP14

        blank,		    blank,		blank,		blank,		blank,		blank,		
        blank,		    blank,		blank,		blank,		blank,		blank,				
        blank,		    blank,		blank,		blank,		blank,		blank,		
        blank,		    blank,		blank,		blank,		blank,		blank,		

                                                glass,      glass,      glass

     ],

     # Lower Layer
    [
        #COL GP29		COL GP28    COL GP27    COL GP26    COL GP15    COL GP14

        blank,		    blank,		blank,		blank,		blank,		blank,		
        blank,		    blank,		blank,		blank,		blank,		blank,				
        blank,		    blank,		blank,		blank,		blank,		blank,		
        blank,		    blank,		blank,		blank,		blank,		blank,		

                                                glass,      glass,      glass

     ]
]

if __name__ == '__main__':
    keyboard.go()
