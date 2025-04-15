//ENGLISH
# InstagramUnfollowers

## About the Project
InstagramUnfollowers is a Python-based automation tool designed to help you identify users who don't follow you back on Instagram. The program uses Selenium for web automation and includes a simple GUI built with Tkinter for ease of use.

### Features
- Logs into your Instagram account.
- Retrieves your followers and following lists.
- Identifies users who don't follow you back.
- Saves the results in a `.txt` file.
- Works on both Windows (`.exe`) and MacOS (`.app`).

---

## How It Works
1. **Login**: The program logs into your Instagram account using the credentials you provide in the GUI.
2. **Retrieve Data**: It collects your followers and following lists by scrolling through the respective sections.
3. **Compare Lists**: It compares the two lists to find users who don't follow you back.
4. **Save Results**: The results are saved in a file named `non_followers.txt`.

---

## Technologies Used
- **Python**: Core programming language.
- **Selenium**: For web automation.
- **Tkinter**: For the graphical user interface (GUI).

---

## Branches
This repository is divided into two branches:

1. **`main` Branch**:
   - Contains the **source code** of the project.
   - Ideal for developers or those who want to understand and modify the code.

2. **`exe-and-app-program` Branch**:
   - Contains the **compiled versions** of the program:
     - `app.exe` for Windows.
     - `app.app` for MacOS.
   - Ideal for non-technical users who just want to run the program.

---

## How to Use
### For Non-Technical Users
1. Go to the **`exe-and-app-program`** branch.
2. Download the appropriate file for your operating system:
   - **Windows**: Download `app.exe`.
   - **MacOS**: Download `app.app`.
3. Run the file:
   - On Windows, double-click `app.exe`.
   - On MacOS, give execute permissions to `app.app`:
     ```bash
     chmod +x app.app
     ./app.app
     ```

### For Developers
1. Clone the repository and switch to the **`main`** branch:
   ```bash
   git clone https://github.com/your-username/InstagramUnfollowers.git
   cd InstagramUnfollowers
   git checkout main

//TÜRKÇE

# InstagramUnfollowers

## Proje Hakkında
InstagramUnfollowers, Instagram'da sizi takip etmeyen kullanıcıları bulmanıza yardımcı olmak için geliştirilmiş Python tabanlı bir otomasyon aracıdır. Program, web otomasyonu için Selenium'u ve kolay kullanım için Tkinter ile oluşturulmuş basit bir GUI'yi kullanır.

### Özellikler
- Instagram hesabınıza giriş yapar.
- Takipçi ve takip edilen listelerinizi alır.
- Sizi takip etmeyen kullanıcıları belirler.
- Sonuçları bir `.txt` dosyasına kaydeder.
- Hem Windows (`.exe`) hem de MacOS (`.app`) üzerinde çalışır.

---

## Nasıl Çalışır?
1. **Giriş Yapma**: Program, GUI'de sağladığınız bilgilerle Instagram hesabınıza giriş yapar.
2. **Veri Toplama**: Takipçi ve takip edilen listelerinizi alır.
3. **Listeleri Karşılaştırma**: İki listeyi karşılaştırarak sizi takip etmeyen kullanıcıları bulur.
4. **Sonuçları Kaydetme**: Sonuçları `non_followers.txt` adlı bir dosyaya kaydeder.

---

## Kullanılan Teknolojiler
- **Python**: Ana programlama dili.
- **Selenium**: Web otomasyonu için.
- **Tkinter**: Grafik kullanıcı arayüzü (GUI) için.

---

## Branch'ler
Bu depo iki branch'e ayrılmıştır:

1. **`main` Branch**:
   - Projenin **kaynak kodlarını** içerir.
   - Geliştiriciler veya kodu anlamak ve değiştirmek isteyenler için uygundur.

2. **`exe-and-app-program` Branch**:
   - Programın **derlenmiş sürümlerini** içerir:
     - Windows için `app.exe`.
     - MacOS için `app.app`.
   - Teknik bilgisi olmayan kullanıcılar için uygundur.

---

## Nasıl Kullanılır?
### Teknik Bilgisi Olmayan Kullanıcılar İçin
1. **`exe-and-app-program`** branch'ine gidin.
2. İşletim sisteminize uygun dosyayı indirin:
   - **Windows**: `app.exe` dosyasını indirin.
   - **MacOS**: `app.app` dosyasını indirin.
3. Dosyayı çalıştırın:
   - Windows'ta `app.exe` dosyasına çift tıklayın.
   - MacOS'ta `app.app` dosyasına çalıştırma izni verin:
     ```bash
     chmod +x app.app
     ./app.app
     ```

### Geliştiriciler İçin
1. Depoyu klonlayın ve **`main`** branch'ine geçin:
   ```bash
   git clone https://github.com/kullanıcı-adınız/InstagramUnfollowers.git
   cd InstagramUnfollowers
   git checkout main
