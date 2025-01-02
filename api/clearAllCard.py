api_name = 'CLEARALLCARD'
description = f'{api_name}: Remove all card'
CLEARALLCARD_PROMPT = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
from api.utils import api_hit

def run_api():
    api_hit("ClearAllCard")

def run_testcase(input=None, expect_output=None):
    ret = run_api()
    if ret == expect_output:
        return True

if __name__ == "__main__":
    run_testcase()