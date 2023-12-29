import json
from datetime import datetime
import uuid

class SessionService:
    def __init__(self, file_name="sessions.json"):
        self.file_name = file_name
        self.session_id = None
        self.session_date = None
        self.work_timers_finished = 0

    def save_session(self, session_data, update=False):
        if update:
            with open(self.file_name, 'w') as file:
                json.dump(session_data, file, indent=4)
        else:
            try:
                data = self.load_statistics()
            except FileNotFoundError:
                data = []
            data.append(session_data)
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)

    def create_session(self):
        self.session_date = datetime.now().strftime("%d/%m/%Y")
        self.session_id = str(uuid.uuid4())
        self.session_data = {
            'session_id':  self.session_id,
            'work_timers_finished': self.work_timers_finished,
            'session_date': self.session_date
        }
        self.save_session(self.session_data, update=False)
        return self.session_data

    def load_statistics(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def update_session(self):
        data = self.load_statistics()
        if data:
            if data[-1]['session_id'] == self.session_id:
                data[-1]['work_timers_finished'] = self.work_timers_finished
        self.save_session(data, update=True)

    def increment_work_timers(self):
        self.work_timers_finished += 1
        self.update_session()

    def get_total_work_timers(self):
        data = self.load_statistics()
        total_work_timers = 0
        for session in data:
            total_work_timers += session['work_timers_finished']
        return total_work_timers
    
    # 
    def load_sessions(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []