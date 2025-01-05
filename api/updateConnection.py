api_name = "UPDATECONNECTION"
description = f'{api_name}: Update a exist connection.'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
try:
    from utils import api_hit
    #from getCardInfoByID import id_exist as id_exist
    from addConnection import run_testcase as create_dummy_connection
    from getAllConnectionInfo import run_api as getAllConnectionInfo
except:
    from api.utils import api_hit
    #from api.getCardInfoByID import id_exist as id_exist
    from api.addConnection import run_testcase as create_dummy_connection
    from api.getAllConnectionInfo import run_api as getAllConnectionInfo

def run_api(id: str, description: str):
    # TODO: Check if the connection exists
#    if not id_exist(id):
#        return None
    msg = {
        "ID":id,
        "Description":description,
    }
    if id is None or description is None:
        return None

    api_hit("UpdateCardConnection", msg, no_return=True)

def run_testcase(id=None, description=None):
    if id is None and description is None: # Dummy testcase
        create_dummy_connection()
        id = "linkdummy0_dummy1"
        description = "connection between dummy0 and dummy1"

    run_api(id=id, description=description)
    try:
        connection_list = getAllConnectionInfo()
        for connection in connection_list:
            if connection["ID"] == id and connection["Description"] == description:
                return True
    except:
        return None


if __name__ == "__main__":
    print(f"== {api_name} ==")

    id = "linkdummy0_dummy1"
    description = "connection between dummy0 and dummy1"
    print(f"Testcase result: {run_testcase(id=id, description=description)}")

