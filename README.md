# 📶 WiFi QR Creator

No more sharing WiFi passwords manually! This simple and efficient tool generates a QR code for your WiFi network, allowing devices to connect instantly by scanning it.

## 🚀 Features

- Automatically generates a WiFi QR code
- Saves the QR code as a `.png` file
- Requires administrator privileges to access WiFi credentials
- No user input required
- Available as both Python script and Windows executable

## 🛠️ Requirements (for Python version)

- Python 3.6 or higher
- `qrcode` and `Pillow` Python libraries

Install with:

```bash
pip install qrcode[pil]
```

## 💾 Installation

### Option 1: Run from Source

1. Clone the repository:

```bash
git clone https://github.com/SerhanTurk/wifi_qr_creator.git
cd wifi_qr_creator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python wifi_qr_creator.py
```

### Option 2: Download Executable (.exe)

If you don’t have Python installed, you can simply download and run the precompiled executable:

👉 [Download WiFi QR Creator (.exe)](https://github.com/SerhanTurk/wifi_qr_creator/releases)  
_No installation needed. Just run and allow administrator access._

## ▶️ Usage

Whether using the Python script or `.exe` version:

- Simply run the program.
- You will be prompted to grant administrator permissions.
- The application will automatically detect your active WiFi network, generate a QR code, and save it as `wifi_qr.png` in the same folder.
- No additional user input is required.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

🛠️ Developed by [Serhan Turk](https://github.com/SerhanTurk)  
💡 Contributions are welcome! Feel free to fork the repo and submit a pull request.

