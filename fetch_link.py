import requests
import re

def get_now_link():
    url = "https://www.nowtv.com.tr/canli-yayin"
    # Sunucuyu gerçek bir tarayıcı olduğunuza ikna etmek için headers ekliyoruz
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.nowtv.com.tr/'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # Kaynak kodun içinde .m3u8 ile biten kalıbı arıyoruz
        # Regex, tırnaklar arasındaki http...m3u8 yapısını yakalar
        matches = re.findall(r'(https?://[^\s"\'<>]+?\.m3u8[^\s"\'<>]*)', response.text)
        
        if matches:
            # Bulunan linkteki ters slaşları düzeltiyoruz
            raw_link = matches[0].replace('\\/', '/')
            
            # Sadece linki içeren now.m3u8 dosyasını oluşturuyoruz
            with open("now.m3u8", "w", encoding="utf-8") as f:
                f.write(raw_link)
            print(f"Link başarıyla güncellendi: {raw_link}")
        else:
            print("Hata: m3u8 linki sayfa kaynağında bulunamadı.")
            
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    get_now_link()
