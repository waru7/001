let fruit = {
    "x" : 2,
    "y" : 4,
    "feq" : 100,
}

let monkey = {
    "x" : 0,
    "y" : 0,
}

function blink(_fruit: any) {
    led.plot(_fruit["x"], _fruit["y"])
    basic.pause(_fruit["feq"])
    led.unplot(_fruit["x"], _fruit["y"])
    basic.pause(_fruit["feq"])
}

basic.forever(function on_forever() {
    led.plot(monkey["x"], monkey["y"])
    blink(fruit)
})
input.onGesture(Gesture.TiltRight, function on_tilt_right() {
    led.unplot(monkey["x"], monkey["y"])
    monkey["x"] = monkey["x"] + 1
})
input.onGesture(Gesture.TiltLeft, function on_tilt_left() {
    led.unplot(monkey["x"], monkey["y"])
    monkey["x"] = monkey["x"] - 1
})
