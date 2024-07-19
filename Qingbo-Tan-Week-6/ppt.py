def find_same_age_acquaintances(friends,ages,search_name,search_age):
    acquaintances = []
    found_friends = []
    queue = [search_name]

    while queue:
        person = queue.pop(0)
        found_friends.append(person)
        if person != search_name and ages[person] == search_age:
            acquaintances.append(person)

        for friend in friends[person]:
            if friend not in queue and friend not in found_friends:
                queue.append(friend)

    return acquaintances

def shortest_steps_between(graph,start,end):
    explored =[]
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            for neighbour in graph[node].get_neighbours():
                if neighbour not in queue and neighbour not in explored:
                    queue.append(neighbour)
                    graph[neighbour].attr["steps"] = graph[node].attr["steps"] +1

    return graph[end].attr["steps"]