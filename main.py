from src.export import exporter
from src.writer import writter

if __name__ == "__main__":
    INPUT_FILE = "data/CIS_Controls_Version_8.xlsx"
    OUTPUT_FILE = "cis_controls.json"
    
    exp = exporter(INPUT_FILE)
    data = exp.export()
    
    writer = writter(OUTPUT_FILE, data)
    writer.write()


