import streamlit as st
import numpy as np
st.set_page_config(page_title="Yemek Kurası", page_icon="🍴")
st.title('Yine Ne Yiyeceğinize Karar Vermediniz 😂')

st.write("Aralarında boşluk koyarak gitmek istediğiniz yerlerin adını giriniz.")

# Kullanıcıdan yerleri alma
yerler_input = st.text_input("örneğin: 'Pideci Dönerci Burger'")

# Kura çekme butonu
if st.button("Kura Çek"):
    if yerler_input.strip():
        # Girilen metni boşlukla ayırıp listeye dönüştürme
        yerler_listesi = [yer.strip() for yer in yerler_input.split(' ') if yer.strip()]
        
        if len(yerler_listesi) < 2:
            st.error("Lütfen en az 2 farklı yemek yeri girin!")
        else:
            # Listeyi karıştır ve iki yer seç
            np.random.shuffle(yerler_listesi)
            secilen_yer = yerler_listesi[0]
            ikinci_yer = yerler_listesi[1] if len(yerler_listesi) > 1 else None
            
            # Sonuçları göster
            st.success(f"Bugün gidilecek yer: **{secilen_yer}** 🎉")
            if ikinci_yer:
                st.info(f"Eğer ilk yere gidemiyorsanız, ikinci seçenek: **{ikinci_yer}** 😊")
    else:
        st.error("Lütfen en az bir yemek yeri girin.")
