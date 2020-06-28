import pandas as pd

info_dict = {
"社員コード":"employee_code",
"社員名":"employee_name",
"業務報告書入力チェック":"input_required_check",
"業務報告書日付":"report_date",
"状態":"status",
}
status_dict = {
"済":"confirmed",
"データ未確定":"unconfirmed",
"申請中":"aplied",
"日報データなし":"no data",
None: None
}

class FileHandler():
    def __init__(self, file):
        self.df = pd.read_csv(file).fill_na(None)

    def convert_row(self, row):
        data = {}
        for jp, eng in info_dict.items():
            data[eng] = row[jp]
            data["status"] = status_dict[data["status"]]
        return data

    def __iter__(self):
        for row in self.df.iterrows:
            yield self.convert_row(row)
