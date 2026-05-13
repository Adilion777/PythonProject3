from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import SleepAnalyser, GpaAnalyser


fm = FileManager('students.csv')
fm.check_file()
fm.create_output_folder()

dl = DataLoader('students.csv')
dl.load()
dl.preview()

# Task 5 — Polymorphism
analysers = [SleepAnalyser(dl.students), GpaAnalyser(dl.students)]

print('-' * 30)
print('Running all analysers:')
print('-' * 30)

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

# Task 4 — Report
saver = ResultSaver(analysers[0].result, 'output/result.json')
report = Report(analysers[0], saver)
report.generate()