
add_library('minim')
def setup():
    global cornerpointx, cornerpointy, canvasx, canvasy, back, showbird
    global t2, t3, mode, bird, bird2, x, y, birdsizex, birdsizey, incrx,incry
    global lbound,rbound,ubound,bbound, mbound
    global snowman, snowmanx, snowmany, snowmanw, snowmanh
    
    snowmanw = 400
    snowmanh = 400
    snowmanx = 200
    snowmany = 400
    cornerpointx = 0
    cornerpointy = 0
    canvasx = 799
    canvasy = 799 
    t2 = 50
    t3 = 60
    mode = "load"
    size( 799,799 )
    lbound = 0
    rbound = canvasx
    ubound = 0
    bbound = 400
    
    minim=Minim(this)
    intro = minim.loadFile("Intro.wav")
    sound=minim.loadFile("game.mp3")
    intro.play()
    delay(4300)
    sound.loop()
    snowman = loadImage( "snowman.png" )
    bird = loadImage( "bird.png" )
    bird2 = loadImage( "bird2.png" )
    showbird = bird
    back = loadImage( "back.png" )
    x = 0
    y = 0
    incrx = 7
    incry = 6
    birdsizex = 100
    birdsizey = 100
    image( back, cornerpointx, cornerpointy, canvasx, canvasy )
    image ( snowman, snowmanx, snowmany, snowmanw, snowmanh )
    
def draw():
    global cornerpointx, cornerpointy, canvasx, canvasy, back, showbird
    global t2, t3, mode, bird, bird2, x, y, birdsizex, birdsizey, incrx,incry
    global lbound,rbound,ubound,bbound, mbound
    global snowman, snowmanx, snowmany, snowmanw, snowmanh
    
    image( back, cornerpointx, cornerpointy, canvasx, canvasy )
    image ( snowman, snowmanx, snowmany, snowmanw, snowmanh )
    
    
    x += incrx
    y += incry
    
     
    image ( showbird, x, y, birdsizex, birdsizey )
   