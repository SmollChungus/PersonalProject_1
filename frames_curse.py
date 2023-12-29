import curses
from helpers import get_com, send_com

class FramesCurse ():
    def __init__ (self, stdscr, timer_curse, achievement_service_curse, session_service):
        self.session_service = session_service
        self.stdscr = stdscr
        self.timer_curse = timer_curse
        self.timer_curse.is_running = timer_curse.is_running
        self.achievement_service_curse = achievement_service_curse

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
        self.stdscr.move(0, 72)
        self.stdscr.addstr(0, 72, f"*******************************", curses.color_pair(1))
        self.stdscr.addstr(1, 72, f"*|~~~~~~~~~~~COM~~~~~~~~~~~~~|*", curses.color_pair(1))
        self.stdscr.addstr(2, 72, f"*|===========================|*", curses.color_pair(1))
        self.stdscr.addstr(3, 72, f"*| Sys: {com_value}|*", curses.color_pair(1))
        self.stdscr.addstr(4, 72, f"*|===========================|*", curses.color_pair(1))
        self.stdscr.addstr(5, 72, f"*******************************", curses.color_pair(1))
        self.stdscr.refresh()

    def curse_status_frame(self):
        if self.timer_curse.is_working == True:
            self.stdscr.move(13, 0)
            self.stdscr.addstr(13, 0, f"***********************************")
            self.stdscr.addstr(14, 0, f"*|~~~~~~~~~~~~~Status~~~~~~~~~~~~|*")
            self.stdscr.addstr(15, 0, f"*|==============WORK=============|*")
            self.stdscr.addstr(16, 0, f"*|   _.--._  _.--._              |*")
            self.stdscr.addstr(17, 0, f"*|\\\\:;:;:;:;:;\\:;:;:;:;:\\        |*")
            self.stdscr.addstr(18, 0, f"*| \\\\:;:;:;:;:;\\:;:;:;:;:\\       |*")
            self.stdscr.addstr(19, 0, f"*|  \\\\:;:;:;:;:;\\:;:;:;:;:\\      |*")
            self.stdscr.addstr(20, 0, f"*|   \\\\:;:;:;:;:;\\;::;:;:;:\\     |*")
            self.stdscr.addstr(21, 0, f"*|    \\\\:;:;::;:;:\\;:;:;::;:\\    |*")
            self.stdscr.addstr(22, 0, f"*|     \\\\:;:;:_:--:\\_:--:_;:;\\   |*")
            self.stdscr.addstr(23, 0, f"*|      \\\\_.-\"      :      \"._\\  |*")
            self.stdscr.addstr(24, 0, f"*|       \`_..--\"\"--.;.--\"\"-.._=>|*")
            self.stdscr.addstr(25, 0, f"*|===============================|*")
            self.stdscr.addstr(26, 0, f"***********************************")
            self.stdscr.refresh()
        elif self.timer_curse.is_working == False:
            self.stdscr.move(11, 0)

            self.stdscr.addstr(11, 0, f" ***********************************", curses.color_pair(3))
            self.stdscr.addstr(12, 0, f" *|~~~~~~~~~~~~~Status~~~~~~~~~~~~|*", curses.color_pair(3))
            self.stdscr.addstr(13, 0, f" *|=============BREAK=============|*", curses.color_pair(3))
            self.stdscr.addstr(14, 0, f" *|                _'*            |*", curses.color_pair(3))
            self.stdscr.addstr(15, 0, f" *|              -'               |*", curses.color_pair(3))
            self.stdscr.addstr(16, 0, f" *|                     ;,'       |*", curses.color_pair(3))
            self.stdscr.addstr(17, 0, f" *|              _;,'             |*"   , curses.color_pair(3))
            self.stdscr.addstr(18, 0, f" *|     _o_    ;:;'               |*", curses.color_pair(3))
            self.stdscr.addstr(19, 0, f" *| ,-.'---`.__ ;                 |*", curses.color_pair(3))
            self.stdscr.addstr(20, 0, f" *|((j`=====',-'                  |*", curses.color_pair(3))
            self.stdscr.addstr(21, 0, f" *| `-\     /                     |*", curses.color_pair(3))
            self.stdscr.addstr(22, 0, f" *|    `-=-'                      |*", curses.color_pair(3))
            self.stdscr.addstr(23, 0, f" *|===============================|*", curses.color_pair(3))
            self.stdscr.addstr(24, 0, f" ***********************************", curses.color_pair(3))
            self.stdscr.refresh()

    def curse_list_frame(self):
        send_com("List loaded!         ")
        self.stdscr.move(7,72)
        self.stdscr.addstr(7, 72, f"***********************************", curses.color_pair(4))
        self.stdscr.addstr(8, 72, f"*|~~~~~~~~~~~~~List~~~~~~~~~~~~~~|*", curses.color_pair(4))
        self.stdscr.addstr(9, 72, f"*|===============================|*", curses.color_pair(4))
        self.stdscr.addstr(10, 72, f"*| ############################# |*", curses.color_pair(4))
        self.stdscr.addstr(11, 72, f"*| 1) List item one              |*", curses.color_pair(4))
        self.stdscr.addstr(12, 72, f"*| 2) You can + or - items       |*", curses.color_pair(4))
        self.stdscr.addstr(13, 72, f"*| 3) Future implementation:     |*", curses.color_pair(4))
        self.stdscr.addstr(14, 72, f"*|    - Sound on events          |*", curses.color_pair(4))
        self.stdscr.addstr(15, 72, f"*|    - Animated UI elements     |*", curses.color_pair(4))
        self.stdscr.addstr(16, 72, f"*|    - List function            |*", curses.color_pair(4))
        self.stdscr.addstr(17, 72, f"*|    - Bugfixes (:              |*", curses.color_pair(4))
        self.stdscr.addstr(18, 72, f"*| 4) Main take-aways:           |*", curses.color_pair(4))
        self.stdscr.addstr(19, 72, f"*|    - Stay consistent in with  |*", curses.color_pair(4))
        self.stdscr.addstr(20, 72, f"*|        file management        |*", curses.color_pair(4))
        self.stdscr.addstr(21, 72, f"*|    - Dont waste too much time |*", curses.color_pair(4))
        self.stdscr.addstr(22, 72, f"*|        on a stupid curses UI  |*", curses.color_pair(4))
        self.stdscr.addstr(23, 72, f"*|===============================|*", curses.color_pair(4))
        self.stdscr.addstr(24, 72, f"***********************************", curses.color_pair(4))
        
