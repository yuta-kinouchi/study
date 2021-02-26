import os, sys
import math
if 'SUMO_HOME' in os.environ:
   tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
   sys.path.append(tools)
else:
   tools = os.path.join('/usr/share/sumo/tools')
   sys.path.append(tools)
   #sys.exit("please declare environment variable 'SUMO_HOME'")
import traci
import gym
import numpy as np
import gym.spaces
import random
from collections import defaultdict
import matplotlib.pyplot as plt
import statistics

class SumoEnv2(gym.Env):
    def __init__(self):
        super().__init__()
        # action_space, observation_space, reward_range を設定する
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Box(
            low=0,
            high=100,
            shape=(28,)
        )
        self.reward_range = [-1., 1.]
        self.started = False
        self.reset()
        self.time = 0
        self.tf = [0,0,0]
        self.idlist = {}
        self.idlist = defaultdict(list)
        self.travel_time = []
        self.cycle = 0
        self.episode = 0
       #self.lane_dict = {"gneE1_0": [0, 0, 0, 0, 1], "gne"}

    def reset(self):
        if self.started:
            traci.close()
        # traci.start(["sumo-gui", "-c", os.path.expanduser("../../cfg/single/single.sumocfg"), "--step-length", "1", "--lanechange.duration","1.0"])
        traci.start(["sumo", "-c", os.path.expanduser("../../cfg/single/single.sumocfg"), "--step-length", "1", "--lanechange.duration","1.0"])
        # while "0" not in traci.vehicle.getIDList():
        #     traci.simulationStep()
        self.started = True
        self.s = 0
        self.done = False
        self.feature = [[],[],[],[],[],[],[],[]]
        self.car_id = {}
        self.car_id = defaultdict(list)
        return self.get_state()


    def state_trans(self,a):
        phase = traci.trafficlight.getPhase("c")
        id = traci.vehicle.getIDList()
        # print(a)
        if a == 0:
            if phase == 0 or phase == 2:
                traci.trafficlight.setPhase("c",0)
            else:
                traci.trafficlight.setPhase("c",9)
                for i in range(3):
                    traci.simulationStep()
                    self.count_traveltime(id,self.cycle)
                traci.trafficlight.setPhase("c",0)
        elif a == 1:
            if phase == 0:
                traci.trafficlight.setPhase("c",1)
                for i in range(3):
                    traci.simulationStep()
                    self.count_traveltime(id,self.cycle)
            elif phase == 2:
                traci.trafficlight.setPhase("c",2)
            else:
                traci.trafficlight.setPhase("c",9)
                for i in range(3):
                    traci.simulationStep()
                    self.count_traveltime(id,self.cycle)
                traci.trafficlight.setPhase("c",2)
        elif a == 2:
            if phase == 4 or phase == 6:
                traci.trafficlight.setPhase("c",4)
            else:
                traci.trafficlight.setPhase("c",8)
                for i in range(3):
                    traci.simulationStep()
                    self.count_traveltime(id,self.cycle)
                traci.trafficlight.setPhase("c",4)
        else:
            if phase == 4:
                traci.trafficlight.setPhase("c",5)
                for i in range(3):
                    traci.simulationStep()
                    self.count_traveltime(id,self.cycle)
            elif phase == 6:
                traci.trafficlight.setPhase("c",6)
            else:
                traci.trafficlight.setPhase("c",8)
                for i in range(3):
                    traci.simulationStep()
                    self.count_traveltime(id,self.cycle)
                traci.trafficlight.setPhase("c",6)

    def choice_trafficflow(self):
        a = random.randint(0,3)
        b = random.randint(0,3)
        c = random.randint(1,3)
        tf = [a,b,c]
        return tf

    def count_traveltime(self,id,cycle):
        for i in id:
            if i not in self.car_id :
                self.car_id[i] =[1]
            else:
                self.car_id[i][0] += 1
        # print(self.car_id)

    def get_feature(self):
        id_t = traci.edge.getLastStepVehicleIDs("tt_t")
        id_b = traci.edge.getLastStepVehicleIDs("bb_b")
        id_r = traci.edge.getLastStepVehicleIDs("rr_r")
        id_l = traci.edge.getLastStepVehicleIDs("ll_l")
        id_t_r = traci.lane.getLastStepVehicleIDs("t_c_2")
        id_b_r = traci.lane.getLastStepVehicleIDs("b_c_2")
        id_r_r = traci.lane.getLastStepVehicleIDs("r_c_2")
        id_l_r = traci.lane.getLastStepVehicleIDs("l_c_2")
        t = 0
        b = 0
        r = 0
        l = 0
        t_r = 0
        b_r = 0
        r_r = 0
        l_r = 0
        for i in id_t:
            if i not in self.idlist:
                self.idlist[i] = [0,0]
                t += 1
            else:
                self.idlist[i][0] = 1
        for i in id_b:
            if i not in self.idlist:
                self.idlist[i] = [0,0]
                b += 1
            else:
                self.idlist[i][0] = 1
        for i in id_r:
            if i not in self.idlist:
                self.idlist[i] = [0,0]
                r += 1
            else:
                self.idlist[i][0] = 1
        for i in id_l:
            if i not in self.idlist:
                self.idlist[i] = [0,0]
                l += 1
            else:
                self.idlist[i][0] = 1

        for i in id_t_r:
            if self.idlist[i][1] == 0:
                self.idlist[i][1] = 1
                t_r += 1
        for i in id_b_r:
            if self.idlist[i][1] == 0:
                self.idlist[i][1] = 1
                b_r += 1
        for i in id_r_r:
            if self.idlist[i][1] == 0:
                self.idlist[i][1] = 1
                r_r += 1
        for i in id_l_r:
            if self.idlist[i][1] == 0:
                self.idlist[i][1] = 1
                l_r += 1

        self.feature[0].append(t)
        self.feature[1].append(b)
        self.feature[2].append(r)
        self.feature[3].append(l)
        self.feature[4].append(t_r)
        self.feature[5].append(b_r)
        self.feature[6].append(r_r)
        self.feature[7].append(l_r)

    def step(self,action):
        if self.time % 300 == 0:
            self.tf = self.choice_trafficflow()
        self.state_trans(action)
        for i in range(10):
            traci.simulationStep()
            self.add_car(self.time)
            id = traci.vehicle.getIDList()
            self.count_traveltime(id,self.cycle)
            self.time += 1
        next_s = self.get_state()
        self.get_feature()
        reward = self._get_reward(next_s, action)
        t = traci.simulation.getTime()
        if t >= 3600:
            a = 1
            b = 1
            for i in self.car_id:
                a += self.car_id[i][0]
                b += 1
            traveltime = a / b
            self.travel_time.append(traveltime)
            self.cycle += 1
            self.done = True
            self.episode += 1
            if self.episode == 10:
                mean = statistics.mean(self.travel_time)
                variance = statistics.variance(self.travel_time)
                print('平均: {0:.2f}'.format(mean))
                print('分散: {0:.2f}'.format(variance))
                self.travel_time.pop(0)
                self.travel_time.pop(0)
                fig = plt.figure()
                ax = fig.add_subplot(111)
                ax.set_xlabel("epiosde", size = 14, weight = "light")
                ax.set_xlabel("travel time", size = 14, weight = "light")
                ax = fig.add_subplot(1, 1, 1)
                ax.plot(self.travel_time)
                plt.show()
        return next_s, np.array(reward), self.done, {}

    def add_car(self,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)
        # if tf[0] == 0:
        #     p = 0.125
        # elif tf[0] == 1:
        #     p = 0.25
        # elif tf[0] == 2:
        #     p = 0.375
        # else:
        #     p = 0.5

        # if tf[1] == 0:
        #     q = 0.2
        # elif tf[1] == 1:
        #     q = 0.4
        # elif tf[1] == 2:
        #     q = 0.6
        # else:
        #     q = 0.8
        if y <= 600:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.5 * 0.1:
                traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4:
                traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.4:
                traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
        elif y <= 1200:
            self.tf[0] = 1
            if np.random.uniform(0,1) < 0.5 * 0.2:
                traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
        elif y <= 1800:
            self.tf[0] = 2
            if np.random.uniform(0,1) < 0.5 * 0.3:
                traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.2:
                traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
        elif y <= 2400:
            self.tf[0] = 3
            if np.random.uniform(0,1) < 0.5 * 0.4:
                traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4 :
                traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.1:
                traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')     
        elif y <= 3000:
            self.tf[0] = 2
            if np.random.uniform(0,1) < 0.5 * 0.3 :
                traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3 :
                traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2 :
                traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.2 :
                traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE') 
        else:
            self.tf[0] = 1
            if np.random.uniform(0,1) < 0.5 * 0.2:
                traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
    def get_state(self):
        r_c = traci.edge.getLastStepVehicleNumber("r_c")
        r_c_l = traci.lane.getLastStepVehicleNumber("r_c_2")
        l_c = traci.edge.getLastStepVehicleNumber("l_c")
        l_c_l = traci.lane.getLastStepVehicleNumber("l_c_2")
        t_c = traci.edge.getLastStepVehicleNumber("t_c")
        t_c_l = traci.lane.getLastStepVehicleNumber("t_c_2")
        b_c = traci.edge.getLastStepVehicleNumber("b_c")
        b_c_l = traci.lane.getLastStepVehicleNumber("b_c_2")
        # r_c = cars_r_c - r_c_l
        # l_c = cars_l_c - l_c_l
        # t_c = cars_t_c - t_c_l
        # b_c = cars_b_c - b_c_l
        phase = traci.trafficlight.getPhase("c")
        if phase < 2:
            phase = [1,0,0,0]
        elif phase < 4:
            phase = [0,1,0,0]
        elif phase < 6:
            phase = [0,0,1,0]
        else:
            phase = [0,0,0,1]


        if len(self.feature[0]) >= 33:
            roc_t = 50 + self.feature[0][-33] + self.feature[0][-32] + self.feature[0][-31] - (self.feature[0][-3] + self.feature[0][-2] + self.feature[0][-1]) 
            roc_b = 50 + self.feature[1][-33] + self.feature[1][-32] + self.feature[1][-31] - (self.feature[1][-3] + self.feature[1][-2] + self.feature[1][-1]) 
            roc_r = 50 + self.feature[2][-33] + self.feature[2][-32] + self.feature[2][-31] - (self.feature[2][-3] + self.feature[2][-2] + self.feature[2][-1]) 
            roc_l = 50 + self.feature[3][-33] + self.feature[3][-32] + self.feature[3][-31] - (self.feature[3][-3] + self.feature[3][-2] + self.feature[3][-1]) 
            roc_t_l = 50 + self.feature[4][-33] + self.feature[4][-32] + self.feature[4][-31] - (self.feature[4][-3] + self.feature[4][-2] + self.feature[4][-1]) 
            roc_b_l = 50 + self.feature[5][-33] + self.feature[5][-32] + self.feature[5][-31] - (self.feature[5][-3] + self.feature[5][-2] + self.feature[5][-1]) 
            roc_r_l = 50 + self.feature[6][-33] + self.feature[6][-32] + self.feature[6][-31] - (self.feature[6][-3] + self.feature[6][-2] + self.feature[6][-1]) 
            roc_l_l = 50 + self.feature[7][-33] + self.feature[7][-32] + self.feature[7][-31] - (self.feature[7][-3] + self.feature[7][-2] + self.feature[7][-1])
            f = [[],[],[],[]]
            f__l = [[],[],[],[]]
            f_t = 0
            f_b = 0
            f_r = 0
            f_l = 0
            f_t_l = 0
            f_b_l = 0
            f_r_l = 0
            f_l_l = 0
            for i in range(30):
                f_t += self.feature[0][-i] 
                f_b += self.feature[1][-i] 
                f_r += self.feature[2][-i] 
                f_l += self.feature[3][-i] 
                f_t_l += self.feature[4][-i] 
                f_b_l += self.feature[5][-i] 
                f_r_l += self.feature[6][-i] 
                f_l_l += self.feature[7][-i] 
            f[0] = f_t
            f[1] = f_b
            f[2] = f_r
            f[3] = f_l_l
            f__l[0] = f_t_l
            f__l[1] = f_b_l
            f__l[2] = f_r_l
            f__l[3] = f_l_l
            state = [r_c,l_c,t_c,b_c,r_c_l,l_c_l,t_c_l,b_c_l,phase[0],phase[1],phase[2],phase[3],f[0],f[1],f[2],f[3],f__l[0],f__l[1],f__l[2],f__l[3],roc_t,roc_b,roc_r,roc_l,roc_t_l,roc_b_l,roc_r_l,roc_l_l]
            # print(state)
            return np.array(state, dtype="float32")
        elif len(self.feature[0]) >= 30:
            f = [[],[],[],[]]
            f__l = [[],[],[],[]]
            f_t = 0
            f_b = 0
            f_r = 0
            f_l = 0
            f_t_l = 0
            f_b_l = 0
            f_r_l = 0
            f_l_l = 0
            for i in range(30):
                f_t += self.feature[0][-i] 
                f_b += self.feature[1][-i] 
                f_r += self.feature[2][-i] 
                f_l += self.feature[3][-i] 
                f_t_l += self.feature[4][-i] 
                f_b_l += self.feature[5][-i] 
                f_r_l += self.feature[6][-i] 
                f_l_l += self.feature[7][-i] 
            f[0] = f_t
            f[1] = f_b
            f[2] = f_r
            f[3] = f_l_l
            f__l[0] = f_t_l
            f__l[1] = f_b_l
            f__l[2] = f_r_l
            f__l[3] = f_l_l
            state = [r_c,l_c,t_c,b_c,r_c_l,l_c_l,t_c_l,b_c_l,phase[0],phase[1],phase[2],phase[3],f[0],f[1],f[2],f[3],f__l[0],f__l[1],f__l[2],f__l[3],0,0,0,0,0,0,0,0]
            return np.array(state, dtype="float32")
        else:
            # 30以下の場合
            state = [r_c,l_c,t_c,b_c,r_c_l,l_c_l,t_c_l,b_c_l,phase[0],phase[1],phase[2],phase[3],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            return np.array(state, dtype="float32")
 
        # for i in range(4):
        #     if f[i] <= 10:
        #         f[i] = 0
        #     elif f[i] <= 20:
        #         f[i] = 1
        #     elif f[i] <= 30:
        #         f[i] = 2
        #     elif f[i] <= 40:
        #         f[i] = 3
        #     elif f[i] <= 50:
        #         f[i] = 4
        #     elif f[i] <= 60:
        #         f[i] = 5
        #     elif f[i] <= 70:
        #         f[i] = 6
        #     elif f[i] <= 80:
        #         f[i] = 7
        #     elif f[i] <= 90:
        #         f[i] = 8
        #     elif f[i] <= 100:
        #         f[i] = 9
        #     else:
        #         f[i] = 10

        # for i in range(4):
        #     if f__l[i] <= 3:
        #         f__l[i] = 0
        #     elif f__l[i] <= 6:
        #         f__l[i] = 1
        #     elif f__l[i] <= 9:
        #         f__l[i] = 2
        #     elif f__l[i] <= 12:
        #         f__l[i] = 3
        #     elif f__l[i] <= 15:
        #         f__l[i] = 4
        #     elif f__l[i]<= 18:
        #         f__l[i] = 5
        #     elif f__l[i] <= 21:
        #         f__l[i] = 6
        #     elif f__l[i] <= 24:
        #         f__l[i] = 7
        #     elif f__l[i] <= 27:
        #         f__l[i] = 8
        #     elif f__l[i] <= 30:
        #         f__l[i] = 9
        #     else:
        #         f__l[i] = 10


    def _get_reward(self,next_s, action):
        t_c = traci.edge.getLastStepHaltingNumber("t_c")
        tt_t = traci.edge.getLastStepHaltingNumber("tt_t")
        r_c = traci.edge.getLastStepHaltingNumber("r_c")
        rr_r = traci.edge.getLastStepHaltingNumber("rr_r")
        l_c = traci.edge.getLastStepHaltingNumber("l_c")
        ll_l = traci.edge.getLastStepHaltingNumber("ll_l")
        b_c = traci.edge.getLastStepHaltingNumber("b_c")
        bb_b = traci.edge.getLastStepHaltingNumber("bb_b")
        reward =  -(t_c + r_c + l_c + b_c + tt_t + rr_r + ll_l + bb_b)/300
        # reward =  -(t_c + r_c + l_c + b_c)/300
        # print(reward)
        return reward
    #    return reward, self.done

    def close(self):
       traci.close()

# if __name__ == '__main__':
#     Env = MyEnv()
#     done = False
#     LCcount = 0
#     traci.vehicle.setLaneChangeMode(0b001000000000) ###
#     #Env.reset()
#     while not done:
#         s, r, done, i = Env.step(action)
#     #    print(r, done)
#     traci.close()

if __name__ == "__main__":
    Env = SumoEnv()
    done = False
    while not done:
        num = random.randint(0,3)
        s, r, done, i = Env.step(0)
    traci.close