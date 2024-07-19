import math


def least_popular_person(graph):
    least_friendship_count = math.inf

    for node in graph:
        if len(graph[node]) < least_friendship_count:
            least_friendship_count = len(graph[node])

    queue_lpp = []

    for node in graph:
        if len(graph[node]) == least_friendship_count:
            queue_lpp.append(node)
    return queue_lpp


file = open('social_network_50.txt')
graph = eval(file.read())
queue = least_popular_person(graph)
print(queue)

visited = []
levels = []

while queue:

    node = queue.pop(0)
    print('dequeue', node)

    if node not in visited:
        visited.append(node)
        print('visiting', node)

        level = []

        for neighbour in graph[node]:
            if neighbour not in queue and neighbour not in visited:
                print('enqueue', neighbour)
                queue.append(neighbour)
                level.append(neighbour)

        if level:
            levels.append(level)

    print('queue:{} visited:{}'.format(queue, visited))

print('levels', levels)



