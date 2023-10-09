import time
import pyautogui

def close_unused_tabs(num_tabs_to_keep=5):
    pyautogui.hotkey('alt', 'tab')
    time.sleep(10)
    for _ in range(num_tabs_to_keep - 1):
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(10)
if __name__ == "__main__":
    num_tabs_to_keep = 5 
    close_unused_tabs(num_tabs_to_keep)


    # Explanation for the code

#The purpose of this code is to help manage browser tabs automatically by closing excess tabs,
#leaving only the specified number of tabs open. This could be useful, for example, if you
#frequently open many tabs while browsing and want to keep your browser more organized by 
# automatically closing some of them. The script can be executed when needed to perform this task.

#This Python code uses the time and pyautogui libraries to automate the process of closing unused tabs 
#in a web browser. The main function, close_unused_tabs, takes an optional argument num_tabs_to_keep
#which specifies the number of tabs to keep open, with a default value of 5.

#The code starts by pressing the 'Alt+Tab' hotkey to switch to the next application window, 
#assuming that a web browser is open and active. It then sleeps for 10 seconds, giving the browser time 
#to respond.

#Next, it enters a loop that runs num_tabs_to_keep - 1 times. Inside the loop, it presses 'Ctrl+W', 
#which is a common keyboard shortcut for closing the current tab in many web browsers. After closing 
#a tab, it sleeps for another 10 seconds, allowing time for the tab to close and the browser to respond 
#before moving on to the next iteration of the loop.





