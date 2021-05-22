fruit = { 'x' : 2, 'y' : 4, 'feq' : 100 } 
monkey = { 'x' : 0, 'y' : 0, }


def blink(_fruit): 
    led.plot(_fruit['x'], _fruit['y']) 
    basic.pause(_fruit['feq']) 
    led.unplot(_fruit['x'], _fruit['y']) 
    basic.pause(_fruit['feq'])


def on_forever(): 
    led.plot(monkey['x'], monkey['y']) 
    blink(fruit) 
basic.forever(on_forever)


def on_tilt_right(): 
    led.unplot(monkey['x'], monkey['y']) 
    monkey['x'] = monkey['x'] + 1 
input.on_gesture(Gesture.TILT_RIGHT, on_tilt_right)


def on_tilt_left(): 
    led.unplot(monkey['x'], monkey['y']) 
    monkey['x'] = monkey['x'] - 1 
input.on_gesture(Gesture.TILT_LEFT, on_tilt_left)