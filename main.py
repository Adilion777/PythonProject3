import os
import csv
import json
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if not os.path.exists(self.filename):
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False
        print(f"File found: {self.filename}")
        return True

    def create_output_folder(self, folder='output'):
        print()
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print()
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = [row for row in reader]
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
        except Exception as e:
            print(f"Error: {e}")
        return self.students

    def preview(self, n=5):
        print()
        print(f"First {n} rows:")
        print("----------------------------")
        for student in self.students[:n]:
            print(f"{student['student_id']} | {student['age']} | {student['gender']} | {student['country']} | GPA: {student['GPA']}")
        print("----------------------------")


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        # lambda filter
        low_sleep_students  = list(filter(lambda s: float(s['sleep_hours']) < 6,  self.students))
        high_sleep_students = list(filter(lambda s: float(s['sleep_hours']) >= 6, self.students))

        # lambda map
        low_sleep_gpas  = list(map(lambda s: float(s['GPA']), low_sleep_students))
        high_sleep_gpas = list(map(lambda s: float(s['GPA']), high_sleep_students))

        avg_low  = round(sum(low_sleep_gpas)  / len(low_sleep_gpas),  2)
        avg_high = round(sum(high_sleep_gpas) / len(high_sleep_gpas), 2)
        difference = round(avg_high - avg_low, 2)

        self.result = {
            "analysis": "Sleep vs GPA",
            "total_students": len(self.students),
            "low_sleep":  {"students": len(low_sleep_gpas),  "avg_gpa": avg_low},
            "high_sleep": {"students": len(high_sleep_gpas), "avg_gpa": avg_high},
            "gpa_difference": difference
        }
        return self.result

    def print_results(self):
        print()
        print("----------------------------")
        print("Sleep vs GPA Analysis")
        print("----------------------------")
        print(f"Students sleeping < 6 hours : {self.result['low_sleep']['students']} "
              f"avg GPA: {self.result['low_sleep']['avg_gpa']}")
        print(f"Students sleeping >= 6 hours : {self.result['high_sleep']['students']} "
              f"avg GPA: {self.result['high_sleep']['avg_gpa']}")
        print(f"GPA difference : {self.result['gpa_difference']}")
        print("----------------------------")



class ResultSaver:
    def __init__(self, result, filepath):
        self.result = result
        self.filepath = filepath

    def save_json(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, indent=4)
        print()
        print(f"Result saved to {self.filepath}")











fm = FileManager('students.csv')
if not fm.check_file():
    print('Stopping program.')
    exit()
fm.create_output_folder()

dl = DataLoader('students.csv')
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()