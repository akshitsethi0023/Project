from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Edge,Station
import sys, collections, heapq


# Create your views here.
def home (request):
    return render(request, 'home.html') 

def Routes(request):
    startDest=request.GET["From"]
    endDest=request.GET["To"]
    start = get_object_or_404(Station, name = startDest)
    dest = get_object_or_404(Station, name = endDest)
    st = Edge.objects.all()
    path = Dijkstra(st, start.id, dest.id)
    #return render(request, 'next.html',  {'S' : st})
    return render(request, 'next.html', {'From':start.id, 'To':dest.id, 'S': st, 'P' : path})

def Dijkstra(st, src, dest) :
    path = list()
    parent = {src : -1}                                         #stores parent of a node in shortest path
    distances = { Row.destination_id : float("inf") for Row in st}
    distances[src] = 0

    graph = collections.defaultdict(dict)
    for Row in st:
        graph[Row.source_id][Row.destination_id] = Row.duration

    min_dist = [(0, src, -1)]                 #min heap  (minDistance, destinationNode, parent)
    heapq.heapify(min_dist)

    while min_dist :
        cur_dist, cur, cur_parent = heapq.heappop(min_dist)
        parent[cur] = cur_parent
        for neighbor in graph[cur]:
            this_dist = cur_dist + graph[cur][neighbor]
            if this_dist  < distances[neighbor]:
                distances[neighbor] = this_dist
                heapq.heappush(min_dist, (this_dist, neighbor, cur))
        if(cur == dest):
            break
    node = dest
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

