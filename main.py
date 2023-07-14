import dearpygui.dearpygui as dpg
from modules.yeelight import *


def connect():
    ip_value = dpg.get_value("ip")
    yeelight_connect(ip_value)


def color():
    color_value = [int(value) for value in dpg.get_value("color")[:3]]
    yeelight_color(color_value)


def brightness():
    brightness_value = dpg.get_value("brightness")
    yeelight_brightness(brightness_value)


def temperature():
    temperature_value = dpg.get_value("temperature")
    yeelight_temperature(temperature_value)


dpg.create_context()

with dpg.window(tag="main"):
    with dpg.group(horizontal=False):
        dpg.add_input_text(tag="ip", width=164, default_value=ip)
        with dpg.group(horizontal=True):
            dpg.add_button(label="Connect", callback=connect)
            dpg.add_button(label="On/Off", callback=yeelight_toggle)
        dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_color_edit(
                default_value=(255, 255, 255),
                tag="color",
                width=113,
                no_alpha=True,
                no_picker=True,
                no_tooltip=True,
            )
            dpg.add_button(label="Apply", callback=color)
        dpg.add_separator()
        dpg.add_text("Brightness")
        with dpg.group(horizontal=True):
            dpg.add_slider_int(
                tag="brightness",
                width=113,
                default_value=100,
                min_value=0,
                max_value=100,
            )
            dpg.add_button(label="Apply", callback=brightness)
        dpg.add_separator()
        dpg.add_text("Temperature")
        with dpg.group(horizontal=True):
            dpg.add_slider_int(
                tag="temperature",
                width=113,
                default_value=6500,
                min_value=1700,
                max_value=6500,
            )
            dpg.add_button(label="Apply", callback=temperature)


dpg.create_viewport(
    title="SimpleRGB",
    large_icon="src/SimpleRGB.ico",
    width=196,
    height=224,
    min_width=0,
    min_height=0,
    resizable=False,
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main", True)
dpg.start_dearpygui()
dpg.destroy_context()
