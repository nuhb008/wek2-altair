def process_instructions(instructions, grid_size):
    x=0
    y=0
    d='N'
    for a in range(0,len(instructions)) :
        if instructions[a]=='L':
            if d=='N':
                d='W'
            elif d=='W':
                d='S'
            elif d=='S':
                d='E'
            else :
                d='N'
        if instructions[a]=='R':
            if d == 'N':
                d = 'E'
            elif d == 'W':
                d = 'N'
            elif d == 'S':
                d = 'W'
            else :
                d = 'S'
        if instructions[a]=='F':
            if d == 'N' and (0<y+1<grid_size[1] or 0>y+1>grid_size[1]):
                y+=1
            elif d == 'W' and (0<x-1<grid_size[0] or 0>x-1>grid_size[0]):
                x-=1
            elif d == 'S' and (0<y-1<grid_size[1] or 0>y-1>grid_size[1]):
                y-=1
            elif d=='E' and (0<x+1<grid_size[0] or 0>x+1>grid_size[0]):
                x+=1

    print(x, y)
    if d == 'N':
        print("North")
    elif d == 'W':
        print("West")
    elif d == 'S':
        print("South")
    else:
        print("East")

instructions = input() #input instriuction
num=input() #input grid size with space
grid_size = tuple(int(i) for i in num.split())
process_instructions(instructions, grid