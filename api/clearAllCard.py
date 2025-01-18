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
    from getAllCardInfo import run_api as getAllCardInfo
except:
    from api.utils import api_hit
    from api.getAllCardInfo import run_api as getAllCardInfo


def run_api(verbose=False):
    api_hit("ClearAllCard", no_return=True, verbose=verbose)

def run_testcase(input=None, expect_output=None, verbose=False):
    ret = run_api(verbose=verbose)
    card_list = getAllCardInfo(verbose=verbose)
    if len(card_list) == 0:
        return True

if __name__ == "__main__":
    print(f"== {api_name} ==")
    print("Testcase Result:", run_testcase())
