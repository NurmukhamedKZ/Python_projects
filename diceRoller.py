import random

def show_plane(num):
    plane_arts = {1: ("┌─────────┐",
                      "│         │",
                      "│    •    │",
                      "│         │",
                      "└─────────┘",),
                  2: ("┌─────────┐",
                      "│  •      │",
                      "│         │",
                      "│      •  │",
                      "└─────────┘",),
                  3: ("┌─────────┐",
                      "│  •      │",
                      "│    •    │",
                      "│      •  │",
                      "└─────────┘",),
                  4: ("┌─────────┐",
                      "│  •   •  │",
                      "│         │",
                      "│  •   •  │",
                      "└─────────┘",),
                  5: ("┌─────────┐",
                      "│ •     • │",
                      "│    •    │",
                      "│ •     • │",
                      "└─────────┘",),
                  6: ("┌─────────┐",
                      "│  •   •  │",
                      "│  •   •  │",
                      "│  •   •  │",
                      "└─────────┘",),}
    pcints = []
    for x in range(num):
        pcints.append(random.randint(1,6))
        
    for i in range(5):    
        for j in range(num):
            print(plane_arts.get(pcints[j])[i], end=" ")
        print()
    print(f"total: {sum(pcints)}")

a = int(input("how many dice?: "))
show_plane(a)