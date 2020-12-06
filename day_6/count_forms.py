import re


def count_yes(formslist):
    formdict = {}
    result = 0
    resulteveryone = 0
    for form in formslist:
        tmp = re.split(r'\n', form)
        checkeveryone = len(tmp)
        formdict.clear()
        for fo in tmp:
            i = 0
            while i < len(fo):
                formdict[fo[i]] = formdict.get(fo[i], 0) + 1
                i += 1
        for k, v in formdict.items():
            if checkeveryone == formdict[k]:
                resulteveryone += 1
        result += len(formdict)
    return result, resulteveryone


if __name__ == '__main__':
    print('----- Sample Forms -----')
    f = open('sample_forms.txt', 'r')
    forms = f.read()
    forms = re.split(r'\n\n', forms)
    print('Count of yes: ' + str(count_yes(forms)))

    print('----- My Forms -----')
    f = open('my_forms.txt', 'r')
    forms = f.read()
    forms = re.split(r'\n\n', forms)
    print('Count of yes: ' + str(count_yes(forms)))
