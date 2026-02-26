import json

class writter : 
    def __init__(self, OUTPUT_FILE, data):
        self.data = data
        self.output_file = OUTPUT_FILE
        
    def write(self):
        with open(f"output/{self.output_file}", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)
        print(f"\n Successfully exported to {self.output_file}")
        