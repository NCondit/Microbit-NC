def on_rotary_encoder1_position_changed():
    global LED
    modules.led1.set_pixel_color(LED, 0xffffff)
    LED += 1
    if LED == 8:
        LED = 0
    modules.led1.set_pixel_color(LED, 0xff8000)
modules.rotary_encoder1.on_position_changed(on_rotary_encoder1_position_changed)

def on_button1_button_down():
    pass
modules.button1.on_event(jacdac.ButtonEvent.DOWN, on_button1_button_down)

LED = 0
LED = 0

def on_forever():
    if modules.button1.pressed():
        pass
basic.forever(on_forever)
