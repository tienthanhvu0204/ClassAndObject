import turtle
from datetime import datetime

class Clock:
    def __init__ (self, h = 0, m = 0, s = 0, r = 100, x = 0, y = 0):
        # Hàm khởi tạo với các giá trị giờ phút giây, bán kính đồng hồ, tọa độ tâm
        self.h = h
        self.m = m
        self.s = s
        self.r = r
        self.x = x
        self.y = y
    # Hàm vẽ vòng tròn đồng hồ
    def drawClock (self, color):
        # r bán kính đường tròn đồng hồ, x,y tọa độ tâm đồng hồ
        r = self.r
        x = self.x
        y = self.y
        t = turtle.Turtle ()
        t.hideturtle ()
        t.penup ()
        t.goto (x, y - r)
        t.pendown ()
        t.pensize (2)
        t.fillcolor (color)
        t.begin_fill ()
        t.circle (r)
        t.end_fill ()
        t.penup ()
        t.goto (x, y)
        t.pensize (1)
        for i in range (60):
            if i%5 == 0:
                j = r / 10
            else:
                j = r / 20
            t.fd (r - j - 5)
            t.pendown ()
            t.fd (j)
            t.penup ()
            t.goto (x, y)
            t.lt (6)

    def runClockHand (self):
        # r bán kính đường tròn đồng hồ, x,y tọa độ tâm đồng hồ
        r = self.r
        x = self.x
        y = self.y
        hourError = datetime.now().hour - self.h
        minuteError = datetime.now().minute - self.m
        secondError = datetime.now().second -self.s

        t0 = turtle.Turtle ()
        t0.hideturtle ()

        t1 = turtle.Turtle ()
        t1.hideturtle ()

        t2 = turtle.Turtle ()
        t2.hideturtle ()
    
        def drawHourHand ():
            t0.penup ()
            t0.home ()
            t0.goto (x, y)
            hour = datetime.now().hour - hourError
            minute = datetime.now().minute - minuteError
            t0.rt (hour * 30 + minute * 0.5 - 90)
            t0.pendown ()
            t0.pensize (3)
            t0.color ("#00008B")
            t0.fd (r * 3 / 5)

        # Hàm vẽ kim phút
        def drawMinuteHand ():
            t1.penup ()
            t1.home ()
            t1.goto (x, y)
            minute = datetime.now().minute - minuteError
            t1.rt (minute * 6 - 90)
            t1.pendown ()
            t1.pensize (2)
            t1.color ("#8B0000")
            t1.fd (r * 3.5 / 5)
        
        # Hàm vẽ kim giây
        def drawSecondHand ():
            t2.penup ()
            t2.home ()
            t2.goto (x, y)
            second = datetime.now().second - secondError
            t2.rt (second * 6 - 90)
            t2.pendown ()
            t2.pensize (1)
            t2.color ("#FF0000")
            t2.fd (r * 4 / 5)
            
        # infinite loop, đồng hồ chạy liên tục
        while True:
            # print (time.time ())
            # Tạo chuyển động kim giờ mỗi 60s
            t0.clear ()
            drawHourHand ()
            screen.update ()

            # Tạo chuyển động cho kim phút mỗi 60s
            t1.clear()
            drawMinuteHand ()
            screen.update()
            # Vòng lặp cho 1 phút

            # for i in range (60):
            # Tạo chuyển động cho kim giây mỗi 1s
            t2.clear() 
            drawSecondHand ()
            screen.update()
            
            # Thời gian delay để chạy đúng thời gian, do có sai số nên một số thời điểm kim sẽ nhảy 2 bước nếu chọn theo thời gian thực
            # time.sleep (0.98)
                

screen = turtle.Screen ()
screen.bgcolor ("#FFEBCD")
screen.tracer(0) 

h = 0
m = 0
s = 0
# print (h, m, s)

dongho = Clock (h, m, s, 150, 10, -50)
dongho.drawClock ("#008000")
dongho.runClockHand ()








