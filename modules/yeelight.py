from yeelight import Bulb

with open("ip.txt", "r") as f:
    ip = f.read()
bulb = Bulb(ip)


def yeelight_connect(ip):
    global bulb
    bulb = Bulb(ip)
    with open("ip.txt", "w") as f:
        f.write(ip)


def yeelight_toggle():
    bulb.toggle()


def yeelight_color(color):
    bulb.set_rgb(*color)


def yeelight_brightness(bright):
    bulb.set_brightness(bright)


def yeelight_temperature(temp):
    bulb.set_color_temp(temp)
