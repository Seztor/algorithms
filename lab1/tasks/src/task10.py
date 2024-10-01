def task10():
    f = open('input.txt')
    f2 = open('output.txt', 'w')


    n = int(f.readline())
    s = f.readline().strip()

    cnt_let = [0] * 26
    offset = 65
    for i in s:
        cnt_let[ord(i) - offset] += 1

    mn_i = -1
    for i in range(len(cnt_let)):
        if cnt_let[i] % 2 == 1:
            mn_i = i
            break
            
    new_s = ''

    for i in range(len(cnt_let)):
        if cnt_let[i] != 0:
            new_s += chr(i + offset) * (cnt_let[i] // 2)

    if mn_i != -1:
        new_s = new_s + chr(mn_i + offset) + new_s[::-1]
    else:
        new_s += new_s[::-1]

    print(new_s, file=f2)

    f.close()
    f2.close()
