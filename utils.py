
import time
import os
import importlib.util
import inspect

default_path = 'api'

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f'LOG: Run time: {execution_time}s')
            return result
        except Exception as e:
            print(f'Error: {str(e)}')
    return wrapper

# def load_functions_from_folder(folder_path: str=default_path) -> dict[str, callable]:
#     funcs_dict ={}
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".py"):
#             module_name = filename[:-3]
#             file_path = os.path.join(folder_path,filename)
#             spec = importlib.util.spec_from_file_location(module_name,file_path)
#             module = importlib.util.module_from_spec(spec)
#             spec.loader.exec_module(module)
#         #  Todo: print all module to test
#         for attr in dir(module):
#             if callable(getattr(module,attr)):
#                 funcs_dict[attr] = getattr(module,attr)
#     return funcs_dict

def load_functions_from_folder(folder_path: str=default_path) -> dict[str, callable]:
    func_dict = {}
    folder_path = os.path.dirname(os.path.abspath(__file__)) + "/api"
    
    # 獲取 prompt 目錄下所有 .py 文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # 移除 .py 後綴

            file_path = os.path.join(folder_path,filename)
            spec = importlib.util.spec_from_file_location(module_name,file_path)
            module = importlib.util.module_from_spec(spec)

            try:
                # 修改導入方式，直接使用完整的包路徑
                module = importlib.import_module(f"api.{module_name}")                
                # 獲取模塊中所有成員
                members = inspect.getmembers(module)

                api_name = None
                func = None
                for name, value in members:
                    if name == "api_name":
                        api_name = value
                    if "_api" in name and callable(value):
                        func = value
                if api_name is not None and func is not None:
                    func_dict[api_name] = func
                    
            except ImportError as e:
                print(f"無法導入模塊 {module_name}: {str(e)}")
                print(f"當前 Python 路徑: {os.sys.path}")
            except Exception as e:
                print(f"處理模塊 {module_name} 時發生錯誤: {str(e)}")
    
    return func_dict

def load_modules_from_folder(folder_path: str=default_path) -> dict[str, str]:
    """
    收集 folder 目錄下所有模塊中的 modules 常量
    """
    modules_dict = {}
    folder_path = os.path.dirname(os.path.abspath(__file__)) + "/api"
    
    # 獲取 prompt 目錄下所有 .py 文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # 移除 .py 後綴
            try:
                # 修改導入方式，直接使用完整的包路徑
                module = importlib.import_module(f"api.{module_name}")                
                # 獲取模塊中所有成員
                members = inspect.getmembers(module)

                for name, value in members:
                    modules_dict[name] = value
                        
            except ImportError as e:
                print(f"無法導入模塊 {module_name}: {str(e)}")
                print(f"當前 Python 路徑: {os.sys.path}")
            except Exception as e:
                print(f"處理模塊 {module_name} 時發生錯誤: {str(e)}")
    
    return modules_dict

def load_description_from_folder(folder_path: str=default_path) -> dict[str, str]:
    """
    收集 folder 目錄下所有模塊中的 XXX_DESCRIPTION 常量
    """
    description_dict = {}
    folder_path = os.path.dirname(os.path.abspath(__file__)) + "/api"
    
    # 獲取 prompt 目錄下所有 .py 文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # 移除 .py 後綴
            try:
                # 修改導入方式，直接使用完整的包路徑
                module = importlib.import_module(f"api.{module_name}")                
                # 獲取模塊中所有成員
                members = inspect.getmembers(module)

                api_name = None
                description = None
                for name, value in members:
                    if name == "api_name":
                        api_name = value
                    if name.endswith('_DESCRIPTION') and isinstance(value, str):
                        description = value
                if api_name is not None and description is not None:
                    description_dict[api_name] = description
                    
            except ImportError as e:
                print(f"無法導入模塊 {module_name}: {str(e)}")
                print(f"當前 Python 路徑: {os.sys.path}")
            except Exception as e:
                print(f"處理模塊 {module_name} 時發生錯誤: {str(e)}")
    
    return description_dict

if __name__ == '__main__':
    api_path = './api'
    functions_dict = load_functions_from_folder(api_path)

    print(f"Current api functions in {api_path}:")
    print(functions_dict)
    # # for func_name in functions_dict:
    # #     if '_api' in func_name:
    # #         print(f"{func_name}")
    
    # description_dict = load_description_from_folder(api_path)
    # print(f"Current api description in {api_path}:")
    # print(description_dict)
    # # for description_name in description_dict:
    # #     # if 'DESCRIPTION' in description_name:
    # #     print(f"{description_name}")

    # # modules_dict = load_modules_from_folder(api_path)
    # # print(f"Current modules in {api_path}:")
    # # print(modules_dict)

    # funcs = load_func()
    # print(funcs)