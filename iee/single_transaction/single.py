import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import traci

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    traci.start(["sumo-gui", "-c", "single.sumocfg"])

class Agent():

    def __init__(self):
        # Qテーブルの状態数は0~車両待ち台数の最大数
        self.Qtable = np.zeros((150,150,2))
        self.epsilon = 0.1

    def get_Qvalue(self,s,a):
        return self.Qtable[s][a]

    def select_action(self,s):
        if self.epsilon < np.random.rand():
            qvalue = self.Qtable[s]
            # 複数の最大q値が出ることを考慮している
            actions = np.where(qvalue == qvalue.max())[0]
            return np.random.choice(actions)
        else:
            return np.random.choice(2)

    def Qlearning(self,Env):
        gamma = 0.9
        alpha = 0.1
        # episodes = 300
        # steps = 200
        mean_reward = []
        mean_wating_time = []
        for episode in range(30):
            reward = []
            wating_time = []
            for steps in range(200):
                s = Env.get_state()
                a = self.select_action(s)
                Env.state_trans(s,a)
                r = Env.reward()
                reward.append(r)
                next_s = Env.get_state()
                self.Qtable[s][a] = (1-alpha)*self.Qtable[s][a] + alpha*(r+self.get_Qvalue(next_s,self.select_action(next_s)))
                w = Env.get_wating_time()
                wating_time.append(w)
                traci.simulationStep()
            ave = sum(reward)/len(reward)
            ave_time = sum(wating_time)/len(wating_time)
            mean_reward.append(ave)
            mean_wating_time.append(ave_time)
        return mean_reward,mean_wating_time


        
class Env():

    def __init__(self,xmlfl):
        self.xmlfl = xmlfl
        self.state = self.get_state()
    
    def get_state(self):
        # 上から下への圧力
        t_c = traci.edge.getLastStepVehicleNumber(t_c)
        c_b = traci.edge.getLastStepVehicleNumber(c_b)
        if t_c >= c_b:
            t_b = t_c - c_b
        else:
            t_b = c_b - t_c
        # 下から上への圧力
        b_c = traci.edge.getLastStepVehicleNumber(b_c)
        c_t = traci.edge.getLastStepVehicleNumber(c_t)
        if b_c >= c_t:
            b_t = b_c - c_t
        else:
            b_t = c_t - b_c
        # 右から左への圧力
        r_c = traci.edge.getLastStepVehicleNumber(r_c)
        c_l = traci.edge.getLastStepVehicleNumber(c_l)
        if r_c >= c_l:
            r_l = r_c - c_l
        else:
            r_l = c_l - r_c
        # 左から右への圧力
        l_c = traci.edge.getLastStepVehicleNumber(l_c)
        c_r = traci.edge.getLastStepVehicleNumber(c_r)
        if l_c >= c_r:
            l_r = l_c - c_r
        else:
            l_r = c_r - l_c
        
        tate = t_b + b_t
        yoko = r_l + l_r

        return tate,yoko

    def state_trans(self,s,a):
        actdct = {0:(0,0),1:(2,-2),2:(-2,2)}
        times = tuple(np.array(self.get_state))
        # 変更なし
        if a == 0:

            
        # スプリットを長く
        elif a == 1:

        # スプリットを短く
        else:

        # if a == 0:
        #     traci.trafficlight.setPhase("c",2)
        # elif a == 1:
        #     traci.trafficlight.setPhase("c",5)
        # pass
    
    def get_split(self):
        times = []
        tree = ET.parse(self.xmlfl)
        tlLogic = tree.find("tlLogic")
        for p in tlLogic:
            if index == "0" or index == "4"

    def reward(self):
        # traci.start(["sumo", "-c", "ts.sumocfg"])
        t = traci.edge.getLastStepHaltingNumber("t_c")
        l = traci.edge.getLastStepHaltingNumber("l_c")
        r = traci.edge.getLastStepHaltingNumber("r_c")
        b = traci.edge.getLastStepHaltingNumber("b_c")
        reward = -(t + l + r + b)
        return reward

    def get_wating_time(self):
        t = traci.edge.getWaitingTime("t_c")
        l = traci.edge.getWaitingTime("l_c")
        r = traci.edge.getWaitingTime("r_c")
        b = traci.edge.getWaitingTime("b_c")
        num_t = traci.edge.getLastStepVehicleNumber("t_c")
        num_l = traci.edge.getLastStepVehicleNumber("l_c")
        num_r = traci.edge.getLastStepVehicleNumber("r_c")
        num_b = traci.edge.getLastStepVehicleNumber("b_c")
        if num_t != 0:
            t = t / num_t
        if num_l != 0:
            l = l / num_l
        if num_r != 0:
            r = r / num_r
        if num_b != 0:
            b = b / num_b
        wating_time = t + l + r + b
        return wating_time


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    tsagent = Agent()
    tsenv = Env("scramble.net.xml")
    #戻り値の値はタプルの形になっている
    reward = tsagent.Qlearning(tsenv)
    plt.rcParams["font.family"] = "serif"
    # plt.plot(reward[0])
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(111)
    ax.plot(reward[0])
    plt.xlabel("episode")
    plt.ylabel("reward")
    plt.show()


