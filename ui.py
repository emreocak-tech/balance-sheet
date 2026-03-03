from dotenv import load_dotenv
load_dotenv()
import os
gemini_api=os.getenv("GOOGLE_GEMINI")

import streamlit as st
st.title("**Kullanıcı Sözleşmesi**")
check_box=st.checkbox("UYARI: **Lütfen Okuyunuz !** Bu uygulama yalnızca bilgilendirme amaçlıdır ve yatırım tavsiyesi içermez.- Finansal piyasalarda işlem yapmak yüksek risk içerir ve sermaye kaybına yol açabilir.- Sağlanan tahminler ve analizler kesin sonuç vermez, yanılabilir.- Alacağınız tüm yatırım kararlarının sorumluluğu tamamen size aittir.- Uygulama geliştiricisi, kullanımdan kaynaklanan herhangi bir zarardan sorumlu değildir.- Yatırım kararı vermeden önce profesyonel bir finansal danışmana başvurmanız önerilir.")
if check_box:
    st.header("Kullanıcı Sözleşmesi Kabul Edildi!")
    asd1,asd2,asd3=st.tabs(["Hakkında","Bilgiler","Gemini Sohbet Botu"])
    with asd1:
        st.write("İyi bir proje şimdilik")
    with asd2:
        st.write("Bilançoyu Analiz Etmemi Sağlıyor Bu Proje :)")
    with