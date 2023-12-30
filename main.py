#curses_ui.py
import curses
from curses import wrapper, napms
from list_helper import ListHelper
from services.session_service import SessionService
from achievement_service_curse import AchievementServiceCurse
from pomodoro_timer_curse import PomodoroTimerCurse
from frames_curse import FramesCurse
from helpers import send_com

list_helper = ListHelper('list_items.json')

def main(stdscr):
    height, width = stdscr.getmaxyx()
    session_service = SessionService()
    achievement_service_curse = AchievementServiceCurse(session_service)
    timer_curse = PomodoroTimerCurse(session_service, achievement_service_curse, stdscr)
    frames_curse = FramesCurse(stdscr, timer_curse, achievement_service_curse, session_service, list_helper)
    stdscr.refresh()
    stdscr.keypad(True)
    curses.cbreak()
    current_item = 0
    browsing_menu = True
    browsing_list = False
    browsing_list_item = False
    is_deleting_list = False
    selected_item_index = 0

    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) 
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK) 
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK) 
        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)  
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK) 
        curses.init_pair(8, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(0)  # Hide the cursor


    # Check if the terminal is large enough
    if height < 26 or width < 90:
        stdscr.clear()
        stdscr.addstr(0, 15, "~~~ Terminal Frame Too Small! ^_^ ~~~",)
        stdscr.addstr(1, 15, "~~~ Please resize your terminal. ~~~",)
        stdscr.addstr(2, 15, "~~~ Press any key to exit       ~~~",)    
        stdscr.addstr(3, 15, "~~~ Terminating in 10 seconds  ~~~",)
        stdscr.refresh()
        if stdscr.getch():
            return
        napms(5000)
        return
    this_session = session_service.create_session()
    achievement_service_curse.check_achievements(stdscr) 
    achievement_service_curse.save_achievements() 

    stdscr.nodelay(True)  # Make getch() non-blocking
    

    
    menu_items = ["Start Timer", "Pause Timer", "Reset Timer", "Statistics", "Achievements", "*List", "Exit"]
    current_item = 0

    while True:
        stdscr.addstr(20, 40, f'menu: {browsing_menu} list: {browsing_list}')
        stdscr.addstr(21, 40, f'item: {frames_curse.current_list_item}')
        stdscr.addstr(22, 40, f'is_deleting_list: {frames_curse.is_deleting_list}')
        stdscr.addstr(23, 40, f'selected_item_index: {selected_item_index}')
        frames_curse.curse_status_frame()
        stdscr.refresh()
        frames_curse.curse_timer_frame()
        frames_curse.curse_com_frame()
        stdscr.refresh()
        frames_curse.curse_list_frame()
        stdscr.refresh()
        stdscr.addstr(0, 0, f"************************************", curses.color_pair(1))
        stdscr.addstr(1, 0, f"*|~~~~~~~~~~~~~~Menu~~~~~~~~~~~~~~|*", curses.color_pair(2))
        stdscr.addstr(2, 0, f"*|================================|*", curses.color_pair(3))
        for i, item in enumerate(menu_items):
            # Format the item string to be 20 characters long, padded with spaces if necessary
            item_str = f"{i+1}. {item:<27}"
            if i == current_item:
                stdscr.addstr(i+3, 0, f"*| {item_str} |*", curses.A_REVERSE)
            else:
                stdscr.addstr(i+3, 0, f"*| {item_str} |*", curses.color_pair(i+2)) 
        stdscr.addstr(i+4, 0, f"*|================================|*", curses.color_pair(3))
        stdscr.addstr(i+5, 0, f"************************************", curses.color_pair(1))      

        # Wait for user input
        key = stdscr.getch()

        # Navigate the menu
        if browsing_menu and key != -1:
            if key == curses.KEY_UP and current_item > 0:
                current_item -= 1
            elif key == curses.KEY_DOWN and current_item < len(menu_items) - 1:
                current_item += 1
            elif key in [ord(str(i)) for i in range(1, len(menu_items) + 1)]:
                current_item = key - ord('1')
            elif key == ord('\n'):  
                if current_item == 0:
                    timer_curse.start()
                elif current_item == 1:
                    timer_curse.pause()
                    stdscr.refresh()
                elif current_item == 2:
                    timer_curse.reset()
                    stdscr.refresh()
                elif current_item == 3:
                    frames_curse.curse_statistics_frame()
                    stdscr.refresh()
                    send_com("Statistics loaded!   ")
                elif current_item == 4:
                    achievement_service_curse.print_unlocked_achievements(stdscr)
                    send_com("Achievements loaded! ")
                    stdscr.refresh()
                elif current_item == 5:
                    
                    browsing_menu = False
                    browsing_list = True
                    frames_curse.curse_navigation_frame()
                    stdscr.refresh()
                    key = None
                elif current_item == 6:
                    break
        
            stdscr.move(0,0)
            napms(50)  # Pause for 100 milliseconds
        
        if browsing_list:
            selected_item_index = None
            frames_curse.curse_navigation_frame()
            stdscr.refresh()
            if key == curses.KEY_UP and frames_curse.current_list_item > 0:
                frames_curse.current_list_item -= 1
            elif key == curses.KEY_DOWN and frames_curse.current_list_item < len(frames_curse.list_menu_items) - 1:
                frames_curse.current_list_item += 1
            elif key in [ord(str(i)) for i in range(1, len(frames_curse.list_menu_items) + 1)]:
                frames_curse.current_list_item = key - ord('1')
            elif key == ord('\n'):  
                if frames_curse.current_list_item == 0:
                    send_com("New List Created!    ")
                    # Get the new item from the user
                    stdscr.addstr(21, 40, "Enter the new item: ")
                    stdscr.refresh()
                    new_item = stdscr.getstr().decode('utf-8')
                    # Add the new item to the list
                    list_helper.add_item(new_item)
                elif frames_curse.current_list_item == 1:
                    send_com("Editing Lists!       ")
                    # Get the item to edit from the user
                    stdscr.addstr(40, 21, "Enter the item to edit: ")
                    stdscr.refresh()
                    old_item = stdscr.getstr().decode('utf-8')
                    stdscr.addstr(40, 21, "Enter the new item: ")
                    stdscr.refresh()
                    new_item = stdscr.getstr().decode('utf-8')
                    # Remove the old item from the list and add the new item
                    list_helper.remove_item(old_item)
                    list_helper.add_item(new_item)
                elif frames_curse.current_list_item == 2:
                    frames_curse.is_deleting_list = True
                    frames_curse.browsing_list = False
                    send_com("Deleting Lists!      ")
                    deleting_item_index = 1
                    # Remove the selected item from the list
                    if deleting_item_index is not None:
                        items = list_helper.read_json_file()['items']
                        item_to_remove = items[deleting_item_index]
                        list_helper.remove_item(item_to_remove)
                    frames_curse.is_deleting_list = False

                elif frames_curse.current_list_item == 3:
                    send_com("Returning to Menu!   ")
                    browsing_menu = True
                    browsing_list = False
                    
                    key = -1
            if browsing_list == False:
                stdscr.clear()
            stdscr.move(0,0)
            
            stdscr.refresh()
    napms(50)
wrapper(main)