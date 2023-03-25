def test_Havel_Hakimi(seq):
    if sum(seq)%2 == 1:
        return False

    while True:
        seq.sort(reverse=True)
        if min(seq) < 0:
            return False
        if max(seq) == 0:
            return True
        if max(seq) > len(seq) - 1:
            return False
        first = seq.pop(0)
        for i in range(first):
            seq[i] -= 1

def main():
    seq = [5,4,4,3,2,1,1]
    print(test_Havel_Hakimi(seq))
    print(test_Havel_Hakimi([8,5,4,4,4,3,1,1,1,1]))
    print(test_Havel_Hakimi([1,3,7,1,1,1,8,8,5,5]))
    print(test_Havel_Hakimi([5,4,4,3,2,1,1]))
    print(test_Havel_Hakimi([4,4,3,3,3,3,3,3]))
main()