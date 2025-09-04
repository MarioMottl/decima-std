import time

def now_ns():
    return time.perf_counter_ns()

def bench_sum(n: int) -> int:
    acc = 0
    for i in range(1, n+1):
        acc += i
    return acc

def sq(x: int) -> int:
    return x*x

def len2(v):
    return sq(v[0]) + sq(v[1])

def bench_len2(n: int) -> int:
    v = (3,4)
    acc = 0
    for _ in range(n):
        acc += len2(v)
    return acc

def report(label, iters, start, end):
    total = end - start
    per = total // iters
    print(label)
    print(total)
    print(per)

def main():
    iters = 50_000_000

    # warmup
    _ = bench_sum(1_000_000)
    _ = bench_len2(100_000)

    s1 = now_ns(); acc1 = bench_sum(iters); e1 = now_ns()
    report("sum 1..N", iters, s1, e1)

    it2 = iters // 10
    s2 = now_ns(); acc2 = bench_len2(it2); e2 = now_ns()
    report("len2(v) call", it2, s2, e2)

    i = 0; t3 = 0
    s3 = now_ns()
    for i in range(iters):
        t3 += 1 if (i % 2 == 0) else 2
    e3 = now_ns()
    report("branch ternary", iters, s3, e3)

    print(acc1); print(acc2); print(t3)

if __name__ == "__main__":
    main()

