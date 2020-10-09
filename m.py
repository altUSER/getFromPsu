from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import psu
from secret import id

try:
    tt = psu.getTT(id)
except:
    tt = "error"

class dayPlate(BoxLayout): #плашка на день недели
    def __init__(self, **kwargs):
        super(dayPlate, self).__init__(**kwargs)

        with self.canvas.before:
            Color(.25, .25, .25, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class subDayPlate(BoxLayout): #плашка на пару или инфу
    def __init__(self, **kwargs):
        super(subDayPlate, self).__init__(**kwargs)

        with self.canvas.before:
            Color(.5, .5, .5, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        if tt == "error":
            layout.add_widget(Label(text="Error: Request error"))
        else:
            for i in tt: #проход по дням
                day = dayPlate(orientation="vertical", spacing=10, padding=30, size_hint_y=None, height=200)
                name = subDayPlate(orientation="vertical", spacing=10, padding=30, size_hint_y=None, height=50)
                name.add_widget(Label(text=i["name"]))
                day.add_widget(name)
                if i["less"] != None: #проход по парам
                    for less in i["less"]:
                        l_box = subDayPlate(orientation="vertical", spacing=10, padding=30, size_hint_y=None, height=20)
                        if i["less"] == "None":
                            day.add_widget(Label(text="Нет пары"))
                        else:
                            day.add_widget(Label(text=less, height=5))
                            #day.add_widget(l_box)
                else:
                    day.add_widget(Label(text="Пар нет!"))
                layout.add_widget(day)

        scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll.add_widget(layout)
        return scroll

if __name__ == '__main__':
    app = MainApp()
    try:
        app.run()
    except:
        print("Some error")
