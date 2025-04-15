import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Instagram giriş bilgileri (GUI'den alınacak)
USERNAME = ""
PASSWORD = ""

def login(driver):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
    
    # Çerezleri kabul et
    try:
        cookie_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow essential and optional cookies')]"))
        )
        cookie_button.click()
    except:
        pass
    
    # Giriş yap
    username_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = driver.find_element(By.NAME, "password")
    
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)
    
    # "Şimdi Değil" butonlarına bas
    try:
        not_now_buttons = WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))
        )
        for button in not_now_buttons:
            button.click()
            time.sleep(1)
    except:
        pass

def get_followers(driver):
    try:
        # Takipçiler butonuna tıkla
        followers_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a")
        followers_button.click()
        time.sleep(2)
        
# Scroll yapılan div'i bul
        scroll_box = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        
        # Scroll işlemi
        last_height = 0
        scroll_attempts = 0  # Scroll sayısını takip etmek için
        max_scrolls = 100  # Maksimum scroll sayısı
        
        while scroll_attempts < max_scrolls:
            # Scroll yap
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            time.sleep(1.5)  # Yeni öğelerin yüklenmesi için bekle
            
            # Yeni yüksekliği kontrol et
            new_height = driver.execute_script("return arguments[0].scrollHeight", scroll_box)
            if new_height == last_height:
                # Eğer yükseklik değişmediyse, daha fazla öğe yüklenmiyor demektir
                break
            last_height = new_height
            scroll_attempts += 1  # Scroll sayısını artır            
        time.sleep(3)
        
        followers = []
        last_count = 0
        
        
        # Takipçi isimlerini al
        follower_elements = driver.find_elements(By.CLASS_NAME, "_ap3a._aaco._aacw._aacx._aad7._aade")
        print("Takipçi isimleri alınıyor...")
        
        for element in follower_elements:
            if element.text and element.text not in followers:
                followers.append(element.text)
                print(f"Bulunan takipçi: {element.text}")  # Terminale yazdır
        
        # Kapat butonuna tıkla
        close_button = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
        close_button.click()
        time.sleep(2)
        
        return followers
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return []

def get_following(driver):
    try:
        # Takip edilenler butonuna tıkla
        following_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a"))
        )
        following_button.click()
        time.sleep(2)
        # Scroll yapılan div'i bul
        scroll_box = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        
        # Scroll işlemi
        last_height = 0
        scroll_attempts = 0  # Scroll sayısını takip etmek için
        max_scrolls = 100  # Maksimum scroll sayısı
        
        while scroll_attempts < max_scrolls:
            # Scroll yap
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            time.sleep(1.5)  # Yeni öğelerin yüklenmesi için bekle
            
            # Yeni yüksekliği kontrol et
            new_height = driver.execute_script("return arguments[0].scrollHeight", scroll_box)
            if new_height == last_height:
                # Eğer yükseklik değişmediyse, daha fazla öğe yüklenmiyor demektir
                break
            last_height = new_height
            scroll_attempts += 1  # Scroll sayısını artır
        
        time.sleep(3)
        
        following = []
        
        # Takip edilen isimlerini al
        following_elements = driver.find_elements(By.CLASS_NAME, "_ap3a._aaco._aacw._aacx._aad7._aade")
        for element in following_elements:
            if element.text and element.text not in following:
                following.append(element.text)
        
        # Kapat butonuna tıkla
        close_button = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
        close_button.click()
        time.sleep(2)
        
        return following
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return []

def main():
    # Chrome options
    options = Options()
    options.add_argument("--start-maximized")
    
    # Otomatik ChromeDriver kullanımı
    driver = webdriver.Chrome(options=options)
    
    try:
        # Giriş yap
        login(driver)
        time.sleep(3)
        
        # Profil sayfasına git
        driver.get(f"https://www.instagram.com/{USERNAME}/")
        time.sleep(5)
        
        # Takipçi listesini al
        print("Takipçi listesi alınıyor...")
        followers = get_followers(driver)
        print(f"{len(followers)} takipçi bulundu.")
        
        # Takip edilenler listesini al
        print("Takip edilenler listesi alınıyor...")
        following = get_following(driver)
        print(f"{len(following)} takip edilen bulundu.")
        
        # Sizi takip etmeyenleri bul
        non_followers = sorted(set(following) - set(followers))
        
        # Sonuçları yazdır
        print("\nSizi takip etmeyenler ({} kişi):".format(len(non_followers)))
        for i, user in enumerate(non_followers, 1):
            print(f"{i}. @{user}")
            
        # Dosyaya kaydet
        with open("non_followers.txt", "w", encoding="utf-8") as f:
            f.write("Sizi takip etmeyenler ({} kişi):\n".format(len(non_followers)))
            for i, user in enumerate(non_followers, 1):
                f.write(f"{i}. @{user}\n")
        
        print("\nSonuçlar 'non_followers.txt' dosyasına kaydedildi.")
        
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
    finally:
        driver.quit()

# GUI oluştur
def start_gui():
    def start_automation():
        global USERNAME, PASSWORD
        USERNAME = username_entry.get()
        PASSWORD = password_entry.get()
        if USERNAME and PASSWORD:
            root.destroy()  # GUI'yi kapat
            main()
        else:
            messagebox.showwarning("Uyarı", "Lütfen kullanıcı adı ve şifre girin!")

    root = tk.Tk()
    root.title("Instagram Otomasyonu")

    tk.Label(root, text="Kullanıcı Adı:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Şifre:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(root, text="Başlat", command=start_automation).grid(row=2, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    start_gui()