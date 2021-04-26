# 交差する交通流が変化する環境
    # 200秒ごとに交通流更新
    def add_car(self,tf,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)
        if y <= 200:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   
        elif y <= 400:
            if np.random.uniform(0,1) < 0.4 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.4 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.4 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.4 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 600:
            if np.random.uniform(0,1) < 0.3 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 800:
            if np.random.uniform(0,1) < 0.2 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.2 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.2 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.2 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')     
        elif y <= 1000:
            if np.random.uniform(0,1) < 0.1 * 0.2:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.1 * 0.2:
                if np.random.uniform(0,1) > 0.2 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.1 * 0.3:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.1 * 0.3:
                if np.random.uniform(0,1)  > 0.2:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 1200:
            if np.random.uniform(0,1) < 0.2 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.2 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 1400:
            if np.random.uniform(0,1) < 0.4 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.4 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.4 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.4 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 1600:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 1800:
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
        elif y <= 2000:
            if np.random.uniform(0,1) < 0.7 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.7 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.7 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.7 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 2200:
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
        elif y <= 2400:
            if np.random.uniform(0,1) < 0.7 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.7 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.7 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.7 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 2600:
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
        elif y <= 2800:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')
        elif y <= 3000:
            if np.random.uniform(0,1) < 0.4 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.4 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.4 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.4 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 3200:
            if np.random.uniform(0,1) < 0.3 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 3400:
            if np.random.uniform(0,1) < 0.2 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.2 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.2 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.2 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 3600:
            if np.random.uniform(0,1) < 0.1 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.1 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.1 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.1 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 

    # 400秒ごとに交通流更新
    def add_car(self,tf,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)

        if y <= 400:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   
        elif y <= 800:
            if np.random.uniform(0,1) < 0.4 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.4 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.4 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.4 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 1200:
            if np.random.uniform(0,1) < 0.3 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 1600:
            if np.random.uniform(0,1) < 0.2 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.2 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.2 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.2 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')     
        elif y <= 2000:
            if np.random.uniform(0,1) < 0.1 * 0.2:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.1 * 0.2:
                if np.random.uniform(0,1) > 0.2 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.1 * 0.3:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.1 * 0.3:
                if np.random.uniform(0,1)  > 0.2:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 2400:
            if np.random.uniform(0,1) < 0.3 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.3 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 2800:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        elif y <= 3200:
            if np.random.uniform(0,1) < 0.7 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.7 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.7 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.7 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 
        else:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE') 

    def add_car(self,tf,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)
        if y <= 600:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
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
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   
        elif y <= 1200:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 1800:
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 2400:
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')     
        elif y <= 3000:
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.2 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1)  > 0.2:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 3600:
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')    

    def add_car(self,tf,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)
        if y <= 600:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
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
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   
        elif y <= 1200:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 1800:
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 2400:
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')     
        elif y <= 3000:
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.2 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1)  > 0.2:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 3600:
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1)  > 0.1:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')    

    def add_car(self,tf,step):
        # テスト環境として相応しい交通流を作成する
        y = int(step)
        x = str(step)
        if y <= 800:
            self.tf[0] = 0
            # if np.random.uniform(0,1) < 0.125 * 0.2 * 0.5:
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
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
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')   
        elif y <= 1600:
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 2400:
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.3:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.2:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  
        elif y <= 3200:
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.1 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.1:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1)  > 0.1 :
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')     
        elif y <= 3600:
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x  + "tl",routeID="t_r", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.4:
                if np.random.uniform(0,1) > 0.2 :
                    traci.vehicle.addFull(vehID=x + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
                else:
                    traci.vehicle.addFull(vehID=x + "br",routeID="b_l", typeID='DEFAULT_VEHTYPE')
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1) > 0.2:
                    traci.vehicle.addFull(vehID=x + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
                else:
                    traci.vehicle.addFull(vehID=x + "rt",routeID="r_b", typeID='DEFAULT_VEHTYPE')  
            if np.random.uniform(0,1) < 0.5 * 0.1:
                if np.random.uniform(0,1)  > 0.2:
                    traci.vehicle.addFull(vehID=x + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   
                else:
                    traci.vehicle.addFull(vehID=x + "lb",routeID="l_t", typeID='DEFAULT_VEHTYPE')  