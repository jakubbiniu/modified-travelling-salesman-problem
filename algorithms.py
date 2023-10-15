def brute_force(dist, fuel, station, capacity):
    n = len(dist); l=list(range(n))
    perm = list(itertools.permutations(l))
    min_dist = 1000000; good_perm = [0]*n
    for p in perm:
        d=0
        f=capacity
        for i in range(n-1):
            d+=dist[p[i]][p[i+1]]
            f-=fuel[p[i]][p[i+1]]
            if f<0:
                continue
            f+=station[p[i+1]]
        d+=dist[p[-1]][p[0]]
        f-=fuel[p[-1]][p[0]]
        if f<0:
            continue
        elif d<=min_dist:
            min_dist=d
            good_perm = p
    return min_dist, good_perm  

def brute_force_multi_optimum(dist, fuel, station, capacity):
    n = len(dist); l=list(range(n))
    perm = list(itertools.permutations(l))
    score = 1000000; good_perm = [0]*n
    for p in perm:
        d=0
        f=capacity
        for i in range(n-1):
            d+=2*dist[p[i]][p[i+1]]+fuel[p[i]][p[i+1]]
            f-=fuel[p[i]][p[i+1]]
            if f<0:
                continue
            f+=station[p[i+1]]
        d+=2*dist[p[-1]][p[0]]+fuel[p[-1]][p[0]]
        f-=fuel[p[-1]][p[0]]
        if f<0:
            continue
        elif d<=score:
            score=d
            good_perm = p
    return score, good_perm

def lowestedge1(dist, fuel, stat, cap):
    n = len(dist)
    v=0
    solution=[0]
    used=[0]*n
    path=0
    f=cap
    while (len(solution)<n):
        candidate=0
        candidate_value=1000000
        for i in range(n):
            if i==v:
                continue
            if (stat[i]+0.001) > fuel[v][i]:
                if (dist[v][i]/(stat[i]+0.001-fuel[v][i]))<candidate_value and f-fuel[v][i]>=0 and used[i]==0:
                    candidate=i
                    candidate_value = dist[v][i]/(stat[i]+0.001-fuel[v][i])
        if candidate_value==1000000:
            candidate_value=-1000000
            for i in range(n):
                if i==v:
                    continue
                if abs(dist[v][i]/(stat[i]+0.001-fuel[v][i]))>candidate_value and f-fuel[v][i]>=0 and used[i]==0:
                    candidate = i
                    candidate_value = abs(dist[v][i]/(stat[i]+0.001-fuel[v][i]))
        if candidate==v:
            print("wrong")
            return path,solution
        solution.append(candidate)
        path+=dist[v][candidate]
        f-=fuel[v][candidate]
        f+=stat[candidate]
        used[v]+=1
        used[candidate]+=1
        v=candidate
    f-=fuel[solution[-1]][0]
    if f<0:
        print("wrong")
        return path,solution
    path+=dist[solution[-1]][0]
    return path, solution

def lowestedge_multi(dist, fuel, stat, cap):
    n = len(dist)
    v=0
    solution=[0]
    used=[0]*n
    path=0
    f=cap
    while (len(solution)<n):
        candidate=0
        candidate_value=1000000
        for i in range(n):
            if i==v:
                continue
            if (stat[i]+0.001) > fuel[v][i]:
                if (dist[v][i]/(stat[i]+0.001-fuel[v][i]))<candidate_value and f-fuel[v][i]>=0 and used[i]==0:
                    candidate=i
                    candidate_value = dist[v][i]/(stat[i]+0.001-fuel[v][i])
        if candidate_value==1000000:
            candidate_value=-1000000
            for i in range(n):
                if i==v:
                    continue
                if abs(dist[v][i]/(stat[i]+0.001-fuel[v][i]))>candidate_value and f-fuel[v][i]>=0 and used[i]==0:
                    candidate = i
                    candidate_value = abs(dist[v][i]/(stat[i]+0.001-fuel[v][i]))
        if candidate==v:
            print("wrong")
            return path,solution
        solution.append(candidate)
        path+=2*dist[v][candidate]+fuel[v][candidate]
        f-=fuel[v][candidate]
        f+=stat[candidate]
        used[v]+=1
        used[candidate]+=1
        v=candidate
    f-=fuel[solution[-1]][0]
    if f<0:
        print("wrong")
        return path,solution
    path+=2*dist[solution[-1]][0]+fuel[solution[-1]][0]
    return path, solution