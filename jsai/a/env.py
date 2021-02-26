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
​
​
class MyEnv(gym.Env):
   def __init__(self):
       super().__init__()
       # action_space, observation_space, reward_range を設定する
       self.action_space = gym.spaces.Discrete(3)
       self.observation_space = gym.spaces.Box(
           low=-100,
           high=100,
           shape=(11,)
       )
       self.reward_range = [-1., 100.]
       self.started = False
       self.reset()
       #self.lane_dict = {"gneE1_0": [0, 0, 0, 0, 1], "gne"}

   def reset(self):
       if self.started:
           traci.close()
       traci.start(["sumo-gui", "-c", os.path.expanduser("~/sotsu/sumo/sotsu.sumocfg"), "--step-length", "0.1", "--fcd-output", "fcd.xml", "--lanechange.duration","1.0"])
       traci.vehicle.setLaneChangeMode("0", 0b001000000000)
       while "0" not in traci.vehicle.getIDList():
           traci.simulationStep()
       self.started = True
       self.s = 0
       self.done = False
       return self._get_state()

   def step(self, action):
       if action == 0:
           traci.vehicle.setAccel("0", 0.5)
           traci.vehicle.setDecel("0", 0)
       elif action == 1:
           traci.vehicle.setDecel("0", 5)
       else:
           now_lane = traci.vehicle.getLaneIndex("0")
           if now_lane == 0:
               traci.vehicle.changeLane("0", 1, 1)
           else:
               traci.vehicle.changeLane("0", 0, 1)
           traci.vehicle.setAccel("0", 0)
           traci.vehicle.setDecel("0", 0)
       s = self._get_state()
       if "1" in traci.vehicle.getIDList() and s[6] < 4:
           traci.vehicle.setSpeed("1", 4)
       traci.simulationStep()
       next_s = self._get_state()
       reward, self.done = self._get_reward(next_s, action)
       return next_s, np.array(reward), self.done, {}

   def _get_state(self):
       # car state
       state = []
       state.append(traci.vehicle.getPosition('0')[0])
       state.append(traci.vehicle.getPosition('0')[1])
       state.append(traci.vehicle.getSpeed('0'))
       state.append(traci.vehicle.getAcceleration('0'))
       #state.append(traci.vehicle.getLaneIndex('0'))
       #bike state
       if '1' in traci.vehicle.getIDList():
           state.append(traci.vehicle.getPosition('1')[0])
           state.append(traci.vehicle.getPosition('1')[1])
           state.append(traci.vehicle.getSpeed('1'))
           state.append(traci.vehicle.getAcceleration('1'))
           #car & bike length
           state.append(traci.vehicle.getLength('0'))
           state.append(traci.vehicle.getLength('1'))
          # state.append(traci.vehicle.getLaneIndex('1'))
       else:
           state.extend([-1.6, 25, 3.0, 0.0, 5, 2])
       a = pow((state[0] - state[4]) , 2) + pow((state[1] - state[5]) , 2)

       dis = math.sqrt(a)
       state.append(dis)
       return np.array(state, dtype="float32")

   def _get_reward(self,next_s, action):
       if len(traci.simulation.getCollidingVehiclesIDList()) > 0:
           reward = -100
           self.done = True
       elif next_s[0] < -95:
           reward = 100
           self.done = True
       elif action == 2:
           reward = -3   #moto -5
#            if LCcount == 1:
#                reward = 3
#            elif LCcount > 1:
#                reward = -10
#            else:
#                reward = -5
#            LCcount += 1
       elif next_s[1] < 3.2:
           reward = -0.4  #-0nara oikosi , -0.6nara oinuki , -2nara tuizyuu
       elif next_s[5]-10 < next_s[0]+next_s[8] and \
            next_s[0] < next_s[5]+next_s[9]+5 and action==2:
           reward = -100
           self.done = True
       else:
           reward = -0.1
       return reward, self.done

   def close(self):
       traci.close()




if __name__ == '__main__':
   Env = MyEnv()
   done = False
   LCcount = 0
   traci.vehicle.setLaneChangeMode(0b001000000000) ###
   #Env.reset()
   while not done:
       s, r, done, i = Env.step(0)
       print(r, done)
   traci.close()
  
"""
​
traci.start(["sumo", "-c", "sotsu.sumocfg"])
traci.vehicle.setLaneChangeMode("0", 0b001000000000)
​
step = 0
while step < 50:
   traci.simulationStep()
​
#空行
   print()
   print()
​
#  現在走行中の車両のIDを表示
   print(traci.vehicle.getIDList())
​
#車について　　
#車の位置、速度、加速度、角度、横方向速度、走行道路id_走行レーンidを表示
   print(traci.vehicle.getPosition('0'))
   print(traci.vehicle.getSpeed('0'))
   print(traci.vehicle.getAcceleration('0'))
   print(traci.vehicle.getAngle('0'))
   print(traci.vehicle.getLateralSpeed('0'))
   print(traci.vehicle.getLaneID('0'))
​
#空行
   print()
​
#バイクについて
#バイクの位置、速度、加速度、角度、横方向速度、走行道路id_走行レーンidを表示
   print(traci.vehicle.getPosition('1'))
   print(traci.vehicle.getSpeed('1'))
   print(traci.vehicle.getAcceleration('1'))
   print(traci.vehicle.getAngle('1'))
   print(traci.vehicle.getLateralSpeed('1'))
   print(traci.vehicle.getLaneID('1'))
​
#空行
   print()
​
#バイクと車の距離
​
   carposi_x = traci.vehicle.getPosition('0')[0]
   carposi_y = traci.vehicle.getPosition('0')[1]
   bikposi_x = traci.vehicle.getPosition('1')[0]
   bikposi_y = traci.vehicle.getPosition('1')[1]
​
   a = pow((carposi_x - bikposi_x) , 2) + pow((carposi_y - bikposi_y) , 2)
   dis = math.sqrt(a)
   print('車とバイクの距離 = ',dis)
​
​
   step += 1
​
traci.close()
"""
