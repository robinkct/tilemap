
import requests
from utils import load_functions_from_folder

class Action:
    def __init__(self, action: str, content: str):
        self.action = action
        self.content = content
        self.func_dict = load_functions_from_folder('api')
        self.card_cnt = 0

    def doAction(self):
        if self.action in self.func_dict:
            self.func_dict[self.action](self.content)
        else:
            print(f"Unknown action: {self.action}")

def main():
    # Example usage
    action = "ADDCARD"  # Define your action here
    content = "Sample Card Content"  # Define your content here

    # Create an instance of Action and perform the action
    a = Action(action, content)
    a.doAction()

if __name__ == "__main__":
    main()