import pyautogui
import cv2
from PIL import ImageGrab
import os
import numpy as np
import time
from load_config import get_champion_preference

def match_template(template_path):
    # Load the template image of the copy icon
    try:
        # Attempt to locate the image on the screen
        result = pyautogui.locateOnScreen(template_path, confidence=0.9)
        
        # If the result is found, return it
        if result:
            #print("Template found at:", result)
            return result
        else:
            #print("Image not found.")
            return None
    except pyautogui.ImageNotFoundException:
        #print("Image not found, exception caught.")
        return None

def click_match(match):
        time.sleep(0.5)
        pyautogui.moveTo(match[0] + (match[2]//2), match[1] + (match[3]//2))
        time.sleep(0.5)
        pyautogui.click()




def select_champion(role, search_match, attempts, search_result):
    click_match(search_result)
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)
    champion = get_champion_preference(role, attempts)
    pyautogui.write(champion)
    time.sleep(0.5)
    champion_box = [search_match[0] - 514, search_match[1] + 66, 90, 90]
    time.sleep(0.5)
    pyautogui.moveTo(champion_box[0] + (champion_box[2]//2), champion_box[1] + (champion_box[3]//2))
    time.sleep(0.5)
    pyautogui.click()
    click_match(search_result)
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)
    pyautogui.press('backspace')

def select_runes(runes_result):
    click_match(runes_result)
    left_rune_result = [runes_result[0] + 191, runes_result[1] -500, 90, 90]
    time.sleep(1)
    click_match(left_rune_result)


def determine_role():
    player_role_position_path = os.path.abspath('imgs/player_select_position.png')
    top_role_path = os.path.abspath('imgs/role_top.png')
    jungle_role_path = os.path.abspath('imgs/role_jungle.png')
    mid_role_path = os.path.abspath('imgs/role_mid.png')
    bot_role_path = os.path.abspath('imgs/role_bot.png')
    support_role_path = os.path.abspath('imgs/role_support.png')

    player_role_position_result = match_template(player_role_position_path)

    top_role_result = match_template(top_role_path)
    jungle_role_result = match_template(jungle_role_path)
    mid_role_result = match_template(mid_role_path)
    bot_role_result = match_template(bot_role_path)
    support_role_result = match_template(support_role_path)

    role_list = [top_role_result, jungle_role_result, mid_role_result, bot_role_result, support_role_result]
    role_string_list = ["top", "jungle", "mid", "bot", "support"]

    min_dist = 99999
    min_ind = 99
    for i in range(len(role_list)):
        role = role_list[i]
        if role is not None:
            dist = np.sqrt( (player_role_position_result[0] - role[0])**2 + (player_role_position_result[1] - role[1])**2  )
            if dist < min_dist:
                min_dist = dist
                min_ind = i

    return role_string_list[min_ind], role_list[min_ind], [top_role_result, jungle_role_result, mid_role_result, bot_role_result, support_role_result]

def check_valid_champ_hover(role, result):
    top_role_path = os.path.abspath('imgs/role_top.png')
    jungle_role_path = os.path.abspath('imgs/role_jungle.png')
    mid_role_path = os.path.abspath('imgs/role_mid.png')
    bot_role_path = os.path.abspath('imgs/role_bot.png')
    support_role_path = os.path.abspath('imgs/role_support.png')
    top_role_result = match_template(top_role_path)
    jungle_role_result = match_template(jungle_role_path)
    mid_role_result = match_template(mid_role_path)
    bot_role_result = match_template(bot_role_path)
    support_role_result = match_template(support_role_path)
    if role == 'top':
        return top_role_result
    elif role == 'jungle':
        return jungle_role_result
    elif role == 'mid':
        return mid_role_result
    elif role == 'bot':
        return bot_role_result
    elif role == 'support':
        return support_role_result

