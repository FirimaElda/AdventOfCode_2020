import re
import day_4.field_validation as fv


def are_passports_valid(passp):
    necessary_fields = ['ecl',
                        'pid',
                        'eyr',
                        'hcl',
                        'byr',
                        'iyr',
                        'hgt']

    result = 0
    for pp in passp:
        isvalid = True
        for field in necessary_fields:
            if field not in pp or not is_valid_field(field, pp[field]):
                isvalid = False
        if isvalid:
            result += 1

    return result


def is_valid_field(field, value):
    ruledic = {
        'ecl': lambda val: fv.valid_ecl(val),
        'pid': lambda val: fv.valid_pid(val),
        'eyr': lambda val: fv.valid_eyr(val),
        'hcl': lambda val: fv.valid_hcl(val),
        'byr': lambda val: fv.valid_byr(val),
        'iyr': lambda val: fv.valid_iyr(val),
        'hgt': lambda val: fv.valid_hgt(val)
    }
    return ruledic[field](value)


def make_passport_dictionary(ppsstring):
    ppsstring = re.split(r'\n\n', ppsstring)
    ppsdiclist = []
    for pa in ppsstring:
        pa = re.sub(r'\n', ' ', pa)
        if not pa:
            continue
        dic = {}
        for pair in re.split(' ', pa):
            if not pair:
                continue
            k, v = re.split(':', pair)
            dic[k] = v
        ppsdiclist.append(dic)
    return ppsdiclist


if __name__ == '__main__':
    print('----- Sample Passports -----')
    f = open('sample_passports.txt', 'r')
    pps = f.read()
    funcinput = make_passport_dictionary(pps)
    print('Valid passports: ' + str(are_passports_valid(funcinput)))

    print('----- My Passports -----')
    f = open('my_passports.txt', 'r')
    pps = f.read()
    funcinput = make_passport_dictionary(pps)
    print('Valid passports: ' + str(are_passports_valid(funcinput)))
