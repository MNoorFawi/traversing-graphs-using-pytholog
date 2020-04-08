import pytholog as pl

graph_kb = pl.KnowledgeBase("MSA_graph")
graph_kb([## routes between adjacent cities
    "route(seattle, chicago, 1737)",
    "route(seattle, san_francisco, 678)",
    "route(san_francisco, riverside, 386)",
    "route(san_francisco, los_angeles, 348)",
    "route(los_angeles, riverside, 50)",
    "route(los_angeles, phoenix, 357)",
    "route(riverside, phoenix, 307)",
    "route(riverside, chicago, 1704)",
    "route(phoenix, dallas, 887)",
    "route(phoenix, houston, 1015)",
    "route(dallas, chicago, 805)",
    "route(dallas, atlanta, 721)",
    "route(dallas, houston, 225)",
    "route(houston, atlanta, 702)",
    "route(houston, miami, 968)",
    "route(atlanta, chicago, 588)",
    "route(atlanta, washington, 543)",
    "route(atlanta, miami, 604)",
    "route(miami, washington, 923)",
    "route(chicago, detroit, 238)",
    "route(detroit, boston, 613)",
    "route(detroit, washington, 396)",
    "route(detroit, new_york, 482)",
    "route(boston, new_york, 190)",
    "route(new_york, philadelphia, 81)",
    "route(philadelphia, washington, 123)",
	## define the rules how can we move from one point to another 
    "path(X, Y, P) :- route(X, Y, P)",
    "path(X, Y, P) :- route(X, Z, P2), path(Z, Y, P3), P is P2 + P3",
	## to make it undirected (two-way) graph
    #"path(X, Y, P) :- route(Y, X, P)",
    "path(X, Y, P) :- route(Y, Z, P2), path(Z, X, P3), P is P2 + P3"
        ])
        
x, y = graph_kb.query(pl.Expr("path(boston, miami, Weight)"), cut = True, show_path = True) ## cut argument to stop searching when a path is found
print(x)
print([x for x in y if str(x) > "Z"]) ## remove weights in the visited nodes

# [{'Weight': 1317}]
# ['washington', 'new_york', 'philadelphia']

## the other way
x, y = graph_kb.query(pl.Expr("path(miami, boston, Weight)"), cut = True, show_path = True)
print(x)
print([x for x in y if str(x) > "Z"])

# [{'Weight': 1317}]
# ['new_york', 'washington', 'philadelphia']

x, y = graph_kb.query(pl.Expr("path(seattle, washington, Weight)"), cut = True, show_path = True)
print(x)
print([x for x in y if str(x) > "Z"])

# [{'Weight': 2371}]
# ['chicago', 'detroit']

x, y = graph_kb.query(pl.Expr("path(san_francisco, atlanta, Weight)"), cut = True, show_path = True)
print(x)
print([x for x in y if str(x) > "Z"])

# [{'Weight': 2678}]
# ['houston', 'dallas', 'riverside', 'chicago']

x, y = graph_kb.query(pl.Expr("path(chicago, detroit, Weight)"), cut = True, show_path = True)
print(x)
print([x for x in y if str(x) > "Z"])

# [{'Weight': '238'}]
# []

x, y = graph_kb.query(pl.Expr("path(los_angeles, dallas, Weight)"), cut = True, show_path = True)
print(x)
print([x for x in y if str(x) > "Z"])

# [{'Weight': 1244}]
# ['phoenix']

x, y = graph_kb.query(pl.Expr("path(riverside, washington, Weight)"), cut = True, show_path = True)
print(x)
print([x for x in y if str(x) > "Z"])

# [{'Weight': 2338}]
# ['miami', 'chicago', 'atlanta', 'detroit']
