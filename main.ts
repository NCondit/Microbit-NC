modules.rotaryEncoder1.onPositionChanged(function () {
    modules.led1.setPixelColor(LED, 0x000000)
    LED += 1
    if (LED == 8) {
        LED = 0
    }
    modules.led1.setPixelColor(LED, 0xff8000)
})
modules.button1.onEvent(jacdac.ButtonEvent.Down, function () {
	
})
let LED = 0
LED = 0
basic.forever(function () {
    if (modules.button1.pressed()) {
    	
    }
})
