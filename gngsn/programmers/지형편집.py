from functools import reduce

def solution(land, P, Q):
    answer = float('inf')
    prev = -1
    block = 0
    
    flat = reduce(lambda x,y :x+y , land)
    total = sum(flat)
    flat.sort()

    for cur in range(len(flat)):
        if prev != flat[cur]:
            add = flat[cur] * cur - block;
            remove = total - (len(flat) * flat[cur]) + add;
            cost = add * P + remove * Q;
            
            if answer > cost:
                answer = cost;
            prev = flat[cur];
            
        block += flat[cur];
    
    return answer
