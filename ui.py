from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from Gemini import Utils
import pandas as pd
from rates import CurrentRatio
from rates import FinancialLeverage
from rates import ROE
from financial_calculations import MonthlyBudgetCalculator
from financial_calculations import DepositRate
from financial_calculations import BES
util=Utils()
st.title("**Kullanıcı Sözleşmesi**")
check_box=st.checkbox("UYARI: **Lütfen Okuyunuz !** Bu uygulama yalnızca bilgilendirme amaçlıdır ve yatırım tavsiyesi içermez.- Finansal piyasalarda işlem yapmak yüksek risk içerir ve sermaye kaybına yol açabilir.- Sağlanan tahminler ve analizler kesin sonuç vermez, yanılabilir.- Alacağınız tüm yatırım kararlarının sorumluluğu tamamen size aittir.- Uygulama geliştiricisi, kullanımdan kaynaklanan herhangi bir zarardan sorumlu değildir.- Yatırım kararı vermeden önce profesyonel bir finansal danışmana başvurmanız önerilir.")
if check_box:
    st.header("Kullanıcı Sözleşmesi Kabul Edildi!")
    asd1,asd2,asd3,asd4=st.sidebar.tabs(["Hakkında","Bilgiler","Gemini Sohbet Botu","Döviz Kuru"])
    with asd1:
        st.write("""Günümüzde finansal verilere ulaşmak hiç olmadığı kadar kolay, ancak bu verileri doğru okumak ve anlamlandırmak özellikle küçük yatırımcılar için büyük bir zorluk teşkil ediyor. Bu proje, finansal okuryazarlığı artırmayı ve veriye dayalı daha bilinçli finansal kararlar almayı kolaylaştırmayı hedefler.Uygulama, iki temel ihtiyaca cevap vermek üzere tasarlanmıştır:1. Şirket Finansal Analizi (Kurumsal Modül):Kullanıcılar, bir şirketin (örneğin Halkbank) ham bilanço verilerini yükleyerek anında önemli finansal oranları hesaplayabilir. Bu modül sayesinde:Şirketin likidite durumu (Cari Oran) analiz edilir.Şirketin borçluluk düzeyi (Finansal Kaldıraç Oranı) incelenir.Şirketin ortaklarına sağladığı getiri (ROE - Özsermaye Kârlılığı) ölçülür.Tüm bu hesaplamalar, Google'ın Gemini yapay zeka modeli ile entegre edilerek kullanıcıya sade bir dille açıklanır. Yapay zeka, ilgili sektörü de dikkate alarak şirketin finansal durumu hakkında genel bir yorum sunar.2. Kişisel Finans Yönetimi (Bireysel Modül):Kullanıcıların kendi kişisel finanslarını yönetmelerine yardımcı olacak araçlar sunar:Aylık Bütçe Hesaplayıcı: Gelir ve giderlerinizi takip ederek aylık net durumunuzu hesaplar ve görselleştirir.Mevduat Faizi Hesaplayıcı: Ana para, vade ve faiz oranına göre mevduat getirisi hesaplar.BES (Bireysel Emeklilik Sistemi) Birikim Hesaplayıcı: Yaş, katkı payı ve yıllık getiri oranlarına göre emeklilik döneminde oluşacak birikimi projekte eder.Teknoloji ve Geliştirme:Proje, kullanıcı dostu bir arayüz için Streamlit ile geliştirilmiş olup, veri analizi için Pandas ve görselleştirme için Matplotlib kütüphanelerini kullanmaktadır. Gelişmiş dil modeli entegrasyonu ile kullanıcı deneyimi zenginleştirilmiştir. Proje sürekli geliştirilmekte olup, gelecekte yeni finansal oranlar ve analiz araçlarıyla genişletilmesi planlanmaktadır.""")
    with asd2:
        st.write("""📊 Proje Hakkında Teknik Bilgiler
Bu proje, finansal okuryazarlığı artırmak ve yatırımcıların şirket bilançolarını daha iyi anlamalarını sağlamak amacıyla geliştirilmiş çok modüllü bir finansal analiz uygulamasıdır.
🚀 Kullanılan Teknolojiler
Teknoloji	Kullanım Amacı
Python 3.11+	Ana programlama dili
Streamlit	Web arayüzü ve kullanıcı etkileşimi
Pandas	Bilanço verilerinin işlenmesi ve analizi
Matplotlib	Finansal grafiklerin oluşturulması
Google Gemini AI	Finansal oranların yapay zeka ile yorumlanması
ExchangeRate-API	Güncel döviz kuru bilgisi
OpenPyXL	Excel dosyalarının okunması
Python-dotenv	Çevre değişkenlerinin yönetimi

📁 Proje Yapısı ve Modüller
1. Bilanço Analiz Modülü (rates.py)
Cari Oran Analizi: Şirketin kısa vadeli borç ödeme gücünü ölçer

Finansal Kaldıraç: Şirketin borçluluk düzeyini analiz eder

ROE (Özsermaye Kârlılığı): Ortakların yatırım getirisini hesaplar

Çeyreklik bazda zamansal değişim grafikleri

Gemini AI ile sektörel karşılaştırmalı analiz

2. Kişisel Finans Modülü (financial_calculations.py)
Aylık Bütçe Hesaplayıcı: Gelir-gider takibi ve net durum analizi

Mevduat Faizi Hesaplama: Günlük, aylık ve yıllık faiz getirisi

BES Birikim Hesaplama: Emeklilik dönemi projeksiyonu

3. Yardımcı Araçlar (Gemini.py)
Gemini AI Entegrasyonu: Finansal yorumlama ve soru-cevap

Döviz Kuru API: Anlık USD/TRY kuru bilgisi


💡 Projenin Sunduğu Değerler
Karmaşık bilanço verilerini basit ve anlaşılır oranlara dönüştürür

Zamansal değişimleri görsel grafiklerle sunar

Yapay zeka desteği ile finansal terimleri ve oranları açıklar

Sektörel karşılaştırma imkanı sağlar

Kişisel finans yönetimi için pratik araçlar sunar



📌 Notlar
Bilanço analizi için Halkbank formatındaki Excel dosyaları kullanılmalıdır

Gemini AI analizleri için Google Gemini API anahtarı gereklidir

Döviz kuru bilgisi için ExchangeRate-API anahtarı gereklidir

Tüm hesaplamalar bilgilendirme amaçlıdır, yatırım tavsiyesi niteliği taşımaz




Versiyon: 1.0.0
Son Güncelleme: Mart 2026
Geliştirici: Emre Ocak

""")
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
            budget=MonthlyBudgetCalculator()
            st.title("**Bütçe Hesaplama Sayfasına Hoşgeldiniz**")
            st.success("**Gerekli bilgileri girerken lütfen aylık değerleri girin!**")
            try:
                st.info("Gelir Bilgisi")
                salary=st.number_input("**Maaşınızı giriniz**",min_value=1,max_value=1000000,value=1)
                bes=st.number_input("**BES Birikiminizi Giriniz**",min_value=1,max_value=10000,value=1)
                other_incomes=st.number_input("**Diğer Gelirlerinizi Giriniz**",min_value=1,max_value=10000,value=1)
                st.info("Gider Bilgisi")
                credit=st.number_input("**Aylık Kredi Ödemelerinizi Giriniz**",min_value=1,max_value=100000,value=1)
                total_tax=st.number_input("**Aylık Ödenen Vergi Miktarı**",min_value=1,max_value=10000,value=1)
                invoice=st.number_input("**Aylık Ödediğiniz Toplam Fatura**",min_value=1,max_value=10000,value=1)
                expenditure=st.number_input("**Aylık Keyfi Harcamalarınızı Giriniz**",min_value=1,max_value=10000,value=1)
                buton=st.button("Aylık Gelir ve Gider Bilginiz için Tıklayınız",use_container_width=True)
                if buton:
                    informations=budget.calculate(salary,bes,other_incomes,credit, total_tax, invoice, expenditure)
                    st.write(f"Aylık Net Durumunuz : {informations[0]}")
                    st.write(f"Aylık Toplam Geliriniz : {informations[1]}")
                    st.write(f"Aylık Toplam Gideriniz : {informations[2]}")
                buton_four=st.button("Görselleştirmek İsterseniz Tıklayın",use_container_width=True)
                if buton_four:
                    graph=budget.show_graph(salary,bes,other_incomes,credit, total_tax, invoice, expenditure)
                    st.pyplot(graph)
            except ValueError as v_error:
                st.error(f"Value Error : {v_error}, Please check the type of values!")
            except ConnectionError as c_error:
                st.error(f"Connection Error : {c_error}, Try Again!")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")
        with page2:
            st.title("**Mevduat Faizi Hesaplama Sayfasına Hoşgeldiniz**")
            st.info("**Gerekli Bilgileri Eksiksiz Bir Şekilde Doldurunuz**")
            st.info("**Zaman Katsayısı Paranızı Gün,Ay veya Yıllık Faize mi Koyduğunuzu Tanımlar**")
            deposit_rate=DepositRate()
            try:
                capital=st.number_input("**Ana Paranızı Giriniz**",min_value=1,max_value=100000,value=1)
                day=st.number_input("**Vade**",min_value=1,max_value=100000,value=1)
                rate=st.number_input("**Faiz Oranını Giriniz**",min_value=1,max_value=15,value=1)
                time_coefficient=st.selectbox("Zaman Katsayısını Giriniz",options=["36500","1200","100"])
                buton=st.button("Mevduat Faizi Hesapla",use_container_width=True)
                if buton:
                    result=deposit_rate.calculate(capital, day, rate, time_coefficient)
                    st.info("Vergi Kesilmemiş Hal Hesaplanmaktadır!")
                    st.write(f"Faizden Kazandığınız Para : {result[0]}")
                    st.write(f"Toplam Geliriniz : {result[1]}")
                buton_graph=st.button("Mevduat Faizi Görselleştirme",use_container_width=True)
                if buton_graph:
                    graph=deposit_rate.show_graph(capital, day, rate, time_coefficient)
                    st.pyplot(graph)
            except ValueError as v_error:
                st.error(f"Value Error : {v_error}, Please check the type of values!")
            except ConnectionError as c_error:
                st.error(f"Connection Error : {c_error}, Try Again!")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")
        with page3:
            st.title("BES Hesaplama Sayfasına Hoşgeldiniz")
            st.info("**Gerekli Bilgileri Eksiksiz Bir Şekilde Doldurmalısınız**")
            bes=BES()
            try:
                min_age = st.number_input("Şuanki Yaşınızı Giriniz", min_value=18, max_value=55, value=26)
                max_age = st.number_input("Emekli Olmak İstediğiniz Yaş", min_value=56, max_value=75, value=56)
                annual_contribution = st.slider("Yıllık Katkı Payınızı Giriniz", min_value=0.1, max_value=10.0,value=0.1)
                annual_yield = st.slider("Yıllık Verim", min_value=1, max_value=10, value=1)
                capital = st.number_input("Sermayenizi Giriniz", min_value=1, max_value=1000000, value=1)
                buton=st.button("BES Birikiminizi Hesaplayın",use_container_width=True)
                if buton:
                    result=bes.calculate(min_age, max_age, annual_contribution, annual_yield, capital)
                    st.write(f"BES Kazancınız : {result}")
                buton_graph=st.button("BES Grafiğiniz",use_container_width=True)
                if buton_graph:
                    image=bes.show_graph(min_age, max_age, annual_contribution, annual_yield, capital)
                    st.pyplot(image)
            except ValueError as v_error:
                st.error(f"Value Error : {v_error}, Please check the type of values!")
            except ConnectionError as c_error:
                st.error(f"Connection Error : {c_error}, Try Again!")
            except Exception as except_error:
                st.error(f"Exception Error : {except_error} , Try Again !")









else:
    st.info("You have to accept contract")