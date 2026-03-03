import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from abc import ABC,abstractmethod
class Analysis(ABC):
    def __init__(self):
        super().__init__()
    def calculate(self,category,file_path):
        pass
    def show_graph(self,category,file_path):
        pass
class Rates(Analysis):
    def calculate(self,category,file_path):


