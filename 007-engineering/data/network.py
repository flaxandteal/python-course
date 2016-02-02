import networkx

G = networkx.DiGraph()
G.add_node('Beach', demand=-5)
G.add_node('High Ground', demand=5)

G.add_edge('Beach', 'Seatown', weight=3, capacity=6)
G.add_edge('Beach', 'River Valley', weight=5, capacity=4)
G.add_edge('Seatown', 'High Ground', weight=5, capacity=6)
G.add_edge('River Valley', 'High Ground', weight=10, capacity=2)

flow_cost, flow_dict = networkx.capacity_scaling(G)
print("Total cost to satisfy these demands: ", flow_cost)
