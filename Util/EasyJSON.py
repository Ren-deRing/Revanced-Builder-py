import json

def loadjs(directory):
    with open(str(directory), 'r', encoding='UTF8') as f:
        dist = json.load(f)
    
    return dist

def savejs(dist, directory):
    with open(str(directory), 'w', encoding='UTF8') as s:
        json.dump(dist, s, indent=4, ensure_ascii=False)

def dumpsjs(dist):
    
    dist2 = json.dumps(str(dist), indent=2)

    return dist2