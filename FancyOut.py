#################################################
## FancyOut                                    ##
#################################################
##                                             ## 
## This 'module' is for helping with creating  ##
## decent looking terminal programs with very  ##
## little effort.                              ##
##                                             ## 
#################################################

import os


def title(title_name, clr_screen=0,width=50):
    if clr_screen > 0:
        os.system('clear')
    print()

    bar = ""
    for _ in range(width):
        bar += '#'

    title_pos = int(width/2) - int(len(title_name)/2)
    title_bar = "##"
    for _ in range(title_pos-2):
        title_bar += " "
    title_bar += title_name.upper()
    for _ in range(width-len(title_bar)-2):
        title_bar += " "
    title_bar += "##"

    print(bar)
    print(title_bar)
    print(bar + '\n')

def output(out_string, leader=0):
    if leader == 0:
        leader = ""
    elif leader == 1 or leader == "indent":
        leader = "     "
    elif leader == 2 or leader == "pointer":
        leader = "---->"
    elif leader == 3 or leader == "warning":
        leader = "#####"

    if leader == "":
        print(out_string)
    else:
        print(leader, out_string)



##################################################
## Testing Code Below                           ##
##################################################
#
# output("hey there", 2)
# output("hey there")
# output("how you doing", 1)
# output("nothing hbu", 'indent')
# output("SOMETHING WENT WRONG", 'warning')
# 
# print('\n')
# 
# title("fancy print")





