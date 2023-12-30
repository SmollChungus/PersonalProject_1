import time
import threading
#from sound_module import _play_sound_thread, play_sound
from helpers import send_com



class PomodoroTimerCurse:
    def __init__(self, session_service, achievement_service, stdscr, is_working=True, work_duration=25, short_break_duration=5, long_break_duration=30):  # assuming you want to count seconds
        self.work_duration = work_duration
        self.short_break_duration = short_break_duration
        self.long_break_duration = long_break_duration
        self.is_running = False
        self.is_working = is_working
        self.session_count = 0
        self.timer_seconds = work_duration*60  
        self.timer_thread = None
        self.session_service = session_service
        self.achievement_service = achievement_service
        self.stdscr = stdscr

    def run_timer(self):
        while self.is_running:
            self.update()
            time.sleep(1) 

    def start(self):
        if not self.is_running:
            send_com("Timer started        ") 
            #_play_sound_thread("assets/audio/chimes_2.wav", stdscr=self.stdscr)
            self.is_running = True
            if self.timer_thread is None or not self.timer_thread.is_alive():
                self.timer_thread = threading.Thread(target=self.run_timer, daemon=True)  # daemon=True will allow the program to exit even if thread is running
                self.timer_thread.start()
        else:
            send_com("Already running!     ") 
    
    def pause(self):
        # Pause the timer
        self.is_running = False
        send_com("Timer Paused!        ")
        
        

    def reset(self):
        self.is_running = False
        self.is_working = True
        self.timer_seconds = self.work_duration*60
        send_com("Timer Reset!         ")
    
    def update(self):
        if self.is_running:
            self.timer_seconds -= 1
            if self.timer_seconds <= 0:
                self.is_running = False
                self.achievement_service.check_achievements(self.stdscr)  
                self.achievement_service.save_achievements()
                # if from working:
                if self.is_working == True:
                    
                    self.is_working = False
                    self.session_count += 1
                    self.session_service.increment_work_timers()
                    if self.session_count % 4 == 0:
                        send_com("Long break!          ")
                        self.timer_seconds = self.long_break_duration*60
                    else:
                        send_com("Short break!         ")
                        self.timer_seconds = self.short_break_duration*60
                # if from breaking:
                else:
                    send_com("Back to work!        ")
                    self.is_working = True
                    self.timer_seconds = self.work_duration*60
                    
                
                
                
                
                