def badge_maker(name):
    
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # for name in names:
    #     return (f'Hello, my name is {name}.')
    new_badges =[f"Hello, my name is {name}." for name in names]
    return new_badges
    

def assign_rooms(names):
    rooms = range(1, 9)
    assignments = []
    for room in rooms:
        assignments.append(f'Hello, {names[room - 1]}! You\'ll be assigned to room {room}!')

    return assignments

def printer(names):
    return None
