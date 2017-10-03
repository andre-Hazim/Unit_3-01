# created by ray, andre, and khoa
# created on october 3, 2017
# created for isc3u
# created for unit 3-01 daily assignment
# this program has a mystery number in which the user has to guess

import ui

# constant

MYSTERYNUM = 5

def check_number_button_touch_up_inside(sender):
    #this function checks if the guess is correct
    
    #input
    number_entered = int(view['number_textfield'].text)
    
    #process
    if number_entered == MYSTERYNUM:
        
        #output
        view['correct_label'].text = "Correct!"

        
    

view = ui.load_view()
view.present('sheet')
