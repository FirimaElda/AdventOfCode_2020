import re


def convert_seat_to_int(seatstr):
    binseat = re.sub('B', '1', seatstr)
    binseat = re.sub('F', '0', binseat)
    binseat = re.sub('L', '0', binseat)
    binseat = re.sub('R', '1', binseat)
    return int(binseat, 2)


def find_my_seat(plist):
    print(plist)
    plist = [convert_seat_to_int(x) for x in plist]
    plist.sort()
    print(plist)
    i = 0
    while i < len(plist):
        nxtnr = plist[i] + 1
        if nxtnr != plist[i + 1]:
            return nxtnr
        i += 1


if __name__ == '__main__':
    print('----- Sample Boarding Passes -----')
    f = open('sample_passes.txt', 'r')
    passes = f.read()
    passlist = re.split(r'\n', passes)
    print('Maximum seat ID: ' + str(max([convert_seat_to_int(x) for x in passlist])))

    print('----- My Boarding Passes -----')
    f = open('my_passes.txt', 'r')
    passes = f.read()
    passlist = re.split(r'\n', passes)
    print('Maximum seat ID: ' + str(max([convert_seat_to_int(x) for x in passlist])))
    print('This is my seat: ' + str(find_my_seat(passlist)))
