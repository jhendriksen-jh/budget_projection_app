import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class BudgetProjectionGUI(App):
    def build(self):
        return kvGrid()

class kvGrid(Widget):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)

    def btn(self):
        print(f"Hello my dear friend: {self.first_name.text} {self.last_name.text}")
        self.first_name.text = ""
        self.last_name.text = ""

    pass

if __name__ == "__main__":
    BudgetProjectionGUI().run()