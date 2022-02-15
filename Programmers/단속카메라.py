def solution(routes):
    answer = 1
    #print(routes) 	[[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
    routes.sort(key=lambda x:x[1])
    #print(routes)  [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    camera = routes[0][1]
    for i in range(len(routes)):
        car_out = routes[i][1]
        car_in = routes[i][0]
        #print(car_in, car_out)
        #print("camera=", camera)
        if camera >= car_in and camera <= car_out:
            continue
        if camera < car_in:
            camera = car_out
            answer += 1
    return answer

#print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
