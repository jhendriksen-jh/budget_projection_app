from library.data_handling import process_username
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class BudgetProjectionApp(App):
    def build(self):
        return BudgetProjectionGUI() 

    

class BudgetProjectionGUI(Widget):
    user = ObjectProperty(None)

    def access_user_data(self):
        """
        Calls relevant functions from data_handling to allow access to user data
        Args:
            self: data from inputs in GUI
        Returns:
            user_data: previously collected user data
        """
        process_username(self.user.text)
        print(f"test: {self.user.text}")

    pass

if __name__ == "__main__":
    BudgetProjectionApp().run()