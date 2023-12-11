def pairs(l):
    it = iter(l)
    return zip(it, it)
 
seeds, *mappings = open('/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input (4).txt').read().split('\n\n')
seeds = seeds.split(": ")[1]
seeds = [int(x) for x in seeds.split()]
seeds = [range(a, a + b) for a, b in pairs(seeds)]
 
for m in mappings:
    _, *ranges = m.splitlines()
    ranges = [[int(x) for x in r.split()] for r in ranges]
    ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]
 
    new_seeds = []
    for r in seeds:
        for tr, fr in ranges:
            offset = tr.start - fr.start
            if r.stop <= fr.start or fr.stop <= r.start:
                continue
            ir = range(max(r.start, fr.start), min(r.stop, fr.stop))
            lr = range(r.start, ir.start)
            rr = range(ir.stop, r.stop)
            if lr:
                seeds.append(lr)
            if rr:
                seeds.append(rr)
            new_seeds.append(range(ir.start + offset, ir.stop + offset))
            break
        else:
            new_seeds.append(r)
    seeds = new_seeds
 
print(min(x.start for x in seeds))
