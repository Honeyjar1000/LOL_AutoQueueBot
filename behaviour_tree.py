import pyautogui
import cv2
from PIL import ImageGrab
import os
import numpy as np
import time
from utils import *

InQueue_TP = os.path.abspath('imgs/in_queue.png')
AcceptMatch_TP = os.path.abspath('imgs/accept_match.png')
StartChampSelect_TP = os.path.abspath('imgs/in_champ_select.png')
SearchChamp_TP = os.path.abspath('imgs/search_champion.png')
LockInValid_TP = os.path.abspath('imgs/lock_in.png')
LockInNotValid_TP = os.path.abspath('imgs/lock_in2.png')
Runes_TP = os.path.abspath('imgs/runes.png')
SmiteCloseCase_TP = os.path.abspath('imgs/replaced_smite_exit.png')

class bt:

    def __init__(self):
        self.state = None
        self.role = None
        self.role_RESULT = None
        self.champ_select_attempts = 0


    def tick(self):

        total_results = []

        # Check In Queue
        InQueue_RESULT = match_template(InQueue_TP)
        if InQueue_RESULT:
            self.state = "In Queue"
            total_results.append(InQueue_RESULT)


        # Check Accept Match
        AcceptMatch_RESULT = match_template(AcceptMatch_TP)
        if AcceptMatch_RESULT:
            self.state = "Game Found"
            total_results.append(AcceptMatch_RESULT)
            click_match(AcceptMatch_RESULT)
            time.sleep(0.2)
        

        # Declare Champion
        if InQueue_RESULT is None: 
            StartChampSelect_RESULT = match_template(StartChampSelect_TP)
            if StartChampSelect_RESULT and (self.role is None):
                self.state = "In Champ Select"
                total_results.append(StartChampSelect_RESULT)

                self.role, self.role_RESULT, AllRoles_result = determine_role()
                print("all roles 1: ", AllRoles_result)
                for r_result in AllRoles_result:
                    total_results.append(r_result)

                if self.role:
                    # Initial Champ Hover
                    SearchChamp_RESULT = match_template(SearchChamp_TP)
                    if SearchChamp_RESULT:
                        select_champion(self.role, SearchChamp_RESULT, self.champ_select_attempts, SearchChamp_RESULT)
                    else:
                        print("Error: no search champ found?")

            SmiteCloseCase_Result = match_template(SmiteCloseCase_TP)
            if SmiteCloseCase_Result:
                total_results.append(SmiteCloseCase_Result)
                click_match(SmiteCloseCase_Result)
                time.sleep(1)

        # Select Champ and Lock In
        if InQueue_RESULT is None:
            
            

            LockInValid_RESULT = match_template(LockInValid_TP)
            LockInNotValid_RESULT = match_template(LockInNotValid_TP)
            if (LockInValid_RESULT) or (LockInNotValid_RESULT):
                if (self.role is not None):
                    if LockInValid_RESULT:
                        # Lock In Champion
                        self.state = 'Locked In'
                        total_results.append(LockInValid_RESULT)
                        click_match(LockInValid_RESULT)
                        time.sleep(2)
                        Runes_RESULT = match_template(Runes_TP)
                        total_results.append(Runes_RESULT)
                        select_runes(Runes_RESULT)
                    elif LockInNotValid_RESULT:
                        # Pick Another Champion
                        self.state = 'Need To Lock In'
                        total_results.append(LockInNotValid_RESULT)
                        self.champ_select_attempts += 1
                        SearchChamp_RESULT = match_template(SearchChamp_TP)
                        select_champion(self.role, SearchChamp_RESULT, self.champ_select_attempts, SearchChamp_RESULT)
                else:
                    print("Re determine role")
                    self.role, self.role_RESULT, AllRoles_result = determine_role()

                    print("all roles 2: ", AllRoles_result)
                    for r_result in AllRoles_result:
                        total_results.append(r_result)


        print(f'State: {self.state} | Role: {self.role}')
        return total_results

    def display_screen(self, results_inputs):
        # Capture the screen (entire virtual screen)
        screenshot = ImageGrab.grab()  # capture the whole screen
        screenshot_np = np.array(screenshot)

        # Convert from RGB to BGR (OpenCV uses BGR format by default)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # Resize the image for convenience (smaller window size)
        scale_factor = 0.4  # Resize to 40% of the original size
        new_width = int(screenshot_bgr.shape[1] * scale_factor)
        new_height = int(screenshot_bgr.shape[0] * scale_factor)
        screenshot_resized = cv2.resize(screenshot_bgr, (new_width, new_height), interpolation=cv2.INTER_AREA)

        # State Text
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_position = (10, 30)  # Position of the text (x, y)
        font_scale = 1
        font_color = (0, 255, 0)  # Green text
        thickness = 2
        cv2.putText(screenshot_resized, f'State: {self.state}', text_position, font, font_scale, font_color, thickness, cv2.LINE_AA)

        # Role Text
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_position = (10, 60)  # Position of the text (x, y)
        font_scale = 1
        font_color = (0, 255, 0)  # Green text
        thickness = 2
        cv2.putText(screenshot_resized, f'Role: {self.role}', text_position, font, font_scale, font_color, thickness, cv2.LINE_AA)

        for result in results_inputs:
            self.draw_bbox(screenshot_resized, result, scale_factor)

        cv2.imshow('Screen with Template Highlight', screenshot_resized)

        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:  # ASCII for 'q' or Esc key
            return True  # Signal to stop the program
        return False

    def draw_bbox(self, screen, result, scale_factor):
        if result is None:
            return
        
        x, y, width, height = result

        # Scale the bounding box coordinates based on the scale factor
        x_resized = int(x * scale_factor)
        y_resized = int(y * scale_factor)
        width_resized = int(width * scale_factor)
        height_resized = int(height * scale_factor)

        # Draw a rectangle on the resized image (in red color)
        # Correct color format (BGR: Blue-Green-Red for OpenCV)
        cv2.rectangle(screen, (x_resized, y_resized), (x_resized + width_resized, y_resized + height_resized), (0, 0, 255), 3)
