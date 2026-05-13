import os


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
        else:
            print(f"File not found: {self.filename}")

    def create_output_folder(self):
        if not os.path.exists('output'):
            os.makedirs('output')
            print("Output folder created.")
        else:
            print("Output folder already exists.")