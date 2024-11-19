from renderers import *

def handle_greeting_stage(stdscr):
    while True:
        render_greeting_stage(stdscr)
        key = stdscr.getch()
        if key == ord("q"):
            return None
        elif key == KEY_ENTER:
            return "choice"

def handle_choice_stage(stdscr):
    current_choice = "Rock"
    while True:
        render_choice_stage(stdscr, current_choice)
        key = stdscr.getch()
        if key == ord("q"):
            return None
        elif key == curses.KEY_DOWN:
            current_choice = CHOICES[(CHOICES.index(current_choice) + 1) % len(CHOICES)]
        elif key == curses.KEY_UP:
            current_choice = CHOICES[(CHOICES.index(current_choice) - 1) % len(CHOICES)]
        elif key == KEY_ENTER:
            return current_choice
        
def handle_results_stage(stdscr, player_choice):
    results_stage = "player_choice"
    while results_stage not in (None, "start_new_game"):
        if results_stage == "player_choice":
            results_stage = render_player_choice(stdscr, player_choice)
        elif results_stage == "ai_wait":
            results_stage = render_wait(
                stdscr,
                message="Let's wait for an AI to make a choice",
                afterstage="final_wait"
            )
        elif results_stage == "final_wait":
            results_stage = render_wait(
                stdscr,
                message="And",
                afterstage="final_results"
            )
        elif results_stage == "final_results":
            results_stage = render_final_results(stdscr, player_choice)
    return "greeting" if results_stage == "start_new_game" else None