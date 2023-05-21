import pygame
import sys
from pygame.locals import QUIT

from datetime import datetime


pygame.init()

display_width = 600
display_height = 300

screen = pygame.display.set_mode([display_width,display_height])
pygame.display.set_caption("Digital clock")


# set up display areas for each of the 4 digits, position coordinates first, then rectangle size
digit_rect_width_offset = display_width / 30
digit_rect_vert_offset = display_height / 10
digit_rect_width = display_width / 7.5
digit_rect_height = display_height / 1.25

hours_digit_one_rect = pygame.draw.rect(screen,(0,0,0),(display_width/15 *1.5 + digit_rect_width_offset, digit_rect_vert_offset, digit_rect_width, digit_rect_height))
hours_digit_two_rect = pygame.draw.rect(screen,(0,0,0),(display_width/15 *4 + digit_rect_width_offset, digit_rect_vert_offset, digit_rect_width, digit_rect_height))
minutes_digit_one_rect = pygame.draw.rect(screen,(0,0,0),(display_width/15 *7.5 + digit_rect_width_offset, digit_rect_vert_offset, digit_rect_width, digit_rect_height))
minutes_digit_two_rect = pygame.draw.rect(screen,(0,0,0),(display_width/15 *10 + digit_rect_width_offset, digit_rect_vert_offset, digit_rect_width, digit_rect_height))


# set up display area for ':' separator
separator_rect_width = display_width / 20
separator_rect_height = display_height / 15
separator_rect_vert_offset = display_height / 5.5
separator_rect = pygame.draw.rect(screen,(0,0,0),(display_width/15 *6.5 + digit_rect_width_offset, separator_rect_vert_offset, separator_rect_width, separator_rect_height))




#set up periodic check of time for display update
time_check = pygame.USEREVENT+1
pygame.time.set_timer(time_check,100)


running = True
while running:
    for event in pygame.event.get():
        
        if event.type == time_check:
            
            current_time = datetime.now()
            #conversion to string from integer, so that digits can be iterated over, in below append operation
            hours = str(current_time.hour)
            minutes = str(current_time.minute)
            micro_secs = current_time.microsecond

            digits = []
            # place current time into 'digits' list
            #
            # if hours or mins less than 10 there will be only one corresponding digit from datetime, 
            #    therefore add zero manually in this case:
            if len(hours)<2:
                digits.append("0")
                digits.append(hours[0])
            else:
                digits.append(hours[0])
                digits.append(hours[1])
            
            if len(minutes)<2:
                digits.append("0")
                digits.append(minutes[0])
            else:
                digits.append(minutes[0])
                digits.append(minutes[1])

            # refreshes the screen, otherwise the numbers write on top of the existing ones
            screen.fill((0,0,0))
            
            #font_choice = pygame.font.get_fonts()     # if different font wanted
            font = pygame.font.SysFont("arial", 200)
            
            display_digit_one = font.render(digits[0],True,(200, 0, 0))
            display_digit_two = font.render(digits[1],True,(200, 0, 0))
            display_digit_three = font.render(digits[2],True,(200, 0, 0))
            display_digit_four = font.render(digits[3],True,(200, 0, 0))

            
            separator_font = pygame.font.SysFont("arial", 150)
            # make separator blink according to microsecond value
            if micro_secs < 500000:
                display_separator = separator_font.render(":",True,(200, 0, 0))
            else:
                display_separator = separator_font.render(":",True,(0, 0, 0))
            
            
            
            screen.blit(display_digit_one,hours_digit_one_rect)
            screen.blit(display_digit_two,hours_digit_two_rect)
            screen.blit(display_digit_three,minutes_digit_one_rect)
            screen.blit(display_digit_four,minutes_digit_two_rect)

            screen.blit(display_separator,separator_rect)
            
            pygame.display.flip() # updates display with new digits and separator rendered above

        
        elif event.type == QUIT: # quit when pygame window closed
            
            running = False