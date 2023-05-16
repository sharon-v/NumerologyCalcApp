from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from calculator import calcNumerology


def callback(instance, input_text, output_label):
    result = calcNumerology(input_text)
    output_label.text = str(result)


class NumerologyCalculator(MDApp):
    def build(self):
        LabelBase.register(name='HebrewFont', fn_regular='FreeSans.ttf')

        self.state = 0
        self.theme_cls.primary_palette = "Cyan"
        screen = MDScreen()

        # toolbar top
        self.toolbar = MDTopAppBar(
            title="Numerology Calculator",
            pos_hint={"top": 1})
        screen.add_widget(self.toolbar)

        # logo image
        screen.add_widget(Image(
            source="logos/logo7.png",
            pos_hint={"center_x": 0.5, "center_y": 0.65}))

        # instruction label
        self.label = MDLabel(
            text="Enter a Hebrew word to calculate its numerological value:",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.40},
            theme_text_color="Primary",
            font_style="H5",
            font_name="HebrewFont")
        screen.add_widget(self.label)

        # text input
        self.text_input = MDTextField(
            text="ןרק דח",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.30},
            size_hint=(0.8, 1),
            font_size=20,
            font_name="HebrewFont")
        screen.add_widget(self.text_input)

        # output label
        self.output_label = MDLabel(
            text="Result",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.20},
            theme_text_color="Primary",
            font_style="H6",
            font_name="HebrewFont")
        screen.add_widget(self.output_label)

        # button squat
        screen.add_widget(MDFillRoundFlatButton(
            text="בושיח",
            halign="center",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_press=lambda instance: callback(instance, self.text_input.text, self.output_label),
            font_name="HebrewFont"))

        return screen


if __name__ == "__main__":
    NumerologyCalculator().run()
