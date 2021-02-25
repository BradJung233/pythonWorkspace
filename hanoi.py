cnt = 0


def hanoi(num, from1, to, other):
    global cnt
    if(num == 0):
        return
    cnt += 1
    print("A:{0}:{1}".format(cnt, num))
    hanoi(num-1, from1, other, to)
    print("B:{0}:{1}".format(cnt, num))
    print(f"{from1}번에서 {to}로 옮긴다.")
    hanoi(num-1, other, to, from1)
    print("C:{0}:{1}".format(cnt, num))


hanoi(4, 0, 1, 2)
