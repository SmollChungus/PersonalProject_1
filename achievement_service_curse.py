# achievement_service_curse.py, to not mess with print based terminal ui
from models.achievement import Achievement
import json
from datetime import datetime
import curses

class AchievementServiceCurse:
    def __init__(self, session_service):
        self.session_service = session_service
        self.achievements = [
            Achievement(
                "Stierheid Tier 1",
                "Complete 5 work cycles in a session",
                lambda: self.session_service.work_timers_finished >= 5,
                1
            ),
            Achievement(
                "Stierheid Tier 2",
                "Complete 8 work cycles in a session",
                lambda: self.session_service.work_timers_finished >= 8,
                2
            ),
            Achievement(
                "Stierheid Tier 3",
                "Complete 10 work cycles in a session",
                lambda: self.session_service.work_timers_finished >= 10,
                3
            ),
            Achievement(
                "Stierheid Tier 4",
                "Complete 12 work cycles in a session",
                lambda: self.session_service.work_timers_finished >= 12,
                4
            ),
            Achievement(
                "Stierheid Tier 5",
                "Complete 15 work cycles in a session",
                lambda: self.session_service.work_timers_finished >= 15,
                5
            ),
            Achievement(
                "Consistency Tier 1",
                "Work for 5 days in a row",
                lambda: self.check_five_day_streak(5),
                1
            ),
            Achievement(
                "Consistency Tier 2",
                "Work for 7 days in a row",
                lambda: self.check_five_day_streak(7),
                2
            ),
            Achievement(
                "Dedicated Tier 1",
                "Complete 10 total work sessions",
                lambda: self.check_sessions_completed(10),
                1
            ),
            Achievement(
                "Dedicated Tier 2",
                "Complete 20 total work sessions",
                lambda: self.check_sessions_completed(20),
                2
            ),
            Achievement(
                "Dedicated Tier 3",
                "Complete 30 total work sessions",
                lambda: self.check_sessions_completed(30),
                3
            ),
            Achievement(
                "Dedicated Tier 4",
                "Complete 40 total work sessions",
                lambda: self.check_sessions_completed(40),
                4
            ),
            Achievement(
                "Dedicated Tier 5",
                "Complete 50 total work sessions",
                lambda: self.check_sessions_completed(50),
                5
            )
        ]
        self.load_achievements()

    def check_five_day_streak(self, days):
        sessions = self.session_service.load_sessions()

        if len(sessions) < days:
            return False

        unique_days = []
        for i in range(len(sessions)-1, -1, -1):
            date = datetime.strptime(sessions[i]['session_date'], "%d/%m/%Y").date()
            if date not in unique_days:
                unique_days.append(date)

            if len(unique_days) >= days:
                for j in range(days-1, 0, -1):
                    if (unique_days[j] - unique_days[j-1]).days > 1:
                        return False
                return True

        return False
  

    def check_sessions_completed(self, sessions):
        return self.session_service.get_total_work_timers() >= sessions

    def check_achievements(self, stdscr):
        for achievement in self.achievements:
            if not achievement.unlocked and achievement.criteria():
                achievement.unlocked = True
                stdscr.addstr(20, 0, f"Achievement unlocked: {achievement.name}\n")

    def print_unlocked_achievements(self, stdscr):
        line = 12
        stdscr.addstr(line-3, 37, f"*******************************", curses.color_pair(6))
        stdscr.addstr(line-2, 37, f"*|~~~~~~~~Achievements~~~~~~~|*", curses.color_pair(6))
        stdscr.addstr(line-1, 37, f"*|===========================|*", curses.color_pair(6))
        for achievement in self.achievements:
            if achievement.unlocked:
                if "workaholic" in achievement.name.lower():
                    stdscr.addstr(line, 37, f"*| {achievement.name}         |*", curses.color_pair(6))
                elif "consistency" in achievement.name.lower():
                    stdscr.addstr(line, 37, f"*| {achievement.name}        |*", curses.color_pair(6))
                elif "dedicated" in achievement.name.lower():
                    stdscr.addstr(line, 37, f"*| {achievement.name}          |*", curses.color_pair(6))
                line += 1
        stdscr.addstr(line, 37, f"*|===========================|*", curses.color_pair(6))
        stdscr.addstr(line+1, 37, f"*******************************", curses.color_pair(6))
        stdscr.move(line+2, 37)
        stdscr.clrtoeol()
        stdscr.move(line+3, 37)
        stdscr.clrtoeol()
        stdscr.move(line+4, 37)
        stdscr.clrtoeol()
        stdscr.move(line+5, 37)
        stdscr.clrtoeol()
        stdscr.move(line+6, 37)
        stdscr.clrtoeol()
        stdscr.refresh()

    def save_achievements(self, ):
        achievements_data = [
            {
                'name': achievement.name,
                'description': achievement.description,
                'unlocked': achievement.unlocked
            }
            for achievement in self.achievements
        ]
        with open('achievements.json', 'w') as f:
            json.dump(achievements_data, f)

    def load_achievements(self):
        try:
            with open('achievements.json', 'r') as f:
                achievements_data = json.load(f)
                for achievement_data in achievements_data:
                    for achievement in self.achievements:
                        if achievement.name == achievement_data['name']:
                            achievement.unlocked = achievement_data['unlocked']
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error: The file 'achievements.json' is empty or not properly formatted.")

    def get_achievement_count(self, stdscr):
        counter = 0
        try:
            with open('achievements.json', 'r') as f:
                achievements_data = json.load(f)
                for achievement in self.achievements:
                    if achievement.unlocked == True:
                        counter += 1
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error: The file 'achievements.json' is empty or not properly formatted.")
        
        return counter
        
