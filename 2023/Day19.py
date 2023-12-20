data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

list1, list2 = data.split('\n\n')

# workflows list - list1
workflows = {}

for l in list1.split('\n'):
    name, rule_str = l[:-1].split('{')
    rules = rule_str.split(',')
    workflows[name] = ([], rules.pop())
    for rule in rules:
        condition, target = rule.split(':')
        key = condition[0]
        con = condition[1] 
        n = int(condition[2:])
        workflows[name][0].append((key, con, n, target))

# PART 1
operators = {
    ">": int.__gt__,
    "<": int.__lt__
}

def is_accaptable (item, name = 'in'):
    if name == "R":
        return False
    elif name == "A":
        return True
    
    rules, fallback = workflows[name]
    
    for key, con, n, target in rules:
        if operators[con](item[key], n):
            return is_accaptable(item, target)
        
    return is_accaptable(item, fallback)

total = 0

# rating list - list2
for l in list2.split('\n'):
    item = {}
    for part in l[1:-1].split(','):
        ch, n = part.split("=")
        item[ch] = int(n)
    if is_accaptable(item):
        total += sum(item.values())
    
print(f"Part one: {total}")

# PART 2
def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]

    total2 = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, min(n - 1, hi))
            F = (max(n, lo), hi)
        else:
            T = (max(n + 1, lo), hi)
            F = (lo, min(n, hi))
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total2 += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total2 += count(ranges, fallback)
    return total2  

c= count({key: (1, 4000) for key in "xmas"})
print(f"Part two: {c}")
