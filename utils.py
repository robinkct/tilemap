
import time
import os
import importlib.util

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

def load_functions_from_folder(folder_path):
    funcs_dict ={}
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            file_path = os.path.join(folder_path,filename)
            spec = importlib.util.spec_from_file_location(module_name,file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        for attr in dir(module):
            if callable(getattr(module,attr)):
                funcs_dict[attr] = getattr(module,attr)
    return funcs_dict



if __name__ == '__main__':
    api_path = './api'
    functions_dict = load_functions_from_folder(api_path)

    print(f"Current api functions in {api_path}:")
    for func_name in functions_dict:
        if '_api' in func_name:
            print(f"{func_name}")