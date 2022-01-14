def solution(N, stages):
    clear = [0]*(N+2)
    fail_dict ={}

    for i in stages:
        clear[i] += 1
    
    for j in range(1,len(clear)-1):
        if (len(stages)-sum(clear[:j])) != 0 :
            fail_dict[j] = clear[j]/(len(stages)-sum(clear[:j]))
        else:  #분모가 0이 되는 경우 제외 (런타임 에러 발생)
            fail_dict[j] = 0

    fail_dict = sorted(fail_dict.items(), key=lambda x: (-x[1],x[0]))
    
    answer = [n[0] for n in fail_dict]
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = solution(N, stages)
print(answer)
