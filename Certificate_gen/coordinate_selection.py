# Capturing mouse events
import cv2 as cv

f = open("./source_file/coords.txt","w")

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        #img[:] = 0
        cv.putText(img,"coordinates (%d,%d)"%(x,y),(60,60),2,1,(0,255,0)) #SELECT LOCATION OF TEXT(TRIAL & ERROR)
        f.write(str(x)+"\n")                                              #SELECT TEXT'S TOP SIDE COORDS 
        f.write(str(y)+"\n")                                              #DOUBLE CLICK TO SELECT
                                                                           #COORDS WITH GREEN TEXT WILL BE DISPLAYED
# Create a black image, a window and bind the function to window
img = cv.imread("./template/template.png")


#cv.imshow('image',img)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(10) & 0xFF == 27:   #Press Escape Key to terminate window
        break
cv.destroyAllWindows()   

f.close()