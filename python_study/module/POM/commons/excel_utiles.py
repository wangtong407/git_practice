import pandas


# 传入excel路径和sheet的名称形参
def read_excel_to_list(excel_path, sheet_name):
    # 读取Excel路径，sheet页名称，使用openpyxl处理Excel
    data = pandas.read_excel(excel_path, sheet_name=sheet_name, engine='openpyxl')
    dict_list = data.to_dict(orient='records')  # to_dict 转化为列表字典形式，
    return dict_list  # return 返回字典


if __name__ == '__main__':
    # 调用函数
    dict_data = read_excel_to_list(r"C:\Users\31646\AppData\Local\Programs\Python\venv\python_study\module\POM\testcases\cases.xlsx", "Sheet1")
