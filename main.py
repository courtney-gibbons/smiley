from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = 0.1

#lecture
RED = (255, 0, 0)
OFF = (0, 0, 0)

def light_one_pixel(pixel_number):
    cp.pixels[pixel_number%10] = RED
    time.sleep(.1)
    cp.pixels[pixel_number%10] = OFF
    #or cp.pixels.fill(OFF) sets all lights to off

#for i in range(20):
    #light_one_pixel(i)

#basic code
def smiley_face(R, G, B):
    color = (R, G, B)
    cp.pixels[1] = color
    cp.pixels[3] = color
    cp.pixels[4] = color
    cp.pixels[5] = color
    cp.pixels[6] = color
    cp.pixels[8] = color
    time.sleep(3)

#smiley_face(60, 20, 0)

#start
def smiley_face_start(R, G, B, start=0):
    color = (R, G, B)
    cp.pixels[(1+start)%10] = color
    cp.pixels[(3+start)%10] = color
    cp.pixels[(4+start)%10] = color
    cp.pixels[(5+start)%10] = color
    cp.pixels[(6+start)%10] = color
    cp.pixels[(8+start)%10] = color
    time.sleep(2)
    cp.pixels.fill(OFF)

#smiley_face_start(80, 0, 0)
#smiley_face_start(60, 20, 0, 1)
#smiley_face_start(30, 20, 0, 0)
#smiley_face_start(0, 80, 0, -1)
#smiley_face_start(0, 80, 20, 12)
#smiley_face_start(0, 40, 40, -13)

#spin
def smiley_face_spin(R, G, B, spin=0):
    color = (R, G, B)
    for i in range(spin):
        cp.pixels[(1+i)%10] = color
        cp.pixels[(3+i)%10] = color
        cp.pixels[(4+i)%10] = color
        cp.pixels[(5+i)%10] = color
        cp.pixels[(6+i)%10] = color
        cp.pixels[(8+i)%10] = color
        time.sleep(.2)
        cp.pixels.fill(OFF)

#smiley_face_spin(60, 20, 0, 30)

#rainbow spin
def smiley_face_rainbow_spin(spin):
    R = 90
    G = 0
    B = 0
    for i in range(spin):
        cp.pixels[(1+i)%10] = (R, G, B)
        cp.pixels[(3+i)%10] = (R, G, B)
        cp.pixels[(4+i)%10] = (R, G, B)
        cp.pixels[(5+i)%10] = (R, G, B)
        cp.pixels[(6+i)%10] = (R, G, B)
        cp.pixels[(8+i)%10] = (R, G, B)
        time.sleep(.5)
        cp.pixels.fill(OFF)
        if i<=4:
            R = R - 30
            G = G + 30
            B = 0
        if i>=5: #it breaks here :(
            R = 0
            G = G - 30
            B = B + 30
        #if i == 7 or 8 or 9:
            #B = B - 30
            #G = 0
            #R = R + 30

smiley_face_rainbow_spin(10)
