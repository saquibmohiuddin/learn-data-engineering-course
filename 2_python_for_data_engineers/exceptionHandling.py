import pandas as pd

e_commerce_data = "./instructor_resources/1_python2/data/data.csv"
fake_path = "../instructor_resources/1_python2/data/fake_data.csv"

try:
    data = pd.read_csv(fake_path)
except:
    print("File not found")

try:
    data = pd.read_csv(fake_path)
except FileNotFoundError as error:
    print(f"{error}, please provide correct path to the file")


class FileTooLargeError(Exception):
    """Raised when the file is too large"""
    def __init__(self, number_of_rows):
        self.number_of_rows = number_of_rows
        self.message = f"File has {number_of_rows} rows, which is too large"
        super().__init__(self.message)


try:
    data = pd.read_csv(e_commerce_data)
    number_of_rows = len(data)
    if number_of_rows > 1000:
        raise FileTooLargeError(number_of_rows)
except FileNotFoundError as error:
    print(f"{error}, please provide correct path to the file")

