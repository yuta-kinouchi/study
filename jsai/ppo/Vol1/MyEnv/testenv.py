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
            shape=(12,)
        )
        self.reward_range = [-1., 1.]
        self.started = False
        self.reset()
        self.time = 0
        self.tf = [0,0,0]
        self.travel_time = []
        self.cycle = 0
        self.episode = 0
       #self.lane_dict = {"gneE1_0": [0, 0, 0, 0, 1], "gne"}

    def reset(self):
        if self.started:
            traci.close()
        # traci.start(["sumo-gui", "-c", os.path.expanduser("../cfg/single/single.sumocfg"), "--step-length", "1", "--lanechange.duration","1.0"])
        traci.start(["sumo", "-c", os.path.expanduser("../../cfg/single/single.sumocfg"), "--step-length", "1", "--lanechange.duration","1.0"])
        # while "0" not in traci.vehicle.getIDList():
        #     traci.simulationStep()
        self.started = True
        self.s = 0
        self.done = False
        self.car_id = {}
        self.car_id = defaultdict(list)
        self.idlist = {}
        self.idlist = defaultdict(list)
        x = 10000
        s = 0
        for i in range(1000):
            traci.simulationStep()
            if i % 10 == 0:
                self.get_feature()
            x = str(x)
            if np.random.uniform(0,1) < 0.5 * 0.1:
                
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID= x + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.4:
                s += 1
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
            x = int(x)
            x += 1
        return self.get_state()

    # def step(self, action):
    #     if action == 0:
    #         traci.vehicle.setAccel("0", 0.5)
    #         traci.vehicle.setDecel("0", 0)
    #     elif action == 1:
    #         traci.vehicle.setDecel("0", 5)
    #     else:
    #         now_lane = traci.vehicle.getLaneIndex("0")
    #         if now_lane == 0:
    #             traci.vehicle.changeLane("0", 1, 1)
    #         else:
    #             traci.vehicle.changeLane("0", 0, 1)
    #         traci.vehicle.setAccel("0", 0)
    #         traci.vehicle.setDecel("0", 0)
    #     s = self._get_state()
    #     if "1" in traci.vehicle.getIDList() and s[6] < 4:
    #         traci.vehicle.setSpeed("1", 4)
    #     traci.simulationStep()
    #     next_s = self._get_state()
    #     reward, self.done = self._get_reward(next_s, action)
    #     return next_s, np.array(reward), self.done, {}

    def state_trans(self,a):
        phase = traci.trafficlight.getPhase("c")
        # print(a)
        if a == 0:
            if phase == 0 or phase == 2:
                traci.trafficlight.setPhase("c",0)
            else:
                traci.trafficlight.setPhase("c",9)
                for i in range(3):
                    self.count_traveltime(id,self.cycle)
                    self.time += 1
                    traci.simulationStep()
                traci.trafficlight.setPhase("c",0)
        elif a == 1:
            if phase == 0:
                traci.trafficlight.setPhase("c",1)
                for i in range(3):
                    self.count_traveltime(id,self.cycle)
                    self.time += 1
                    traci.simulationStep()
            elif phase == 2:
                traci.trafficlight.setPhase("c",2)
            else:
                traci.trafficlight.setPhase("c",9)
                for i in range(3):
                    self.count_traveltime(id,self.cycle)
                    self.time += 1
                    traci.simulationStep()
                traci.trafficlight.setPhase("c",2)
        elif a == 2:
            if phase == 4 or phase == 6:
                traci.trafficlight.setPhase("c",4)
            else:
                traci.trafficlight.setPhase("c",8)
                for i in range(3):
                    self.count_traveltime(id,self.cycle)
                    self.time += 1
                    traci.simulationStep()
                traci.trafficlight.setPhase("c",4)
        else:
            if phase == 4:
                traci.trafficlight.setPhase("c",5)
                for i in range(3):
                    self.count_traveltime(id,self.cycle)
                    self.time += 1
                    traci.simulationStep()
            elif phase == 6:
                traci.trafficlight.setPhase("c",6)
            else:
                traci.trafficlight.setPhase("c",8)
                for i in range(3):
                    self.count_traveltime(id,self.cycle)
                    self.time += 1
                    traci.simulationStep()
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

    def step(self,action):
        if self.time % 400 == 0:
            self.tf = self.choice_trafficflow()
        self.state_trans(action)
        for i in range(10):
            traci.simulationStep()
            self.add_car(self.tf,self.time)
            id = traci.vehicle.getIDList()
            self.count_traveltime(id,self.cycle)
            self.time += 1
        next_s = self.get_state()
        reward = self._get_reward(next_s, action)
        t = traci.simulation.getTime()

            a = 0
            b = 1
            for i in self.car_id:
                a += self.car_id[i][0]
                b += 1
            traveltime = a / b
            self.travel_time.append(traveltime)
            self.cycle += 1
            self.done = True
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
            self.episode += 1
        return next_s, np.array(reward), self.done, {}

    def add_car(self,tf,step):
        x = str(step)
        if tf[0] == 0:
            p = 0.25
        elif tf[0] == 1:
            p = 0.50
        elif tf[0] == 2:
            p = 0.75
        else:
            p = 1

        if tf[1] == 0:
            q = 0.2
        elif tf[1] == 1:
            q = 0.4
        elif tf[1] == 2:
            q = 0.6
        else:
            q = 0.8

        if np.random.uniform(0,1) < p*q*0.5:
            if np.random.uniform(0,1) > 0.1 * int(tf[2]):
                traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
            else:
                traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < p*q*0.5:
            if np.random.uniform(0,1) > 0.1 * int(tf[2]):
                traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
            else:
                traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            if np.random.uniform(0,1) > 0.1 * int(tf[2]):
                traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
            else:
                traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            if np.random.uniform(0,1)  > 0.1 * int(tf[2]):
                traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
            else:
                traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  


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
        state = [r_c,l_c,t_c,b_c,r_c_l,l_c_l,t_c_l,b_c_l,phase[0],phase[1],phase[2],phase[3]]
        return np.array(state, dtype="float32")

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