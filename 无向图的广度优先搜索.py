from collections import deque

class Vertex:
    """顶点类定义"""
    def __init__(self,val:int):
        self.val = val

def vals_to_vets(vals:list[int])->list["Vertex"]:
    """输入值列表 vals ，返回顶点列表 vets"""
    return [Vertex(val) for val in vals]

class GraphAdjList:
    """邻接表类定义"""
    def __init__(self,edges:list[list[Vertex]]):
        self.adj_list: dict[Vertex,list[Vertex]]={}
        for edge in edges:
            if edge[0] not in self.adj_list:
                self.add_vertex(edge[0])
            if edge[1] not in self.adj_list:
                self.add_vertex(edge[1])
            self.add_edge(edge[0],edge[1])

    def add_edge(self,vet1:Vertex,vet2:Vertex):
        """添加边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list:
            raise ValueError("顶点不存在")
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def add_vertex(self,vet:Vertex):
        """添加顶点"""
        if vet in self.adj_list:
            raise ValueError("顶点已存在")
        self.adj_list[vet] = []

def graph_bfs(graph:GraphAdjList,start_vet:Vertex)->list[Vertex]:
    """广度优先搜索"""
    res=[]
    visited = set([start_vet])
    que = deque([start_vet])
    while len(que)>0:
        vet = que.popleft()
        res.append(vet)
        for adj_vet in graph.adj_list[vet]:
            if adj_vet  in visited:
                 continue
            visited.add(adj_vet)
            que.append(adj_vet)
    return  res
"""Driver Code"""
if __name__ == "__main__":
    v=vals_to_vets([0,1,2,3,4])
    edges =[
        [v[0],v[1]],
        [v[0],v[3]],
        [v[1],v[2]],
        [v[1],v[4]],
        [v[4],v[3]],

    ]
    graph = GraphAdjList(edges)
    del edges
    res = graph_bfs(graph,v[0])

