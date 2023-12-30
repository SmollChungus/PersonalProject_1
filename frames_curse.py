import curses
from helpers import get_com, send_com
import os
from list_helper import ListHelper


class FramesCurse ():
    def __init__ (self, stdscr, timer_curse, achievement_service_curse, session_service, list_helper, current_list_item=0, list_menu_items=["New List", "Edit List", "Delete List", "Return"]):
        self.session_service = session_service
        self.stdscr = stdscr
        self.timer_curse = timer_curse
        self.timer_curse.is_running = timer_curse.is_running
        self.achievement_service_curse = achievement_service_curse
        self.current_list_item = current_list_item
        self.list_menu_items = list_menu_items
        self.list_helper = list_helper
        self.is_deleting_list = False
    def curse_achievement_frame (self): 
        pass # actual achievement service used is in achievement_service_curse.py, yeah i know

    def curse_timer_frame (self):
        minutes, seconds = divmod(self.timer_curse.timer_seconds, 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.stdscr.move(2,37)
        self.stdscr.addstr(0, 37, f"*******************************", curses.color_pair(2))
        self.stdscr.addstr(1, 37, f"*|~~~~~~~~~~~~Timer~~~~~~~~~~|*", curses.color_pair(2))
        self.stdscr.addstr(2, 37, f"*|===========================|*", curses.color_pair(2))
        self.stdscr.addstr(3, 37, f"*| Time remaining   : {time_str}  |*"  , curses.color_pair(2))
        self.stdscr.addstr(4, 37, f"*| Finished sessions: {self.timer_curse.session_count}      |*", curses.color_pair(2))
        if self.timer_curse.is_working == True:
            self.stdscr.addstr(5, 37, f"*| Working          : Yes    |*", curses.color_pair(2))
        else:
            self.stdscr.addstr(5, 37, f"*| Working          : No     |*", curses.color_pair(2))
        self.stdscr.addstr(6, 37, f"*|===========================|*", curses.color_pair(2))
        self.stdscr.addstr(7, 37, f"*******************************", curses.color_pair(2))

    def curse_statistics_frame (self):
        self.stdscr.move(9,37)
        self.stdscr.addstr(9, 37, f"*******************************", curses.color_pair(5))
        self.stdscr.addstr(10, 37, f"*|~~~~~~~~~Statistics~~~~~~~~|*", curses.color_pair(5))
        self.stdscr.addstr(11, 37, f"*|===========================|*", curses.color_pair(5))
        if self.session_service.get_total_work_timers() < 10:
            self.stdscr.addstr(12, 37, f"*| Total sessions : {self.session_service.get_total_work_timers()}        |*", curses.color_pair(5))
        elif self.session_service.get_total_work_timers() < 100:
            self.stdscr.addstr(12, 37, f"*| Total sessions : {self.session_service.get_total_work_timers()}       |*", curses.color_pair(5))
        elif self.session_service.get_total_work_timers() < 1000:
            self.stdscr.addstr(12, 37, f"*| Total sessions : {self.session_service.get_total_work_timers()}      |*", curses.color_pair(5))
        if self.session_service.get_total_work_timers() * self.timer_curse.work_duration < 10:
            self.stdscr.addstr(13, 37, f"*| Total work time: {self.session_service.get_total_work_timers() * self.timer_curse.work_duration} min    |*", curses.color_pair(5))
        elif self.session_service.get_total_work_timers() * self.timer_curse.work_duration < 100:
            self.stdscr.addstr(13, 37, f"*| Total work time: {self.session_service.get_total_work_timers() * self.timer_curse.work_duration} min   |*", curses.color_pair(5))
        elif self.session_service.get_total_work_timers() * self.timer_curse.work_duration < 1000:
            self.stdscr.addstr(13, 37, f"*| Total work time: {self.session_service.get_total_work_timers() * self.timer_curse.work_duration} min  |*", curses.color_pair(5))
        elif self.session_service.get_total_work_timers() * self.timer_curse.work_duration < 10000:
            self.stdscr.addstr(13, 37, f"*| Total work time: {self.session_service.get_total_work_timers() * self.timer_curse.work_duration} min |*", curses.color_pair(5))
        if self.achievement_service_curse.get_achievement_count(self.stdscr) < 10:
            self.stdscr.addstr(14, 37, f"*| Achievements   : {self.achievement_service_curse.get_achievement_count(self.stdscr)}        |*" , curses.color_pair(5))
        elif self.achievement_service_curse.get_achievement_count(self.stdscr) < 100:
            self.stdscr.addstr(14, 37, f"*| Achievements    : {self.achievement_service_curse.get_achievement_count(self.stdscr)}      |*" , curses.color_pair(5))
        self.stdscr.addstr(15, 37, f"*|===========================|*" , curses.color_pair(5))
        self.stdscr.addstr(16, 37, f"*******************************", curses.color_pair(5))
        self.stdscr.move(17,37)
        self.stdscr.clrtoeol()
        self.stdscr.move(18,37)
        self.stdscr.clrtoeol()
        self.stdscr.move(19,37)
        self.stdscr.clrtoeol()
        self.stdscr.move(20,37)
        self.stdscr.clrtoeol()
        self.stdscr.move(21,37)
        self.stdscr.clrtoeol()
        self.stdscr.move(22,37)
        self.stdscr.clrtoeol()
        self.stdscr.move(23,37)
        self.stdscr.clrtoeol()
        self.stdscr.refresh()

    # More mess
    #def curse_menu_frame(self, current_item=0):
    #    self.stdscr.addstr(0, 0, f"************************************", curses.color_pair(1))
    #    self.stdscr.addstr(1, 0, f"*|~~~~~~~~~~~~~~Menu~~~~~~~~~~~~~~|*", curses.color_pair(1))
    #    self.stdscr.addstr(2, 0, f"*|================================|*", curses.color_pair(1))
    #    for i, item in enumerate(self.menu_items):
    #        if i == current_item:
    #            self.stdscr.addstr(i+3, 0, f"*| {i+1}. {item:<24}    |*", curses.A_REVERSE)  # Highlight the current item
    #        else:
    #            self.stdscr.addstr(i+3, 0, f"*| {i+1}. {item:<24}    |*", curses.color_pair(i+2))
    #    self.stdscr.addstr(i+4, 0, f"*|================================|*", curses.color_pair(1))
    #   self.stdscr.addstr(i+5, 0, f"************************************", curses.color_pair(1))

    def curse_com_frame (self):
        com_value = get_com(self.stdscr) or " " * 21
        i,j = 0,69
        self.stdscr.move(i, j)
        self.stdscr.addstr(i, j, f"*******************************", curses.color_pair(1))
        self.stdscr.addstr(i+1, j, f"*|~~~~~~~~~~~COM~~~~~~~~~~~~~|*", curses.color_pair(1))
        self.stdscr.addstr(i+2, j, f"*|===========================|*", curses.color_pair(1))
        self.stdscr.addstr(i+3, j, f"*| Sys: {com_value}|*", curses.color_pair(1))
        self.stdscr.addstr(i+4, j, f"*|===========================|*", curses.color_pair(1))
        self.stdscr.addstr(i+5, j, f"*******************************", curses.color_pair(1))
        self.stdscr.refresh()

    def curse_status_frame(self):
        if self.timer_curse.is_working == True:
            self.stdscr.move(13, 0)
            i = 12
            self.stdscr.addstr(i, 0, f"***********************************")
            self.stdscr.addstr(i+1, 0, f"*|~~~~~~~~~~~~~Status~~~~~~~~~~~~|*")
            self.stdscr.addstr(i+2, 0, f"*|==============WORK=============|*")
            self.stdscr.addstr(i+3, 0, f"*|   _.--._  _.--._              |*")
            self.stdscr.addstr(i+4, 0, f"*|\\\\:;:;:;:;:;\\:;:;:;:;:\\        |*")
            self.stdscr.addstr(i+5, 0, f"*| \\\\:;:;:;:;:;\\:;:;:;:;:\\       |*")
            self.stdscr.addstr(i+6, 0, f"*|  \\\\:;:;:;:;:;\\:;:;:;:;:\\      |*")
            self.stdscr.addstr(i+7, 0, f"*|   \\\\:;:;:;:;:;\\;::;:;:;:\\     |*")
            self.stdscr.addstr(i+8, 0, f"*|    \\\\:;:;::;:;:\\;:;:;::;:\\    |*")
            self.stdscr.addstr(i+9, 0, f"*|     \\\\:;:;:_:--:\\_:--:_;:;\\   |*")
            self.stdscr.addstr(i+10, 0, f"*|      \\\\_.-\"      :      \"._\\  |*")
            self.stdscr.addstr(i+11, 0, f"*|       \`_..--\"\"--.;.--\"\"-._=> |*")
            self.stdscr.addstr(i+12, 0, f"*|===============================|*")
            self.stdscr.addstr(i+13, 0, f"***********************************")
            self.stdscr.refresh()
        elif self.timer_curse.is_working == False:
            self.stdscr.move(11, 0)
            i = 12
            self.stdscr.addstr(i, 0, f" ***********************************", curses.color_pair(3))
            self.stdscr.addstr(i+1, 0, f" *|~~~~~~~~~~~~~Status~~~~~~~~~~~~|*", curses.color_pair(3))
            self.stdscr.addstr(i+2, 0, f" *|=============BREAK=============|*", curses.color_pair(3))
            self.stdscr.addstr(i+3, 0, f" *|                _'*            |*", curses.color_pair(3))
            self.stdscr.addstr(i+4, 0, f" *|              -'               |*", curses.color_pair(3))
            self.stdscr.addstr(i+5, 0, f" *|                     ;,'       |*", curses.color_pair(3))
            self.stdscr.addstr(i+6, 0, f" *|              _;,'             |*"   , curses.color_pair(3))
            self.stdscr.addstr(i+7, 0, f" *|     _o_    ;:;'               |*", curses.color_pair(3))
            self.stdscr.addstr(i+8, 0, f" *| ,-.'---`.__ ;                 |*", curses.color_pair(3))
            self.stdscr.addstr(i+9, 0, f" *|((j`=====',-'                  |*", curses.color_pair(3))
            self.stdscr.addstr(i+10, 0, f" *| `-\     /                     |*", curses.color_pair(3))
            self.stdscr.addstr(i+11, 0, f" *|    `-=-'                      |*", curses.color_pair(3))
            self.stdscr.addstr(i+12, 0, f" *|===============================|*", curses.color_pair(3))
            self.stdscr.addstr(i+13, 0, f" ***********************************", curses.color_pair(3))
            self.stdscr.refresh()

    def curse_list_frame(self):
        i, j = 0, 101
        self.stdscr.move(i, j)
        # Get the list of items
        data = self.list_helper.read_json_file()
        items = data['items']


        # Define the starting and ending lines for the list
        start_line = 4
        end_line = 36

        # Print each item in the list, but don't exceed the frame size
        line = start_line

        self.stdscr.addstr(i, j, f"***************************************************************************", curses.color_pair(4))
        self.stdscr.addstr(i+1, j, f"*|~~~~~~~~~~~~~List~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|*", curses.color_pair(4))
        self.stdscr.addstr(i+2, j, f"*|=======================================================================|*", curses.color_pair(4))
        self.stdscr.addstr(i+3, j, f"*| ##################################################################### |*", curses.color_pair(4))
        if not self.is_deleting_list:
            for index, item in enumerate(items, start=1):
                # Split the item into lines
                item_lines = item.split('\n')

                for line_index, item_line in enumerate(item_lines):
                    if line > end_line:
                        break
                    # Print the index only for the first line of each item
                    if line_index == 0:
                        if len(item_lines) != 1:
                            self.stdscr.addstr(i+line, j, f"*| {index}) {item_line: <65} |*", curses.color_pair(4))
                        else:
                            self.stdscr.addstr(i+line, j, f"*| {index}) {item_line: <65} |* \n", curses.color_pair(4))
                    elif line_index == len(item_lines) - 1:
                        self.stdscr.addstr(i+line, j, f"*|     {item_line: <65} |*", curses.color_pair(4))
                    else:
                        self.stdscr.addstr(i+line, j, f"*|     {item_line: <65} |* \n,", curses.color_pair(4))
                    line += 1
                    self.stdscr.addstr(line+2, j, f"*|=======================================================================|*", curses.color_pair(4))
                    self.stdscr.addstr(line+1, j, f"***************************************************************************", curses.color_pair(4))
        elif self.is_deleting_list:
            for index, item in enumerate(items, start=1):
                if line == self.selected_item_index + 4:
                    # Highlight the selected item
                    self.stdscr.attron(curses.color_pair(1))
                    self.stdscr.addstr(i+line, j, f"*| {index}) {item_line: <65} |*", curses.color_pair(4))
                    self.stdscr.attroff(curses.color_pair(1))
                    # Save the selected item index
                    deleting_item_index = index - 1
                else:
                    self.stdscr.addstr(i+line, j, f"*| {index}) {item_line: <65} |*", curses.color_pair(4))


            self.stdscr.addstr(line+1, j, f"*|=======================================================================|*", curses.color_pair(4))
            self.stdscr.addstr(line+2, j, f"***************************************************************************", curses.color_pair(4))
            self.stdscr.move(0, 0)
            self.stdscr.refresh()



    def curse_navigation_frame(self):
        i, j = 7, 69
        self.list_menu_items = ["New List", "Edit List", "Delete List", "Return"]
        
        self.stdscr.move(i, j)
        self.stdscr.addstr(i, j, f"******************************", curses.color_pair(1))
        self.stdscr.addstr(i+1, j, f"*|~~~~~Submenu~Navigation~~~|*", curses.color_pair(1))
        self.stdscr.addstr(i+2, j, f"*|==========================|*", curses.color_pair(1))
        for k, item in enumerate(self.list_menu_items):
            # Format the item string to be 20 characters long, padded with spaces if necessary
            item_str = f"{k+1}. {item:<20}"
            if k == self.current_list_item:
                self.stdscr.addstr(i+3, j, f"*| {item_str} |*", curses.A_REVERSE)
                i += 1
            else:
                self.stdscr.addstr(i+3, j, f"*| {item_str} |*", curses.color_pair(k+2)) 
                i +=1
        
        self.stdscr.addstr(i+4, j, f"*|==========================|*", curses.color_pair(1))
        self.stdscr.addstr(i+5, j, f"******************************", curses.color_pair(1))
        # If the user chooses "Return", clear the submenu
        if self.current_list_item == len(self.list_menu_items) - 1 and self.stdscr.getch() == ord('\n'):
            for line in range(i, i+6):
                self.stdscr.move(line, j)
                self.stdscr.clrtoeol()

        self.stdscr.refresh()

