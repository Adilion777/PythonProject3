import csv


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        with open(self.filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.students = [row for row in reader]
        print(f"Loaded {len(self.students)} students.")

    def preview(self):
        print("Preview (first 3 students):")
        for student in self.students[:3]:
            print(student)