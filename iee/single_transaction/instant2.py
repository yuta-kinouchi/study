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
        self.Qtable = np.zeros((150,150,2))
        self.epsilon = 0.1

    def get_Qvalue(self,s,a):
        return self.Qtable[s][a]

    def select_greedy(self, s):
        qs = self.Qtable[s]
        actions = np.where(qs == qs.max())[0]
        print(actions)
        return np.random.choice(actions)

    def select_egreedy(self, s):
        if self.epsilon < np.random.rand():
            return self.select_greedy(s)
        else:
            return np.random.choice(3)

    def QLearning(self, Env):
        gamma = 0.9
        alpha = 0.1
        rs = []
        for i in range(300):
            s = Env.get_state()
            a = self.select_egreedy(s)
            Env.state_trans(s, a)
            r = Env.reward()
            # print(r)
            # print("----------------------------")
            next_s = Env.get_state()
            # print(next_s)
            rs.append(r)
            self.Qtable[s][a] = (1-alpha)*self.Qtable[s][a] + alpha*(r + self.get_Qvalue(next_s,self.select_greedy(next_s)))
        return rs


class Env():
    def __init__(self,xmlfl):
        self.xmlfl = xmlfl
        self.signal_state = self.get_signal_state()

    def get_state(self):
        t = traci.edge.getLastStepVehicleNumber("t_c")
        b = traci.edge.getLastStepVehicleNumber("b_c")
        r = traci.edge.getLastStepVehicleNumber("r_c")
        l = traci.edge.getLastStepVehicleNumber("l_c")
        tate = t + b
        yoko = r + l

        return tate,yoko


    def get_signal_state(self):
        times = []
        tree = ET.parse(self.xmlfl)
        tlLogic = tree.find('tlLogic')
        for p in tlLogic:
            if "GG" in p.attrib["state"]:
                times.append(int(p.attrib["duration"]))
        """
        timesは交差点で交差する両交通流の青現示時間を表している
        """
        print(times)
        return tuple(times)

    def state_trans(self, s, a):
        """
        状態遷移関数: 次状態に遷移し，xmlファイルにそれを書きこむ
        """
        # 辞書式のデータ型
        actdct = {0: (0, 0), 1: (2, -2), 2: (-2, 2)}
        # もともとの青現示時間に変更を加えている
        times = tuple(np.array(self.get_signal_state()) + np.array(actdct[a]))
        # timesの中の値が0にならないようにしている
        if np.count_nonzero(times) == len(self.get_signal_state()):
            # 内包表記　タプルの中には一番左で示された値が入る、今回ならx
            self.signal_state = tuple([x for x in times])
        # parse xmlファイルをプログラム内で使えるように解析
        tree = ET.parse(self.xmlfl)
        tlLogic = tree.find('tlLogic')
        i = 0
        for p in tlLogic:
            print(p.attrib["state"])
            if "0" == p.attrib["index"] or "4" == p.attrib["index"] :
                p.set("duration", str(self.signal_state[i]))
                i += 1
        tree.write("single.net.xml", encoding='utf-8')
        return self.signal_state


    def reward(self):
        """
        平均旅行時間を報酬としたい
        とりあえず、なんでもいいので報酬を決めた
        """
        stops = 0
        for step in range(200):
            ves = traci.vehicle.getIDList()
            for v in ves:
                if traci.vehicle.getSpeed(v) == 0:
                    stops += 1
            # traci.simulationStep()
        # traci.close()

        return -stops

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    tsagent = Agent()
    tsenv = Env("single.net.xml")
    #戻り値の値はタプルの形になっている
    reward = tsagent.QLearning(tsenv)
    plt.rcParams["font.family"] = "serif"
    # plt.plot(reward[0])
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(111)
    ax.plot(reward[0])
    plt.xlabel("episode")
    plt.ylabel("reward")
    plt.show()

