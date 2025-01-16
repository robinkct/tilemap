api_name = 'ClearCardConnectionByID'
description = f'{api_name}: Remove connection by ID'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
try:
    from utils import api_hit
    from getConnectionByID import run_api as getConnectionByID
    from addConnection import run_testcase as create_dummy_connection
except:
    from api.utils import api_hit
    from api.addConnection import run_testcase as create_dummy_connection
    from api.getConnectionByID import run_api as getConnectionByID


def run_api(id: str):
    msg = { 
        "ID": id,
    }
    api_hit("ClearCardConnectionByID", msg, no_return=True)

def run_testcase(testcase_id=None, expect_output=None):

    if testcase_id is None:
        create_dummy_connection()
        testcase_id = "linkdummy0_dummy1"

    connection = getConnectionByID(testcase_id)
    ret = run_api(testcase_id)
    connection = getConnectionByID(testcase_id, verbose=False)
    assert connection is None
    if connection is None:
        return True

if __name__ == "__main__":
    print(f"== {api_name} ==")
    print("Testcase Result:", run_testcase())
