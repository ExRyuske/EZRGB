import PySimpleGUI as sg
from modules.yeelight import *


def main():
    sg.theme("Dark")

    layout = [ #yeelight_layout = [
        [
            sg.InputText(default_text=ip, size=(23), key="ip"),
            sg.InputText(change_submits=True, key="ColorText", visible=False),
        ],
        [
            sg.Button("Connect"),
            sg.Button("On/Off"),
            sg.ColorChooserButton("Color", target="ColorText", key="ColorButton"),
        ],
        [
            sg.Slider(
                range=(0, 100),
                default_value=100,
                orientation="horizontal",
                disable_number_display=True,
                change_submits=True,
                size=(18.3, 20),
                key="BrightnessSlider",
            )
        ],
        [
            sg.Text("Brightness:", pad=((6, 0),(0, 0))),
            sg.Text("100", pad=((0, 21),(0, 0)), key="BrightnessText"),
            sg.Button("Apply", key="BrightnessApply"),
        ],
        [
            sg.Slider(
                range=(1700, 6500),
                default_value=6500,
                orientation="horizontal",
                disable_number_display=True,
                change_submits=True,
                size=(18.3, 20),
                key="TemperatureSlider",
            )
        ],
        [
            sg.Text("Temperature:", pad=((6, 0),(0, 0))),
            sg.Text("6500", pad=((0, 4),(0, 0)), key="TemperatureText"),
            sg.Button("Apply", key="TemperatureApply"),
        ],
    ]
    """
    test_layout = [[sg.Text("In progress...")]]

    layout = [
        [
            sg.TabGroup(
                [[sg.Tab("Yeelight", yeelight_layout), sg.Tab("TEST", test_layout)]]
            )
        ],
    ]
    """
    window = sg.Window("EZRGB", layout, element_justification="left", resizable=False)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        try:
            if event == "Connect":
                yeelight_connect(values["ip"])

            if event == "On/Off":
                yeelight_toggle()

            if event == "ColorText":
                yeelight_color(values["ColorText"])

            if event == "BrightnessApply":
                yeelight_brightness(values["BrightnessSlider"])

            if event == "TemperatureApply":
                yeelight_temperature(values["TemperatureSlider"])
        except Exception as e:
            sg.Popup(str(e))

        window.Element("BrightnessText").Update("{:.0f}".format(values["BrightnessSlider"]).rstrip("."))
        window.Element("TemperatureText").Update("{:.0f}".format(values["TemperatureSlider"]).rstrip("."))

    window.close()


if __name__ == "__main__":
    main()
