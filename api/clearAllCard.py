api_name = 'CLEARALLCARD'
description = f'{api_name}: Remove all card'
CLEARALLCARD_PROMPT = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
try:
    from utils import api_hit
except:
    from api.utils import api_hit


def run_api():
    api_hit("ClearAllCard", no_return=True)

def run_testcase(input=None, expect_output=None):
    ret = run_api()
    if ret == None:
        return True

if __name__ == "__main__":
    run_testcase()