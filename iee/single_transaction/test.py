import pickle

with open("./qtable/a.txt","rb") as table:
    q = pickle.load(table)

print(q)