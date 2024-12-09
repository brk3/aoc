def main():
    m = []
    with open('input', 'r') as f:
        for line in f.readlines():
            result, nums = line.split(":")
            m.append((int(result), [int(i) for i in nums.split()]))

    ans = 0
    for k, v in m:
        s = {v[0]}
        for i in v[1:]:
            ns = set()
            for n in s:
                if n > k: continue
                ns.add(n + i)
                ns.add(n * i)
                ns.add(int("{}{}".format(n, i)))
            s = ns
        if k in s: ans += k
        print(s)
    print(ans)
main()
