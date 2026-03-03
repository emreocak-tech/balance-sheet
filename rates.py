import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from abc import ABC,abstractmethod
from dotenv import load_dotenv
load_dotenv()
import os
from google.genai import types
from google import genai
gemini_api=os.getenv("GOOGLE_GEMINI")
class AbstractCurrentRatio(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calculate(self,df,category,tarih="2025/12"):
        pass
    @abstractmethod
    def show_graph(self,df,category,tarih=["2025/12","2025/9","2025/6","2025/3"]):
        pass
    @abstractmethod
    def analysis_gemini(self,df,category):
        pass
class CurrentRatio(AbstractCurrentRatio):
    def calculate(self,df,category,tarih="2025/12"):
        donen_varlıklar=df[tarih][1]
        kısa_vadeli_yükümlülükler=df[tarih][31]
        cari_oran_değeri=donen_varlıklar/kısa_vadeli_yükümlülükler
        print(f"Şirketin Cari Oran Değeri : {cari_oran_değeri}")
        return [cari_oran_değeri,category]
    def show_graph(self,df,category,tarih=["2025/12","2025/9","2025/6","2025/3"]):
        current_ratio=[]
        donen_varlıklar=df[tarih[0]][1]
        kısa_vadeli_yükümlülükler=df[tarih[0]][31]
        cari_oran_değeri=donen_varlıklar/kısa_vadeli_yükümlülükler
        current_ratio.append(cari_oran_değeri)

        donen_varlıklar2=df[tarih[1]][1]
        kısa_vadeli_yükümlülükler2=df[tarih[1]][31]
        cari_oran_değeri2=donen_varlıklar2/kısa_vadeli_yükümlülükler2
        current_ratio.append(cari_oran_değeri2)


        donen_varlıklar3=df[tarih[2]][1]
        kısa_vadeli_yükümlülükler3=df[tarih[2]][31]
        cari_oran_değeri3=donen_varlıklar3/kısa_vadeli_yükümlülükler3
        current_ratio.append(cari_oran_değeri3)


        donen_varlıklar4=df[tarih[3]][1]
        kısa_vadeli_yükümlülükler4=df[tarih[3]][31]
        cari_oran_değeri4=donen_varlıklar4/kısa_vadeli_yükümlülükler4
        current_ratio.append(cari_oran_değeri4)

        plt.plot(tarih,current_ratio,color="Black",linewidth=4,label="Cari Oran")
        plt.xlabel("Zaman(Günümüzden Geçmişe)",color="Black",fontsize=18)
        plt.ylabel("Değerler",color="Black",fontsize=18)
        plt.title("Şirketin Cari Oran Değerinin Zamana Göre Değişimi",color="Black",fontsize=20)
        plt.grid(True)
        plt.legend()
        return plt

    def analysis_gemini(self,df,category):
        try:
            client=genai.Client(api_key=gemini_api)
            response=client.models.generate_content(model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=f"You are an quant trader and you want to explain basically what user said."),contents=f"Sen finansal danışmanlık hizmeti veren bir şirketin en üst düzey ve en profesyonel çalışanısın.Karşındaki kişi ise şirketlerin finansal tablolarını okumakta zorlanan küçük yatırımcı kitlesi.Sen şirketin cari oran değerlerine bakarak yatırımcıya şirketi anlatıyorsun : {df.head(100)} ,Yatırım yapılıp yapılmayacağını anlatıp bu değerin sektördeki rakip şirketlere göre konumunu gösteriyorsun.Şirketin sektörü ise {category}.Titiz ve profesyonel ol.Sana verdiğim dosyada bütün değerlere ulaşabilirsin sütunları dikkatli incele sana verdiğim dosyada KISA VADELİ YÜKÜMLÜLÜKLER kısmı da var!")
            return response.text
        except ConnectionError as c_error:
            print(f"Internet connection error : {c_error}")
        except Exception as except_error:
            print(f"General Error : {except_error}")
class AbstractFinancialLeverage(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calculate(self,df,category,tarih="2025/12"):
        pass
    @abstractmethod
    def show_financial_leverage(self,df,category,tarih=["2025/12","2025/9","2025/6","2025/3"]):
        pass
    @abstractmethod
    def analysis_gemini(self,df,category):
        pass
class FinancialLeverage(AbstractFinancialLeverage):
    def calculate(self,df,category,tarih="2025/12"):
        toplam_borc=df[tarih][31]+df[tarih][45]
        ozsermaye_orani=df[tarih][58]
        financial_leverage=toplam_borc/ozsermaye_orani
        return financial_leverage
    def show_financial_leverage(self,df,category,tarih=["2025/12","2025/9","2025/6","2025/3"]):
        plt.clf()
        finansal_kaldirac_list=[]

        toplam_borc = df[tarih[0]][31] + df[tarih[0]][45]
        ozsermaye_orani = df[tarih[0]][58]
        finansal_kaldirac = toplam_borc / ozsermaye_orani
        finansal_kaldirac_list.append(finansal_kaldirac)

        toplam_borc2 = df[tarih[1]][31] + df[tarih[1]][45]
        ozsermaye_orani2 = df[tarih[1]][58]
        finansal_kaldirac2 = toplam_borc2 / ozsermaye_orani2
        finansal_kaldirac_list.append(finansal_kaldirac2)

        toplam_borc3 = df[tarih[2]][31] + df[tarih[2]][45]
        ozsermaye_orani3 = df[tarih[2]][58]
        finansal_kaldirac3 = toplam_borc3 / ozsermaye_orani3
        finansal_kaldirac_list.append(finansal_kaldirac3)

        toplam_borc4 = df[tarih[3]][31] + df[tarih[3]][45]
        ozsermaye_orani4 = df[tarih[3]][58]
        finansal_kaldirac4 = toplam_borc4 / ozsermaye_orani4
        finansal_kaldirac_list.append(finansal_kaldirac4)

        plt.plot(tarih,finansal_kaldirac_list,color="Black",linewidth=3,label="Finansal Kaldıraç Oranı")
        plt.xlabel("Zaman(Günümüzden Geçmişe)",color="Black",fontsize=18)
        plt.ylabel("Değerler",color="Black",fontsize=18)
        plt.title("Şirketin Finansal Kaldıraç Oranının Zamana Göre Değişimi",color="Black",fontsize=20)
        plt.grid()
        plt.legend()
        return plt
    def analysis_gemini(self,df,category):
        try:
            client=genai.Client(api_key=gemini_api)
            response=client.models.generate_content(model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=f"You are an quant trader and you want to explain basically what user said."),contents=f"Sen finansal danışmanlık hizmeti veren bir şirketin en üst düzey ve en profesyonel çalışanısın.Karşındaki kişi ise şirketlerin finansal tablolarını okumakta zorlanan küçük yatırımcı kitlesi.Sen şirketin finansal kaldıraç değerlerine bakarak yatırımcıya şirketi anlatıyorsun : {df.head(100)} ,Yatırım yapılıp yapılmayacağını anlatıp bu değerin sektördeki rakip şirketlere göre konumunu gösteriyorsun.Şirketin sektörü ise {category}.Titiz ve profesyonel ol.Sana verdiğim dosyada bütün değerlere ulaşabilirsin sütunları dikkatli incele")
            return response.text
        except ConnectionError as c_error:
            print(f"Internet connection error : {c_error}")
        except Exception as except_error:
            print(f"General Error : {except_error}")

class AbstractROE(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calculate(self,df,category,tarih):
        pass
    @abstractmethod
    def show_graph(self,df,category,tarih):
        pass
    @abstractmethod
    def gemini_analysis(self,df,category,tarih):
        pass
class ROE(AbstractROE):
    def calculate(self,df,category,tarih="2025/12"):
        net_kar = df[tarih][67]
        ozsermaye = df[tarih][58]
        roe_değeri = (net_kar / ozsermaye) * 1000
        return roe_değeri
    def show_graph(self,df,category,tarih=["2025/12","2025/9","2025/6","2025/3"]):
        plt.clf()

        roe_list=[]

        net_kar = df[tarih[0]][67]
        ozsermaye = df[tarih[0]][58]
        roe_değeri = (net_kar / ozsermaye) * 1000
        roe_list.append(roe_değeri)

        net_kar2 = df[tarih[1]][67]
        ozsermaye2 = df[tarih[1]][58]
        roe_değeri2 = (net_kar2 / ozsermaye2) * 1000
        roe_list.append(roe_değeri2)

        net_kar3 = df[tarih[2]][67]
        ozsermaye3 = df[tarih[2]][58]
        roe_değeri3 = (net_kar3 / ozsermaye3) * 1000
        roe_list.append(roe_değeri3)

        net_kar4 = df[tarih[3]][67]
        ozsermaye4 = df[tarih[3]][58]
        roe_değeri4 = (net_kar4 / ozsermaye4) * 1000
        roe_list.append(roe_değeri4)

        plt.plot(tarih,roe_list,color="Black",linewidth=4,label="ROE Oranı")
        plt.xlabel("Zaman(Günümüzden Geçmişe Doğru)",color="Black",fontsize=18)
        plt.ylabel("Değerler",color="Black",fontsize=18)
        plt.title("ROE Oranının Zamana Göre Değişimi",fontsize=20)
        plt.grid()
        plt.legend()
        return plt
    def gemini_analysis(self,df,category,tarih="2025/12"):
        try:
            client=genai.Client(api_key=gemini_api)
            response=client.models.generate_content(model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=f"You are an quant trader and you want to explain basically what user said."),contents=f"Sen finansal danışmanlık hizmeti veren bir şirketin en üst düzey ve en profesyonel çalışanısın.Karşındaki kişi ise şirketlerin finansal tablolarını okumakta zorlanan küçük yatırımcı kitlesi.Sen şirketin ROE değerlerine bakarak yatırımcıya şirketi anlatıyorsun : {df.head(100)} ,Yatırım yapılıp yapılmayacağını anlatıp bu değerin sektördeki rakip şirketlere göre konumunu gösteriyorsun.Şirketin sektörü ise {category}.Titiz ve profesyonel ol.Sana verdiğim dosyada bütün değerlere ulaşabilirsin sütunları dikkatli incele")
            return response.text
        except ConnectionError as c_error:
            print(f"Internet connection error : {c_error}")
        except Exception as except_error:
            print(f"General Error : {except_error}")
