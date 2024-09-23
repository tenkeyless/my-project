import random
from benchmark.algorithm_benchmark import AlgorithmBenchmark

# 그래프 생성 (Mock 데이터로 시뮬레이션)
def generate_mock_graph(size):
    graph = {}
    for i in range(size):
        graph[i] = {j: random.randint(1, 10) for j in range(size) if i != j}
    return graph

# 성능 측정 실행
def benchmark_algorithms():
    graph = generate_mock_graph(100)  # 100개의 노드를 가진 mock 그래프
    start, goal = 0, 99

    benchmark = AlgorithmBenchmark()

if __name__ == "__main__":
    benchmark_algorithms()
