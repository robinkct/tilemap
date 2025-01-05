api_name = "GetAllConnectionInfo"
description = f'{api_name}: Get all connection info'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

try:
    from utils import api_hit
    from addCard import run_api as addCard
except:
    from api.utils import api_hit
    from api.addCard import run_api as addCard


def run_api():
    def remove_duplicate(connection_info_list):
        seen = set()
        unique_list = []
        for d in connection_info_list:
            key = d['ID']
            if key not in seen:
                seen.add(key)
                unique_list.append(d)
        return unique_list

    connection_info_list = api_hit("GetAllCardConnectionInfo")
    connection_info_list = remove_duplicate(connection_info_list)
    if connection_info_list == "[]":
        print(f"{api_name}: No connection")
    return connection_info_list

def run_testcase(input=None, expect_output=None):
    ret = run_api()

    if type(ret) is list:
        return True
    else:
        return None

if __name__ == "__main__":
    print(f"== {api_name} ==")

    print("Result:")
    connection_info_list = run_api()
    for connection in connection_info_list:
        print(connection)

    print("Testcase Result:", run_testcase())