import pandas as pd

e_commerce_data = "../instructor_resources/1_python2/data/data.csv"
fake_path = "../instructor_resources/1_python2/data/fake_data.csv"


try:
    data = pd.read_csv(fake_path)
except:
    print("File not found")

