import pew


pew.init()
screen = pew.Pix.from_iter((
    (1, 1, 1, 4, 1, 1, 1, 1),
    (1, 2, 2, 2, 3, 0, 2, 1),
    (1, 1, 3, 1, 2, 5, 2, 1),
    (1, 2, 2, 1, 2, 1, 1, 1),
    (1, 2, 0, 3, 2, 3, 2, 1),
    (1, 2, 0, 5, 2, 2, 2, 1),
    (1, 2, 2, 2, 2, 2, 2, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
))

blink = 1
dead = False
for y in range(8):
    for x in range(8):
        if screen.pixel(x, y) == 4:
            break;
    else:
        continue
    break

while not dead:
    screen.pixel(x, y, 0)
    pressed = pew.keys()
    dx = 0
    dy = 0
    if pressed & pew.K_UP:
        dy = -1
    elif pressed & pew.K_DOWN:
        dy = 1
    elif pressed & pew.K_LEFT:
        dx = -1
    elif pressed & pew.K_RIGHT:
        dx = 1
    if screen.pixel(x + dx, y + dy) in {0, 2, 5, 6}:
        x += dx
        y += dy
    elif screen.pixel(x + dx, y + dy) == 3 and dy == 0:
        if screen.pixel(x + dx + dx, y + dy + dy) == 0:
            screen.pixel(x + dx + dx, y + dy + dy, 3)
            screen.pixel(x + dx, y + dy, 0)
            x += dx
            y += dy
    count = 0
    for a in range(8):
        for b in range(7, -1, -1):
            if (screen.pixel(a, b) == 3 and
                    screen.pixel(a, b + 1) == 0 and
                    (a, b + 1) != (x, y)):
                screen.pixel(a, b, 0)
                screen.pixel(a, b + 1, 3)
                if (a, b + 2) == (x, y):
                    dead = True
            if screen.pixel(a, b) in {5, 6}:
                screen.pixel(a, b, 5 if blink else 6)
                count += 1
    if count == 0:
        break
    screen.pixel(x, y, 3 if blink else 0)
    blink = 0 if blink else 1
    pew.show(screen)
    pew.tick(1 / 6)
