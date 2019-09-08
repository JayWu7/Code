class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        '''
        thinking: is a circle map, so we only need to do is telling which direction is the faster way
        to get to the destination, from right or left.
        '''
        if start > destination:
            start, destination = destination, start
        right = sum(distance[start:destination])
        left = sum(distance[destination:]) + sum(distance[:start])

        return right if right < left else left
