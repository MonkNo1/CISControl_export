import pandas as pd


class exporter:
    def __init__(self, input_file):
        self.input_file = input_file
        
    def export(self):
        df = pd.read_excel(self.input_file, sheet_name="Controls v8.1.2")
        df.columns = df.columns.str.strip()
        controls = {}
        for _, row in df.iterrows():
            control_id = str(row["CIS Control"]).strip()
            safeguard_id = row["CIS Safeguard"]
            if pd.isna(safeguard_id):
                continue
            safeguard_id = str(safeguard_id).strip()

            if control_id not in controls:
                controls[control_id] = {
                    "control_id": control_id,
                    "control_name": None,
                    "safeguards": []
                }

            safeguard = {
                "safeguard_id": safeguard_id,
                "title": row["Title"],
                "description": row["Description"],
                "asset_class": row["Asset Class"],
                "security_function": row["Security Function"],
                "ig1": str(row["IG1"]).lower() == "x",
                "ig2": str(row["IG2"]).lower() == "x",
                "ig3": str(row["IG3"]).lower() == "x"
            }

            controls[control_id]["safeguards"].append(safeguard)
        output = list(controls.values())
        return output
