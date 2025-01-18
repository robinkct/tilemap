api_name = "GetAllConnectionInfo"
description = f'{api_name}: Get all connection info'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

try:
    from utils import api_hit, remove_duplicate
    from addCard import run_api as addCard
except:
    from api.utils import api_hit, remove_duplicate
    from api.addCard import run_api as addCard


def run_api(verbose=True):
    connection_info_list = api_hit("GetAllCardConnectionInfo", verbose=verbose)
    connection_info_list = remove_duplicate(connection_info_list)
    
    if connection_info_list == "[]" and verbose:
        print(f"{api_name}: No connection")
    return connection_info_list

def run_testcase(input=None, expect_output=None, verbose=False):
    # 获取API返回结果
    card_info = run_api(verbose=verbose)
    
    # 检查返回值是否为列表类型
    if isinstance(card_info, list):
        return True
    return False

if __name__ == "__main__":
    print(f"== {api_name} ==")

    print("Result:")
    connection_info_list = run_api()
    for connection in connection_info_list:
        print(connection)

    print("Testcase Result:", run_testcase())