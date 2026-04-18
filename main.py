from collections import deque

def bfs(graph, start_node):
    # Множество для посещенных узлов
    visited = set()
    # Очередь для обхода (FIFO)
    queue = deque([start_node])
    
    visited.add(start_node)
    traversal_order = []

    print(f"--- Запуск BFS с узла {start_node} ---")

    while queue:
        # Достаем первый элемент из очереди
        current_node = queue.popleft()
        traversal_order.append(current_node)
        
        # Перебираем соседей
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal_order

# Список смежности (наш граф)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Вывод результата
if __name__ == "__main__":
    result = bfs(graph, 'A')
    print("Порядок обхода:", " -> ".join(result))