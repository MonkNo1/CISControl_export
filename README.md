# CIS Controls v8 JSON Exporter

A simple Python utility that extracts CIS Controls v8 data from the official Excel file and exports it into structured JSON format.

---

## 📁 Project Structure

```
.
├── data/
│   └── CIS_Controls_Version_8.xlsx
├── output/
│   └── cis_controls.json
├── src/
│   ├── export.py
│   └── writer.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

- Python 3.9+

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

---

## 🧠 How It Works

### `exporter`

- Loads the Excel file
- Reads the **Controls v8** sheet
- Extracts:
  - CIS Control
  - CIS Safeguard
  - Asset Class
  - Security Function
  - Title
  - Description
  - IG1 / IG2 / IG3
- Converts IG flags (`x`) into boolean values
- Groups safeguards under their respective control

### `writter`

- Takes structured data
- Writes formatted JSON into the `output/` directory
- Uses `json.dump(..., indent=2)` for readable output

---

## 🖥 Example `main.py`

```python
from src.export import exporter
from src.writer import writter

if __name__ == "__main__":
    INPUT_FILE = "data/CIS_Controls_Version_8.xlsx"
    OUTPUT_FILE = "cis_controls.json"

    exp = exporter(INPUT_FILE)
    data = exp.export()

    writer = writter(OUTPUT_FILE, data)
    writer.write()
```

---

## 📄 Output Example

```json
[
  {
    "control_id": "1",
    "safeguards": [
      {
        "safeguard_id": "1.1",
        "title": "Establish and Maintain Detailed Enterprise Asset Inventory",
        "asset_class": "Devices",
        "security_function": "Identify",
        "ig1": true,
        "ig2": true,
        "ig3": true
      }
    ]
  }
]
```

---

## 📌 Notes

- This tool exports the **CIS Controls framework**, not CIS Benchmarks.
- Ensure the Excel file contains the **Controls v8** sheet.
- Refer to official CIS licensing terms before redistributing framework content.

---

## 📜 License

For educational use.  
Refer to official CIS licensing for redistribution terms.
