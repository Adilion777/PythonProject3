import os
import csv
import json

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder="output"):
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
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.students = [row for row in reader]
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
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
        low_sleep_gpas  = []
        high_sleep_gpas = []

        for student in self.students:
            try:
                sleep = float(student["sleep_hours"])
                gpa   = float(student["GPA"])
                if sleep < 6:
                    low_sleep_gpas.append(gpa)
                else:
                    high_sleep_gpas.append(gpa)
            except ValueError:
                print(f"Warning: could not convert value for student {student.get('student_id', '?')} — skipping row.")
                continue

        avg_low    = round(sum(low_sleep_gpas)  / len(low_sleep_gpas),  2)
        avg_high   = round(sum(high_sleep_gpas) / len(high_sleep_gpas), 2)
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
        print(f"Students sleeping < 6 hours : {self.result['low_sleep']['students']} avg GPA: {self.result['low_sleep']['avg_gpa']}")
        print(f"Students sleeping >= 6 hours : {self.result['high_sleep']['students']} avg GPA: {self.result['high_sleep']['avg_gpa']}")
        print(f"GPA difference : {self.result['gpa_difference']}")
        print("----------------------------")


class ResultSaver:
    def __init__(self, result, filepath):
        self.result   = result
        self.filepath = filepath

    def save_json(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.result, f, indent=4)
        print()
        print(f"Result saved to {self.filepath}")


fm = FileManager("students.csv")
if not fm.check_file():
    print("Stopping program.")
    exit()
fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()