#curses_ui.py
import curses
from curses import wrapper, napms
from services.session_service import SessionService
from achievement_service_curse import AchievementServiceCurse
from pomodoro_timer_curse import PomodoroTimerCurse
from frames_curse import FramesCurse
from helpers import send_com

def main(stdscr):
    height, width = stdscr.getmaxyx()
    session_service = SessionService()
    achievement_service_curse = AchievementServiceCurse(session_service)
    timer_curse = PomodoroTimerCurse(session_service, achievement_service_curse, stdscr)
    frames_curse = FramesCurse(stdscr, timer_curse, achievement_service_curse, session_service)
    stdscr.refresh()
    stdscr.keypad(True)
    curses.cbreak()
    current_item = 0

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

        frames_curse.curse_status_frame()
        frames_curse.curse_timer_frame()
        frames_curse.curse_com_frame()
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
        stdscr.addstr(10, 0, f"*|================================|*", curses.color_pair(3))
        stdscr.addstr(11, 0, f"************************************", curses.color_pair(1))      

        # Wait for user input
        key = stdscr.getch()

        # Navigate the menu
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
                frames_curse.curse_list_frame()
            elif current_item == 6:
                break
    
        stdscr.move(0,0)
        napms(50)  # Pause for 100 milliseconds

wrapper(main)