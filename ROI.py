import numpy as np
import matplotlib.pyplot as plt
def roi_region(c1,c2,l,b,xi,yi,xf,yf,a):
    a=a*(np.pi)/180
    x1=c1-b/2
    y1=c2-l/2
    x2=c1+b/2
    y2=c2-l/2
    x3=c1+b/2
    y3=c2+l/2
    x4=c1-b/2
    y4=c2+l/2                                                         #calculaton of co-ordinates
    fx1=round((x1-c1)*(np.cos(a))-(y1-c2)*(np.sin(a))+c1,1)
    fy1=round((x1-c1)*(np.sin(a))+(y1-c2)*(np.cos(a))+c2,1)
    fx2=round((x2-c1)*(np.cos(a))-(y2-c2)*(np.sin(a))+c1,1)
    fy2=round((x2-c1)*(np.sin(a))+(y2-c2)*(np.cos(a))+c2,1)
    fx3=round((x3-c1)*(np.cos(a))-(y3-c2)*(np.sin(a))+c1,1)
    fy3=round((x3-c1)*(np.sin(a))+(y3-c2)*(np.cos(a))+c2,1)
    fx4=round((x4-c1)*(np.cos(a))-(y4-c2)*(np.sin(a))+c1,1)
    fy4=round((x4-c1)*(np.sin(a))+(y4-c2)*(np.cos(a))+c2,1)          #rotation of co-ordinates through angle a
    if xi<=fx1<=xf and xi<=fx2<=xf and xi<=fx3<=xf and xi<=fx4<=xf and yi<=fy1<=yf and yi<=fy2<=yf and yi<=fy3<=yf and yi<=fy4<=yf:
        print('Initial Coordinates:',(fx1,fy1),(fx2,fy2),(fx3,fy3),(fx4,fy4))
        plt.plot([fx1,fx2,fx3,fx4,fx1],[fy1,fy2,fy3,fy4,fy1])
        plt.show()
    else:
        print('Initial Coordinates:',(fx1,fy1),(fx2,fy2),(fx3,fy3),(fx4,fy4))
        xc=[fx1,fx2,fx3,fx4]
        yc=[fy1,fy2,fy3,fy4]
        xt=[1,1,1,1]
        yt=[1,1,1,1]
        lt=[]
        for i in range(4):
            if xi<=xc[i]<=xf:
                xt[i]=0
            if yi<=yc[i]<=yf:
                yt[i]=0
        for i in range(4):                                  #Calculating the shortest distance along the diagonal  
            if xt[i]==1 or yt[i]==1:
                if xc[i]<xi or yc[i]<yi:
                    m=((c2-yc[i])/(c1-xc[i]))
                    a1,b1 = (xc[i]+(yi-yc[i])/m),yi
                    a2,b2 = xi,(yc[i]+m*(xi-xc[i]))
                    cd1 = np.sqrt((c1-a1)**2+(c2-b1)**2)
                    cd2 = np.sqrt((c1-a2)**2+(c2-b2)**2)
                    if cd1>cd2:
                        lt.append([a2,b2])
                    else:
                        lt.append([a1,b1])
                if xc[i]>xf or yc[i]>yf:
                    m=((c2-yc[i])/(c1-xc[i]))
                    a1,b1 = (xc[i]+(yf-yc[i])/m),yf
                    a2,b2 = xf,(yc[i]+m*(xf-xc[i]))
                    cd1 = np.sqrt((c1-a1)**2+(c2-b1)**2)
                    cd2 = np.sqrt((c1-a2)**2+(c2-b2)**2)
                    if cd1>cd2:
                        lt.append([a2,b2])
                    else:
                        lt.append([a1,b1])       
        d=[]
        for i,j in lt:
            d.append((np.sqrt((c1-i)**2+(c2-j)**2)))
        dt=min(d)
        ans=lt[d.index(min(d))]
        odt=np.sqrt((c1-fx1)**2+(c2-fy1)**2)
        '''Calculating the co-ordinates from the shortest distance and centroid'''
        if round((c2-fy1)*(ans[0]-fx1))==round((ans[1]-fy1)*(c1-fx1)):
            if (np.sqrt((ans[0]-fx1)**2+(ans[1]-fy1)**2))<(np.sqrt((ans[0]-fx3)**2+(ans[1]-fy3)**2)):
                xf1=round(ans[0],1)
                yf1=round(ans[1],1)
                xf3=2*c1-xf1
                yf3=2*c2-yf1
                xf2=round((((1-dt/odt)))*c1 + (dt/odt)*fx2,1)
                yf2=round((((1-dt/odt)))*c2 + (dt/odt)*fy2,1)
                xf4=round((((1-dt/odt)))*c1 + (dt/odt)*fx4,1)
                yf4=round((((1-dt/odt)))*c2 + (dt/odt)*fy4,1)
                print('Final Coordinates:',(xf1,yf1),(xf2,yf2),(xf3,yf3),(xf4,yf4))
            else:
                xf3=round(ans[0],1)
                yf3=round(ans[1],1)
                xf2=round((((1-dt/odt)))*c1 + (dt/odt)*fx2,1)
                yf2=round((((1-dt/odt)))*c2 + (dt/odt)*fy2,1)
                xf4=round((((1-dt/odt)))*c1 + (dt/odt)*fx4,1)
                yf4=round((((1-dt/odt)))*c2 + (dt/odt)*fy4,1)
                xf1=2*c1-xf3
                yf1=2*c2-yf3
                print('Final Coordinates:',(xf1,yf1),(xf2,yf2),(xf3,yf3),(xf4,yf4))
        if round((c2-fy2)*(ans[0]-fx2))==round((ans[1]-fy2)*(c1-fx2)):
            if (np.sqrt((ans[0]-fx2)**2+(ans[1]-fy2)**2))<(np.sqrt((ans[0]-fx4)**2+(ans[1]-fy4)**2)):
                print(4)
                xf2=round(ans[0],1)
                yf2=round(ans[1],1)
                xf4=2*c1-xf2
                yf4=2*c2-yf2
                xf3=round((((1-dt/odt)))*c1 + (dt/odt)*fx3,1)
                yf3=round((((1-dt/odt)))*c2 + (dt/odt)*fy3,1)
                xf1=round((((1-dt/odt)))*c1 + (dt/odt)*fx1,1)
                yf1=round((((1-dt/odt)))*c2 + (dt/odt)*fy1,1)
                print('Final Coordinates:',(xf1,yf1),(xf2,yf2),(xf3,yf3),(xf4,yf4))
            else:
                xf4=round(ans[0],1)
                yf4=round(ans[1],1)
                xf1=round((((1-dt/odt)))*c1 + (dt/odt)*fx1,1)
                yf1=round((((1-dt/odt)))*c2 + (dt/odt)*fy1,1)
                xf3=round((((1-dt/odt)))*c1 + (dt/odt)*fx3,1)
                yf3=round((((1-dt/odt)))*c2 + (dt/odt)*fy3,1)
                xf2=2*c1-xf4
                yf2=2*c2-yf4
                print('Final Coordinates:',(xf1,yf1),(xf2,yf2),(xf3,yf3),(xf4,yf4))
        ox=[fx1,fx2,fx3,fx4]
        oy=[fy1,fy2,fy3,fy4]
        fx=[xf1,xf2,xf3,xf4]
        fy=[yf1,yf2,yf3,yf4]
        plt.plot(ox,oy,'r*')
        for xy in zip(ox,oy):
            plt.annotate('(%.1f, %.1f)' % xy, xy=xy)
        for xy in zip(fx,fy):
            plt.annotate('(%.1f, %.1f)' % xy, xy=xy)
        plt.plot([xf1,xf2,xf3,xf4,xf1],[yf1,yf2,yf3,yf4,yf1])  
        plt.plot([fx1,fx2,fx3,fx4,fx1],[fy1,fy2,fy3,fy4,fy1])
        plt.show()
roi_region(254,2,4,6,0,0,256,256,30)
