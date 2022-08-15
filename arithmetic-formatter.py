def arithmetic_arranger(problems, ans=None):
    ma = []
    arranged_problems = ""
    #l = len(problems)
    i = 0

    if len(problems) > 5:
        return ('Error: Too many problems.')

    for p in problems:
        pl = p.split()
        if pl[1] not in ['+', '-']:
            return ("Error: Operator must be '+' or '-'.")

        if len(pl[0]) > 5 or len(pl[2]) > 4:
            return ("Error: Numbers cannot be more than four digits.")

        for character in pl[0]:
            if character not in "0123456789":
                return ('Error: Numbers must only contain digits.')

        for character in pl[2]:
            if character not in "0123456789":
                return ('Error: Numbers must only contain digits.')

        answer = calculate(pl[0], pl[1], pl[2])
        len1 = len(pl[0])
        len2 = len(pl[2])
        biggest = max(len1, len2)
        if len1 > len2: firstbiggest = 1
        else: firstbiggest = 0

        ma.append([pl[0], pl[1], pl[2], answer, biggest, firstbiggest])
        i += 1

    #PRINT THE OPERAND LINE
    for sublist in ma:
        spacegap = int(sublist[4]) + 2 - len(sublist[0])
        line1fragments = (' ' * (spacegap), sublist[0], '    ')
        line1part = "".join(line1fragments)
        arranged_problems += line1part
        arranged_problems.rstrip()
    arranged_problems = arranged_problems.rstrip()
    arranged_problems += '\n'

    #PRINT THE OPERATOR LINE
    for sublist in ma:
        spacegap = int(sublist[4]) + 1 - (len(sublist[2]))
        line2fragments = (sublist[1] + ' ' * (spacegap), sublist[2], '    ')
        line2part = "".join(line2fragments)
        arranged_problems += line2part
        #"".join(arranged_problems.rstrip())
    arranged_problems = arranged_problems.rstrip()
    arranged_problems += '\n'

    #PRINT THE DASHES LINE
    for sublist in ma:
        dashnum = int(sublist[4]) + 2
        line3fragments = ('-' * (dashnum), '    ')
        line3part = "".join(line3fragments)
        arranged_problems += line3part
    arranged_problems = arranged_problems.rstrip()

    #PRINT THE ANSWER LINE
    if ans == True:
        arranged_problems += '\n'
        for sublist in ma:
            spacegap = int(sublist[4]) + 2 - (len(sublist[3]))
            line4fragments = (' ' * (spacegap), sublist[3], '    ')
            line4part = "".join(line4fragments)
            arranged_problems += line4part
    arranged_problems = arranged_problems.rstrip()
    return arranged_problems


#def format_line():


def calculate(op1, op2, op3):
    if op2 == '+':
        ans = int(op1) + int(op3)
    elif op2 == '-':
        ans = int(op1) - int(op3)
    else:
        ans = 'error'
    return str(ans)