import re


def valid_passwords(pwlist):
    print(pwlist)
    validcount = 0
    for a, b, c in pwlist:
        rangelist = re.split('-', a)
        rangetuple = (int(rangelist[0]), int(rangelist[1]))
        bcount = c.count(b)
        if bcount in range(rangetuple[0], rangetuple[1] + 1):
            validcount = validcount + 1
    return validcount


def valid_passwords_tobogga(pwlist):
    print(pwlist)
    validcount = 0
    for a, b, c in pwlist:
        rangelist = re.split('-', a)
        rangetuple = (int(rangelist[0]), int(rangelist[1]))
        # make it zero-based...
        rangetuple = (rangetuple[0] - 1, rangetuple[1] - 1)
        if (c[rangetuple[0]] == b and c[rangetuple[1]] != b) or (c[rangetuple[0]] != b and c[rangetuple[1]] == b):
            validcount = validcount + 1
    return validcount


if __name__ == '__main__':
    f = open('sample_passwords.txt', 'r')
    pws = f.read()
    pws = re.split('\n', pws)
    pwl = []
    for p in pws:
        pwl.append((re.split(' |: ', p)))
    res = valid_passwords(pwl)
    print('Valid passwords in sample: ' + str(res))

    f = open('my_passwords.txt', 'r')
    pws = f.read()
    pws = re.split('\n', pws)
    pwl = []
    for p in pws:
        pwl.append((re.split(' |: ', p)))
    res = valid_passwords(pwl)
    print('Valid passwords: ' + str(res))

    print('-------- Tobogga Passwords --------')
    f = open('sample_passwords.txt', 'r')
    pws = f.read()
    pws = re.split('\n', pws)
    pwl = []
    for p in pws:
        pwl.append((re.split(' |: ', p)))
    res = valid_passwords_tobogga(pwl)
    print('Valid passwords in sample: ' + str(res))

    f = open('my_passwords.txt', 'r')
    pws = f.read()
    pws = re.split('\n', pws)
    pwl = []
    for p in pws:
        pwl.append((re.split(' |: ', p)))
    res = valid_passwords_tobogga(pwl)
    print('Valid passwords: ' + str(res))
