import os, json, time, sys
from run import Goal, Rule, Main_Graph

def loop(instance_name):
    dir_name = 'examples/Hanoi'
    goal_json = open(dir_name + '/goal.json').read()
    rules_json = open(dir_name + '/rules.json').read()
    instance_json = open(dir_name + '/instances/' + instance_name).read()

    # 读取 goal.json 文件
    goal = json.loads(goal_json)
    goal = Goal(goal)
    # 读取 rules.json 文件
    rules = json.loads(rules_json)
    rules = [Rule(rule) for rule in rules]
    # 读取 instance/trivial.json 文件
    graph = json.loads(instance_json)
    graph = Main_Graph(graph['objects'], graph.get('relations', []), goal, rules)
    print(instance_name, '\n')
    start_time = time.time()

    if graph.dfs():
        print("--- %s seconds ---" % (time.time() - start_time))
        print('success\n')#final state:\n', graph)
    else:
        print("--- %s seconds ---" % (time.time() - start_time))
        print('fail')

sys.setrecursionlimit(1500)
for root, dirs, files in os.walk('./examples/Hanoi/instances'):
    files.sort()
    for name in files:
        if name.endswith('.json'):
            loop(name)
