import heapq
from .base_algorithm import BaseAlgorithm

class AStarAlgorithm(BaseAlgorithm):
    def heuristic(self, node, goal):
        # 단순한 유클리드 거리 또는 맨해튼 거리를 사용할 수 있습니다.
        # 여기에선 간단하게 차이로 사용 (사용자 데이터에 맞춰 수정 가능)
        return abs(node - goal)

    def run(self, graph, start, goal):
        # 거리 및 휴리스틱 초기화
        distances = {node: float('infinity') for node in graph}
        distances[start] = 0

        priority_queue = [(0, start)]
        explored_nodes = 0
        previous_nodes = {start: None}
        
        while priority_queue:
            current_f_score, current_node = heapq.heappop(priority_queue)
            explored_nodes += 1

            # 목표 지점 도착 시
            if current_node == goal:
                break

            # 인접 노드 처리
            for neighbor, weight in graph[current_node].items():
                tentative_g_score = distances[current_node] + weight
                f_score = tentative_g_score + self.heuristic(neighbor, goal)

                if tentative_g_score < distances[neighbor]:
                    distances[neighbor] = tentative_g_score
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (f_score, neighbor))

        # 경로 재구성
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        return path, explored_nodes