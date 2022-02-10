import pandas as pd
import glob
import os

try:
    path = r'C:\Users\Janan\Desktop\MDLZ\Absenteeism project'
    files = glob.glob(os.path.join(path, "*.csv"))