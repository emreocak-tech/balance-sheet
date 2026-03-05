from abc import ABC,abstractmethod
import matplotlib.pyplot as plt
class AbstractMonthlyBudgetCalculator(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calculate(self,salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure):
        pass
    @abstractmethod
    def show_graph(self,salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure):
        pass
class MonthlyBudgetCalculator(AbstractMonthlyBudgetCalculator):
    def calculate(self,salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure):
        total_income=salary+retirement_salary+other_salaries
        total_expense=credit+total_tax+invoice+expenditure
        return [total_income-total_expense,total_income,total_expense]
    def show_graph(self,salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure):
        plt.clf()
        x_labels=["Maaşınız","BES","Diğer Gelirler","Kredi Maliyeti","Vergi","Faturalar","Harcamalar"]
        y_labels=[salary,retirement_salary,other_salaries,credit,total_tax,invoice,expenditure]
        plt.bar(x_labels,y_labels,color="Black",linewidth=4,label="Değerler")
        plt.xlabel("Bilgiler",fontsize=18,color="Black")
        plt.ylabel("Değerler",fontsize=18,color="Black")
        plt.title("Bütçe Grafiği",color="Black",fontsize=20)
        plt.grid()
        return plt
class AbstractDepositRate(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calculate(self,capital,day,rate,time_coefficient):
        pass
    @abstractmethod
    def show_graph(self,capital,day,rate,time_coefficient):
        pass
class DepositRate(AbstractDepositRate):
    def calculate(self,capital,day,rate,time_coefficient):
        time_coefficient=int(time_coefficient)
        total_income=(capital*rate*day)/time_coefficient
        return [total_income,capital+total_income]
    def show_graph(self,capital,day,rate,time_coefficient):
        plt.clf()
        time_coefficient=int(time_coefficient)
        total_income = (capital * rate * day) / time_coefficient
        plt.bar(["Ana Para","Toplam Tutar"],[capital,total_income+capital],color="Black",linewidth=3)
        plt.xlabel("Bilgiler",fontsize=18,color="Black")
        plt.ylabel("Değerler",fontsize=18,color="Black")
        plt.title("Ana Para vs Mevduat Faizi",fontsize=20,color="Black")
        plt.grid(True)
        return plt
class AbstractBES(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calculate(self,min_age,max_age,annual_contribution,annual_yield,capital):
        pass
    @abstractmethod
    def show_graph(self,min_age,max_age,annual_contribution,annual_yield,capital):
        pass
class BES(AbstractBES):
    def calculate(self,min_age,max_age,annual_contribution,annual_yield,capital):
        total_balance = 0
        time = max_age - min_age
        current_year_payment = capital
        for year in range(time):
            this_year_deposit = current_year_payment * 1.30
            total_balance += this_year_deposit
            total_balance = total_balance * (1 + annual_yield)
            current_year_payment = current_year_payment * (1 + annual_contribution)
        return total_balance
    def show_graph(self,min_age,max_age,annual_contribution,annual_yield,capital):
        plt.clf()
        total_balance = 0
        time = max_age - min_age
        current_year_payment = capital
        for year in range(time):
            this_year_deposit = current_year_payment * 1.30
            total_balance += this_year_deposit
            total_balance = total_balance * (1 + annual_yield)
            current_year_payment = current_year_payment * (1 + annual_contribution)
        plt.bar(["BES Kullanmamış Olsaydınız","BES Kullandığınız Zaman"],[capital*(max_age-min_age),total_balance],color="Black",linewidth=3)
        plt.xlabel("Bilgiler",fontsize=18,color="Black")
        plt.ylabel("Değerler",fontsize=18,color="Black")
        plt.title("BES Değerlendirme",fontsize=20,color="Black")
        plt.grid(True)
        return plt



