import cv2
terminalWidth = 120
terminalHeight = 28
text = open("badapple.bat","w",encoding="utf-8")

slowdown = "\nchoice /n /c x /d x /t 0 > nul"
v = cv2.VideoCapture("BadApple.flv")
max = int(v.get(cv2.CAP_PROP_FRAME_COUNT))
fps = 1/v.get(cv2.CAP_PROP_FPS)*1000
print(max,fps)
empty = "."
full = "#"


text.write(f'@echo off\nchcp 65001\nmode {terminalWidth},{terminalHeight}\n\ncls\n')
success = True
c = 1
for i in range(max-1):
    success, image = v.read()
    frame = ""
    frame+="\necho "
    try:
        image = cv2.resize(image,(terminalWidth,terminalHeight))
    except TypeError:
        success = False
        continue
    for j in range(terminalHeight):

        for k in range(terminalWidth):
            color = image[j,k][0]
            if color <= 100:
                frame += empty
            else:
                frame += full
            pass

    if c%5 == 1:
        frame += slowdown
        frame += slowdown
        frame += slowdown
    else:
        frame += slowdown
        frame += slowdown

    text.write(frame)
    print(str(int(c/(max-1)*100))+"%",str(c)+"/"+str(int(max-1)))
    c +=1
print("Done")


