

```
1, 2, 5, 10

四人过河，只有一把手电，过河要有手电，桥每次只能两个人过。
求最短时间

5，10      2，1       时间 2
5，10，1     2             3
1          2，5，10        13
1，2        5，10          15
           1，2，5，10      17

```



def get_go_two(peoples: list):
    result = []
    for i in range(len(peoples)):
        for j in range(i+1, len(peoples)):
            result.append([peoples[i],peoples[j]])
    return result


def go(here: list, there:list, moving: list, timeuse: int):
    print(f"before go here: {tuple(here)},there: {tuple(there)},time:{timeuse}")
    if len(moving) == 2:
        timeuse = timeuse + max(moving[0],moving[1])
    if len(moving) == 1:
        timeuse = timeuse + moving[0]
    here = list(set(here) - set(moving))
    there = there+moving
    here.sort()
    there.sort()
    print(f"after go here: {tuple(here)},there: {tuple(there)},time:{timeuse}")
    return tuple(here), tuple(there),timeuse



def back(here:list, there:list, moving:int, timeuse:int):
    print(f"before back here:{tuple(here)}, threre:{tuple(there)} time:{timeuse}")
    timeuse = timeuse + moving
    here.append(moving)
    here.sort()
    there = list(set(there) - set([moving,]))
    there.sort()
    print(f"after back here:{tuple(here)}, threre:{tuple(there)} time:{timeuse}")
    return tuple(here), tuple(there), timeuse


def print_kinde(kinde:dict):
    for key, value in kinde.items():
        print(f"\t\there {key} \t\tthere {value[0]},time:{value[1]}")




def run(here:list, there:list):
    here.sort()
    there.sort()
    khere = here.copy()
    kthere = there.copy()
    print(f"{khere} {kthere}")

    kinde = {} # 过桥的状态
    kinde[tuple(khere)] =(tuple(),0)
    stop_flag = False
    print_kinde(kinde)
    while not stop_flag:
        go_kinde = {}
        for this_here, (this_there, this_time) in kinde.items():
            go_list = get_go_two(list(this_here))
            for i in go_list:
                ahere, athere ,time = go(list(this_here),list(this_there), i, this_time)
                if ahere in go_kinde.keys():
                    if time < go_kinde[ahere][1]:
                        go_kinde[ahere] = (athere, time)
                else:
                    go_kinde[ahere] = (athere, time)
        print_kinde(go_kinde)

        for i in go_kinde.keys():
            if len(i) == 0:
                print("break")
                stop_flag = True
                kinde = go_kinde
                break
        if stop_flag:
            break
        back_kinde = {}
        for this_here, (this_there, this_time) in go_kinde.items():
            for i in this_there:
                ahere, athere,time = back(list(this_here),list(this_there),i,this_time)
                if ahere in back_kinde.keys():
                    if time < back_kinde[ahere][1]:
                        back_kinde[ahere] = (athere, time)
                else:
                    back_kinde[ahere] = (athere, time)
        print_kinde(back_kinde)
        kinde = back_kinde

    print("result:")
    print_kinde(kinde)


if __name__ == "__main__":

    test = 3
    if test == 1:
        here = [10, 2, 5, 8, 9,20]
        there = []
    elif test == 2:
        here = [10, 2, 1, 8]
        there = []
    else:
        here = [1, 2, 5, 10]
        there = []
    result = get_go_two(here)
    print(result)
    run(here, there)
