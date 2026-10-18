import pygame as pg
from numpy import zeros, shape, array,kron, dot,transpose, conjugate, all , trace,empty,real
from math import sqrt, cos ,sin, pi,e
from matplotlib.pyplot import bar, title, xlabel, ylabel, savefig, ylim, imshow, clf
from PIL import Image
import vpython as vp


#單位設定-------------------------------------------------------------------------

unit=50
nCol=20
nRaw=12

#12個按鈕設定(讀取圖片，取得圖片中心座標)---------------------------------------------------------------------

class Hgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Hgate,self).__init__()
        self.image = pg.image.load("hgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class Xgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Xgate,self).__init__()
        self.image = pg.image.load("xgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class CNOTgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(CNOTgate,self).__init__()
        self.image = pg.image.load("cnotgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class Ygate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Ygate,self).__init__()
        self.image = pg.image.load("ygate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class Tgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Tgate,self).__init__()
        self.image = pg.image.load("tgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class Sgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Sgate,self).__init__()
        self.image = pg.image.load("sgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id         
class Zgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Zgate,self).__init__()
        self.image = pg.image.load("zgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class RZgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(RZgate,self).__init__()
        self.image = pg.image.load("rzgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class Zmeasurement(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Zmeasurement,self).__init__()
        self.image = pg.image.load("zmeasurement.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class Ostate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Ostate,self).__init__()
        self.image = pg.image.load("0state.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class RXgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(RXgate,self).__init__()
        self.image = pg.image.load("rxgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class RYgate(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(RYgate,self).__init__()
        self.image = pg.image.load("rygate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
class Probability_image(pg.sprite.Sprite):
    def __init__(self,xpos,ypos,id):
        super(Probability_image,self).__init__()
        self.image = pg.image.load("probabilities1.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
        self.id = id 
        
#選擇框設定-----------------------------------------------------------------------------

class Select():
    def __init__(self,xpos,ypos):
        super(Select,self).__init__()
        self.image = pg.image.load("xgate.png")
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.rect.center  = xpos,ypos
    def draw(self):
        pg.draw.rect(window, (220,220,220), self.rect, 4)  
        
#user------------------------------------------------------------------

class User():
    def __init__(self,name):
        self.name = name
    #判斷滑鼠移動狀態，並判斷按鈕哪個被移到，即被移到哪裡，及按鈕對應矩陣
    def Move(self):
       #利用pg.sprite.Group使每個按鈕無限產生
       zmeasurement_number = 0
       operation = ''
       Operator_list = pg.sprite.Group()
       Operator_list.add(Hgate(45,65,1))
       Operator_list.add(Xgate(105,65,1))
       Operator_list.add(CNOTgate(165,65,1))
       Operator_list.add(Tgate(225,65,1))
       Operator_list.add(Sgate(45,145,1))
       Operator_list.add(Zgate(105,145,1))
       Operator_list.add(RZgate(165,145,1))
       Operator_list.add(Zmeasurement(225,145,1))
       Operator_list.add(Ostate(45,225,1))
       Operator_list.add(Ygate(105,225,1))
       Operator_list.add(RXgate(165,225,1))
       Operator_list.add(RYgate(225,225,1))
       operator_and_position = []
       drawagain_position = []
       drawagain_operation = []
       matrix = []
       C = 0
       All_1 = [0 for i in range(0,11,1)]
       All_2 = [0 for i in range(0,11,1)]
       #判斷滑鼠移到位置，繪製選擇框，並記錄位置
       def square_under_mouse(drag_position):
           for i in range(60,121,60):
               for j in range(325,986,60):
                   if i<drag_position[1]<i+60 and j<drag_position[0]<j+60:
                       #判斷有沒有在格子裡
                       select_position = Select(j+30,i+30)
                       select_position.draw()
                       #判斷在整個whiteboard中的相對位置
                       if i == 60:
                           yy = 0
                       if i ==120:
                           yy = 1
                       k = 0
                       I = [325,385,445,505,565,
                            625,685,745,805,865,925]
                       while I[k]!=j:
                           k+=1
                       xx = k
                       operator_and_position.append([xx,yy])
           return operator_and_position
       state = 'waiting'
       #當視窗被點開後
       while state=='waiting':
           #螢幕設定
           window.fill(gainsboso)#一定要加，不然會連續出現
           window.blit(whiteboard, (275,0))
           pg.draw.line(window, (105,105,105), (0,275), (1000, 275), 2) 
           pg.draw.line(window, (105,105,105), (274,0), (274,275), 2) 
           pg.draw.rect(window, (128,128,128),rect1,0)
           window.blit(text1,(870,230))
           whiteboard.blit(text2,text2rect)
           whiteboard.blit(text3,text3rect)
           whiteboard.blit(text4,text4rect)
           window.blit(HGATE,HGATE1)
           window.blit(XGATE,XGATE1)
           window.blit(CNOTGATE,CNOTGATE1)
           window.blit(TGATE,TGATE1)
           window.blit(SGATE,SGATE1)
           window.blit(ZGATE,ZGATE1)
           window.blit(RZGATE,RZGATE1)
           window.blit(ZMEASUREMENT,ZMEASUREMENT1)
           window.blit(OSTATE,OSTATE1)
           window.blit(YGATE,YGATE1)
           window.blit(RXGATE,RXGATE1)
           window.blit(RYGATE,RYGATE1)
           for i in range(0,len(drawagain_operation),1):
               window.blit(drawagain_operation[i],drawagain_position[i])
           #判斷滑鼠狀態
           for event in pg.event.get():
               #若按下關閉鍵
               if event.type == pg.QUIT:
                   state = 'finished'
               #若按下按鈕
               if event.type == pg.MOUSEBUTTONDOWN:
                   pos =  pg.mouse.get_pos()     #找出滑鼠座標
                   x = pos[0]
                   y=  pos[1]
                   if event.button == 1:         #若按左鍵
                       #若不小心按到其他地方，關閉視窗
                       try:
                       #判斷按到哪個按鈕    
                       #第一行    
                           if 20<pos[0]<70 and 40<pos[1]<90:
                               operation = 'hgate'
                               H = empty((2,2),dtype=complex)
                               H[0,0] = 1
                               H[1,0] = 1
                               H[0,1] = 1
                               H[1,1] = -1
                               H = H*1/sqrt(2)
                               matrix = H
                           if 80<pos[0]<130 and 40<pos[1]<90:
                               operation = 'xgate'
                               X = empty((2,2),dtype=complex)
                               X[0,0] = 0
                               X[1,0] = 1
                               X[0,1] = 1
                               X[1,1] = 0
                               matrix = X
                           if 140<pos[0]<190 and 40<pos[1]<90:
                               operation = 'cnot'
                               CNOT = zeros((4,4),dtype=(complex))
                               CNOT[0,0] = 1
                               CNOT[1,1] = 1
                               CNOT[2,3] = 1
                               CNOT[3,2] = 1
                               matrix = CNOT
                           if 200<pos[0]<250 and 40<pos[1]<90:
                               operation = 'tgate'
                               T = empty((2,2),dtype=complex)
                               T[0,0] = 1
                               T[0,1] = 0
                               T[1,0] = 0
                               T[1,1] = e**(1j*pi/4)  # exp()不能打複數
                               matrix = T #這邊若設 T = T(pi) 則後面 Tdagger內的T(theta))發生錯誤，因為此時T is not the array
                           #第二行
                           if 20<pos[0]<70 and 120<pos[1]<170:
                               operation = 'sgate'
                               S = empty((2,2),dtype=complex)
                               S[0,0] = 1
                               S[0,1] = 0
                               S[1,0] = 0
                               S[1,1] = 1j
                               matrix = S
                           if 80<pos[0]<130 and 120<pos[1]<170:
                               operation = 'zgate'
                               Z = empty((2,2),dtype=complex)
                               Z[0,0] = 1
                               Z[0,1] = 0
                               Z[1,0] = 0
                               Z[1,1] = -1
                               matrix = Z
                           if 140<pos[0]<190 and 120<pos[1]<170:
                               operation = 'rzgate'
                               def Rz(theta):
                                   Rz = empty((2,2),dtype=complex)
                                   Rz[0,0] = e**(-1j*theta/2)
                                   Rz[0,1] = 0
                                   Rz[1,0] = 0
                                   Rz[1,1] = e**(1j*theta/2)
                                   return Rz
                               matrix = Rz(pi/2)
                           if 200<pos[0]<250 and 120<pos[1]<170:
                               operation = 'zmeasurement'
                               zmeasurement_number = 1
                               unit_matrix = zeros((2,2),dtype=(complex))
                               unit_matrix[0,0] = 1
                               unit_matrix[1,1] = 1
                               matrix = unit_matrix
                           #第三行
                           if 20<pos[0]<70 and 200<pos[1]<250:
                               operation = 'ostate'
                               O = zeros((2,1),dtype=(complex))
                               O[0,0] = 1
                               matrix = O
                           if 80<pos[0]<130 and 200<pos[1]<250:
                               operation = 'ygate'
                               Y = empty((2,2),dtype=complex)
                               Y[0,0] = 0
                               Y[0,1] = -1j
                               Y[1,0] = 1j
                               Y[1,1] = 0
                               matrix = Y
                           if 140<pos[0]<190 and 200<pos[1]<250:
                               operation = 'rxgate'
                               def Rx(theta):
                                   Rx = empty((2,2),dtype=complex)
                                   Rx[0,0] = cos(theta/2)
                                   Rx[0,1] = -1j*sin(theta/2)
                                   Rx[1,0] = -1j*sin(theta/2)
                                   Rx[1,1] = cos(theta/2)
                                   return Rx
                               matrix = Rx(pi/2)
                           if 200<pos[0]<250 and 200<pos[1]<250:
                               operation = 'rygate'
                               def Ry(theta):
                                   Ry = empty((2,2),dtype=complex)
                                   Ry[0,0] = cos(theta/2)
                                   Ry[0,1] = -sin(theta/2)
                                   Ry[1,0] = -sin(theta/2)
                                   Ry[1,1] = cos(theta/2)
                                   return Ry
                               matrix = Ry(pi/2) 
                           #若是calculate鍵被按下
                           if rect1.collidepoint(event.pos):
                               pg.draw.rect(window, (255,0,0),rect1,0)
                               window.blit(text1,(870,230))
                               print('Calculate button has been pressed.')
                               unit_matrix = zeros((2,2),dtype=(complex))
                               unit_matrix[0,0] = 1
                               unit_matrix[1,1] = 1
                               #跑出電路兩行元素，有空的元素補上unit matrix
                               for i in range(0,11,1):
                                   if shape(All_1[i]) == shape(C):
                                       All_1.pop(i)
                                       All_1.insert(i,unit_matrix)
                                   if shape(All_2[i]) == shape(C):
                                       All_2.pop(i)
                                       All_2.insert(i,unit_matrix)
                               AllAll_1 = All_1
                               AllAll_2 = All_2
                               All_1 = []
                               All_2 = []
                               state = 'f' 
                               return AllAll_1,AllAll_2,zmeasurement_number
                           #判斷哪個按鈕被按下
                           for operator in Operator_list:
                               if operator.rect.collidepoint(pos):
                                   operator.clicked = True
                           operator_and_position.append(matrix)
                           operator_and_position.append(operation)
                       except:
                            state = 'finish'
                            print("操作錯誤")
                            print('請一次點選運算子按鈕並移到可以放的格子內')
                            print('不可中途重複按或放開按鈕又移到其他地方')
                            pg.quit()
               #滑鼠在移動
               if event.type == pg.MOUSEMOTION:
                   for operator in Operator_list:
                       if operator.clicked == True:
                           drag_position = pg.mouse.get_pos()
                           drag_position=list(drag_position)#tuple轉成list
                           square_under_mouse(drag_position)#劃出選擇框並輸出位置            
               if event.type == pg.MOUSEBUTTONUP:
                   #把按下哪個變數復原
                   for operator in Operator_list:
                       operator.clicked = False
                   #原本移走的在滑鼠放開後都補上一個
                   #此部分也使最後出現機率圖，螢幕翻新後，電路還會存在
                   #若不小心按到其他地方或移到不是電路上，關閉視窗
                   try:
                       #第一排
                       if operation=='hgate':
                           Operator_list.add(Hgate(45,65,len(Operator_list)+1))
                           OPERATION = HGATE
                       if operation== 'xgate':
                           Operator_list.add(Xgate(105,65,len(Operator_list)+1))
                           OPERATION = XGATE
                       if operation== 'cnot':
                           Operator_list.add(CNOTgate(165,65,len(Operator_list)+1))
                           OPERATION = CNOTGATE
                       if operation=='tgate':
                           Operator_list.add(Tgate(225,65,len(Operator_list)+1))
                           OPERATION = TGATE
                       #第二排    
                       if operation=='sgate':
                           Operator_list.add(Sgate(45,145,len(Operator_list)+1))
                           OPERATION = SGATE
                       if operation== 'zgate':
                           Operator_list.add(Zgate(105,145,len(Operator_list)+1))
                           OPERATION = ZGATE
                       if operation== 'rzgate':
                           Operator_list.add(RZgate(165,145,len(Operator_list)+1))   
                           OPERATION = RZGATE
                       if operation=='zmeasurement':
                           Operator_list.add(Zmeasurement(225,145,len(Operator_list)+1))
                           OPERATION = ZMEASUREMENT
                       #第三行
                       if operation=='ostate':
                           Operator_list.add(Ostate(45,225,len(Operator_list)+1))
                           OPERATION = OSTATE
                       if operation== 'ygate':
                           Operator_list.add(Ygate(105,225,len(Operator_list)+1))
                           OPERATION = YGATE
                       if operation== 'rxgate':
                           Operator_list.add(RXgate(165,225,len(Operator_list)+1))   
                           OPERATION = RXGATE
                       if operation=='rygate':
                           Operator_list.add(RYgate(225,225,len(Operator_list)+1))
                           OPERATION = RYGATE
                       drag_position[0] = drag_position[0]-25
                       drag_position[1] = drag_position[1]-25
                       drawagain_position.append(drag_position)
                       drawagain_operation.append(OPERATION)   
                       #滑鼠放開，把移到的相對位置和operator紀錄
                       #y座標是0，第零排
                       #移到不是電路上，關閉視窗
                       if type(operator_and_position[len(operator_and_position)-1]) ==list:
                           pass
                       else:
                            state = 'finish'
                            print("操作錯誤")
                            print('請一次點選運算子按鈕並移到可以放的格子內')
                            print('不可中途重複按或放開按鈕又移到其他地方')
                            pg.quit()
                        
                       if operator_and_position[len(operator_and_position)-1][1]==0:
                           for i in range(0,11,1):
                                if operator_and_position[len(operator_and_position)-1][0]==i:
                                    All_1.pop(i) #抽掉原本設的0矩陣元素
                                    All_1.insert(i,operator_and_position[0])#補上對應矩陣
                        #y座標是1，第一排
                       if operator_and_position[len(operator_and_position)-1][1]==1:
                           for i in range(0,11,1):
                                if operator_and_position[len(operator_and_position)-1][0]==i:
                                    All_2.pop(i) #抽掉原本設的0矩陣元素
                                    All_2.insert(i,operator_and_position[0]) #補上對應矩陣
                       operator_and_position = []
                   except:
                       print("操作錯誤")
                       print('請一次點選運算子按鈕並移到可以放的格子內')
                       print('不可中途重複按或放開按鈕又移到其他地方')
                       pg.quit()
           #計算每個按鈕中心點的位置，為了109行要判斷位置
           for operator in Operator_list:
               if operator.clicked == True:
                   pos =pg.mouse.get_pos()
                   operator.rect.x = pos[0]-(operator.rect.width/2)
                   operator.rect.y = pos[1]-(operator.rect.height/2)
           Operator_list.draw(window)
           pg.display.flip()
           #視窗翻新率
           clock.tick(60) 
           
#-----------------------------------------------------------------------------------------

#server
class Server():
    #初始化
    def __init__(self,name):
        self.state = 'start'
        #時間翻新針數
        self.clock = pg.time.Clock()
        self.user = User(name)
        #回傳電路第一排和第二排，與其中的每個位置小矩陣
    #當按關閉鍵，關閉
    def Finish(self):
        while self.state!='finish':           
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.state = 'finish'
    #計算電路及畫出機率圖和Q-sphere
    def Calculate_and_Draw(self):
        unit_matrix = zeros((2,2),dtype=(complex))
        unit_matrix[0,0] = 1
        unit_matrix[1,1] = 1
        #引入Move()的回傳結果
        line = self.user.Move()
        O = line[0] 
        l = line[1]
        phi_ket = kron(unit_matrix,unit_matrix)
        CNOT = zeros((4,4),dtype=(complex))
        CNOT[0,0] = 1
        CNOT[1,1] = 1
        CNOT[2,3] = 1
        CNOT[3,2] = 1
        Z = empty((2,2),dtype=complex)
        Z[0,0] = 1
        Z[0,1] = 0
        Z[1,0] = 0
        Z[1,1] = -1
        #運算過程
        for i in range (0,11,1):
            if shape(O[i]) == shape(CNOT) :  #因cnot矩陣較大，因此不用再和unit matrix相乘#比較兩者矩陣大小
                if all(O[i] == CNOT):   #比較矩陣內的每個元素是否相等
                    phi_ket = dot(conjugate(transpose(O[i])),phi_ket)
            else :
                if i ==0:
                    phi_ket = dot(conjugate(transpose(phi_ket)),kron(O[i],l[i]))#先第一行中元素與第二行矩陣tensor，在與上個結果內積
                else:
                    phi_ket = dot(conjugate(transpose(kron(O[i],l[i]))),phi_ket)#先第一行中元素與第二行矩陣tensor，在與上個結果內積
        #計算projector
        phi_bra = conjugate(transpose(phi_ket))
        density_matrix = dot(phi_ket,phi_bra)
        EA0 = (unit_matrix + Z)/2
        EA1 = (unit_matrix - Z)/2
        EB0 = (unit_matrix + Z)/2
        EB1 = (unit_matrix - Z)/2
        #print(dot(kron(EA0,EB0),density_matrix))
        #計算probability
        P00 = trace(dot(kron(EA0,EB0),density_matrix))
        P01 = trace(dot(kron(EA0,EB1),density_matrix))
        P10 = trace(dot(kron(EA1,EB0),density_matrix))
        P11 = trace(dot(kron(EA1,EB1),density_matrix))
        #print(P00,P01,P10,P11)
        #產生Probability圖------------------------------------------------------
        """
        Probabilities 長條圖
        """
        x = ['00','01','10','11']
        y = [P00,P01,P10,P11]  #輸入 Probabilities
        y = [P00,P01,P10,P11]  #輸入 Probabilities
        y = real(y) #繪圖需要先將 y 轉換成實數 
        # 清除上一輪的圖
        clf()
        #繪製長條圖
        bar(x, y)
        title('Probabilities')
        ylabel('Probability')
        xlabel('Computational basis state')
        ylim(0, 1)  # 設定Y軸的取值0到1
        savefig('Probabilities.png',dpi=300)  # 設定分辨率為300dpi
        #用PIL中Image進行縮圖製作
        img = Image.open( "Probabilities.png" )
        img.thumbnail( (450,300) ) #指定長與寬並進行縮圖製作
        img.save( "Probabilities1.png" )
        #讓圖出現在視窗上
        pro = pg.image.load('Probabilities1.png')
        pro_rect = pro.get_rect()
        pro_rect.center = (500,435)
        window.blit(pro,pro_rect)
        pg.display.update()   #更新視窗
        
        #產生bloch sphere圖----------------------------------------------------------------
        """
        Q-sphere #只是單純讓使用者可以具體點的知道做出來的結果在Q-sphere上的位置在哪
        """
        # 設定圓環的參數
        radius = 0.5   # 圓環的半徑
        thickness = 0.01  # 圓環的厚度
        # 建立圓環
        vp.ring(pos=vp.vector(0, 0, 0), axis=vp.vector(0, 0, 1), radius=radius, thickness=thickness, color=vp.color.white)
        vp.ring(pos=vp.vector(0, 0, 0), axis=vp.vector(0, 1, 0), radius=radius, thickness=thickness, color=vp.color.white)
        #判斷有沒有放zmeasurement，所畫出的Q-Sphere會不同
        if line[2] == 1:
            if real(P00) != 0 or real(P11) != 0 and real(P10) == 0 and real(P01) == 0 :
                vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(0,0.5,0), color=vp.color.blue)
                vp.text(pos=vp.vector(0, 0.6, 0), text="|00>", align='center', color=vp.color.white,height=0.1)
            elif real(P01) != 0 or real(P10) != 0 and real(P00) == 0 and real(P11) == 0 :
                vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(0.5,0,0), color=vp.color.blue)
                vp.text(pos=vp.vector(0.7, 0, 0), text="|01>", align='center', color=vp.color.white,height=0.1)
            else:
                if real(P00) != 0:
                    vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(0,0.5,0), color=vp.color.blue)
                    vp.text(pos=vp.vector(0, 0.6, 0), text="|00>", align='center', color=vp.color.white,height=0.1)
                if real(P01) != 0:
                    vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(-0.5,0,0), color=vp.color.blue)
                    vp.text(pos=vp.vector(-0.7, 0, 0), text="|01>", align='center', color=vp.color.white,height=0.1)
                if real(P10) != 0:
                    vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(0.5,0,0), color=vp.color.blue)
                    vp.text(pos=vp.vector(0.7, 0, 0), text="|10>", align='center', color=vp.color.white,height=0.1)
                if real(P11) != 0:
                    vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(0,-0.5,0), color=vp.color.blue)
                    vp.text(pos=vp.vector(0, -0.7, 0), text="|11>", align='center', color=vp.color.white,height=0.1)
        elif line[2] == 0:
            if real(P00) != 0:
                vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(0,0.5,0), color=vp.color.blue)
                vp.text(pos=vp.vector(0, 0.6, 0), text="|00>", align='center', color=vp.color.white,height=0.1)
            if real(P01) != 0:
                vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(-0.5,0,0), color=vp.color.blue)
                vp.text(pos=vp.vector(-0.7, 0, 0), text="|01>", align='center', color=vp.color.white,height=0.1)
            if real(P10) != 0:
                vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(0.5,0,0), color=vp.color.blue)
                vp.text(pos=vp.vector(0.7, 0, 0), text="|10>", align='center', color=vp.color.white,height=0.1)
            if real(P11) != 0:
                vp.arrow(pos = vp.vector(0,0,0),axis = vp.vector(0,-0.5,0), color=vp.color.blue)
                vp.text(pos=vp.vector(0, -0.7, 0), text="|11>", align='center', color=vp.color.white,height=0.1)
#----------------------------------------------------------------    
pg.init()
#介面設定
gainsboso = (220,220,220)
pg.display.set_caption('IBMQ Simulator')
window=pg.display.set_mode((unit*nCol,unit*nRaw))
whiteboard = pg.Surface((14.5*unit, 5.5*unit))
whiteboard.fill((255,255,255))   #以白色填滿
window.blit(whiteboard, (275,0))
#按鈕
font = pg.font.SysFont("Arial", 18)
text1=font.render(" Calculate ", True, (0,0,0))
rect1 = text1.get_rect(center=(880,230),width =120,height = 40)
pg.draw.rect(window, (128,128,128),rect1,0)
#q0 q1 c2
font = pg.font.SysFont("Arial", 18)
text2=font.render(" q [0] ", True, (128,128,128))
text2rect = text2.get_rect()
text2rect.center = (25,90)
font = pg.font.SysFont("Arial", 18)
text3=font.render(" q [1] ", True, (128,128,128))
text3rect = text3.get_rect()
text3rect.center = (25,150)
font = pg.font.SysFont("Arial", 18)
text4=font.render(" c2 ", True, (128,128,128))
text4rect = text4.get_rect()
text4rect.center = (25,210)
#12個按鈕
#第一行
HGATE = pg.image.load("hgate.png")
HGATE1 = HGATE.get_rect()
HGATE1.center = (45,65)
XGATE = pg.image.load('xgate.png')
XGATE1 = XGATE.get_rect()
XGATE1.center = (105,65)
CNOTGATE = pg.image.load('cnotgate.png')
CNOTGATE1 = CNOTGATE.get_rect()
CNOTGATE1.center = (165,65)
TGATE = pg.image.load('tgate.png')
TGATE1 = TGATE.get_rect()
TGATE1.center = (225,65)
#第二行
SGATE = pg.image.load('sgate.png')
SGATE1 = XGATE.get_rect()
SGATE1.center = (45,145)
ZGATE = pg.image.load('Zgate.png')
ZGATE1 = ZGATE.get_rect()
ZGATE1.center = (105,145)
RZGATE = pg.image.load('rzgate.png')
RZGATE1 = RZGATE.get_rect()
RZGATE1.center = (165,145)
ZMEASUREMENT = pg.image.load('zmeasurement.png')
ZMEASUREMENT1 = ZMEASUREMENT.get_rect()
ZMEASUREMENT1.center = (225,145)
#第三行
OSTATE = pg.image.load('0state.png')
OSTATE1 = OSTATE.get_rect()
OSTATE1.center = (45,225)
YGATE = pg.image.load('ygate.png')
YGATE1 = YGATE.get_rect()
YGATE1.center = (105,225)
RXGATE = pg.image.load('rxgate.png')
RXGATE1 = RXGATE.get_rect()
RXGATE1.center = (165,225)
RYGATE = pg.image.load('rygate.png')
RYGATE1 = RYGATE.get_rect()
RYGATE1.center = (225,225)

clock = pg.time.Clock()#螢幕翻新速度 

pg.draw.line(whiteboard, (128,128,128), (40,90), (710, 90), 2)
pg.draw.line(whiteboard, (128,128,128), (40,150), (710, 150), 2)
pg.draw.line(whiteboard, (128,128,128), (40,210), (710, 210), 1)

pg.display.flip()   #更新視窗

print('This is a IBMQ Simulator.')

#main--------------------------------------------------------------------------------

#初始化
server = Server('Irene')
#calculate and draw graph& Q-sphere
server.Calculate_and_Draw()
#當按下關閉鍵，螢幕關閉
server.Finish()
pg.quit()
      