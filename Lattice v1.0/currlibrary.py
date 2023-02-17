from math import sin,cos,tan,pi,sqrt
from numpy import cross,arccos,arctan
from numpy.linalg import norm

def gen_cellpoints_v1(a1,a2,a3,al,be,ga):
    points= [[0,0,0]]
    points.append([a1,0,0])
    points.append([a2*cos(ga),a2*sin(ga),0])
    points.append([points[-1][0]+a1,points[-1][1],0])
    g1 = arctan((cos(al)-(cos(ga)*cos(be)))/(sin(ga)*cos(be)))
    z = a3*sqrt(1 - ((cos(be)/cos(g1))**2))
    x = (a3*cos(be)*cos(g1))/cos(g1)
    y = (a3*cos(be)*sin(g1))/cos(g1)
    for i in range(4):
        points.append([points[i][0]+x,points[i][1]+y,points[i][2]+z])
    return points

def gen_latvec_v1(a1,a2,a3,al,be,ga):
    latvec = []
    latvec.append([a1,0,0])
    latvec.append([a2*cos(ga),a2*sin(ga),0])
    g1 = arctan((cos(al)-(cos(ga)*cos(be)))/(sin(ga)*cos(be)))
    z = a3*sqrt(1 - ((cos(be)/cos(g1))**2))
    x = (a3*cos(be)*cos(g1))/cos(g1)
    y = (a3*cos(be)*sin(g1))/cos(g1)
    latvec.append([x,y,z])
    return latvec

def gen_cellpoints_v2(latvec):
    points2 = [[0,0,0]]
    points2.append(latvec[0])
    points2.append(latvec[1])
    points2.append([points2[2][0]+points2[1][0],points2[2][1],0])
    for i in range(4):
        points2.append([points2[i][0]+latvec[2][0],points2[i][1]+latvec[2][1],points2[i][2]+latvec[2][2]])
    return points2

def gen_normal(latvec,hklval):
    nzeroindices = []
    for i in range(3):
        if hklval[i] != 0:
            nzeroindices.append(i)
    vecstocross = []

    if len(nzeroindices) == 1:
        for i in range(3):
            if i not in nzeroindices:
                vecstocross.append(latvec[i][:])

    elif len(nzeroindices) ==  2:
        points=[]
        for i in range(3):
            if i in nzeroindices:
                points.append(latvec[i][:])
            else:
                vecstocross.append(latvec[i][:])
        for k in range(3):
            points[0][k] = points[0][k] / hklval[nzeroindices[0]]
            points[1][k] = points[1][k] / hklval[nzeroindices[1]]
        vecstocross.append([])
        for k in range(3):
            vecstocross[1].append(points[1][k]-points[0][k])
    
    else:
        points = [latvec[0][:],latvec[1][:],latvec[2][:]]
        for k in range(3):
            points[0][k] = points[0][k] / hklval[0]
            points[1][k] = points[1][k] / hklval[1]
            points[2][k] = points[2][k] / hklval[2]
        vecstocross = [[],[]]
        for k in range(3):
            vecstocross[0].append(points[2][k]-points[0][k])
            vecstocross[1].append(points[2][k]-points[1][k])
    # print(vecstocross)
    crossvec = cross(vecstocross[0],vecstocross[1])
    return crossvec/norm(crossvec)

def angleswithaxes(vec):
    vecabs = norm(vec)
    angles = []
    for i in range(3):
        angles.append((180/pi)*arccos(vec[i]/vecabs))
    return angles