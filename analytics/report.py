class Report:
    def __init__(self, analyser, saver):
        self.analyser = analyser      # USES-A DataAnalyser
        self.saver = saver            # USES-A ResultSaver

    def generate(self):
        print("Generating report...")
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.save_json()
        print("Report complete.")