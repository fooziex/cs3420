import guidata
_app = guidata.qapplication()

import guidata.dataset.datatypes as dt
import guidata.dataset.dataitems as di
from guidata.dataset.dataitems import ChoiceItem, ColorItem

class DisplayBoard(dt.DataSet):
    """c4o5x5
    The following text is the DataSet 'comment': <br>Plain text or
    <b>rich text<sup>2</sup></b> are both supported,
    as well as special characters (α, β, γ, δ, ...)
    """ #leaving this in as an example
    
    #ideally we'd have an array of 5x5 but the UI toolkit won't render arrays like it does variables, as far as I can tell
    #worst case we're writing a "move from UI to backend class" function
    A1 = ColorItem("A1", default="black")
    A2 = ColorItem("A2", default="black").set_pos(col=1)
    A3 = ColorItem("A3", default="black").set_pos(col=2)
    A4 = ColorItem("A4", default="black").set_pos(col=3)
    A5 = ColorItem("A5", default="black").set_pos(col=4)
    B1 = ColorItem("B1", default="black")
    B2 = ColorItem("B2", default="black").set_pos(col=1)
    B3 = ColorItem("B3", default="black").set_pos(col=2)
    B4 = ColorItem("B4", default="black").set_pos(col=3)
    B5 = ColorItem("B5", default="black").set_pos(col=4)
    C1 = ColorItem("C1", default="black")
    C2 = ColorItem("C2", default="black").set_pos(col=1)
    C3 = ColorItem("C3", default="black").set_pos(col=2)
    C4 = ColorItem("C4", default="black").set_pos(col=3)
    C5 = ColorItem("C5", default="black").set_pos(col=4)
    D1 = ColorItem("D1", default="black")
    D2 = ColorItem("D2", default="black").set_pos(col=1)
    D3 = ColorItem("D3", default="black").set_pos(col=2)
    D4 = ColorItem("D4", default="black").set_pos(col=3)
    D5 = ColorItem("D5", default="black").set_pos(col=4)
    E1 = ColorItem("E1", default="black")
    E2 = ColorItem("E2", default="black").set_pos(col=1)
    E3 = ColorItem("E3", default="black").set_pos(col=2)
    E4 = ColorItem("E4", default="black").set_pos(col=3)
    E5 = ColorItem("E5", default="black").set_pos(col=4)
    
class ChooseMove(dt.DataSet):
    """c4o5x5
    Player N, select your move:
    """ #need to make N change with player number
    move_set=[((0,0), 'A1'),
             ((0,1), "A2"),
             ((0,2), "A3"),
             ((0,3), "A4"),
             ((0,4), "A5"),
             ((1,0), 'B1'),
             ((1,1), "B2"),
             ((1,2), "B3"),
             ((1,3), "B4"),
             ((1,4), "B5"),
             ((2,0), 'C1'),
             ((2,1), "C2"),
             ((2,2), "C3"),
             ((2,3), "C4"),
             ((2,4), "C5"),
             ((3,0), 'D1'),
             ((3,1), "D2"),
             ((3,2), "D3"),
             ((3,3), "D4"),
             ((3,4), "D5"),
             ((4,0), 'E1'),
             ((4,1), "E2"),
             ((4,2), "E3"),
             ((4,3), "E4"),
             ((4,4), "E5")
             ]
    Move = ChoiceItem("Single choice 1",
                        move_set)
    
board_results = DisplayBoard() #this stuff is just for demo purposes
board_results.view()           #this too    

new_move = ChooseMove()        #ditto
new_move.edit()                #"
