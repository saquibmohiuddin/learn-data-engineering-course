import logging
import pandas as pd

e_commerce_data = "./instructor_resources/1_python2/data/data.csv"

df = pd.read_csv(e_commerce_data)


logging.basicConfig(filename='./2_python_for_data_engineers/data/reading_csvs.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


