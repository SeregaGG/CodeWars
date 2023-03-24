def solution(args):
    result = '' + str(args[0])
    seq = False
    seq_len = 0

    for i in range(1, len(args)):
        if args[i] - 1 == args[i - 1] and not seq:
            seq = True
            seq_len = 1
            continue
        elif args[i] - 1 == args[i - 1]:
            seq_len += 1
            continue

        if seq:
            if seq_len >= 2:
                result += f'-{args[i - 1]},{args[i]}'
            else:
                result += f',{args[i - 1]},{args[i]}'
            seq = False
            seq_len = 0
            continue
        result += f',{args[i]}'

    if seq_len >= 2:
        result += f'-{args[-1]}'
    elif seq_len != 0:
        result += f',{args[-1]}'
    return result
