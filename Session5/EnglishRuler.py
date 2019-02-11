def drawInterval(n):
    'Draw Intervals within 1 unit'
    if n == 1:
        print("-")
    else:
        drawInterval(n-1)
        _line = ""
        for i in range(0, n):
            _line += '-'
        print(_line)
        drawInterval(n-1)

def drawLine(n, m):
    'Draw Line at between intervals'
    _line = ""
    for i in range(0, n):
        _line += '-'
    _line += m
    print(_line)

def draw(n, s):
    drawLine(s, '0')
    for i in range(0, n):
        drawInterval(s-1)
        drawLine(s, str(i+1))

draw(2, 4)