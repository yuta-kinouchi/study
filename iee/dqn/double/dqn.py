#交差点一つのdqnの実装を行う
import numpy as np
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import plot_model
from collections import deque
from keras import backend as K
import tensorflow as tf

import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

import os, sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

import traci

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

    rewards = []
    travel_time = []
    # traci.start(["sumo-gui", "-c", "dqn.sumocfg"])
    traci.start(["sumo", "-c", "dqn.sumocfg"])
    # traci.simulationStep(1000)
    cycle = 0
    j = 0
    for iter in range(20):
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
            # print(travel_time)
            cycle += 1
    traci.close()
    return travel_time

#損失関数を定義している

def dqn():
    def huberloss(y_true, y_pred):
        err = y_true - y_pred
        cond = K.abs(err) < 1.0
        L2 = 0.5 * K.square(err)
        L1 = (K.abs(err) - 0.5)
        loss = tf.where(cond, L2, L1)  # Keras does not cover where function in tensorflow :-(
        return K.mean(loss)

    def get_state(c):
        if c == "c1":
            cars_r_c = traci.edge.getLastStepHaltingNumber("c2_c1")
            cars_l_c = traci.edge.getLastStepHaltingNumber("l1_c1")
            cars_t_c = traci.edge.getLastStepHaltingNumber("t1_c1")
            cars_b_c = traci.edge.getLastStepHaltingNumber("b1_c1")
            tate = (cars_t_c + cars_b_c)
            yoko = (cars_r_c + cars_l_c)
            phase = traci.trafficlight.getPhase("c1")
            if phase < 4:
                phase = 0
            else:
                phase = 1
            state = [tate,yoko,phase]
            return state
        else:
            cars_r_c = traci.edge.getLastStepHaltingNumber("r1_c2")
            cars_l_c = traci.edge.getLastStepHaltingNumber("c1_c2")
            cars_t_c = traci.edge.getLastStepHaltingNumber("t2_c2")
            cars_b_c = traci.edge.getLastStepHaltingNumber("b2_c2")
            tate = (cars_t_c + cars_b_c)
            yoko = (cars_r_c + cars_l_c)
            phase = traci.trafficlight.getPhase("c2")
            if phase < 4:
                phase = 0
            else:
                phase = 1
            state = [tate,yoko,phase]
            return state


    def count_traveltime(id,cycle):
        for i in id:
            # そのIDがリストの中にあるかないかチェック
            if i not in car_id or car_id[i][1] != cycle:
                car_id[i] =[0, cycle]
                
            else:
                car_id[i][0] += 1
            # print(car_id[i])
            
    def reward(c):
        if c == "c1":
            t_c = traci.edge.getLastStepHaltingNumber("t1_c1")
            r_c = traci.edge.getLastStepHaltingNumber("c2_c1")
            l_c = traci.edge.getLastStepHaltingNumber("l1_c1")
            b_c = traci.edge.getLastStepHaltingNumber("b1_c1")
            r =  -(t_c + r_c + l_c + b_c)/300
            return r
        else:
            t_c = traci.edge.getLastStepHaltingNumber("t2_c2")
            r_c = traci.edge.getLastStepHaltingNumber("r1_c2")
            l_c = traci.edge.getLastStepHaltingNumber("c1_c2")
            b_c = traci.edge.getLastStepHaltingNumber("b2_c2")
            r =  -(t_c + r_c + l_c + b_c)/300
            return r

    def get_action(state, episode, mainQN):   # [C]ｔ＋１での行動を返す
        # 徐々に最適行動のみをとる、ε-greedy法
        # epsilon = 0.001 + 0.9 / (1.0+episode)
        epsilon = 0.1
        if epsilon <= np.random.uniform(0, 1):
            retTargetQs = mainQN.model.predict(state)[0]
            action = np.argmax(retTargetQs)  # 最大の報酬を返す行動を選択する
            # print("A")
            # print(action)
        else:
            action = np.random.choice([0, 1])  # ランダムに行動する
            # print("B")
            # print(action)
        return action

    def state_trans(a,c):
        if c == "c1":
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
        else:
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

    #Q関数の定義
    class QNetwork:
        def __init__(self, learning_rate=0.01, state_size=3, action_size=2, hidden_size=10):
            self.model = Sequential()
            self.model.add(Dense(hidden_size, activation='relu', input_dim=state_size))
            self.model.add(Dense(hidden_size, activation='relu'))
            self.model.add(Dense(action_size, activation='linear'))
            self.optimizer = Adam(lr=learning_rate)  # 誤差を減らす学習方法はAdam
            # self.model.compile(loss='mse', optimizer=self.optimizer)
            self.model.compile(loss=huberloss, optimizer=self.optimizer)
            
        def replay(self, memory, batch_size, gamma, targetQN):
            inputs = np.zeros((batch_size, 3))
            targets = np.zeros((batch_size, 2))
            mini_batch = memory.sample(batch_size)
            for i, (state_b, action_b, reward_b, next_state_b) in enumerate(mini_batch):
                inputs[i:i + 1] = state_b
                target = reward_b

                if not (next_state_b == np.zeros(state_b.shape)).all(axis=1):
                    # 価値計算（DDQNにも対応できるように、行動決定のQネットワークと価値観数のQネットワークは分離）
                    retmainQs = self.model.predict(next_state_b)[0]
                    next_action = np.argmax(retmainQs)  # 最大の報酬を返す行動を選択する
                    target = reward_b + gamma * targetQN.model.predict(next_state_b)[0][next_action]

                targets[i] = self.model.predict(state_b)    # Qネットワークの出力
                targets[i][action_b] = target               # 教師信号

            # shiglayさんよりアドバイスいただき、for文の外へ修正しました
            self.model.fit(inputs, targets, epochs=1, verbose=0)  # epochsは訓練データの反復回数、verbose=0は表示なしの設定

    # [3]Experience ReplayとFixed Target Q-Networkを実現するメモリクラス
    class Memory:
        def __init__(self, max_size=1000):
            self.buffer = deque(maxlen=max_size)

        def add(self, experience):
            self.buffer.append(experience)

        def sample(self, batch_size):
            idx = np.random.choice(np.arange(len(self.buffer)), size=batch_size, replace=False)
            return [self.buffer[ii] for ii in idx]

        def len(self):
            return len(self.buffer)



    gamma = 0.99 
    hidden_size = 16               # Q-networkの隠れ層のニューロンの数
    learning_rate = 0.00001         # Q-networkの学習係数
    memory_size = 10000            # バッファーメモリの大きさ
    batch_size = 64                # Q-networkを更新するバッチの大記載


    mainQN1 = QNetwork(hidden_size=hidden_size, learning_rate=learning_rate)     # メインのQネットワーク
    targetQN1 = QNetwork(hidden_size=hidden_size, learning_rate=learning_rate)   # 価値を計算するQネットワーク

    mainQN2 = QNetwork(hidden_size=hidden_size, learning_rate=learning_rate)     # メインのQネットワーク
    targetQN2 = QNetwork(hidden_size=hidden_size, learning_rate=learning_rate)   # 価値を計算するQネットワーク
    # plot_model(mainQN.model, to_file='Qnetwork.png', show_shapes=True)        # Qネットワークの可視化
    memory = Memory(max_size=memory_size)
    # actor = Actor()


    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    num1 = 0
    num2 = 0
    cycle = 0
    travel_time = []
    phase_before1 = 0
    phase_before2 = 0

    action1 = 0
    action2 = 0
    car_id = {}
    car_id = defaultdict(list)
    targetQN1.model.set_weights(mainQN1.model.get_weights())
    targetQN2.model.set_weights(mainQN2.model.get_weights())
    for episode in range(20):

        # traci.start(["sumo-gui", "-c", "dqn.sumocfg"])
        traci.start(["sumo", "-c", "dqn.sumocfg"])
        state1 = get_state("c1")
        state1 = np.reshape(state1, [1, 3]) 
        state2 = get_state("c2")
        state2 = np.reshape(state2, [1, 3]) 
        for step in range(1000):
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)

            # state, reward, done, _ = env.step(env.action_space.sample())

            phase1 = traci.trafficlight.getPhase("c1")
            phase2 = traci.trafficlight.getPhase("c2")
            if phase_before1 == phase1:
                if num1 == 10:
                    before_state1 = state1
                    state1 = get_state("c1")
                    state1 = np.reshape(state1, [1, 3]) 
                    before_action1 = action1
                    action1 = get_action(state1, episode, mainQN1)
                    r1 = reward("c1")
                    memory.add((before_state1, before_action1, r1, state1)) 
                    state_trans(action1,"c2")
                    # state = np.reshape(state, [1, 3]) 
                    phase_before1 = traci.trafficlight.getPhase("c1")
                    num1 = -1
            else:
                if num1 == 13:
                    before_state1 = state1
                    state1 = get_state("c1")
                    state1 = np.reshape(state1, [1, 3]) 
                    before_action1 = action1
                    action1 = get_action(state1, episode, mainQN1)
                    r = reward("c1")
                    memory.add((before_state1, before_action1, r1, state1)) 
                    state_trans(action1,"c1")
                    # next_state = np.reshape(next_state, [1, 3]) 
                    phase_before1 = traci.trafficlight.getPhase("c1")
                    num1 = -1
            if phase_before2 == phase2:
                if num2 == 10:
                    before_state2 = state2
                    state2 = get_state("c2")
                    state2 = np.reshape(state2, [1, 3]) 
                    before_action2 = action2
                    action2 = get_action(state2, episode, mainQN2)
                    r2 = reward("c2")
                    memory.add((before_state2, before_action2, r2, state2)) 
                    state_trans(action2,"c2")
                    # state = np.reshape(state, [1, 3]) 
                    phase_before2 = traci.trafficlight.getPhase("c2")
                    num2 = -1
            else:
                if num2 == 13:
                    before_state2 = state2
                    state2 = get_state("c2")
                    state2 = np.reshape(state2, [1, 3]) 
                    before_action2 = action2
                    action2 = get_action(state2, episode, mainQN2)
                    r = reward("c2")
                    memory.add((before_state2, before_action2, r2, state2)) 
                    state_trans(action2,"c2")
                    # next_state = np.reshape(next_state, [1, 3]) 
                    phase_before2 = traci.trafficlight.getPhase("c2")
                    num2 = -1

            targetQN1.model.set_weights(mainQN1.model.get_weights())
            targetQN2.model.set_weights(mainQN2.model.get_weights())

            # if memory.len() > batch_size:
            #     mainQN.replay(memory, batch_size, gamma, targetQN)

            num1+= 1
            num2+= 1
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
    
dqn = dqn()
rulebase = rulebase()

p1 = plt.plot(rulebase)
p2 = plt.plot(dqn)
plt.legend((p1[0],p2[0]), ("rulebase","dqn"), loc=2)

plt.xlabel("step(×1000)")
plt.ylabel("travel time")
plt.show()