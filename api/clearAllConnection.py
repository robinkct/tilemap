api_name = 'ClearAllCardConnection'
description = f'{api_name}: Remove all connection'
CLEARALLCARD_PROMPT = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
try:
    from utils import api_hit
    from getAllConnectionInfo import run_api as getAllConnectionInfo
except:
    from api.utils import api_hit
    from api.getAllConnectionInfo import run_api as getAllConnectionInfo


def run_api(verbose=False):
    api_hit("ClearAllCardConnection", no_return=True, verbose=verbose)

def run_testcase(input=None, expect_output=None, verbose=False):
    ret = run_api(verbose=verbose)
    connection_list = getAllConnectionInfo(verbose=verbose)
    if len(connection_list) == 0:
        return True

if __name__ == "__main__":
    print(f"== {api_name} ==")
    print("Testcase Result:", run_testcase())
