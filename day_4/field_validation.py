import re


def valid_ecl(val):
    cololist = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if val in cololist:
        return True


def valid_pid(val):
    return len(val) == 9


def valid_eyr(val):
    return 2020 <= int(val) <= 2030


def valid_hcl(val):
    return re.search(r'#[0-9a-f]{6}', val) is not None


def valid_byr(val):
    return 1920 <= int(val) <= 2002


def valid_iyr(val):
    return 2010 <= int(val) <= 2020


def valid_hgt(val):
    print(val)
    isinch = re.search(r'\d*in', val) is not None
    print('isinch: ' + str(isinch))
    iscm = re.search(r'\d*cm', val) is not None
    print('iscm: ' + str(iscm))
    height = int(re.search(r'\d*', val)[0])
    print(height)
    if iscm:
        return 150 <= height <= 193
    if isinch:
        return 59 <= height <= 76
