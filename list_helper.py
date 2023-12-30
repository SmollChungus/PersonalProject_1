import os
import json
from helpers import send_com

class ListHelper:
    def write_json_file(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.write_json_file({'items': []})

    def read_json_file(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        return data

    def add_item(self, item):
        data = self.read_json_file()
        data['items'].append(item)
        self.write_json_file(data)

    def remove_item(self, item):
        data = self.read_json_file()
        if item in data['items']:
            data['items'].remove(item)
            self.write_json_file(data)
        else:
            send_com(f"Item '{item}' not found in the list.")