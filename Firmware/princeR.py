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


split = Split(split_type=SplitType.UART, split_side=SplitSide.RIGHT, data_pin=board.GP0, data_pin2=board.GP1 )

keyboard.modules.append(split)

keyboard.row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.col_pins = (board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

rise = KC.MO(1)
blank = KC.NO
glass = KC.TRNS


keyboard.keymap = [
    # Base Layer
    [
        #COL GP7		COL GP6	    COL GP5	    COL GP4     COL GP3     COL GP2

        KC.N6,		    KC.N7,		KC.N8,		KC.N9,		KC.N0,		KC.MINUS,		
        KC.Y			KC.U,		KC.I,		KC.O,		KC.P,		KC.EQL,				
        KC.H,		    KC.J,		KC.K,		KC.L,		KC.SCOLON,	KC.QUOTE		
        KC.N,		    KC.M,		KC.COMMA,	KC.DOT,		KC.SLASH,	KC.RCTRL,		

        rise,          KC.SPACE,   KC.RCTRL
     ],

     # Raise Layer
    [
        #COL GP2		COL GP2	    COL GP4	    COL GP5    COL GP6  COL GP7

        KC.F6,		    KC.F7,		KC.F8,		KC.F10,		KC.F11,		KC.F12,		
        blank,			blank,		KC.UP,		blank,		KC.LBRACKET,KC.RBRACKET,				
        blank,		    KC.RGHT,	KC.DOWN,    KC.LEFT,	blank,		blank,		
        blank,		    blank,		blank,		blank,		KC.BSLASH,	blank,		

        glass,      glass,      glass

     ],

     # Lower Layer
    [
        #COL GP2		COL GP2	    COL GP4	    COL GP5    COL GP6  COL GP7

        blank,		    blank,		blank,		blank,		blank,		blank,		
        blank,		    blank,		blank,		blank,		blank,		blank,				
        blank,		    blank,		blank,		blank,		blank,		blank,		
        blank,		    blank,		blank,		blank,		blank,		blank,		

        glass,      glass,      glass

     ]

]

if __name__ == '__main__':
    keyboard.go()
