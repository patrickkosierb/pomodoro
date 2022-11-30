'''
Pomodoro Timer:

    Requirements:
    - Have a "Session" class for a new session
    - User input for the amount of time alloted for pomodoro session (30 min - 12 hours)
    - Ask what interval user wants breaks (30 min or 1 hour intervals : 5min or 10 min breaks *after 3 hours 30 min break) 
    - Start command
    - Display a timer on terminal 
    - Allow for user text input for random thoughts that get saved to a .txt file (have terminal clear after input)


'''


class Pomodoro:
    def __init__(self, total_time):
        self.total_time = total_time


session_length = input("How much time do you want to allocate to your Pomodoro session?\n")
session = Pomodoro(session_length)
