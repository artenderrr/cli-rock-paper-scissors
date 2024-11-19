from curses import wrapper
from handlers import *

def init_colors():
    curses.init_pair(8, 240, -1) # gray
    curses.init_pair(9, 124, -1) # red
    curses.init_pair(10, curses.COLOR_WHITE, -1) # white with no background
    curses.init_pair(11, 118, -1) # green
    curses.init_pair(12, 220, -1) # yellow

def init(stdscr):
    curses.use_default_colors()
    curses.curs_set(False)
    init_colors()
    stdscr.nodelay(True)
    stdscr.clear()

def main(stdscr):
    init(stdscr)
    stage = "greeting"
    while stage:
        if stage == "greeting":
            stage = handle_greeting_stage(stdscr)
        elif stage == "choice":
            player_choice = handle_choice_stage(stdscr)
            stage = "results" if player_choice else None
        elif stage == "results":
            stage = handle_results_stage(stdscr, player_choice)

wrapper(main)