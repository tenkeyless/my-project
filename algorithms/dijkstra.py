import heapq
from .base_algorithm import BaseAlgorithm

class DijkstraAlgorithm(BaseAlgorithm):
    def run(self, graph, start, goal):
        # 거리 저장소 초기화
        distances = {node: float('infinity') for node in graph}
        distances[start] = 0

        # 우선순위 큐
        priority_queue = [(0, start)]
        explored_nodes = 0
        previous_nodes = {start: None}
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            explored_nodes += 1

            if current_distance > distances[current_node]:
                continue

            # 목표 지점 도착 시
            if current_node == goal:
                break

            # 인접 노드 처리
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        # 경로 재구성
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        return path, explored_nodes