import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import traci
from collections import defaultdict


def rulebase():
    car_id = {}
    car_id = defaultdict(list)
    def count_traveltime(id,cycle):
        for i in id:
            # そのIDがリストの中にあるかないかチェック
            if i not in car_id or car_id[i][1] != cycle:
                car_id[i] =[0, cycle]
                
            else:
                car_id[i][0] += 1
            # print(car_id[i])
            # print(car_id[i][0])

    if __name__ == "__main__":
        os.chdir(os.path.dirname(os.path.abspath(__file__)))    
        rewards = []
        travel_time = []
        # traci.start(["sumo-gui", "-c", "nine.sumocfg"])
        traci.start(["sumo", "-c", "nine.sumocfg"])
        cycle = 0
        j = 0
        for iter in range(30):
            for step in range(1000):
                # r = reward()
                # rewards.append(r)
                id = traci.vehicle.getIDList()
                # check_car()
                count_traveltime(id,cycle)
                traci.simulationStep()   
            if j == 0:
                j += 1
            else:
                a = 0
                b = 1
                for i in car_id:
                    if car_id[i][1] == cycle:
                        a += car_id[i][0]
                        b += 1
                traveltime = a / b
                # print(traveltime)
                travel_time.append(traveltime)
                cycle += 1
        traci.close()
        return travel_time

def reinforcement():
    Qtable_c1 = np.zeros((300,300,2,2))
    Qtable_c2 = np.zeros((300,300,2,2))
    Qtable_c3 = np.zeros((300,300,2,2))
    Qtable_c4 = np.zeros((300,300,2,2))
    Qtable_c5 = np.zeros((300,300,2,2))
    Qtable_c6 = np.zeros((300,300,2,2))
    Qtable_c7 = np.zeros((300,300,2,2))
    Qtable_c8 = np.zeros((300,300,2,2))
    Qtable_c9 = np.zeros((300,300,2,2))
    epsilon = 0.1
    gamma = 0.9
    alpha = 0.1
    xmlfl = "choice.net.xml"
    car_id = {}
    car_id = defaultdict(list)
    def count_traveltime(id,cycle):
        for i in id:
            if i not in car_id or car_id[i][1] != cycle:
                car_id[i] =[0, cycle]
            else:
                car_id[i][0] += 1

    def get_state_c1():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c2_c1")
        cars_l_c = traci.edge.getLastStepHaltingNumber("l1_c1")
        cars_t_c = traci.edge.getLastStepHaltingNumber("t1_c1")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c4_c1")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c1")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def get_state_c2():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c3_c2")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c1_c2")
        cars_t_c = traci.edge.getLastStepHaltingNumber("t2_c2")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c5_c2")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c2")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def get_state_c3():
        cars_r_c = traci.edge.getLastStepHaltingNumber("r1_c3")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c2_c3")
        cars_t_c = traci.edge.getLastStepHaltingNumber("t3_c3")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c6_c3")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c3")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def get_state_c4():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c5_c4")
        cars_l_c = traci.edge.getLastStepHaltingNumber("l2_c4")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c1_c4")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c7_c4")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c4")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def get_state_c5():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c6_c5")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c4_c5")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c2_c5")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c8_c5")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c5")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def get_state_c6():
        cars_r_c = traci.edge.getLastStepHaltingNumber("r2_c6")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c5_c6")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c3_c6")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c9_c6")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c6")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def get_state_c7():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c8_c7")
        cars_l_c = traci.edge.getLastStepHaltingNumber("l3_c7")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c4_c7")
        cars_b_c = traci.edge.getLastStepHaltingNumber("b1_c7")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c7")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def get_state_c8():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c9_c8")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c7_c8")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c5_c8")
        cars_b_c = traci.edge.getLastStepHaltingNumber("b2_c8")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c8")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def get_state_c9():
        cars_r_c = traci.edge.getLastStepHaltingNumber("r3_c9")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c8_c9")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c6_c9")
        cars_b_c = traci.edge.getLastStepHaltingNumber("b3_c9")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c9")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase]
        return state

    def select_action(s,c):
        if c == 1:
            if epsilon < np.random.rand():
                q = Qtable_c1[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 2:
            if epsilon < np.random.rand():
                q = Qtable_c2[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 3:
            if epsilon < np.random.rand():
                q = Qtable_c3[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 4:
            if epsilon < np.random.rand():
                q = Qtable_c4[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)         
        elif c == 5:
            if epsilon < np.random.rand():
                q = Qtable_c5[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 6:
            if epsilon < np.random.rand():
                q = Qtable_c6[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 7:
            if epsilon < np.random.rand():
                q = Qtable_c7[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)   
        elif c == 8:
            if epsilon < np.random.rand():
                q = Qtable_c8[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 9:
            if epsilon < np.random.rand():
                q = Qtable_c9[s[0]][s[1]][s[2]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)       

    def select_greedy_action(s):
        q = Qtable[s[0]][s[1]][s[2]]
        actions = np.where(q == q.max())[0]
        return np.random.choice(actions)

    def state_trans(a,c):
        if c == 1:
            phase = traci.trafficlight.getPhase("c1")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c1",0)
                else:
                    traci.trafficlight.setPhase("c1",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c1",2)
                else:
                    traci.trafficlight.setPhase("c1",1)
        elif c == 2:
            phase = traci.trafficlight.getPhase("c2")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c2",0)
                else:
                    traci.trafficlight.setPhase("c2",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c2",2)
                else:
                    traci.trafficlight.setPhase("c2",1)
        elif c == 3:
            phase = traci.trafficlight.getPhase("c3")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c3",0)
                else:
                    traci.trafficlight.setPhase("c3",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c3",2)
                else:
                    traci.trafficlight.setPhase("c3",1)
        elif c == 4:
            phase = traci.trafficlight.getPhase("c4")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c4",0)
                else:
                    traci.trafficlight.setPhase("c4",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c4",2)
                else:
                    traci.trafficlight.setPhase("c4",1)
        elif c == 5:
            phase = traci.trafficlight.getPhase("c5")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c5",0)
                else:
                    traci.trafficlight.setPhase("c5",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c5",2)
                else:
                    traci.trafficlight.setPhase("c5",1)
        elif c == 6:
            phase = traci.trafficlight.getPhase("c6")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c6",0)
                else:
                    traci.trafficlight.setPhase("c6",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c6",2)
                else:
                    traci.trafficlight.setPhase("c6",1)
        elif c == 7:
            phase = traci.trafficlight.getPhase("c7")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c7",0)
                else:
                    traci.trafficlight.setPhase("c7",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c7",2)
                else:
                    traci.trafficlight.setPhase("c7",1)
        elif c == 8:
            phase = traci.trafficlight.getPhase("c8")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c8",0)
                else:
                    traci.trafficlight.setPhase("c8",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c8",2)
                else:
                    traci.trafficlight.setPhase("c8",1)
        elif c == 9:
            phase = traci.trafficlight.getPhase("c9")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c9",0)
                else:
                    traci.trafficlight.setPhase("c9",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c9",2)
                else:
                    traci.trafficlight.setPhase("c9",1)


    def reward_c1():
        t_c = traci.edge.getLastStepHaltingNumber("t1_c1")
        r_c = traci.edge.getLastStepHaltingNumber("c2_c1")
        l_c = traci.edge.getLastStepHaltingNumber("l1_c1")
        b_c = traci.edge.getLastStepHaltingNumber("c4_c1")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c2():
        t_c = traci.edge.getLastStepHaltingNumber("t2_c2")
        r_c = traci.edge.getLastStepHaltingNumber("c3_c2")
        l_c = traci.edge.getLastStepHaltingNumber("c1_c2")
        b_c = traci.edge.getLastStepHaltingNumber("c5_c2")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c3():
        t_c = traci.edge.getLastStepHaltingNumber("t3_c3")
        r_c = traci.edge.getLastStepHaltingNumber("r1_c3")
        l_c = traci.edge.getLastStepHaltingNumber("c2_c3")
        b_c = traci.edge.getLastStepHaltingNumber("c6_c3")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c4():
        t_c = traci.edge.getLastStepHaltingNumber("c1_c4")
        r_c = traci.edge.getLastStepHaltingNumber("c5_c4")
        l_c = traci.edge.getLastStepHaltingNumber("l2_c4")
        b_c = traci.edge.getLastStepHaltingNumber("c7_c4")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c5():
        t_c = traci.edge.getLastStepHaltingNumber("c2_c5")
        r_c = traci.edge.getLastStepHaltingNumber("c6_c5")
        l_c = traci.edge.getLastStepHaltingNumber("c4_c5")
        b_c = traci.edge.getLastStepHaltingNumber("c8_c5")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c6():
        t_c = traci.edge.getLastStepHaltingNumber("c3_c6")
        r_c = traci.edge.getLastStepHaltingNumber("r2_c6")
        l_c = traci.edge.getLastStepHaltingNumber("c5_c6")
        b_c = traci.edge.getLastStepHaltingNumber("c9_c6")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c7():
        t_c = traci.edge.getLastStepHaltingNumber("c4_c7")
        r_c = traci.edge.getLastStepHaltingNumber("c8_c7")
        l_c = traci.edge.getLastStepHaltingNumber("l3_c7")
        b_c = traci.edge.getLastStepHaltingNumber("b1_c7")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c8():
        t_c = traci.edge.getLastStepHaltingNumber("c5_c8")
        r_c = traci.edge.getLastStepHaltingNumber("c9_c8")
        l_c = traci.edge.getLastStepHaltingNumber("c7_c8")
        b_c = traci.edge.getLastStepHaltingNumber("b2_c8")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c9():
        t_c = traci.edge.getLastStepHaltingNumber("c6_c9")
        r_c = traci.edge.getLastStepHaltingNumber("r3_c9")
        l_c = traci.edge.getLastStepHaltingNumber("c8_c9")
        b_c = traci.edge.getLastStepHaltingNumber("b3_c9")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def get_Qvalue(s,a,c):
        if c == 1:
            return Qtable_c1[s[0]][s[1]][s[2]][a]
        elif c == 2:
            return Qtable_c2[s[0]][s[1]][s[2]][a]
        elif c == 3:
            return Qtable_c3[s[0]][s[1]][s[2]][a]
        elif c == 4:
            return Qtable_c4[s[0]][s[1]][s[2]][a]
        elif c == 5:
            return Qtable_c5[s[0]][s[1]][s[2]][a]
        elif c == 6:
            return Qtable_c6[s[0]][s[1]][s[2]][a]
        elif c == 7:
            return Qtable_c7[s[0]][s[1]][s[2]][a]
        elif c == 8:
            return Qtable_c8[s[0]][s[1]][s[2]][a]
        elif c == 9:
            return Qtable_c9[s[0]][s[1]][s[2]][a]

    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    cycle = 0
    traci.start(["sumo", "-c", "nine.sumocfg"]) 
    # traci.start(["sumo-gui", "-c", "nine.sumocfg"]) 
    # traci.simulationStep(2000)
    s1 = get_state_c1()
    s2 = get_state_c2()
    s3 = get_state_c3()
    s4 = get_state_c4()
    s5 = get_state_c5()
    s6 = get_state_c6()
    s7 = get_state_c7()
    s8 = get_state_c8()
    s9 = get_state_c9()
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    a9 = 0
    phase_before1 = 0
    phase_before2 = 0
    phase_before3 = 0
    phase_before4 = 0
    phase_before5 = 0
    phase_before6 = 0
    phase_before7 = 0
    phase_before8 = 0
    phase_before9 = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    # traci.simulationStep(500)
    for iter in range(30):
        for step in range(1000):
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            phase1 = traci.trafficlight.getPhase("c1")
            phase2 = traci.trafficlight.getPhase("c2")
            phase3 = traci.trafficlight.getPhase("c3")
            phase4 = traci.trafficlight.getPhase("c4")
            phase5 = traci.trafficlight.getPhase("c5")
            phase6 = traci.trafficlight.getPhase("c6")
            phase7 = traci.trafficlight.getPhase("c7")
            phase8 = traci.trafficlight.getPhase("c8")
            phase9 = traci.trafficlight.getPhase("c9")
            if phase_before1 == phase1:
                if num1 == 10:
                    before_s1 = s1
                    s1 = get_state_c1()
                    before_a1 = a1
                    a1 = select_action(s1,1)
                    r = reward_c1()
                    Qtable_c1[before_s1[0]][before_s1[1]][before_s1[2]][before_a1] = (1-alpha)*Qtable_c1[before_s1[0]][before_s1[1]][before_s1[2]][before_a1] + alpha*(r + gamma*get_Qvalue(s1,a1,1))
                    state_trans(a1,1)
                    phase_before1 = traci.trafficlight.getPhase("c1")
                    num1 = -1
            else:
                if num1 == 13:
                    before_s1 = s1
                    s1 = get_state_c1()
                    before_a1 = a1
                    a1 = select_action(s1,1)
                    r = reward_c1()
                    Qtable_c1[before_s1[0]][before_s1[1]][before_s1[2]][before_a1] = (1-alpha)*Qtable_c1[before_s1[0]][before_s1[1]][before_s1[2]][before_a1] + alpha*(r + gamma*get_Qvalue(s1,a1,1))
                    state_trans(a1,1)
                    phase_before = traci.trafficlight.getPhase("c1")
                    num1 = -1
            if phase_before2 == phase2:
                if num2 == 10:
                    before_s2 = s2
                    s2 = get_state_c2()
                    before_a2 = a2
                    a2 = select_action(s2,2)
                    r = reward_c2()
                    Qtable_c2[before_s2[0]][before_s2[1]][before_s2[2]][before_a2] = (1-alpha)*Qtable_c2[before_s2[0]][before_s2[1]][before_s2[2]][before_a2] + alpha*(r + gamma*get_Qvalue(s2,a2,2))
                    state_trans(a2,2)
                    phase_before1 = traci.trafficlight.getPhase("c2")
                    num2 = -1
            else:
                if num2 == 13:
                    before_s2 = s2
                    s2 = get_state_c2()
                    before_a2 = a2
                    a2 = select_action(s2,2)
                    r = reward_c2()
                    Qtable_c2[before_s2[0]][before_s2[1]][before_s2[2]][before_a2] = (1-alpha)*Qtable_c2[before_s2[0]][before_s2[1]][before_s2[2]][before_a2] + alpha*(r + gamma*get_Qvalue(s2,a2,2))
                    state_trans(a2,2)
                    phase_before = traci.trafficlight.getPhase("c2")
                    num2 = -1
            if phase_before3 == phase3:
                if num3 == 10:
                    before_s3 = s3
                    s3 = get_state_c3()
                    before_a3 = a3
                    a3 = select_action(s3,3)
                    r = reward_c3()
                    Qtable_c3[before_s3[0]][before_s3[1]][before_s3[2]][before_a3] = (1-alpha)*Qtable_c3[before_s3[0]][before_s3[1]][before_s3[2]][before_a3] + alpha*(r + gamma*get_Qvalue(s3,a3,3))
                    state_trans(a3,3)
                    phase_before3 = traci.trafficlight.getPhase("c3")
                    num3 = -1
            else:
                if num3 == 13:
                    before_s3 = s3
                    s3 = get_state_c3()
                    before_a3 = a3
                    a3 = select_action(s3,3)
                    r = reward_c3()
                    Qtable_c3[before_s3[0]][before_s3[1]][before_s3[2]][before_a3] = (1-alpha)*Qtable_c3[before_s3[0]][before_s3[1]][before_s3[2]][before_a3] + alpha*(r + gamma*get_Qvalue(s3,a3,3))
                    state_trans(a3,3)
                    phase_before = traci.trafficlight.getPhase("c3")
                    num3 = -1
            if phase_before4 == phase4:
                if num4 == 10:
                    before_s4 = s4
                    s4 = get_state_c4()
                    before_a4 = a4
                    a4 = select_action(s4,4)
                    r = reward_c4()
                    Qtable_c4[before_s4[0]][before_s4[1]][before_s4[2]][before_a4] = (1-alpha)*Qtable_c4[before_s4[0]][before_s4[1]][before_s4[2]][before_a4] + alpha*(r + gamma*get_Qvalue(s4,a4,4))
                    state_trans(a4,4)
                    phase_before4 = traci.trafficlight.getPhase("c4")
                    num4 = -1
            else:
                if num4 == 13:
                    before_s4 = s4
                    s4 = get_state_c4()
                    before_a4 = a4
                    a4 = select_action(s4,4)
                    r = reward_c4()
                    Qtable_c4[before_s4[0]][before_s4[1]][before_s4[2]][before_a4] = (1-alpha)*Qtable_c4[before_s4[0]][before_s4[1]][before_s4[2]][before_a4] + alpha*(r + gamma*get_Qvalue(s4,a4,4))
                    state_trans(a4,4)
                    phase_before = traci.trafficlight.getPhase("c4")
                    num4 = -1
            if phase_before4 == phase4:
                if num5 == 10:
                    before_s5 = s5
                    s5 = get_state_c5()
                    before_a5 = a5
                    a5 = select_action(s5,5)
                    r = reward_c5()
                    Qtable_c5[before_s5[0]][before_s5[1]][before_s5[2]][before_a5] = (1-alpha)*Qtable_c5[before_s5[0]][before_s5[1]][before_s5[2]][before_a5] + alpha*(r + gamma*get_Qvalue(s5,a5,5))
                    state_trans(a5,5)
                    phase_before5 = traci.trafficlight.getPhase("c5")
                    num5 = -1
            else:
                if num5 == 13:
                    before_s5 = s5
                    s5 = get_state_c5()
                    before_a5 = a5
                    a5 = select_action(s5,5)
                    r = reward_c5()
                    Qtable_c5[before_s5[0]][before_s5[1]][before_s5[2]][before_a5] = (1-alpha)*Qtable_c5[before_s5[0]][before_s5[1]][before_s5[2]][before_a5] + alpha*(r + gamma*get_Qvalue(s5,a5,5))
                    state_trans(a5,5)
                    phase_before = traci.trafficlight.getPhase("c5")
                    num5 = -1
            if num6 == 10:
                    before_s6 = s6
                    s6 = get_state_c6()
                    before_a6 = a6
                    a6 = select_action(s6,6)
                    r = reward_c6()
                    Qtable_c6[before_s6[0]][before_s6[1]][before_s6[2]][before_a6] = (1-alpha)*Qtable_c6[before_s6[0]][before_s6[1]][before_s6[2]][before_a6] + alpha*(r + gamma*get_Qvalue(s6,a6,6))
                    state_trans(a6,6)
                    phase_before6 = traci.trafficlight.getPhase("c6")
                    num6 = -1
            else:
                if num6 == 13:
                    before_s6 = s6
                    s6 = get_state_c6()
                    before_a6 = a6
                    a6 = select_action(s6,6)
                    r = reward_c6()
                    Qtable_c6[before_s6[0]][before_s6[1]][before_s6[2]][before_a6] = (1-alpha)*Qtable_c6[before_s6[0]][before_s6[1]][before_s6[2]][before_a6] + alpha*(r + gamma*get_Qvalue(s6,a6,6))
                    state_trans(a6,6)
                    phase_before = traci.trafficlight.getPhase("c6")
                    num6 = -1
            if num7 == 10:
                    before_s7 = s7
                    s7 = get_state_c7()
                    before_a7 = a7
                    a7 = select_action(s7,7)
                    r = reward_c7()
                    Qtable_c7[before_s7[0]][before_s7[1]][before_s7[2]][before_a7] = (1-alpha)*Qtable_c7[before_s7[0]][before_s7[1]][before_s7[2]][before_a7] + alpha*(r + gamma*get_Qvalue(s7,a7,7))
                    state_trans(a7,7)
                    phase_before7 = traci.trafficlight.getPhase("c7")
                    num7 = -1
            else:
                if num7 == 13:
                    before_s7 = s7
                    s7 = get_state_c7()
                    before_a7 = a7
                    a7 = select_action(s7,7)
                    r = reward_c7()
                    Qtable_c7[before_s7[0]][before_s7[1]][before_s7[2]][before_a7] = (1-alpha)*Qtable_c7[before_s7[0]][before_s7[1]][before_s7[2]][before_a7] + alpha*(r + gamma*get_Qvalue(s7,a7,7))
                    state_trans(a7,7)
                    phase_before = traci.trafficlight.getPhase("c7")
                    num7 = -1
            if num8 == 10:
                    before_s8 = s8
                    s8 = get_state_c8()
                    before_a8 = a8
                    a8 = select_action(s8,8)
                    r = reward_c8()
                    Qtable_c8[before_s8[0]][before_s8[1]][before_s8[2]][before_a8] = (1-alpha)*Qtable_c8[before_s8[0]][before_s8[1]][before_s8[2]][before_a8] + alpha*(r + gamma*get_Qvalue(s8,a8,8))
                    state_trans(a8,8)
                    phase_before8 = traci.trafficlight.getPhase("c8")
                    num8 = -1
            else:
                if num8 == 13:
                    before_s8 = s8
                    s8 = get_state_c8()
                    before_a8 = a8
                    a8 = select_action(s8,8)
                    r = reward_c8()
                    Qtable_c8[before_s8[0]][before_s8[1]][before_s8[2]][before_a8] = (1-alpha)*Qtable_c8[before_s8[0]][before_s8[1]][before_s8[2]][before_a8] + alpha*(r + gamma*get_Qvalue(s8,a8,8))
                    state_trans(a8,8)
                    phase_before = traci.trafficlight.getPhase("c8")
                    num8 = -1
            if num9 == 10:
                    before_s9 = s9
                    s9 = get_state_c9()
                    before_a9 = a9
                    a9 = select_action(s9,9)
                    r = reward_c9()
                    Qtable_c9[before_s9[0]][before_s9[1]][before_s9[2]][before_a9] = (1-alpha)*Qtable_c9[before_s9[0]][before_s9[1]][before_s9[2]][before_a9] + alpha*(r + gamma*get_Qvalue(s9,a9,9))
                    state_trans(a9,9)
                    phase_before9 = traci.trafficlight.getPhase("c9")
                    num9 = -1
            else:
                if num9 == 13:
                    before_s9 = s9
                    s9 = get_state_c9()
                    before_a9 = a9
                    a9 = select_action(s9,9)
                    r = reward_c9()
                    Qtable_c9[before_s9[0]][before_s9[1]][before_s9[2]][before_a9] = (1-alpha)*Qtable_c9[before_s9[0]][before_s9[1]][before_s9[2]][before_a9] + alpha*(r + gamma*get_Qvalue(s9,a9,9))
                    state_trans(a9,9)
                    phase_before = traci.trafficlight.getPhase("c9")
                    num9 = -1
            num1 += 1
            num2 += 1
            num3 += 1
            num4 += 1
            num5 += 1
            num6 += 1
            num7 += 1
            num8 += 1
            num9 += 1
            
            traci.simulationStep()
        c = 0
        b = 1
        for i in car_id:
            if car_id[i][1] == cycle:
                c += car_id[i][0]
                b += 1
        traveltime = c / b
        travel_time.append(traveltime)
        # print(travel_time)
        cycle += 1
    traci.close()
    return travel_time

def reinforcement2():
    Qtable_c1 = np.zeros((300,300,2,2,2,2))
    Qtable_c2 = np.zeros((300,300,2,2,2,2,2))
    Qtable_c3 = np.zeros((300,300,2,2,2,2))
    Qtable_c4 = np.zeros((300,300,2,2,2,2,2))
    Qtable_c5 = np.zeros((300,300,2,2,2,2,2,2))
    Qtable_c6 = np.zeros((300,300,2,2,2,2,2))
    Qtable_c7 = np.zeros((300,300,2,2,2,2))
    Qtable_c8 = np.zeros((300,300,2,2,2,2,2))
    Qtable_c9 = np.zeros((300,300,2,2,2,2))
    epsilon = 0.1
    gamma = 0.9
    alpha = 0.1
    xmlfl = "choice.net.xml"
    car_id = {}
    car_id = defaultdict(list)
    def count_traveltime(id,cycle):
        for i in id:
            if i not in car_id or car_id[i][1] != cycle:
                car_id[i] =[0, cycle]
            else:
                car_id[i][0] += 1

    def get_state_c1():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c2_c1")
        cars_l_c = traci.edge.getLastStepHaltingNumber("l1_c1")
        cars_t_c = traci.edge.getLastStepHaltingNumber("t1_c1")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c4_c1")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c1")
        phase2 = traci.trafficlight.getPhase("c2")
        phase4 = traci.trafficlight.getPhase("c4")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase2 < 4:
            phase2 = 0
        else:
            phase2 = 1
        if phase4 < 4:
            phase4 = 0
        else:
            phase4 = 1
        state = [tate,yoko,phase,phase2,phase4]
        return state

    def get_state_c2():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c3_c2")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c1_c2")
        cars_t_c = traci.edge.getLastStepHaltingNumber("t2_c2")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c5_c2")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c2")
        phase1 = traci.trafficlight.getPhase("c1")
        phase3 = traci.trafficlight.getPhase("c3")
        phase5 = traci.trafficlight.getPhase("c5")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase1 < 4:
            phase1 = 0
        else:
            phase1 = 1
        if phase3 < 4:
            phase3 = 0
        else:
            phase3 = 1
        if phase5 < 4:
            phase5 = 0
        else:
            phase5 = 1
        state = [tate,yoko,phase,phase1,phase3,phase5]
        return state

    def get_state_c3():
        cars_r_c = traci.edge.getLastStepHaltingNumber("r1_c3")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c2_c3")
        cars_t_c = traci.edge.getLastStepHaltingNumber("t3_c3")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c6_c3")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c3")
        phase2 = traci.trafficlight.getPhase("c2")
        phase6 = traci.trafficlight.getPhase("c6")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase2 < 4:
            phase2 = 0
        else:
            phase2 = 1
        if phase6 < 4:
            phase6 = 0
        else:
            phase6 = 1
        state = [tate,yoko,phase,phase2,phase6]
        return state

    def get_state_c4():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c5_c4")
        cars_l_c = traci.edge.getLastStepHaltingNumber("l2_c4")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c1_c4")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c7_c4")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c4")
        phase1 = traci.trafficlight.getPhase("c1")
        phase5 = traci.trafficlight.getPhase("c5")
        phase7 = traci.trafficlight.getPhase("c7")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase1 < 4:
            phase1 = 0
        else:
            phase1 = 1
        if phase5 < 4:
            phase5 = 0
        else:
            phase5 = 1
        if phase7 < 4:
            phase7 = 0
        else:
            phase7 = 1
        state = [tate,yoko,phase,phase1,phase5,phase7]
        return state
    
    def get_state_c5():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c6_c5")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c4_c5")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c2_c5")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c8_c5")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c5")
        phase2 = traci.trafficlight.getPhase("c2")
        phase4 = traci.trafficlight.getPhase("c4")
        phase6 = traci.trafficlight.getPhase("c6")
        phase8 = traci.trafficlight.getPhase("c8")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase2 < 4:
            phase2 = 0
        else:
            phase2 = 1
        if phase4 < 4:
            phase4 = 0
        else:
            phase4 = 1
        if phase6 < 4:
            phase6 = 0
        else:
            phase6 = 1
        if phase8 < 4:
            phase8 = 0
        else:
            phase8 = 1
        state = [tate,yoko,phase,phase2,phase4,phase6,phase8]
        return state

    def get_state_c6():
        cars_r_c = traci.edge.getLastStepHaltingNumber("r2_c6")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c5_c6")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c3_c6")
        cars_b_c = traci.edge.getLastStepHaltingNumber("c9_c6")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c6")
        phase3 = traci.trafficlight.getPhase("c3")
        phase5 = traci.trafficlight.getPhase("c5")
        phase9 = traci.trafficlight.getPhase("c9")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase3 < 4:
            phase3 = 0
        else:
            phase3 = 1
        if phase5 < 4:
            phase5 = 0
        else:
            phase5 = 1
        if phase9 < 4:
            phase9 = 0
        else:
            phase9 = 1
        state = [tate,yoko,phase,phase3,phase5,phase9]
        return state

    def get_state_c7():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c8_c7")
        cars_l_c = traci.edge.getLastStepHaltingNumber("l3_c7")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c4_c7")
        cars_b_c = traci.edge.getLastStepHaltingNumber("b1_c7")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c7")
        phase4 = traci.trafficlight.getPhase("c4")
        phase8 = traci.trafficlight.getPhase("c8")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase4 < 4:
            phase4 = 0
        else:
            phase4 = 1
        if phase8 < 4:
            phase8 = 0
        else:
            phase8 = 1
        state = [tate,yoko,phase,phase4,phase8]
        return state

    def get_state_c8():
        cars_r_c = traci.edge.getLastStepHaltingNumber("c9_c8")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c7_c8")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c5_c8")
        cars_b_c = traci.edge.getLastStepHaltingNumber("b2_c8")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c8")
        phase5 = traci.trafficlight.getPhase("c5")
        phase7 = traci.trafficlight.getPhase("c7")
        phase9 = traci.trafficlight.getPhase("c9")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase5 < 4:
            phase5 = 0
        else:
            phase5 = 1
        if phase7 < 4:
            phase7 = 0
        else:
            phase7 = 1
        if phase9 < 4:
            phase9 = 0
        else:
            phase9 = 1
        state = [tate,yoko,phase,phase5,phase7,phase9]
        return state

    def get_state_c9():
        cars_r_c = traci.edge.getLastStepHaltingNumber("r3_c9")
        cars_l_c = traci.edge.getLastStepHaltingNumber("c8_c9")
        cars_t_c = traci.edge.getLastStepHaltingNumber("c6_c9")
        cars_b_c = traci.edge.getLastStepHaltingNumber("b3_c9")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c8")
        phase6 = traci.trafficlight.getPhase("c6")
        phase8 = traci.trafficlight.getPhase("c8")
        if phase < 4:
            phase = 0
        else:
            phase = 1
        if phase6 < 4:
            phase6 = 0
        else:
            phase6 = 1
        if phase8 < 4:
            phase8 = 0
        else:
            phase8 = 1
        state = [tate,yoko,phase,phase6,phase8]
        return state

    def select_action(s,c):
        if c == 1:
            if epsilon < np.random.rand():
                q = Qtable_c1[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 2:
            if epsilon < np.random.rand():
                q = Qtable_c2[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 3:
            if epsilon < np.random.rand():
                q = Qtable_c3[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 4:
            if epsilon < np.random.rand():
                q = Qtable_c4[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)  
        elif c == 5:
            if epsilon < np.random.rand():
                q = Qtable_c5[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 6:
            if epsilon < np.random.rand():
                q = Qtable_c6[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 7:
            if epsilon < np.random.rand():
                q = Qtable_c7[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)      
        elif c == 8:
            if epsilon < np.random.rand():
                q = Qtable_c8[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)
        elif c == 9:
            if epsilon < np.random.rand():
                q = Qtable_c9[s[0]][s[1]][s[2]][s[3]][s[4]]
                actions = np.where(q == q.max())[0]
                return np.random.choice(actions)
            else:
                return np.random.choice(2)         

    def select_greedy_action(s):
        q = Qtable[s[0]][s[1]][s[2]][s[3]][s[4]]
        actions = np.where(q == q.max())[0]
        return np.random.choice(actions)

    def state_trans(a,c):
        if c == 1:
            phase = traci.trafficlight.getPhase("c1")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c1",0)
                else:
                    traci.trafficlight.setPhase("c1",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c1",2)
                else:
                    traci.trafficlight.setPhase("c1",1)
        elif c == 2:
            phase = traci.trafficlight.getPhase("c2")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c2",0)
                else:
                    traci.trafficlight.setPhase("c2",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c2",2)
                else:
                    traci.trafficlight.setPhase("c2",1)
        elif c == 3:
            phase = traci.trafficlight.getPhase("c3")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c3",0)
                else:
                    traci.trafficlight.setPhase("c3",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c3",2)
                else:
                    traci.trafficlight.setPhase("c3",1)
        elif c == 4:
            phase = traci.trafficlight.getPhase("c4")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c4",0)
                else:
                    traci.trafficlight.setPhase("c4",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c4",2)
                else:
                    traci.trafficlight.setPhase("c4",1)
        elif c == 5:
            phase = traci.trafficlight.getPhase("c5")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c5",0)
                else:
                    traci.trafficlight.setPhase("c5",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c5",2)
                else:
                    traci.trafficlight.setPhase("c5",1)
        elif c == 6:
            phase = traci.trafficlight.getPhase("c6")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c6",0)
                else:
                    traci.trafficlight.setPhase("c6",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c6",2)
                else:
                    traci.trafficlight.setPhase("c6",1)
        elif c == 7:
            phase = traci.trafficlight.getPhase("c7")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c7",0)
                else:
                    traci.trafficlight.setPhase("c7",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c7",2)
                else:
                    traci.trafficlight.setPhase("c7",1)
        elif c == 8:
            phase = traci.trafficlight.getPhase("c8")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c8",0)
                else:
                    traci.trafficlight.setPhase("c8",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c8",2)
                else:
                    traci.trafficlight.setPhase("c8",1)
        elif c == 9:
            phase = traci.trafficlight.getPhase("c9")
            if a == 0:
                if phase == 0:
                    traci.trafficlight.setPhase("c9",0)
                else:
                    traci.trafficlight.setPhase("c9",3)
            elif a == 1:
                if phase == 2:
                    traci.trafficlight.setPhase("c9",2)
                else:
                    traci.trafficlight.setPhase("c9",1)

    def reward_c1():
        t_c = traci.edge.getLastStepHaltingNumber("t1_c1")
        r_c = traci.edge.getLastStepHaltingNumber("c2_c1")
        l_c = traci.edge.getLastStepHaltingNumber("l1_c1")
        b_c = traci.edge.getLastStepHaltingNumber("c4_c1")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c2():
        t_c = traci.edge.getLastStepHaltingNumber("t2_c2")
        r_c = traci.edge.getLastStepHaltingNumber("c3_c2")
        l_c = traci.edge.getLastStepHaltingNumber("c1_c2")
        b_c = traci.edge.getLastStepHaltingNumber("c5_c2")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c3():
        t_c = traci.edge.getLastStepHaltingNumber("t3_c3")
        r_c = traci.edge.getLastStepHaltingNumber("r1_c3")
        l_c = traci.edge.getLastStepHaltingNumber("c2_c3")
        b_c = traci.edge.getLastStepHaltingNumber("c6_c3")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c4():
        t_c = traci.edge.getLastStepHaltingNumber("c1_c4")
        r_c = traci.edge.getLastStepHaltingNumber("c5_c4")
        l_c = traci.edge.getLastStepHaltingNumber("l2_c4")
        b_c = traci.edge.getLastStepHaltingNumber("c7_c4")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r
    
    def reward_c5():
        t_c = traci.edge.getLastStepHaltingNumber("c2_c5")
        r_c = traci.edge.getLastStepHaltingNumber("c6_c5")
        l_c = traci.edge.getLastStepHaltingNumber("c4_c5")
        b_c = traci.edge.getLastStepHaltingNumber("c8_c5")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r
    
    def reward_c6():
        t_c = traci.edge.getLastStepHaltingNumber("c3_c6")
        r_c = traci.edge.getLastStepHaltingNumber("r2_c6")
        l_c = traci.edge.getLastStepHaltingNumber("c5_c6")
        b_c = traci.edge.getLastStepHaltingNumber("c9_c6")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c7():
        t_c = traci.edge.getLastStepHaltingNumber("c4_c7")
        r_c = traci.edge.getLastStepHaltingNumber("c8_c7")
        l_c = traci.edge.getLastStepHaltingNumber("l3_c7")
        b_c = traci.edge.getLastStepHaltingNumber("b1_c7")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c8():
        t_c = traci.edge.getLastStepHaltingNumber("c5_c8")
        r_c = traci.edge.getLastStepHaltingNumber("c9_c8")
        l_c = traci.edge.getLastStepHaltingNumber("c7_c8")
        b_c = traci.edge.getLastStepHaltingNumber("b2_c8")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def reward_c9():
        t_c = traci.edge.getLastStepHaltingNumber("c6_c9")
        r_c = traci.edge.getLastStepHaltingNumber("r3_c9")
        l_c = traci.edge.getLastStepHaltingNumber("c8_c9")
        b_c = traci.edge.getLastStepHaltingNumber("b3_c9")
        r =  -(t_c + r_c + l_c + b_c)/300
        return r

    def get_Qvalue(s,a,c):
        if c == 1:
            return Qtable_c1[s[0]][s[1]][s[2]][s[3]][s[4]][a]
        elif c == 2:
            return Qtable_c2[s[0]][s[1]][s[2]][s[3]][s[4]][a]
        elif c == 3:
            return Qtable_c3[s[0]][s[1]][s[2]][s[3]][s[4]][a]
        elif c == 4:
            return Qtable_c4[s[0]][s[1]][s[2]][s[3]][s[4]][a]
        elif c == 5:
            return Qtable_c5[s[0]][s[1]][s[2]][s[3]][s[4]][a]
        elif c == 6:
            return Qtable_c6[s[0]][s[1]][s[2]][s[3]][s[4]][a]
        elif c == 7:
            return Qtable_c7[s[0]][s[1]][s[2]][s[3]][s[4]][a]
        elif c == 8:
            return Qtable_c8[s[0]][s[1]][s[2]][s[3]][s[4]][a]
        elif c == 9:
            return Qtable_c9[s[0]][s[1]][s[2]][s[3]][s[4]][a]

    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    cycle = 0
    traci.start(["sumo", "-c", "nine.sumocfg"]) 
    # traci.start(["sumo-gui", "-c", "nine.sumocfg"]) 
    # traci.simulationStep(2000)
    s1 = get_state_c1()
    s2 = get_state_c2()
    s3 = get_state_c3()
    s4 = get_state_c4()
    s5 = get_state_c5()
    s6 = get_state_c6()
    s7 = get_state_c7()
    s8 = get_state_c8()
    s9 = get_state_c9()
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    a9 = 0
    phase_before1 = 0
    phase_before2 = 0
    phase_before3 = 0
    phase_before4 = 0
    phase_before5 = 0
    phase_before6 = 0
    phase_before7 = 0
    phase_before8 = 0
    phase_before9 = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    # traci.simulationStep(500)
    for iter in range(30):
        i = 0
        for step in range(1000):
            i += 1
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            phase1 = traci.trafficlight.getPhase("c1")
            phase2 = traci.trafficlight.getPhase("c2")
            phase3 = traci.trafficlight.getPhase("c3")
            phase4 = traci.trafficlight.getPhase("c4")
            phase5 = traci.trafficlight.getPhase("c5")
            phase6 = traci.trafficlight.getPhase("c6")
            phase7 = traci.trafficlight.getPhase("c7")
            phase8 = traci.trafficlight.getPhase("c8")
            phase9 = traci.trafficlight.getPhase("c9")
            if phase_before1 == phase1:
                if num1 == 10:
                    before_s1 = s1
                    s1 = get_state_c1()
                    before_a1 = a1
                    a1 = select_action(s1,1)
                    r = reward_c1()
                    Qtable_c1[before_s1[0]][before_s1[1]][before_s1[2]][before_s1[3]][before_s1[4]][before_a1] = (1-alpha)*Qtable_c1[before_s1[0]][before_s1[1]][before_s1[2]][before_s1[3]][before_s1[4]][before_a1] + alpha*(r + gamma*get_Qvalue(s1,a1,1))
                    state_trans(a1,1)
                    phase_before1 = traci.trafficlight.getPhase("c1")
                    num1 = -1
            else:
                if num1 == 13:
                    before_s1 = s1
                    s1 = get_state_c1()
                    before_a1 = a1
                    a1 = select_action(s1,1)
                    r = reward_c1()
                    Qtable_c1[before_s1[0]][before_s1[1]][before_s1[2]][before_s1[3]][before_s1[4]][before_a1] = (1-alpha)*Qtable_c1[before_s1[0]][before_s1[1]][before_s1[2]][before_s1[3]][before_s1[4]][before_a1] + alpha*(r + gamma*get_Qvalue(s1,a1,1))
                    state_trans(a1,1)
                    phase_before = traci.trafficlight.getPhase("c1")
                    num1 = -1
            if phase_before2 == phase2:
                if num2 == 10:
                    before_s2 = s2
                    s2 = get_state_c2()
                    before_a2 = a2
                    a2 = select_action(s2,2)
                    r = reward_c2()
                    Qtable_c2[before_s2[0]][before_s2[1]][before_s2[2]][before_s2[3]][before_s2[4]][before_a2] = (1-alpha)*Qtable_c2[before_s2[0]][before_s2[1]][before_s2[2]][before_s2[3]][before_s2[4]][before_a2] + alpha*(r + gamma*get_Qvalue(s2,a2,2))
                    state_trans(a2,2)
                    phase_before1 = traci.trafficlight.getPhase("c2")
                    num2 = -1
            else:
                if num2 == 13:
                    before_s2 = s2
                    s2 = get_state_c2()
                    before_a2 = a2
                    a2 = select_action(s2,2)
                    r = reward_c2()
                    Qtable_c2[before_s2[0]][before_s2[1]][before_s2[2]][before_s2[3]][before_s2[4]][before_a2] = (1-alpha)*Qtable_c2[before_s2[0]][before_s2[1]][before_s2[2]][before_s2[3]][before_s2[4]][before_a2] + alpha*(r + gamma*get_Qvalue(s2,a2,2))
                    state_trans(a2,2)
                    phase_before = traci.trafficlight.getPhase("c2")
                    num2 = -1
            if phase_before3 == phase3:
                if num3 == 10:
                    before_s3 = s3
                    s3 = get_state_c3()
                    before_a3 = a3
                    a3 = select_action(s3,3)
                    r = reward_c3()
                    Qtable_c3[before_s3[0]][before_s3[1]][before_s3[2]][before_s3[3]][before_s3[4]][before_a3] = (1-alpha)*Qtable_c3[before_s3[0]][before_s3[1]][before_s3[2]][before_s3[3]][before_s3[4]][before_a3] + alpha*(r + gamma*get_Qvalue(s3,a3,3))
                    state_trans(a3,3)
                    phase_before3 = traci.trafficlight.getPhase("c3")
                    num3 = -1
            else:
                if num3 == 13:
                    before_s3 = s3
                    s3 = get_state_c3()
                    before_a3 = a3
                    a3 = select_action(s3,3)
                    r = reward_c3()
                    Qtable_c3[before_s3[0]][before_s3[1]][before_s3[2]][before_s3[3]][before_s3[4]][before_a3] = (1-alpha)*Qtable_c3[before_s3[0]][before_s3[1]][before_s3[2]][before_s3[3]][before_s3[4]][before_a3] + alpha*(r + gamma*get_Qvalue(s3,a3,3))
                    state_trans(a3,3)
                    phase_before = traci.trafficlight.getPhase("c3")
                    num3 = -1
            if phase_before4 == phase4:
                if num4 == 10:
                    before_s4 = s4
                    s4 = get_state_c4()
                    before_a4 = a4
                    a4 = select_action(s4,4)
                    r = reward_c4()
                    Qtable_c4[before_s4[0]][before_s4[1]][before_s4[2]][before_s4[3]][before_s4[4]][before_a4] = (1-alpha)*Qtable_c4[before_s4[0]][before_s4[1]][before_s4[2]][before_s4[3]][before_s4[4]][before_a4] + alpha*(r + gamma*get_Qvalue(s4,a4,4))
                    state_trans(a4,4)
                    phase_before4 = traci.trafficlight.getPhase("c4")
                    num4 = -1
            else:
                if num4 == 13:
                    before_s4 = s4
                    s4 = get_state_c4()
                    before_a4 = a4
                    a4 = select_action(s4,4)
                    r = reward_c4()
                    Qtable_c4[before_s4[0]][before_s4[1]][before_s4[2]][before_s4[3]][before_s4[4]][before_a4] = (1-alpha)*Qtable_c4[before_s4[0]][before_s4[1]][before_s4[2]][before_s4[3]][before_s4[4]][before_a4] + alpha*(r + gamma*get_Qvalue(s4,a4,4))
                    state_trans(a4,4)
                    phase_before = traci.trafficlight.getPhase("c4")
                    num4 = -1
            if phase_before5 == phase5:
                if num5 == 10:
                    before_s5 = s5
                    s5 = get_state_c5()
                    before_a5 = a5
                    a5 = select_action(s5,5)
                    r = reward_c5()
                    Qtable_c5[before_s5[0]][before_s5[1]][before_s5[2]][before_s5[3]][before_s5[4]][before_a5] = (1-alpha)*Qtable_c5[before_s5[0]][before_s5[1]][before_s5[2]][before_s5[3]][before_s5[4]][before_a5] + alpha*(r + gamma*get_Qvalue(s5,a5,5))
                    state_trans(a5,5)
                    phase_before5 = traci.trafficlight.getPhase("c5")
                    num5 = -1
            else:
                if num5 == 13:
                    before_s5 = s5
                    s5 = get_state_c5()
                    before_a5 = a5
                    a5 = select_action(s5,5)
                    r = reward_c5()
                    Qtable_c5[before_s5[0]][before_s5[1]][before_s5[2]][before_s5[3]][before_s5[4]][before_a5] = (1-alpha)*Qtable_c5[before_s5[0]][before_s5[1]][before_s5[2]][before_s5[3]][before_s5[4]][before_a5] + alpha*(r + gamma*get_Qvalue(s5,a5,5))
                    state_trans(a5,5)
                    phase_before = traci.trafficlight.getPhase("c5")
                    num5 = -1
            if phase_before6 == phase6:
                if num6 == 10:
                    before_s6 = s6
                    s6 = get_state_c6()
                    before_a6 = a6
                    a6 = select_action(s6,6)
                    r = reward_c6()
                    Qtable_c6[before_s6[0]][before_s6[1]][before_s6[2]][before_s6[3]][before_s6[4]][before_a6] = (1-alpha)*Qtable_c6[before_s6[0]][before_s6[1]][before_s6[2]][before_s6[3]][before_s6[4]][before_a6] + alpha*(r + gamma*get_Qvalue(s6,a6,6))
                    state_trans(a6,6)
                    phase_before6 = traci.trafficlight.getPhase("c6")
                    num6 = -1
            else:
                if num6 == 13:
                    before_s6 = s6
                    s6 = get_state_c6()
                    before_a6 = a6
                    a6 = select_action(s6,6)
                    r = reward_c6()
                    Qtable_c6[before_s6[0]][before_s6[1]][before_s6[2]][before_s6[3]][before_s6[4]][before_a6] = (1-alpha)*Qtable_c6[before_s6[0]][before_s6[1]][before_s6[2]][before_s6[3]][before_s6[4]][before_a6] + alpha*(r + gamma*get_Qvalue(s6,a6,6))
                    state_trans(a6,6)
                    phase_before = traci.trafficlight.getPhase("c6")
                    num6 = -1
            if phase_before7 == phase7:
                if num7 == 10:
                    before_s7 = s7
                    s7 = get_state_c7()
                    before_a7 = a7
                    a7 = select_action(s7,7)
                    r = reward_c7()
                    Qtable_c7[before_s7[0]][before_s7[1]][before_s7[2]][before_s7[3]][before_s7[4]][before_a7] = (1-alpha)*Qtable_c7[before_s7[0]][before_s7[1]][before_s7[2]][before_s7[3]][before_s7[4]][before_a7] + alpha*(r + gamma*get_Qvalue(s7,a7,7))
                    state_trans(a7,7)
                    phase_before7 = traci.trafficlight.getPhase("c7")
                    num7 = -1
            else:
                if num7 == 13:
                    before_s7 = s7
                    s7 = get_state_c7()
                    before_a7 = a7
                    a7 = select_action(s7,7)
                    r = reward_c7()
                    Qtable_c7[before_s7[0]][before_s7[1]][before_s7[2]][before_s7[3]][before_s7[4]][before_a7] = (1-alpha)*Qtable_c7[before_s7[0]][before_s7[1]][before_s7[2]][before_s7[3]][before_s7[4]][before_a7] + alpha*(r + gamma*get_Qvalue(s7,a7,7))
                    state_trans(a7,7)
                    phase_before = traci.trafficlight.getPhase("c7")
                    num7 = -1
            if phase_before8 == phase8:
                if num8 == 10:
                    before_s8 = s8
                    s8 = get_state_c8()
                    before_a8 = a8
                    a8 = select_action(s8,8)
                    r = reward_c8()
                    Qtable_c8[before_s8[0]][before_s8[1]][before_s8[2]][before_s8[3]][before_s8[4]][before_a8] = (1-alpha)*Qtable_c8[before_s8[0]][before_s8[1]][before_s8[2]][before_s8[3]][before_s8[4]][before_a8] + alpha*(r + gamma*get_Qvalue(s8,a8,8))
                    state_trans(a8,8)
                    phase_before8 = traci.trafficlight.getPhase("c8")
                    num8 = -1
            else:
                if num8 == 13:
                    before_s8 = s8
                    s8 = get_state_c8()
                    before_a8 = a8
                    a8 = select_action(s8,8)
                    r = reward_c8()
                    Qtable_c8[before_s8[0]][before_s8[1]][before_s8[2]][before_s8[3]][before_s8[4]][before_a8] = (1-alpha)*Qtable_c8[before_s8[0]][before_s8[1]][before_s8[2]][before_s8[3]][before_s8[4]][before_a8] + alpha*(r + gamma*get_Qvalue(s8,a8,8))
                    state_trans(a8,8)
                    phase_before = traci.trafficlight.getPhase("c8")
                    num8 = -1
            if phase_before9 == phase9:
                if num9 == 10:
                    before_s9 = s9
                    s9 = get_state_c9()
                    before_a9 = a9
                    a9 = select_action(s9,9)
                    r = reward_c9()
                    Qtable_c9[before_s9[0]][before_s9[1]][before_s9[2]][before_s9[3]][before_s9[4]][before_a9] = (1-alpha)*Qtable_c9[before_s9[0]][before_s9[1]][before_s9[2]][before_s9[3]][before_s9[4]][before_a9] + alpha*(r + gamma*get_Qvalue(s9,a9,9))
                    state_trans(a9,9)
                    phase_before9 = traci.trafficlight.getPhase("c9")
                    num9 = -1
            else:
                if num9 == 13:
                    before_s9 = s9
                    s9 = get_state_c9()
                    before_a9 = a9
                    a9 = select_action(s9,9)
                    r = reward_c9()
                    Qtable_c9[before_s9[0]][before_s9[1]][before_s9[2]][before_s9[3]][before_s9[4]][before_a9] = (1-alpha)*Qtable_c9[before_s9[0]][before_s9[1]][before_s9[2]][before_s9[3]][before_s9[4]][before_a9] + alpha*(r + gamma*get_Qvalue(s9,a9,9))
                    state_trans(a9,9)
                    phase_before = traci.trafficlight.getPhase("c9")
                    num9 = -1
            num1 += 1
            num2 += 1
            num3 += 1
            num4 += 1
            num5 += 1
            num6 += 1
            num7 += 1
            num8 += 1
            num9 += 1
            traci.simulationStep()
        c = 0
        b = 1
        for i in car_id:
            if car_id[i][1] == cycle:
                c += car_id[i][0]
                b += 1
        traveltime = c / b
        travel_time.append(traveltime)
        # print(travel_time)
        cycle += 1
    traci.close()
    return travel_time

rulebase = rulebase()
reinforcement = reinforcement()
reinforcement2 = reinforcement2()

p1 = plt.plot(rulebase)
p2 = plt.plot(reinforcement)
p3 = plt.plot(reinforcement2)
plt.legend((p1[0],p2[0],p3[0]), ("rulebase","reinforcement","reinforcement2"), loc=2)
# plt.legend((p2[0],p3[0]), ("reinforcement","reinforcement2"), loc=2)
# plt.legend((p1[0],p3[0]), ("rulebase","reinforcement"), loc=2)
plt.xlabel("step(×5000)")
plt.ylabel("travel time")
plt.show()


# time = sum(car_id.values())
# number_of_car = len(car_id)
# travel_time = time / number_of_car
# print(travel_time)


plt.rcParams["font.family"] = "serif"
# # plt.plot(reward[0])
# fig = plt.figure(figsize=(8,5))
# ax = fig.add_subplot(111)
# ax.plot(rewards)
# plt.xlabel("episode")
# plt.ylabel("reward")
# plt.show()