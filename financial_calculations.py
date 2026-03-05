import math
from abc import ABC,abstractmethod
import matplotlib.pyplot as plt
class AbstractMonthlyBudgetCalculator(ABC):
    def __init__(self):
        super().__init__()
    def calculate(self,salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure):
        pass
    def show_graph(self,salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure):
        pass
class MonthlyBudgetCalculator(AbstractMonthlyBudgetCalculator):
    def calculate(self,salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure):
        total_income=salary+retirement_salary+other_salaries
        total_expense=credit+total_tax+invoice+expenditure
        return [total_income-total_expense,total_income,total_expense]
    def show_graph(self,salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure):
        plt.clf()
        x_labels=["Maaşınız","BES","Diğer Birikimleriniz","Kredi Maliyetiniz","Ödenen Vergi","Faturalar","Harcamalar"]
        y_labels=[salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure]
        plt.bar(x_labels,y_labels,color="Black",linewidth=4,label="Değerler")
        plt.xlabel("Bilgiler",fontsize=18,color="Black")
        plt.ylabel("Değerler",fontsize=18,color="Black")
        plt.title("Bütçe Grafiği",color="Black",fontsize=20)
        plt.grid()
        return plt


