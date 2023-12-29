#sound_module.py - needs implementation
#import pygame
#import threading
#import curses
#from curses import wrapper, napms

#def play_sound(file_path, stdscr):
    
    #stdscr.refresh()            
    # Create and start a new thread to play the sound
    #sound_thread = threading.Thread(target=_play_sound_thread, args=(file_path, stdscr), daemon=True)
    #sound_thread.start()

#def _play_sound_thread(file_path, stdscr):
    #counter = 0
    #counter += 1
    #stdscr.addstr(19, 0, f"Starting _play_sound_thread with file_path: {file_path} and counter: {counter}")
    #stdscr.refresh()
    #try:
        #sound = pygame.mixer.Sound(file_path)  # Load the sound file into a Sound object
        #stdscr.addstr(20, 0, f"Sound file loaded")
        #stdscr.refresh()
        #sound.play()  # Play the sound
        #stdscr.addstr(21, 0, f"Sound playing")
        #stdscr.refresh()
        #while pygame.mixer.get_busy():  # Check if any Sound objects are still playing
            #stdscr.addstr(22, 0, f"Sound is busy")
            #stdscr.refresh()
            #return    
    #except Exception as e:
        #stdscr.addstr(23, 0, f"An error occurred: {e}")
        #stdscr.refresh()    