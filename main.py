def Dfs(graphe, sommet, visite):
    visite.add(sommet)
    print(sommet)

    for voisin in graphe[sommet]:
        if voisin not in visite:
            DFS(graphe, voisin, visite)

    return visite



def Bfs(graphe, depart):
    visites = {depart}
    file = [depart]

    while file:
        sommet = file[0]
        file.pop(0)
        print(sommet)

        for voisin in graphe[sommet]:
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)

    return visites



def dijkstra(graphe, depart):
    d = {s: float('inf') for s in graphe}
    pere = {s: None for s in graphe}
    restants = list(graphe)

    d[depart] = 0

    while restants:
        u = min(restants, key=d.get)
        restants.remove(u)

        for v, poids in graphe[u]:
            if d[u] + poids < d[v]:
                d[v] = d[u] + poids
                pere[v] = u

    return d, pere
