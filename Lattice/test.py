# import matplotlib.pyplot as plt
import numpy as np
# # from itertools import product, combinations

# # fig = plt.figure()

# # # # draw vector
# # # # soa = np.array([[0, 0, 1, 1, -2, 0], [0, 0, 2, 1, 1, 0],
# # #             #    [0, 0, 3, 2, 1, 0], [0, 0, 4, 0.5, 0.7, 0]])
# # # soa = [[0, 0, 1, 1, -2, 0]]
# # # X, Y, Z, U, V, W = zip(*soa)
# # # ax = fig.add_subplot(131, projection='3d')
# # # ax.quiver(0, 0, 1, 1, -2, 0)
# # # ax.set_xlim([-1, 0.5])
# # # ax.set_ylim([-1, 1.5])
# # # ax.set_zlim([-1, 8])
# # # ax.set_title("Vectors")

# # # # draw cube
# # ax = fig.add_subplot(132, projection='3d')
# # r = [-1, 1]
# # ax.plot3D([0,1,1],[0,0,1],[0,0,0],c='g')
# # # for s, e in combinations(np.array(list(product(r, r, r))), 2):
# # #    if np.sum(np.abs(s-e)) == r[1]-r[0]:
# # #       ax.plot3D(*zip(s, e), color="green")
# # #       print(*zip(s,e))
# # # #    print('missed',s,e)
# # # ax.set_title("Cube")

# # # # draw sphere
# # # ax = fig.add_subplot(133, projection='3d')
# # # u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
# # # x = np.cos(u)*np.sin(v)
# # # y = np.sin(u)*np.sin(v)
# # # z = np.cos(v)
# # # ax.plot_wireframe(x, y, z, color="red")
# # # ax.set_title("Sphere")

# # plt.show()

# # # soa = np.array([[0, 0, 1, 1, -2, 0], [0, 0, 2, 1, 1, 0],
# # #                [0, 0, 3, 2, 1, 0], [0, 0, 4, 0.5, 0.7, 0]])
# # # soa = np.transpose(soa)
# # # # X, Y, Z, U, V, W = zip(*soa)
# # # print(*soa)

# # a = np.array([1,2,3])
# # b = np.array([3,4,5])
# # c= np.array([])
# # c = np.append(c,[a,b],axis = 0)
# # print(c)

# c = np.array([[1,2],[3,4]])
# c = list(c)
# # d = np.array([3,4])
# # a = [c,d]
# # b = list(zip(*a))

# # fig = plt.figure()
# # ax = plt.axes(projection='3d')
        
# # points = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]])
# # points = np.transpose(points)
# # print(points)
# # # print(pointsnormal)
# # # print(*zip(*pointsnormal))
# # ax.plot_surface(points[0],points[1],points[2])
# # ax.plot_surface([0, 1, 1, 0],[0, 0, 1, 1],[0, 0, 0, 0])

# fig = plt.figure(num=1, clear=True)
# ax = fig.add_subplot(1, 1, 1, projection='3d')

# x = np.array([[0, 1], [0.5, 1]])
# y = np.array([[0, 1], [0.5, 1]])
# z = np.array([[0, 0], [0.75, 1]])

# points = np.array([[0,0,0],[1,0,0],[0,1,0],[1,1,0]])

# x = np.array([[points[0][0],points[1][0]],[points[2][0],points[3][0]]])
# y = np.array([[points[0][1],points[1][1]],[points[2][1],points[3][1]]])
# z = np.array([[points[0][2],points[1][2]],[points[2][2],points[3][2]]])
# print(x)
# print(y)
# print(z)

# # x = np.array([[0, 1], [1, 0]])
# # y = np.array([[0, 0], [1, 1]])
# # z = np.array([[0, 0], [0, 0]])

# ax.plot_surface(x, y, z)
# ax.set(xlabel='x', ylabel='y', zlabel='z')

# fig.tight_layout()
# plt.show()

a = np.array([[0,1],[2,3]])
# print(min(a))