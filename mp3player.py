import os
from pygame import *



init()
res=[800,640]
window=display.set_mode(res)
clock = time.Clock()
Font=font.SysFont("arial",16)
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)



'''
for file in os.listdir(path):
    print file
'''

class Player(object):
    def __init__(self):
        self.path="."
        self.list=self.createlist(os.listdir(self.path))
        self.ind=0
        self.pauseb=False
        self.volume=0.5
        mixer.music.set_volume(self.volume)

    def enter(self):
        if len(self.list)>0:
            if self.list[self.ind-1][-4:]==".mp3":
                #mixer.Channel(1).play(mixer.Sound(self.list[self.ind-1]))
                mixer.music.stop()
                mixer.music.load("./"+self.list[self.ind-1])
                #mixer.music.load("
                #/home/rozwadowski/Pulpit/Madox/music/aaa.mp3")
                mixer.music.play(1)
        if os.path.isdir(self.path+"/"+self.list[self.ind-1]):
            self.path=self.path+"/"+self.list[self.ind-1]
            self.list = self.createlist(os.listdir(self.path))
        if self.ind==0:
            self.path=self.path+"/.."
            self.list = self.createlist(os.listdir(self.path))

    def drawscreen(self):
        window.fill(black)
        n=1
        for i in range(len(self.list)):
            if os.path.isdir(self.path+"/"+self.list[i]):
                text = Font.render(self.list[i],True,blue)
                window.blit(text,(20,16*n))
                n=n+1
        for i in range(len(self.list)):
            if os.path.isfile(self.path+"/"+self.list[i]):
                text = Font.render(self.list[i],True,white)
                window.blit(text,(20,16*n))
                n=n+1
        text = Font.render("<-",True,white)
        window.blit(text,(20,0))  
        draw.rect(window,green,Rect(19,16*self.ind,200,20),1)

    def createlist(self,list):
            result=[]
            for i in range(len(list)):
                if os.path.isdir(self.path+"/"+list[i]):
                    result.append(list[i])
            for i in range(len(list)):
                if os.path.isfile(self.path+"/"+list[i]):
                    result.append(list[i])

            return result
    def pause(self):
        if mixer.music.get_busy() and not self.pauseb:
            mixer.music.pause()
            self.pauseb = True
        elif self.pauseb:
            mixer.music.unpause()
            self.pauseb = False

end=False
player=Player()
while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
        if zet.type==KEYDOWN:
            if zet.key==K_DOWN:
                if player.ind<39 and player.ind<len(player.list):
                    player.ind=player.ind+1
            if zet.key==K_UP:
                if player.ind>0:
                     player.ind=player.ind-1
            if zet.key==K_RETURN or zet.key==K_KP_ENTER:
                player.enter()
            if zet.key==K_SPACE:
                player.pause()
            if zet.key==K_KP_PLUS:
                if player.volume<1.0:
                    player.volume=player.volume+0.1
                    mixer.music.set_volume(player.volume)
            if zet.key==K_KP_MINUS:
                if player.volume>0.0:
                    player.volume=player.volume-0.1
                    mixer.music.set_volume(player.volume)

	player.drawscreen()
	clock.tick(15)
	display.flip()