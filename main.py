from kivy.app import App
from kivy.uix.button import Button


class HowMuchIn(App):
    def build(self):
        button = Button(text="example")
        return button


if __name__ == "__main__":
    HowMuchIn().run()