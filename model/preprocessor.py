messages = {}

def read_raw():
    lines = []
    with open("input.txt", 'r',  encoding='utf-8') as fin:
        lines = fin.readlines()
    return lines


def categorize(lines):
    
    name = ""
    runningMessage = ""
    
    for _line in lines:
        timestamp, _, line = _line.partition('-')
        if (timestamp.count('/') == 2): 
            
            if (":" not in line):
                continue  
            if name in messages:
                messages[name].append(runningMessage.replace("<Media omitted>", ""))
            else:
                messages[name] = [runningMessage.replace("<Media omitted>", "")]  
                
            name, _, runningMessage = line.partition(':')
            runningMessage = runningMessage.strip()
        else:
            runningMessage += " " + _line.strip()
        
    
    if name in messages:
        messages[name].append(runningMessage)
    else:
        messages[name] = [runningMessage] 


def get_messages():
    categorize(read_raw())
    return messages


if __name__ == "__main__":
    for name in get_messages():
        print(name, messages[name])
