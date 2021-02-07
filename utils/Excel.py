# Excel操作工具类
import pandas as pd
from core.config import Settings
import os


class Excel:
    def __init__(self, filepath):
        self.filepath = filepath

    def import_cmdb_record(self):
        pf = pd.read_excel(self.filepath)
        # 第一行数据是key
        keys = pf.columns.values
        # 获取所有数据
        all_records = []
        for i in pf.index.values:
            record = pf.loc[i, keys].astype('str').to_dict()
            all_records.append(record)
        return all_records


if __name__ == '__main__':
    excel = Excel(os.path.join(Settings.CMDB_FOLDER, "mysql模板.xlsx"))
    excel.import_cmdb_record()
