def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    messages = []
    for index, name in enumerate(names, start=1):
        messages.append("Hello, " + name + "! You'll be assigned to room " + str(index) + "!")
    return messages

def printer(names):
    badges = batch_badge_creator(names)
    messages = assign_rooms(names)

    for badge in badges:
        print(badge)
    
    for message in messages:
        print(message)
