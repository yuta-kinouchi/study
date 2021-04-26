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

# 比を変化させずに、交通流全体が変化する環境
# 右折比率は1割にする
    def add_car(self,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)

        if y <= 600:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.6 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.6 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.6 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.6 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   
        elif y <= 1200:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 1800:
            if np.random.uniform(0,1) < 1 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 1 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 1 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 1 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 2400:
            if np.random.uniform(0,1) < 1 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 1 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 1 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 1 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')     
        elif y <= 3000:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        else:
            if np.random.uniform(0,1) < 0.6 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.6 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.6 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.6 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')        

# 交通量全体は固定するが、比を変化させる
    def add_car(self,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)

        if y <= 600:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.8 * 0.1:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.1:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.4:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.4:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   
        elif y <= 1200:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 1800:
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 2400:
            if np.random.uniform(0,1) < 0.8 * 0.4:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.4:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.1:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.1:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')     
        elif y <= 3000:
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        else:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   

# 直進車両に対する右折車両比率を変更する
    def add_car(self,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)

        if y <= 600:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   
        elif y <= 1200:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.2 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.2 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 1800:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.3:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.3 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.3:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1)  > 0.3 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 2400:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.3:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.3 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.3:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.3 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')     
        elif y <= 3000:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.2 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.2:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        else:
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.8 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   


    def add_car(self,tf,step):
        x = str(step)
        if tf[0] == 0:
            p = 0.125
        elif tf[0] == 1:
            p = 0.25
        elif tf[0] == 2:
            p = 0.375
        else:
            p = 0.5

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