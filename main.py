from behaviour_tree import bt
import cv2 

def main():
    bot = bt()
    while True:
        results = bot.tick()
        if bot.display_screen(results):  # Check for exit signal
            print("Exiting program...")
            break

    cv2.destroyAllWindows()  # Close all OpenCV windows


# Call the main function
if __name__ == '__main__':
    main()
