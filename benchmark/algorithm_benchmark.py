import time

class AlgorithmBenchmark:
    def measure_performance(self, algorithm, graph, start, goal):
        # 시간 측정
        start_time = time.time()

        # 알고리즘 실행
        path, explored_nodes = algorithm.run(graph, start, goal)

        # 시간 측정 종료
        end_time = time.time()

        # 실행 시간, 탐색된 노드, 경로 길이
        return {
            'execution_time': end_time - start_time,
            'explored_nodes': explored_nodes,
            'path_length': len(path) if path else 0,
            'complexity_estimate': f"O({len(graph)}^2)"
        }