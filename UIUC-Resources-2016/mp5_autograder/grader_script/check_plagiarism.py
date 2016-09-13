import os
import tools
from string import whitespace

def check_plagiarism(location_submission):
    copied = 0
    message = "\n"
    if (location_submission in location_fa15):
        copied = 1
        message += "location coordinates copied from fall 2015\n"
    return copied, message

# Fall 2015
location_l_bookstore_sol  = ['40.108', '-88.229']
location_l_eceb_sol       = ['40.114', '-88.231']
location_l_powerplant_sol = ['40.105', '-88.241']
location_l_siebel_sol     = ['40.114', '-88.226']
location_l_union_sol      = ['40.109', '-88.229']

location_w_armory_sol     = ['40.105', '-88.233']
location_w_hilton_sol     = ['40.098', '-88.246']
location_w_isr_sol        = ['40.109', '-88.220']
location_w_panda_sol      = ['40.110', '-88.228']
location_w_terminal_sol   = ['40.115', '-88.241']
 
location_fa15 = [location_l_bookstore_sol,
                 location_l_eceb_sol,
                 location_l_powerplant_sol,
                 location_l_siebel_sol,
                 location_l_union_sol,
                 location_w_armory_sol,
                 location_w_hilton_sol,
                 location_w_isr_sol,
                 location_w_panda_sol,
                 location_w_terminal_sol]
