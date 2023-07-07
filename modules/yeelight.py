from yeelight import Bulb

ip = ""
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
    rgb = [int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)]
    if rgb[0] == 0 and rgb[1] == 0 and rgb[2] == 0:
        rgb = [255, 255, 255]
    bulb.set_rgb(*rgb)


def yeelight_brightness(bright):
    bulb.set_brightness(bright)


def yeelight_temperature(temp):
    bulb.set_color_temp(temp)
