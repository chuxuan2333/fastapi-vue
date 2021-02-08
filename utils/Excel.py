# Excel操作工具类
import pandas as pd
from pandas import DataFrame
from core.config import Settings
import os


class Excel:
    def __init__(self, filepath):
        self.filepath = filepath

    def create_cmdb_template(self, keys):
        """
        创建cmdb上传模板
        """
        pf = pd.DataFrame(columns=keys)
        pf.to_excel(self.filepath, index=False)

    def import_cmdb_record(self):
        """
        获取用户上传的Excel中的数据
        """
        pf = pd.read_excel(self.filepath)
        # 第一行数据是key
        keys = pf.columns.values
        print(keys)
        # 获取所有数据
        all_records = []
        for i in pf.index.values:
            record = pf.loc[i, keys].astype('str').to_dict()
            all_records.append(record)
        return all_records


# if __name__ == '__main__':
#     excel = Excel(os.path.join(Settings.CMDB_FOLDER, "mysql模板.xlsx"))
#     excel.create_cmdb_template(keys=["name","host","port","password","abc"])
#     excel.import_cmdb_record()
