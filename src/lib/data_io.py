import os

import pandas as pd

from lib.constants import DATA_DIR


def load_raw_data():
    return pd.read_csv(os.path.join(DATA_DIR, "raw/ObesityDataSet_raw_and_data_sinthetic.csv"))


def load_cleaned_data():
    return pd.read_csv(os.path.join(DATA_DIR, "processed/cleaned_data.csv"))


def load_encoded_data():
    return pd.read_csv(os.path.join(DATA_DIR, "processed/encoded_data.csv"))
