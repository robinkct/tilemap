
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

    # def call_clearAllCard(self):
    #     try:
    #         response = requests.post(
    #             url=self.url_clearAllCard,
    #             json={},
    #         )
    #         response.raise_for_status()
    #         print("All cards cleared successfully.")
    #     except requests.RequestException as e:
    #         print(f"Error clearing cards: {e}")

    # def call_addCard(self, text):
    #     demo_format = {
    #         "X": 100 + 100 * self.card_cnt,
    #         "Y": 100 + 100 * self.card_cnt,
    #         "TextInfo": {
    #             "Text": text,
    #         },
    #     }
    #     self.card_cnt += 1
    #     try:
    #         response = requests.post(
    #             url=self.url_addCard,
    #             json=demo_format,
    #         )
    #         response.raise_for_status()
    #         print("Card added successfully.")
    #     except requests.RequestException as e:
    #         print(f"Error adding card: {e}")

def main():
    # Example usage
    action = "add_card_api"  # Define your action here
    content = "Sample Card Content"  # Define your content here

    # Create an instance of Action and perform the action
    a = Action(action, content)
    a.doAction()

if __name__ == "__main__":
    main()