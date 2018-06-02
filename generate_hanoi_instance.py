import json

def generate(disk_num, rod_num):
    objects = [{'id': 'goal', 'type': 'Goal_Rod'}]
    relations = []

    for i in range(disk_num):
        name = 'disk_' + str(i)
        obj = {'id': name, 'type': 'Disk'}
        objects.append(obj)

    for i in range(rod_num):
        name = 'rod_' + str(i)
        obj = {'id': name, 'type': 'Rod'}
        objects.append(obj)
        if i != int(rod_num)-1:
            rel = {'type': 'rod_is_not_goal',
                    'source': name,
                    'target': 'goal'}
            relations.append(rel)
    relations.append({'type': 'disk_on_rod',
                        'source': 'disk_'+str(disk_num - 1),
                        'target': 'rod_0'})
    for i in range(disk_num - 1):
        name = 'disk_' + str(i)
        name_under = 'disk_' + str(i+1)
        rel = {'type': 'disk_on_disk',
                    'source': name,
                    'target': name_under}
        relations.append(rel)

    for i in range(disk_num):
        for j in range(i+1, disk_num):
            name = 'disk_' + str(i)
            name_under = 'disk_' + str(j)
            rel = {'type': 'disk_is_smaller_than',
                        'source': name,
                        'target': name_under}
            relations.append(rel)
    Result = {'objects': objects, 'relations': relations}
    file_name = './examples/Hanoi/instances/' + str(disk_num) + 'disks_' + str(rod_num) + 'rods.json'
    with open(file_name, "w") as f:
        json.dump(Result, f, sort_keys=True, indent=4)

for disk_num in range(1, 11):
    for rod_num in range(2, 6):
        generate(disk_num, rod_num)
