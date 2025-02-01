import logging
import pandas as pd

e_commerce_data = "./instructor_resources/1_python2/data/data.csv"

df = pd.read_csv(e_commerce_data)


logging.basicConfig(filename='./2_python_for_data_engineers/data/reading_csvs.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def is_positive(number):
    logging.debug(f"Checking if {number} is positive")
    if number > 0:
        logging.info(f"{number} is positive")
        return True
    else:
        logging.error(f"{number} is not positive")
        return False
    

quantities = df['Quantity'].to_list()

# writing error log, and writing information to log file
for quantity in quantities:
    is_positive(quantity)