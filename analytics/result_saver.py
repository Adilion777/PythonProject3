import json
import os


class ResultSaver:
    def __init__(self, result, filepath):
        self.result = result
        self.filepath = filepath

    def save_json(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, indent=4)
        print(f"Result saved to {self.filepath}")