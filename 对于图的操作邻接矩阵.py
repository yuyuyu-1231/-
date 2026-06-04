def print_matrix(matrix: list[list[int]]):
    """辅助函数：打印矩阵"""
    for row in matrix:
        print(row)


class GraphAdjMat:
    """基于邻接矩阵实现的无向图类"""

    def __init__(self, vertices: list[int], edges: list[list[int]]):
        """
        构造方法：初始化图
        :param vertices: 顶点值列表，例如 [1, 2, 3]
        :param edges: 边列表，每个元素是顶点索引对，例如 [[0, 1], [1, 2]] 表示顶点0-1和顶点1-2之间有边
        """
        # 顶点列表，元素代表"顶点值"，索引代表"顶点索引"
        self.vertices: list[int] = []
        # 邻接矩阵，行列索引对应"顶点索引"，值为1表示有边，0表示无边
        self.adj_mat: list[list[int]] = []
        
        # 添加所有顶点到图中
        for val in vertices:
            self.add_vertex(val)
        
        # 添加所有边到图中
        # 注意：edges 中的元素是顶点在 vertices 列表中的索引，而不是顶点值
        for e in edges:
            self.add_edge(e[0], e[1])

    def size(self) -> int:
        """获取顶点数量"""
        return len(self.vertices)

    def add_vertex(self, val: int):
        """
        添加顶点
        :param val: 顶点的值
        """
        n = self.size()  # 获取当前顶点数量，即新顶点的索引
        
        # 向顶点列表中添加新顶点的值
        self.vertices.append(val)
        
        # 在邻接矩阵中添加一行（全0），表示新顶点与其他顶点的连接关系
        new_row = [0] * n
        self.adj_mat.append(new_row)
        
        # 在邻接矩阵中每一行添加一列（全0），保持矩阵为方阵
        for row in self.adj_mat:
            row.append(0)

    def remove_vertex(self, index: int):
        """
        删除顶点
        :param index: 要删除的顶点在 vertices 列表中的索引
        """
        # 检查索引是否越界
        if index >= self.size():
            raise IndexError(f"顶点索引 {index} 越界，当前顶点数为 {self.size()}")
        
        # 从顶点列表中移除指定索引的顶点
        self.vertices.pop(index)
        
        # 从邻接矩阵中删除对应索引的行
        self.adj_mat.pop(index)
        
        # 从邻接矩阵的每一行中删除对应索引的列
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i: int, j: int):
        """
        添加边
        :param i: 第一个顶点的索引
        :param j: 第二个顶点的索引
        """
        # 参数 i, j 是顶点在 vertices 列表中的索引
        
        # 检查索引是否越界或是否为自环（i == j）
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError(f"边的索引无效: i={i}, j={j}, 顶点数={self.size()}")
        
        # 在无向图中，邻接矩阵关于主对角线对称
        # 设置 (i, j) 和 (j, i) 位置为1，表示两个顶点之间有边
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i: int, j: int):
        """
        删除边
        :param i: 第一个顶点的索引
        :param j: 第二个顶点的索引
        """
        # 参数 i, j 是顶点在 vertices 列表中的索引
        
        # 检查索引是否越界或是否为自环
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError(f"边的索引无效: i={i}, j={j}, 顶点数={self.size()}")
        
        # 将邻接矩阵中对应位置设为0，表示删除边
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0

    def get_vertex_index(self, val: int) -> int:
        """
        根据顶点值获取顶点索引
        :param val: 顶点值
        :return: 顶点索引，如果不存在则返回 -1
        """
        if val in self.vertices:
            return self.vertices.index(val)
        return -1

    def has_edge(self, i: int, j: int) -> bool:
        """
        判断两个顶点之间是否有边
        :param i: 第一个顶点的索引
        :param j: 第二个顶点的索引
        :return: True 表示有边，False 表示无边
        """
        # 检查索引有效性
        if i < 0 or j < 0 or i >= self.size() or j >= self.size():
            return False
        return self.adj_mat[i][j] == 1

    def get_neighbors(self, index: int) -> list[int]:
        """
        获取指定顶点的所有邻居顶点
        :param index: 顶点索引
        :return: 邻居顶点的索引列表
        """
        # 检查索引有效性
        if index < 0 or index >= self.size():
            raise IndexError(f"顶点索引 {index} 越界")
        
        neighbors = []
        # 遍历邻接矩阵的第 index 行，找出所有值为1的位置
        for j in range(self.size()):
            if self.adj_mat[index][j] == 1:
                neighbors.append(j)
        return neighbors

    def print(self):
        """打印邻接矩阵和顶点信息"""
        print("顶点列表 =", self.vertices)
        print("邻接矩阵 =")
        print_matrix(self.adj_mat)


# 测试代码
if __name__ == "__main__":
    # 创建一个图：4个顶点，值分别为 1, 2, 3, 4
    vertices = [1, 2, 3, 4]
    
    # 定义边：使用顶点索引
    # 边 (0,1) 表示顶点1和顶点2相连
    # 边 (0,2) 表示顶点1和顶点3相连
    # 边 (1,2) 表示顶点2和顶点3相连
    # 边 (2,3) 表示顶点3和顶点4相连
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    
    # 初始化图
    graph = GraphAdjMat(vertices, edges)
    
    print("=== 初始图 ===")
    graph.print()
    
    print("\n=== 添加顶点 5 ===")
    graph.add_vertex(5)
    graph.print()
    
    print("\n=== 添加边 (0, 3)，即顶点1和顶点4相连 ===")
    graph.add_edge(0, 3)
    graph.print()
    
    print("\n=== 检查顶点0和顶点3是否有边 ===")
    print(f"has_edge(0, 3) = {graph.has_edge(0, 3)}")
    
    print("\n=== 获取顶点0的邻居 ===")
    neighbors = graph.get_neighbors(0)
    print(f"顶点0的邻居索引: {neighbors}")
    print(f"对应的顶点值: {[graph.vertices[i] for i in neighbors]}")
    
    print("\n=== 删除边 (0, 1) ===")
    graph.remove_edge(0, 1)
    graph.print()
    
    print("\n=== 删除顶点 2（索引为1） ===")
    graph.remove_vertex(1)
    graph.print()