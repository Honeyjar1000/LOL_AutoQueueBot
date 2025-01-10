from scripts.behaviour_tree import bt
import cv2 
import keyboard

def main():
    bot = bt()
    try:
        while True:

            if keyboard.is_pressed('q') or keyboard.is_pressed('esc'):
                print("Exiting program...")
                break

            results = bot.tick()
            bot.display_screen(results)
    finally:            
        cv2.destroyAllWindows()  # Close all OpenCV windows


# Call the main function
if __name__ == '__main__':
    main()
