import time
import random
import curses
from constants import *

def render_greeting_stage(stdscr):
    try:
        curses.update_lines_cols()
        stdscr.clear()
        greeting = "Welcome to Rock/Paper/Scissors game!"
        info = "Press Enter to continue. At any time - to quit, press q."
        stdscr.addstr(
            curses.LINES // 2,
            curses.COLS // 2 - len(greeting) // 2,
            greeting
        )
        stdscr.addstr(
            curses.LINES - 1,
            curses.COLS // 2 - len(info) // 2,
            info,
            curses.color_pair(8)
        )
        stdscr.refresh()
    except:
        stdscr.clear()
        stdscr.addstr(0, 0, "This window is too small! Please stretch it a bit.", curses.color_pair(9))
    
def render_choice_stage(stdscr, current_choice):
    try:
        curses.update_lines_cols()
        stdscr.clear()
        info = "   Make a choice!"
        stdscr.addstr(
            0,
            curses.COLS // 2 - len(info) // 2,
            info,
            curses.color_pair(8)
        )
        for i in range(len(CHOICES)):
            stdscr.addstr(
            curses.LINES // 2 + (i - len(CHOICES) // 2),
            curses.COLS // 2 - len(CHOICES[i]) // 2,
            ("> " if current_choice == CHOICES[i] else "  ") + CHOICES[i],
            curses.color_pair(10 if current_choice == CHOICES[i] else 8)
        )
        stdscr.refresh()
    except:
        stdscr.clear()
        stdscr.addstr(0, 0, "This window is too small! Please stretch it a bit.", curses.color_pair(9))

def render_player_choice(stdscr, player_choice):
    start = time.time()
    sleep_time = 1.5
    while time.time() - start < sleep_time:
        try:
            key = stdscr.getch()
            if key == ord("q"):
                return None
            curses.update_lines_cols()
            stdscr.clear()
            player_choice_info = "You have chosen "
            stdscr.addstr(
                curses.LINES // 2,
                curses.COLS // 2 - (len(player_choice_info) + len(player_choice) + 1) // 2,
                player_choice_info
            )
            stdscr.addstr(f"{player_choice}", curses.A_BOLD)
            stdscr.addstr("!")
            stdscr.refresh()
        except:
            stdscr.clear()
            stdscr.addstr(0, 0, "This window is too small! Please stretch it a bit.", curses.color_pair(9))
    return "ai_wait"

def render_wait(stdscr, *, message, afterstage):
    start = time.time()
    sleep_time = 3
    while time.time() - start < sleep_time:
        try:
            key = stdscr.getch()
            if key == ord("q"):
                return None
            curses.update_lines_cols()
            stdscr.clear()
            dots_amount = round((time.time() - start) // 0.75)
            ai_wait_info = message + "." * dots_amount
            stdscr.addstr(
                curses.LINES // 2,
                curses.COLS // 2 - (len(ai_wait_info) - dots_amount + 3) // 2,
                ai_wait_info
            )
            stdscr.refresh()
        except:
            stdscr.clear()
            stdscr.addstr(0, 0, "This window is too small! Please stretch it a bit.", curses.color_pair(9))
    return afterstage

def get_final_results(player_choice):
    ai_choice = random.choice(CHOICES)
    if RULES[player_choice] == ai_choice:
        return "You've won!", 11, ai_choice
    elif RULES[ai_choice] == player_choice:
        return "You've lost!", 9, ai_choice
    return "That's a draw!", 12, ai_choice

def render_final_results(stdscr, player_choice):
    final_result, color_id, ai_choice = get_final_results(player_choice)
    while True:
        key = stdscr.getch()
        if key == ord("q"):
            return None
        elif key == KEY_ENTER:
            return "start_new_game"
        try:
            curses.update_lines_cols()
            stdscr.clear()
            stdscr.addstr(
                curses.LINES // 2,
                curses.COLS // 2 - len(final_result) // 2,
                final_result,
                curses.color_pair(color_id)
            )
            ai_choice_info = f"AI choice was {ai_choice}!"
            stdscr.addstr(
                curses.LINES // 2 + 1,
                curses.COLS // 2 - len(ai_choice_info) // 2,
                ai_choice_info,
                curses.color_pair(8)
            )
            new_game_info = "Press Enter to play again! If you're done, smash q."
            stdscr.addstr(
                curses.LINES - 1,
                curses.COLS // 2 - len(new_game_info) // 2,
                new_game_info,
                curses.color_pair(8)
            )
        except:
            stdscr.clear()
            stdscr.addstr(0, 0, "This window is too small! Please stretch it a bit.", curses.color_pair(9))