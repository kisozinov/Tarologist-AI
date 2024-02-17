from datasets import load_dataset
import pandas as pd

def get_dataset():
    dataset = pd.read_csv("data/tarot_readings.csv")
    
    return dataset