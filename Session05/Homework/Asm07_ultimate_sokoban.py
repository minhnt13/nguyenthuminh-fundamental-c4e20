map = {
    "size_x": 6, 
    "size_y": 6
}

player = {"x": 1, "y": 1}

boxes = [
    {"x": 0, "y": 2},
    {"x": 1, "y": 2},
    {"x": 2, "y": 2},
    {"x": 3, "y": 2}
]

destination = [
    {"x": 0, "y": 3},
    {"x": 1, "y": 4},
    {"x": 0, "y": 5},
    {"x": 3, "y": 5}
]

obstacle = [
    {"x": 1, "y": 3},
    {"x": 4, "y": 5}
]

playing = True
while playing:
# print map
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            box_is_here = False
            player_is_here = False
            des_is_here = False
            obst_is_here = False
            if y == player["y"] and x == player["x"]:
                player_is_here = True
            for box in boxes:
                if y == box["y"] and x == box["x"]:
                    box_is_here = True
            for des in destination:
                if y == des["y"] and x == des["x"]:
                    des_is_here = True
            for obst in obstacle:
                if y == obst["y"] and x == obst["x"]:
                    obst_is_here = True
            if player_is_here:
                print("P ", end="")
            elif box_is_here:
                print("B ", end="")
            elif des_is_here:
                print("D ", end="")
            elif obst_is_here:
                print("O ", end="")
            else:
                print("- ", end="")
                
        print()
    # end of map printing
    win = True
    for box in boxes: 
        if box not in destination:
            win = False
    if win:
        print("YOU WIN")
        break
    # move player

    move = input("What is your next move? W/A/S/D Or (Undo - Z) ").upper()
   
    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        playing = False
   
    # Player Can't move pass obstance:
    if 0 <= player["y"] + dy < map["size_y"] and 0 <= player["x"] + dx < map["size_x"]:
        player_can_move = True
        moving_box = True
        for obst in obstacle:
            if player["y"] + dy == obst["y"] and player["x"] + dx == obst["x"]:
                player_can_move = False
                print("Oops! Obstacle :' <")
                break
        # kkhó vl không làm nổi nữa gâu gâu baiz
        if moving_box and player_can_move:
                player["y"] += dy
                player["x"] += dx
    
    for box in boxes:
        if  box["y"] == player["y"] and box["x"] == player["x"]:
            box["y"] += dy
            box["x"] += dx

