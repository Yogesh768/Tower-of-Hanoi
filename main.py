#TOWER OF HANOI
def hanoi(rings, start_tower, end_tower, hold_tower):
    if rings == 1:
        print ("Move ring %r from %r to %r" % (rings, start_tower['name'], end_tower['name']),
        end_tower['contents'].insert(0, start_tower['contents'].pop(0)))
        print_towers(start_tower, end_tower, hold_tower)
    else:
        hanoi(rings-1, start_tower, hold_tower, end_tower)
        print ("Move ring %r from %r to %r" % (rings, start_tower['name'], end_tower['name']),
        end_tower['contents'].insert(0, start_tower['contents'].pop(0)))
        print_towers(start_tower, end_tower, hold_tower)
        hanoi(rings-1, hold_tower, end_tower, start_tower)

def print_towers(A, B, C):
    towers = {}
    towers[A['name']] = A['contents']
    towers[B['name']] = B['contents']
    towers[C['name']] = C['contents']
    for k in sorted(towers.keys()):
        print (k + ": ", towers[k],)
    print

        
hanoi(1, {'name': 'A', 'contents':[1]}, {'name': 'B', 'contents': []}, {'name': 'C', 'contents': []})
print ( "-------")
hanoi(2, {'name': 'A', 'contents':[1, 2]}, {'name': 'B', 'contents': []}, {'name': 'C', 'contents': []})
print ("-------")
hanoi(3, {'name': 'A', 'contents':[1, 2, 3]}, {'name': 'B', 'contents': []}, {'name': 'C', 'contents': []})
print ("-------")
hanoi(4, {'name': 'A', 'contents':[1, 2, 3, 4]}, {'name': 'B', 'contents': []}, {'name': 'C', 'contents': []})