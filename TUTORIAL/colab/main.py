import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class MyApp(App):

    def build(self):
        return Label(text='Hello world',color= (0,0,1,1))


if __name__ == '__main__':
    MyApp().run()
