#python -m streamlit run ui.py
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from Gemini import Utils
import pandas as pd
import numpy as np
from rates import CurrentRatio
from rates import FinancialLeverage
from rates import ROE
util=Utils()
st.title("**Kullanıcı Sözleşmesi**")
check_box=st.checkbox("UYARI: **Lütfen Okuyunuz !** Bu uygulama yalnızca bilgilendirme amaçlıdır ve yatırım tavsiyesi içermez.- Finansal piyasalarda işlem yapmak yüksek risk içerir ve sermaye kaybına yol açabilir.- Sağlanan tahminler ve analizler kesin sonuç vermez, yanılabilir.- Alacağınız tüm yatırım kararlarının sorumluluğu tamamen size aittir.- Uygulama geliştiricisi, kullanımdan kaynaklanan herhangi bir zarardan sorumlu değildir.- Yatırım kararı vermeden önce profesyonel bir finansal danışmana başvurmanız önerilir.")
if check_box:
    st.header("Kullanıcı Sözleşmesi Kabul Edildi!")
    asd1,asd2,asd3,asd4=st.sidebar.tabs(["Hakkında","Bilgiler","Gemini Sohbet Botu","Döviz Kuru"])
    with asd1:
        st.write("İyi bir proje şimdilik")
    with asd2:
        st.write("Bilançoyu Analiz Etmemi Sağlıyor Bu Proje :)")
    with asd3:
        text=st.text_input("You can ask a question")
        buton=st.button("Gemini")
        if buton:
            response = util.gemini_entegration(text)
            st.write(response)
    with asd4:
        buton=st.button("Döviz Kuru",use_container_width=True)
        if buton:
            cevap=util.exchange_rate_api()
            st.write(f"Döviz Kuru : {cevap}")
    tab1,tab2,tab3=st.tabs(["Bilanço Analizi","Nasıl Bilanço Okurum ? ","Genel Finansal Hesaplamalar"])
    with tab1:
        category = st.selectbox("Şirketin Bulunduğu Sektörü Seçin",
                                options=["Enerji", "Finans", "Sağlık", "Sanayi", "Çelik", "İnşaat Malzemeleri",
                                         "Ham Madde",
                                         "Hizmet", "Tüketim", "Ulaşım", "İletişim", "Otomotiv", "Teknoloji", "Otel",
                                         "Gıda ve İçecek", "Yaşam", "Savunma", "Sigorta"])
        excel = st.file_uploader("You have to select Halkbank's balance sheet", type=['xlsx', 'xls'])
        if excel is not None:
            df = pd.read_excel(excel, engine='openpyxl')
            df.to_csv('file_path', index=False)
            try:
                current_ratio = CurrentRatio()
                result = current_ratio.calculate(df, category)
                st.info("Şirketin Cari Oran Değeri")
                buton = st.button("Current Ratio", use_container_width=True)
                if buton:
                    st.write(result[0])
                    st.write(result[1])
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

            try:
                current_ratio_graph = CurrentRatio()
                image = current_ratio_graph.show_graph(df, category)
                st.info("Şirketin Cari Oran Değerinin Zamana Göre Değişimi")
                buton = st.button("Cari Oranın Değişimi", use_container_width=True)
                if buton:
                    with st.spinner('Görsel Oluşturuluyor...') as spin:
                        image = current_ratio_graph.show_graph(df, category)
                        st.write(spin)
                        st.pyplot(image)
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

            try:
                st.info("Gemini ile Cari Oran Analizi")
                current_ratio_gemini = CurrentRatio()
                model = st.selectbox("Model Seçin", options=["gemini-3.1-pro-preview", "gemini-3-flash-preview",
                                                             "gemini-3.1-flash-lite-preview", "gemini-2.5-flash",
                                                             "gemini-2.5-flash-lite", "gemini-2.5-pro"])
                metin = current_ratio_gemini.analysis_gemini(df, category, model)
                buton = st.button("Gemini Cari Oran Analizi", use_container_width=True)
                if buton:
                    with st.spinner('Gemini Mesaj Üretiyor...') as spin:
                        st.write(spin)
                        st.write(metin)
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

            try:
                st.info("Finansal Kaldıraç Hesaplama")
                buton = st.button("Son Çeyrek Finansal Kaldıraç Oranı", use_container_width=True)
                financial_leverage = FinancialLeverage()
                if buton:
                    result = financial_leverage.calculate(df, category)
                    st.write(f"Finansal Kaldıraç Oranı : {result}")
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

            try:
                financial_leverage_graph = FinancialLeverage()
                st.info("Finansal Kaldıraç Zamana Göre Değişimi")
                buton_two = st.button("Finansal Kaldıraç Grafiği", use_container_width=True)
                if buton_two:
                    graph_leverage = financial_leverage_graph.show_financial_leverage(df, category)
                    st.pyplot(graph_leverage)
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

            try:
                st.info("Finansal Kaldıraç Oranının Gemini ile Analizi")
                model_two = st.selectbox("2.Modeli Seçin", options=["gemini-3.1-pro-preview", "gemini-3-flash-preview",
                                                                    "gemini-3.1-flash-lite-preview", "gemini-2.5-flash",
                                                                    "gemini-2.5-flash-lite", "gemini-2.5-pro"])
                buton = st.button("Finansal Kaldıraç Oranı ile Gemini Analizi", use_container_width=True)
                if buton:
                    cevap = FinancialLeverage()
                    cevap = cevap.analysis_gemini(df, category, model_two)
                    st.write(cevap)
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

            try:
                st.info("Son Çeyrek ROE Oranı")
                buton = st.button("ROE Oranı Hesapla", use_container_width=True)
                if buton:
                    roe = ROE()
                    sonuc = roe.calculate(df, category)
                    st.write(f"Şirketin ROE oranı {sonuc}")
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

            try:
                st.info("ROE Oranının Zamana Göre Değişimi")
                buton = st.button("ROE Grafiği", use_container_width=True)
                roe = ROE()
                if buton:
                    result = roe.show_graph(df, category)
                    st.pyplot(result)
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

            try:
                st.info("Gemini ile ROE Analizi")
                model_three = st.selectbox("3.Modeli Seçin",
                                           options=["gemini-3.1-pro-preview", "gemini-3-flash-preview",
                                                    "gemini-3.1-flash-lite-preview", "gemini-2.5-flash",
                                                    "gemini-2.5-flash-lite", "gemini-2.5-pro"])
                roe = ROE()
                buton = st.button("Gemini ile ROE Analizi", use_container_width=True)
                if buton:
                    text_two = roe.gemini_analysis(df, category, model_three)
                    st.write(text_two)
            except FileExistsError as fe_error:
                st.error(f"File Exist Error : {fe_error} , Try Again !")
            except FileNotFoundError as file_not_found_error:
                st.error(f"File was not found : {file_not_found_error}, Try Again !")
            except TimeoutError as time_error:
                st.error(f"Timeout Error , {time_error} , Try Again !")
            except ConnectionError as internet_error:
                st.error(f"Connection Error : {internet_error} , Try Again !")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")
    with tab2:
        st.title("**Nasıl Bilanço Okurum Sayfasına Hoşgeldiniz**")
        st.header("**Fiyat/Gelir Oranı**")
        st.info("Ne olduğu: Bir şirketin hisse senedi fiyatının, hisse başına net kârına bölünmesi.\nNe anlatır?Şirketin kaç yılda kendini amorti edeceğini gösterir.")
        st.header("**Fiyat/Satışlar Oranı**")
        st.info("Ne olduğu: Piyasa değerinin (fiyatın), şirketin toplam satışlarına (ciro)bölünmesi.Ne anlatır? Şirketin her bir birim satışına karşılık yatırımcıların ne kadar ödediğini gösterir.")
        st.header("**Fiyat/Nakit Akışı**")
        st.info("Hisse fiyatının, hisse başına nakit akışına bölünmesi. Nakit akışı,şirketin kasasına giren ve çıkan paradır (kâğıt üstündeki kârdan daha gerçekçidir). F/K gibidir ama kâr yerine nakde bakar.")
        st.header("**Fiyat/Serbest Nakit Akışı**")
        st.info("Hisse fiyatının, hisse başına serbest nakit akışına bölünmesi.Serbest nakit akışı, şirketin tüm giderlerini ve yatırımlarını yaptıktan sonra elindekalan 'gerçek' nakittir.")
        st.header("**Fiyat/Defter Değeri (F/DD)**")
        st.info("Hisse fiyatının, şirketin bir hisseye düşen özsermayesine (defter değeri) bölünmesi.Şirketin bilançodaki varlıklarının kaç katı fiyattan satıldığını gösterir.")
        st.header("**Fiyat/Maddi Defter Değeri**")
        st.info("Bir üstteki oranın (F/DD) aynısıdır, ancak şirketin 'şerefiye' (markadeğeri, patent gibi soyut varlıklar) gibi maddi olmayan duran varlıkları hesaptan çıkarılır.Sadece fiziksel varlıklara (bina, arsa, makine) bakarak şirketin değerini ölçer.")
    with tab3:
        st.title("**Finansal Hesaplamalar Sayfasına Hoşgeldiniz**")
        page1,page2,page3=st.tabs(["Aylık Bütçe Hesaplayıcı","Mevduat Faizi Hesaplama","Bireysel Emeklilik Birikim Hesaplama"])
        with page1:
            st.title("**Bütçe Hesaplama Sayfasına Hoşgeldiniz**")
            st.info("Gerekli bilgileri girerken lütfen aylık değerleri girin!")
            try:
                salary=st.number_input("**Maaşınızı giriniz**",min_value=1,max_value=1000000,value=1)
                bes=st.number_input("**BES Birikiminizi Giriniz**",min_value=1,max_value=10000,value=0)
                
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")

else:
    st.info("You have to accept contract")