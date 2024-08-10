from math import pi
from numpy import cross,sin,cos,sqrt,arccos,arctan,array,append,copy
from numpy.linalg import norm
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


def gen_cellpoints_v1(a1,a2,a3,al,be,ga):
    points= array([[0,0,0]])
    points=append(points,[[a1,0,0]],axis = 0)
    points=append(points,[[a2*cos(ga),a2*sin(ga),0]],axis=0)
    points=append(points,[[points[-1][0]+a1,points[-1][1],0]],axis=0)
    g1 = arctan((cos(al)-(cos(ga)*cos(be)))/(sin(ga)*cos(be)))
    z = a3*sqrt(1 - ((cos(be)/cos(g1))**2))
    x = (a3*cos(be)*cos(g1))/cos(g1)
    y = (a3*cos(be)*sin(g1))/cos(g1)
    for i in range(4):
        points=append(points,[[points[i][0]+x,points[i][1]+y,points[i][2]+z]],axis = 0)
    return points

def gen_latvec_v1(a1,a2,a3,al,be,ga):
    al *= (pi/180)
    be *= (pi/180)
    ga *= (pi/180)
    latvec = array([[a1,0,0]])
    latvec = append(latvec,[[a2*cos(ga),a2*sin(ga),0]],axis=0)
    g1 = arctan((cos(al)-(cos(ga)*cos(be)))/(sin(ga)*cos(be)))
    z = a3*sqrt(1 - ((cos(be)/cos(g1))**2))
    x = (a3*cos(be)*cos(g1))/cos(g1)
    y = (a3*cos(be)*sin(g1))/cos(g1)
    latvec = append(latvec,[[x,y,z]],axis=0)
    return latvec

def gen_cellpoints_v2(latvec):
    points2 = array([[0,0,0]])
    points2 = append(points2,[latvec[0]],axis = 0)
    points2 = append(points2,[latvec[1]],axis = 0)
    points2 = append(points2,[[points2[2][0]+points2[1][0],points2[2][1],0]],axis=0)
    for i in range(4):
        points2 = append(points2,[[points2[i][0]+latvec[2][0],points2[i][1]+latvec[2][1],points2[i][2]+latvec[2][2]]],axis=0)
    return points2

def gen_normal(latlen,latang,hklval,figure = False):
    latvec = gen_latvec_v1(*latlen,*latang) 

    cellcorners = gen_cellpoints_v2(latvec)

    nzeroindices = []
    for i in range(3):
        if hklval[i] != 0:
            nzeroindices.append(i)
    vecstocross = []

    if len(nzeroindices) == 1:
        for i in range(3):
            if i not in nzeroindices:
                vecstocross.append(copy(latvec[i]))
        if nzeroindices[0] == 0:
            points = [copy(cellcorners[i]) for i in range(0,7,2)]
        elif nzeroindices[0] == 1:
            points = [copy(cellcorners[i]) for i in [0,1,4,5]]
        else:
            points = [copy(cellcorners[i]) for i in range(0,4)]
        points=array(points)

        
    elif len(nzeroindices) ==  2:
        points=[]
        for i in range(3):
            if i in nzeroindices:
                points.append(copy(latvec[i]))
            else:
                zeroindex = i
                vecstocross.append(copy(latvec[zeroindex]))
        points = array(points)
        points[0] = points[0] / hklval[nzeroindices[0]]
        points[1] = points[1] / hklval[nzeroindices[1]]
        vecstocross.append(points[1]-points[0])

        points = append(points,[points[0]+latvec[zeroindex],points[1]+latvec[zeroindex]],axis=0)
    else:
        points = array([copy(latvec[0]),copy(latvec[1]),copy(latvec[2])])
        points[0] = points[0] / hklval[0]
        points[1] = points[1] / hklval[1]
        points[2] = points[2] / hklval[2]
        vecstocross = [points[2]-points[1],points[2]-points[0]]
        points = append(points,[(points[2]+points[1])/2],axis=0)
        # points[[2,3]] = points[[3,2]]
    # print(vecstocross)
    crossvec = cross(vecstocross[0],vecstocross[1])
    crossvec = crossvec/norm(crossvec)

    print("##----------------RESULTS----------------##")
    print("\nlattice vectors: \n",latvec,'\n')
    print("plane miller indices: \n",hklval,'\n')
    print("normal to this plane: \n",crossvec,'\n')
    print("normal's angles with axes:,\n",angleswithaxes(crossvec))

    # print(points)
    planecenter = array([0.,0.,0.])
    for point in points:
        planecenter += point
    planecenter = planecenter / len(points)
    normalarrow = append(planecenter,crossvec)
    # print(planecenter)

    if figure is True:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        cornersxyz = np.transpose(cellcorners)
        
        #drawing cell framework
        for i in range(0,7,2):
            ax.plot3D(*zip(cellcorners[i],cellcorners[i+1]),c='g')
        for i in [0,1,4,5]:
            ax.plot3D(*zip(cellcorners[i],cellcorners[i+2]),c='g')
        for i in range(4):
            ax.plot3D(*zip(cellcorners[i],cellcorners[i+4]),c='g')
        
        #drawing the plane
        x = array([[points[0][0],points[1][0]],[points[2][0],points[3][0]]])
        y = array([[points[0][1],points[1][1]],[points[2][1],points[3][1]]])
        z = array([[points[0][2],points[1][2]],[points[2][2],points[3][2]]])
        ax.plot_surface(x,y,z,color='tab:gray',alpha=0.8)

        #drawing cell corners
        ax.scatter(cornersxyz[0],cornersxyz[1],cornersxyz[2],s=200,c='r', marker='o')

        #drawing the vector
        # print(normalarrow)
        ax.quiver(*normalarrow)
        ax.set_title("cell 3D")
        ax.set(xlabel='X', ylabel='Y', zlabel='Z')
        # ax.set_aspect('auto')
        plt.tight_layout()
        plt.axis('square')
        plt.show()



        
        



def angleswithaxes(vec):
    vecabs = norm(vec)
    angles = []
    for i in range(3):
        angles.append((180/pi)*arccos(vec[i]/vecabs))
    return angles


def parse(file_name):
    # A function to parse data in a specific format. Read README file in the repository for more details
    with open(file_name) as file:
        lines = file.readlines()
        file.close()
    inputs = {}
    numlines = len(lines)
    line_index =3
    while bool(lines[line_index].split()) is False:
        line_index += 1
    line_index += 1
    while line_index < numlines:
        # print(lines[line_index])
        type_name = lines[line_index].split()
        line_index+= 1
        if type_name[0] == 'int':
            inputs[type_name[1]] = int(lines[line_index].split()[0])
            line_index += 1
        
        elif type_name[0] == 'float':
            inputs[type_name[1]] = float(lines[line_index].split()[0])
            line_index += 1

        elif type_name[0] == 'str':
            inputs[type_name[1]] = lines[line_index][:-1]
            line_index += 1

        elif type_name[0] == 'int_list':
            inputs[type_name[1]] = list(map(int,lines[line_index].split()))
            line_index += 1

        elif type_name[0] == 'float_list':
            inputs[type_name[1]] = list(map(float,lines[line_index].split()))
            line_index += 1

        elif type_name[0] == 'float_numpyarray':
            inputs[type_name[1]] = array(list(map(float,lines[line_index].split())))
            line_index += 1

        elif type_name[0] == 'str_list':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(lines[line_index][:-1])
                line_index += 1

        elif type_name[0] == 'int_mat':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(list(map(int,lines[line_index].split())))
                line_index += 1
        
        elif type_name[0] == 'float_mat':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(list(map(float,lines[line_index].split())))
                line_index += 1

        elif type_name[0] == 'str_mat':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(lines[line_index].split())
                line_index += 1

        elif type_name[0] == 'float_numpymat':
            inputs[type_name[1]] = []
            while lines[line_index][0] != '#':
                inputs[type_name[1]].append(list(map(float,lines[line_index].split())))
                line_index += 1
            inputs[type_name[1]] = array(inputs[type_name[1]])

        elif type_name[0] == 'xydata':
            inputs[type_name[1]] = []
            inputs[type_name[2]] = []
            while lines[line_index][0] != '#':
                lines[line_index] = lines[line_index].split()
                try:
                    inputs[type_name[1]].append(float(lines[line_index][0]))
                    inputs[type_name[2]].append(float(lines[line_index][1]))
                except:
                    print('{} input inproper! check {}'.format(type_name[0],file_name))
                line_index += 1

        elif type_name[0] == 'xysigdata':
            inputs[type_name[1]] = []
            inputs[type_name[2]] = []
            inputs[type_name[3]] = []
            while lines[line_index][0] != '#':
                lines[line_index] = lines[line_index].split()
                try:
                    inputs[type_name[1]].append(float(lines[line_index][0]))
                    inputs[type_name[2]].append(float(lines[line_index][1]))
                    inputs[type_name[3]].append(float(lines[line_index][2]))
                except:
                    print('{} input inproper! check {}'.format(type_name[0],file_name))
                line_index += 1

        else:
            return inputs
        
        line_index += 1
        while lines[line_index][0] == '#':
            line_index += 1
