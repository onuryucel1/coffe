import streamlit as st
import numpy as np

st.title('Yine Ne Yiyeceğinize Karar Vermediniz 😂')

st.write("Aralarında boşluk koyarak gitmek istediğiniz yerlerin adını giriniz.")

# Kullanıcıdan yerleri alma
yerler_input = st.text_input("Yerleri girin (örneğin: 'Pideci Dönerci Burger')")

# Kura çekme butonu
if st.button("Kura Çek"):
    if yerler_input.strip():
        # Girilen metni boşlukla ayırıp listeye dönüştürme
        yerler_listesi = [yer.strip() for yer in yerler_input.split(' ') if yer.strip()]
        
        if len(yerler_listesi) < 2:
            st.error("Lütfen en az 2 farklı yemek yeri girin!")
        else:
            # Rastgele seçim yapma
            secilen_yer = np.random.choice(yerler_listesi)
            st.success(f"Bugün gidilecek yer: **{secilen_yer}** 🎉")
    else:
        st.error("Lütfen en az bir yemek yeri girin.")
