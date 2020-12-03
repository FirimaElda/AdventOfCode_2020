import re


def traverse_forest(frs, stepsright=3, stepsdown=1):
    currentposx = stepsright
    currentposy = stepsdown
    treecounter = 0
    while currentposy < len(frs) and currentposx < len(frs[currentposy]):
        if frs[currentposy][currentposx] == '#':
            treecounter += 1
        currentposx = currentposx + stepsright
        if currentposx >= len(frs[currentposy]):
            currentposx = currentposx - len(frs[currentposy])
        currentposy = currentposy + stepsdown
    return treecounter


if __name__ == '__main__':
    print('----- Sample Forest -----')
    f = open('sample_forest.txt', 'r')
    frst = f.read()
    frst = re.split('\n|  --->| ', frst)
    frst = [list(x) for x in frst if list(x)]
    print('Trees encountered: ' + str(traverse_forest(frst)))
    treeproduct = 1
    slopelist = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for right, down in slopelist:
        treeproduct = treeproduct * traverse_forest(frst, right, down)
    print('Checking rest of the slopes: ' + str(treeproduct))

    print('----- My Forest -----')
    f = open('my_forest.txt', 'r')
    frst = f.read()
    frst = re.split('\n|  --->| ', frst)
    frst = [list(x) for x in frst if list(x)]
    print('Trees encountered: ' + str(traverse_forest(frst)))
    treeproduct = 1
    slopelist = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for right, down in slopelist:
        treeproduct = treeproduct * traverse_forest(frst, right, down)
    print('Checking rest of the slopes: ' + str(treeproduct))
