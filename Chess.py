# -*- coding: cp936 -*-

import pygame,sys,time,math
from pygame.locals import *
dict={1:'data\\images\\1.png',2:'data\\images\\2.png',3:'data\\images\\3.png',4:'data\\images\\4.png',5:'data\\images\\5.png',6:'data\\images\\6.png'}
from random import randrange
pygame.init() 
screen=pygame.display.set_mode((825,627),0,32)
pygame.display.set_caption('Flying Chess')
background1=pygame.image.load('data\\images\\background.jpg').convert()
background2=pygame.image.load('data\\images\\backgroundnm.jpg').convert()
buttontouzi=pygame.image.load('data\\images\\touzi.png').convert_alpha()
winp=pygame.image.load('data\\images\\win.png').convert_alpha()
losep=pygame.image.load('data\\images\\lose.png').convert_alpha()
TurnPicture=pygame.image.load('data\\images\\turnp.png').convert_alpha()
pygame.mixer.pre_init(44100,16,2,1024*4)

coor=[[556, 358] ,[556, 391] ,[523, 391] ,[490, 391] ,[457, 391] ,
        [424, 424] ,[424, 457] ,[424, 490] ,[424, 523] ,[391, 523] ,
        [358, 523] ,[325, 523] ,[292, 523] ,[259, 523] ,[226, 523] ,
        [226, 490] ,[226, 457] ,[226, 424] ,[193, 391] ,[160, 391] ,
        [127, 391] ,[94, 391] ,[94, 358] ,[94, 325] ,[94, 292] ,
        [94, 259] ,[94, 226] ,[94, 193] ,[127, 193] ,[160, 193] ,
        [193, 193] ,[226, 160] ,[226, 127] ,[226, 94] ,[226, 61] ,      
        [259, 61] ,[292, 61] ,[325, 61] ,[358, 61] ,[391, 61] ,
        [424, 61] ,[424, 94] ,[424, 127] ,[424, 160] ,[457, 193] ,
        [490, 193] ,[523, 193] ,[556, 193] ,[556, 226] ,[556, 259] ,
        [556, 292] ,[556, 325] ,[556, 358] ,[523, 292] ,[490, 292] ,
        [457, 292] ,[424, 292] ,[391, 292] ,[358, 292] ,[325, 94] ,
        [325, 127] ,[325, 160] ,[325, 193] ,[325, 226] ,[325, 259] ,
        [127, 292] ,[160, 292] ,[193, 292] ,[226, 292] ,[259, 292] ,
        [292, 292] ,[325, 490] ,[325, 457] ,[325, 424] ,[325, 391] ,
        [325, 358],[325,325],
        [507-3,474+15],[547-3,474+15],[507-3,511+15],[547-3,511+15],[596-40,431],
        [507+9,71-15],[547+9,71-15],[507+9,111-15],[547+9,111-15],[464,21+40],
        [104+4,71-14],[144+4,71-14],[104+4,111-14],[144+4,111-14],[54+40,153],
        [104-13,474+17],[144-13,474+17],[104-13,511+17],[144-13,511+17],[186,537],
        [413,380]
      ]

touzi=[0]#显示骰子开关
speed=10#调速开关
      #ready，crash，     arrive
Time=3000
DiceTime=200
turnspeed=200
background=[background1]#背景图
mus=[1]#音乐开关
#初始化
ad=[77,78,79,80,82,83,84,85,87,88,89,90,92,93,94,95]
s=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
state=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

stars=[]
coorstars=[]
plane=[]
CoorTurn=[[544,526]]
for i in range (4):
        o=pygame.image.load('data\\images\\planeb.png').convert_alpha()
        plane.append(o)
for i in range (4):
        o=pygame.image.load('data\\images\\planeg.png').convert_alpha()
        plane.append(o)
for i in range (4):
        o=pygame.image.load('data\\images\\planey.png').convert_alpha()
        plane.append(o)
for i in range (4):
        o=pygame.image.load('data\\images\\planer.png').convert_alpha()
        plane.append(o)
#初始化结束     

def Exit():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        
def End(Picture):
         while 1:
                UpdateWholeBackgroundNoButton()
                screen.blit(Picture,(0,0))
                pygame.display.update()
                if pygame.mouse.get_pressed()[0]:
                        x,y = pygame.mouse.get_pos()
                        if 195<=x<=300 and 494<=y<=526:
                                init()
                                Game()
                        elif 359<=x<=470 and 494<=y<=526:
                                Menu()
                        elif 521<=x<=629 and 494<=y<=526:
                                pygame.quit()
                                sys.exit()    

def Click(d):
        while 1:
                a=b=1
                if pygame.mouse.get_pressed()[0]:
                        a,b = pygame.mouse.get_pos()
                        if d==6:
                                for i in range(4):
                                        if state[i]!=2 and a>coor[ad[i]][0] and a<coor[ad[i]][0]+44 and b>coor[ad[i]][1] and b<coor[ad[i]][1]+44:
                                                return i
                        else:
                                for i in range(4):
                                        if state[i]==1 and a>coor[ad[i]][0] and a<coor[ad[i]][0]+44 and b>coor[ad[i]][1] and b<coor[ad[i]][1]+44:
                                                return i
                        ButtonGame(a,b)
                UpdateWholeBackgroundNoButton()
                pygame.display.update()
  
def ShowDice():
        i=0
        Music(2)
        pygame.time.delay(DiceTime)
        for i in range (10):
                d = randrange(1,7)
                a=dict[d]
                touzi[0]=pygame.image.load(a).convert_alpha()
                UpdateWholeBackgroundNoButton()
                pygame.display.update()
                pygame.time.delay(speed*4)
        return d
def ButtonGame(a,b):
        if a>702 and b>490 and a<812 and b<523:
                if mus[0]==1:
                        mus[0]=0
                        background[0]=background2
                        UpdateWholeBackground()
                else:
                        mus[0]=1
                        background[0]=background1
                        UpdateWholeBackground()
                pygame.time.delay(300)
        elif a>702 and b>532 and a<812 and b<567:
                init()
                Game()
        elif a>702 and b>577 and a<812 and b<807:
                Menu()
def Dice():
        a=b=d=0
        while d==0: 
                if pygame.mouse.get_pressed()[0]:
                        a,b = pygame.mouse.get_pos()
                        if (a-693)**2+(b-420)**2<=2800:
                                d=ShowDice()
                        else:
                                ButtonGame(a,b)
                UpdateWholeBackground()
                pygame.display.update()
        return d
def UpdateBackground(n):#飞机移动时用
        screen.blit(background[0],(0,0))
        screen.blit(TurnPicture,CoorTurn[0])
        for b in range (16):
                if b!=n:
                        screen.blit(plane[b],coor[ad[b]])
        if len(stars)>0:
                for b in range ( len(stars)):
                        screen.blit(stars[b],coorstars[b])
        if touzi[0]!=0:
                screen.blit(touzi[0],[640,160])

def UpdateWholeBackgroundNoButton():#显示骰子读数，无按钮
        screen.blit(background[0],(0,0))
        screen.blit(TurnPicture,CoorTurn[0])
        for b in range (16):
                screen.blit(plane[b],coor[ad[b]])
        if len(stars)>0:
                for b in range (len(stars)):
                        screen.blit(stars[b],coorstars[b])
        if touzi[0]!=0:
                screen.blit(touzi[0],[640,160])
        Exit()
def UpdateWholeBackground():#显示骰子按钮
        UpdateWholeBackgroundNoButton()
        screen.blit(buttontouzi,[640,360])
def Music(mu):
        if mus[0]==1:
                if mu==1:
                        pygame.mixer.music.load('data\\sounds\\landoff.wav')
                        pygame.mixer.music.play()
                elif mu==2:
                        pygame.mixer.music.load('data\\sounds\\click.wav')
                        pygame.mixer.music.play()
                elif mu==3:
                        pygame.mixer.music.load('data\\sounds\\arrive.wav')
                        pygame.mixer.music.play()
                elif mu==4:
                        pygame.mixer.music.load('data\\sounds\\crash.wav')
                        pygame.mixer.music.play()

def SoundDelay():
        if mus[0]==0:
                time=Time/10
        else:
                time=Time
        pygame.time.delay(time)
        
def GoHome(n):
        home=[77,78,79,80,82,83,84,85,87,88,89,90,92,93,94,95]
        if ad[n]!=home[n]:
                TargetFly(n,home[n])
                if n<4:
                        PlanePicture='data\\images\\planeb.png'
                elif n<8:
                        PlanePicture='data\\images\\planeg.png'
                elif n<12:
                        PlanePicture='data\\images\\planey.png'
                elif n<16:
                        PlanePicture='data\\images\\planer.png'
                        
                plane[n]=pygame.image.load(PlanePicture).convert_alpha()
                state[n]=0
                s[n]=0
        UpdateWholeBackgroundNoButton()
        pygame.display.update()
def Transposition(n,degree):
        plane[n] = pygame.transform.flip(plane[n],0,0)
        plane[n] = pygame.transform.rotate(plane[n],degree)
        UpdateWholeBackgroundNoButton()
        pygame.display.update()
        
def Ready(n):
        j=0
        if n in[0,1,2,3]:
                j=81
        elif n in[4,5,6,7]:
                j=86
        elif n in[8,9,10,11]:
                j=91
        elif n in[12,13,14,15]:
                j=96
        Music(1)
        pygame.time.delay(Time/10)
        TargetFly(n,j) 
        state[n]=1
        Transposition(n,90)
        SoundDelay()
        s[n]=0
        
def Launch(n,d):
        if n in[0,1,2,3]:
                j=1
        elif n in[4,5,6,7]:
                j=40
        elif n in[8,9,10,11]:
                j=27
        elif n in[12,13,14,15]:
                j=14
        TargetFly(n,j)            
        d-=1
        s[n]=1
        Fly(n,d)  
def Back(n,d):       
        for i in range (d):
                TargetFly(n,ad[n]-1)
                s[n]-=1
def Fly(n,d):
        for i in range (d):
                if ad[n]+1==53:
                        ad[n]=0
                TargetFly(n,ad[n]+1)
                if ad[n]-1 in [4,17,30,43]:    
                        Transposition(n,90)
                elif ad[n]-1 in [7,13,20,26,33,39,46,0]:
                        Transposition(n,-90)                
        s[n]+=d
def Arrive(n,jh):
        Music(3)
        GoHome(n)
        o=pygame.image.load('data\\images\\star.png').convert_alpha()
        stars.append(o)
        o=coor[ad[n]]
        coorstars.append(o)
        state[n]=2
        UpdateWholeBackgroundNoButton()
        pygame.display.update()
        if mus[0]==0:
                time=Time*6/5/10
        else:
                time=Time*6/5
        pygame.time.delay(time)
        if state[jh[0]]==state[jh[1]]==state[jh[2]]==state[jh[3]]==2:
                if n in [0,1,2,3]:
                        End(winp)
                else:
                        End(losep)
def Move(n,d):
        nb=[0,1,2,3]
        ng=[4,5,6,7]
        ny=[8,9,10,11]
        nr=[12,13,14,15]
        if n in nb:
                jh=nb
                bj=nr+ny+ng
                j1=53
        elif n in ng:
                jh=ng
                bj=nr+ny+nb
                j1=59
        elif n in ny:
                jh=ny
                bj=nr+ng+nb
                j1=65
        elif n in nr:
                jh=nr
                bj=nb+ny+ng
                j1=71
        k=1
        if s[n]+d<=50:#未入 未将入
                Fly(n,d)
                Happen(n)
        else:
                if s[n]<50 and s[n]+d>50:#未入将入
                        e=d-50+s[n]-1
                        Fly(n,50-s[n])
                        Transposition(n,-90)
                        TargetFly(n,j1)
                        s[n]=51
                        Fly(n,e)
                elif s[n]==50:#正要入
                        TargetFly(n,j1)
                        s[n]=51
                        Fly(n,d-1)
                        if s[n]==56:
                                Arrive(n,jh)
                elif s[n]>50 and s[n]+d<56:#已入未到
                        Fly(n,d)
                elif s[n]+d==56:#已到
                        Fly(n,d)
                        Arrive(n,jh)
                elif s[n]+d>56:#超过
                        e=d-56+s[n]
                        Fly(n,56-s[n])
                        Back(n,e)

def QuicklyFly(n):
        if n<4:
                j1,j2=67,30
                bj=[4,5,6,7,8,9,10,11,12,13,14,15]
        elif n<8:
                j1,j2=73,17
                bj=[0,1,2,3,8,9,10,11,12,13,14,15]
        elif n<12:
                j1,j2=55,4
                bj=[0,1,2,3,4,5,6,7,12,13,14,15]
        elif n<16:
                j1,j2=61,43
                bj=[0,1,2,3,4,5,6,7,8,9,10,11]
        Transposition(n,-90)
        TargetFly(n,j1)
        cd=0
        for i in bj:
                if ad[n]==ad[i]:
                        Music(4)
                        GoHome(i)
                        cd+=1
                        SoundDelay()
        if cd>=2:
                Music(4)
                GoHome(n)
                SoundDelay()
                        
        else:
                TargetFly(n,j2)
                s[n]+=12
                Transposition(n,-90)
def TargetFly(n,T):
        x,y=coor[ad[n]]
        x1,y1=coor[T]
        ds =((abs(x1-x)+abs(y1-y))/2.75)
        dx=(x1-x)/ds
        dy=(y1-y)/ds
        ds=int(ds)
        for c in range(ds):
                x+=dx
                y+=dy
                UpdateBackground(n)
                screen.blit(plane[n],(x,y))
                pygame.time.delay(speed)
                pygame.display.update()
        ad[n]=T
def Crash(n,bj):
        cd,k=0,1
        for i in bj:
                if ad[n]==ad[i]:
                        Music(4)
                        GoHome(i)
                        k=0
                        cd+=1
                        SoundDelay()
        if cd>=2:
                Music(4)
                GoHome(n)
                SoundDelay()
        return k

def Happen(n):
        nb=[0,1,2,3]
        ng=[4,5,6,7]
        ny=[8,9,10,11]
        nr=[12,13,14,15]
        if n in nb:
                jh=nb   #该色飞机编号集合
                bj=ng+ny+nr#补集
        elif n in ng:
                jh=ng
                bj=nb+ny+nr
        elif n in ny:
                jh=ny
                bj=nb+ng+nr
        else:
                jh=nr
                bj=nb+ny+ng
        k=1#未撞
        k=Crash(n,bj)
        if k==1:
                if s[n]==14:
                        Fly(n,4)
                        k=Crash(n,bj)
                        if k==1:
                                QuicklyFly(n)
                                k=Crash(n,bj)
                elif s[n]==18:
                        QuicklyFly(n)
                        k=Crash(n,bj)
                        if k==1:
                                d=Fly(n,4)
                                k=Crash(n,bj)
                elif s[n]%4==2 and s[n]+4<=50:
                        Fly(n,4)
                        Crash(n,bj)
        if s[n]==50:
                Transposition(n,-90)
def ComputerTurn(jh,qfd,home,FirstAd,bj) :
        d=ShowDice()
        pygame.time.delay(turnspeed)
        touzi[0]=0
        if d==6:
                n=AI(d,jh,qfd,FirstAd,bj)
                if ad[n]==qfd:
                        Launch(n,d)
                        Happen(n)
                elif ad[n] in home:
                        Ready(n)
                else:
                        Move(n,d)
                ComputerTurn(jh,qfd,home,FirstAd,bj) 
        elif state[jh[0]]==1 or state[jh[1]]==1 or state[jh[2]]==1 or state[jh[3]]==1:
                n=AI(d,jh,qfd,FirstAd,bj)
                if ad[n]==qfd:
                        Launch(n,d)
                        Happen(n)
                else:
                        Move(n,d)
        pygame.time.delay(turnspeed)
def AI(d,jh,qfd,FirstAd,bj):
        a=[0,0,0,0]##快速选择
        for i in range(4):
                a[i]=state[jh[0]+i]
        if d==6:  
                if a.count(2)==3:
                        if a.count(1)==1:
                                return  a.index(1)+jh[0]
                        else:
                                return  a.index(0)+jh[0]
        elif d!=6:
                if a.count(1)==1:
                        return a.index(1)+jh[0]
        NewAd=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for n in jh:#编号变换
                if ad[n]==qfd:
                        NewAd[n]=FirstAd-1
                elif ad[n]+d>52 and ad[n]<=52:
                                NewAd[n]=ad[n]-52
                else:
                        NewAd[n]=ad[n]
        for n in jh:#到达优先
                if s[n]+d==56:
                        return n
        for n in jh:#撞击其次
                if state[n]==1:
                        for i in bj:
                                if ad[i]<=52:
                                        if NewAd[n]+d==ad[i]:
                                                return n
                                        elif (s[n]+d)%4==2 and NewAd[n]+d+4==ad[i]:
                                                return n
        for n in jh:#大飞
                if state[n]==1:
                        if s[n]+d==14 or s[n]+d==18:
                                return n
        if d==6:#ready
                for n in jh:
                        if state[n]==0:
                                return n
        for n in jh:#多走四步
                if s[n]<50 and (s[n]+d)%4==2 and state[n]==1:
                        return n
        for n in jh:#逼近终点
                if s[n]>=50 and s[n]+d<56:
                        return n
        n=randrange(jh[0],jh[3]+1)
        while state[n]==2 or (state[n]==0 and d!=6):
                n=randrange(jh[0],jh[3]+1)
        return n

        
def GTurn():
        CoorTurn[0]=[596,56]
        jh=[4,5,6,7]
        qfd=86
        home=[82,83,84,85]
        FirstAd,bj=40,[0,1,2,3,8,9,10,11,12,13,14,15]
        ComputerTurn(jh,qfd,home,FirstAd,bj) 
def YTurn():
        CoorTurn[0]=[51+25,56]
        jh=[8,9,10,11]
        qfd=91
        home=[87,88,89,90]
        FirstAd,bj=27,[0,1,2,3,4,5,6,7,12,13,14,15]
        ComputerTurn(jh,qfd,home,FirstAd,bj) 
def RTurn():
        CoorTurn[0]=[51+7,528]
        jh=[12,13,14,15]
        qfd=96
        home=[92,93,94,95]
        FirstAd,bj=14,[0,1,2,3,4,5,6,7,8,9,10,11]
        ComputerTurn(jh,qfd,home,FirstAd,bj) 
def UserTurn():
        jh=[0,1,2,3]
        a=[0,0,0,0]
        CoorTurn[0]=[584,526]
        d=Dice()
        if d==6:
                for n in jh:
                        a[n]=state[n]
                if a.count(2)==3:
                        if a.count(0)==1:
                                return  a.index(0)
                        else:
                                return a.index(1)
                else:
                        n=Click(d)
                        
                if ad[n]==81:
                        Launch(n,d)
                        Happen(n)
                elif ad[n] in [77,78,79,80]:
                        Ready(n)
                elif ad[n] in range(76):
                        Move(n,d)
                UserTurn()
        elif state[0]==1 or state[1]==1 or state[2]==1 or state[3]==1:
                for n in jh:
                        a[n]=state[n]
                if a.count(1)==1:
                        n=a.index(1)
                else:
                        n=Click(d)
                        
                if ad[n]==81:
                        Launch(n,d)
                        Happen(n)
                elif ad[n] in range(76):
                        Move(n,d)
        pygame.time.delay(turnspeed)
def init():
        for i in range(16):
                GoHome(i)
                state[i]=0
                s[i]=0
        a=len(stars)
        for i in range(a):
                stars[len(stars)-1]=0
                coorstars[len(coorstars)-1]=0
                stars.remove(0)
                coorstars.remove(0)
        CoorTurn=[[544,526]]
                        
                        
def Game():
        while 1:
                Exit()
                UpdateWholeBackgroundNoButton()
                pygame.display.update()
                UserTurn()
                GTurn()
                YTurn()
                RTurn()

        
def Background_Music():
        if mus[0]==1: 
                backgroundone=pygame.image.load('data\\images\\music.jpg')
        else:
                backgroundone=pygame.image.load('data\\images\\quiet.jpg')
        x,y=0,0
        while 1:
                screen.blit(backgroundone,(0,0))
                x,y=pygame.mouse.get_pos()
                pygame.display.update()
                Exit()
                if pygame.mouse.get_pressed()[0]:
                        a,b = pygame.mouse.get_pos()
                        if a>=258 and a<=403 and b>=302 and b<=431:
                                mus[0]=1#有声音
                                background[0]=background1
                                backgroundone=pygame.image.load('data\\images\\music.jpg')
                        elif a>=537 and a<=680 and b>=296 and b<=428:
                                mus[0]=0#无声音
                                background[0]=background2
                                backgroundone=pygame.image.load('data\\images\\quiet.jpg')
                        elif a>=41 and a<=238 and b>=49 and b<=145:
                                return
           
##Help（帮助）
##游戏规则没说明                                   
def Help():
        backgroundtwo=pygame.image.load('data\\images\\help_background.jpg')
        x,y=0,0
        while True:
                screen.blit(backgroundtwo,(0,0))
                x,y=pygame.mouse.get_pos()    
                pygame.display.update()
                Exit()
                if pygame.mouse.get_pressed()[0]:
                        a,b = pygame.mouse.get_pos()
                        if a>=614 and a<=792 and b>=520 and b<=612:
                                return
       
##The menu of game（游戏菜单）                                  
def Menu():
        menu=pygame.image.load('data\\images\\menu1.jpg')
        while True:
                screen.blit(menu,(0,0))
                pygame.display.update()
                Exit()
                x,y=0,0
                if pygame.mouse.get_pressed()[0]:
                        a,b = pygame.mouse.get_pos()
                        if (a-350)*(a-350)+(b-155)*(b-155)<8100:
                                Background_Music()
                        elif (a-725)*(a-725)+(b-270)*(b-270)<6400:
                                pygame.quit()
                                sys.exit()         
                        elif (a-495)*(a-495)+(b-355)*(b-355)<4900:
                                Help()
                        elif (a-120)*(a-120)+(b-256)*(b-256)<10000:
                                Game()  
            
Menu()
