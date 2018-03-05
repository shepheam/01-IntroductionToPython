"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and ASHLEY_SHEPHERD.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg
window = rg.SimpleTurtle()

ashley = rg.SimpleTurtle('turtle')
ashley.speed = 75
ashley.pen = rg.Pen('blue',5)

size = 75
for k in range (5):
    ashley.draw_circle(size)
    ashley.pen_up()
    ashley.right(22)
    ashley.backward(144)
    ashley.left(22)
    ashley.pen_down()
    size = size - 12

brooke = rg.SimpleTurtle('turtle')
brooke.speed = 100
brooke.pen = rg.Pen('pink',5)

size = 125
for k in range (20):
    brooke.draw_square(size)
    brooke.pen_up()
    brooke.right(45)
    brooke.forward(122)
    brooke.left(45)
    brooke.pen_down()
    size = size - 30