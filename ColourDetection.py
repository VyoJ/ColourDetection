import pandas as pd
import cv2

img = cv2.imread("test.jpg")    #Filename here

index = ["colour", "colour_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

r = g = b = 0
xpos = ypos = 0
clicked = False

def colour_detection(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i,"R"])) + abs(G - int(csv.loc[i,"G"]))+ abs(B - int(csv.loc[i,"B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i,"colour_name"]
    return cname

def click(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r, g, b, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('Colour Detection')
cv2.setMouseCallback('Colour Detection', click)

while True:
    cv2.imshow("Colour Detection", img)
    if clicked:
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        text = colour_detection(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        cv2.putText(img, text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img, text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
        clicked=False
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()