import pygame.camera
pygame = pygame

running = False

def init():
    import pygame.camera
    pygame.camera.init()
    
def close():
    pygame.camera.quit()
    

def getCamera(num):
    return pygame.camera.Camera(pygame.camera.list_cameras()[num], (1280,720))

def takePicture(cam):
    #print("Taking Picture")
    cam.start()
    return cam.get_image()
    

def savePicture(img):
    import pygame.image
    import time
    pygame.image.save(img, "photo"+str(time.time())+".bmp")

def takePictures(cam, x):
    for y in range(x):
        takePicture(cam)

def startVideos():
    pictues = []
    pictues2 = []
    i = 1
    running = True
    cam1 = getCamera(0)
    #cam2 = getCamera(1)
    while running:
        i += 1
        pictues.append(takePicture(cam1))
        #pictues2.append(takePicture(cam2))
    return [pictues, pictues2]
        
def stopVideos(cam):
    running = False
    

def testMessage(str):
    print(str)

def takeVideo():
    print("test")
