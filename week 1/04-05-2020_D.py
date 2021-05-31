from sys import stdin
PI = 3.141592653590

while 1:
    t=stdin.readline()
    if not t:
        break
    t=t.split(' ')
    n, s = int(t[0]), int(t[1])
    holes = [] # r, z - r
    Vtot = 10**15 # µm^3
    for _ in range(n):
        r, x, y, z = stdin.readline().strip().split(' ')
        Vtot -= (4/3)*PI*(int(r)**3)
        holes.append([int(r), int(z)-int(r)])

    # https://stackoverflow.com/questions/20099669/sort-multidimensional-array-based-on-2nd-element-of-the-subarray
    if n > 0:
        holes.sort(key=lambda x:x[1])
        r, zmin = holes[0] # Sort the list such that the first hole encountered along z axis is first in the list
    else:
        zmin = 10**5
    Vslice = Vtot/s
    dz = 1
    z, z_prev = 0, 0
    for _ in range(s):
        Vleft = Vslice
        while Vleft > 0:
            z += dz
            Vleft -= dz*10**10
            while len(holes) > 0 and z >= zmin + 2*r:
                holes.pop(0)
                if len(holes) > 0:
                    zmin, r = holes[0]
                else:
                    zmin, r = 10**5, 1
            for a, b in holes:
                if z > b:
                    Vleft += dz*PI*(a**2 - (b+a - z)**2)
        print('{:6.6f}'.format((z-z_prev)/10**3))
        z_prev = z
