import networkx as nx
import matplotlib.pyplot as plt
import math
import random
with open('Keywords greater than 8.txt','r') as f:
    kws=f.read()
    kws=kws.split('",\n"')
f.close()
numowords=len(kws)
with open('Counts greater than 8.txt','r') as f:
    dm=f.read()
    dm=dm.split(',\n')
f.close()
G=nx.Graph()
F=nx.Graph()
for i in kws:
    G.add_node(i)
    F.add_node(i)
i=0
j=0
while i<numowords:
    j=i+1
    while j<numowords:
        cv=i*numowords+j
        val=dm[cv]
        if val>0:
            weight=float(val)/(math.sqrt(float(dm[i*numowords+i]))*math.sqrt(float(dm[j*numowords+j])))
            G.add_edge(kws[i],kws[j],weight=str(weight))
            if weight!=0:
                F.add_edge(kws[i],kws[j],weight=str(1/weight))
        j=j+1
    i=i+1

#edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
#nx.draw(G, with_labels=1, node_color='b', edgelist=edges, node_size=10, edge_color=weights, width=0.01, edge_cmap=plt.cm.Blues)
#plt.show()
# uncomment these if you want to display the original graph
count=0
maxweight=0
newnode=''
oldnode=''
H=nx.Graph()
H.add_node('Cyber security')
while len(H.nodes())<len(G.nodes()):
    for nih in H.nodes():
        for neigh in G.neighbors(nih):
            if neigh in H.nodes():
                continue

            else:
                if G[neigh][nih]['weight']>maxweight:
                    newnode=neigh
                    oldnode=nih
                    maxweight=G[neigh][nih]['weight']
    H.add_node(newnode)
    count=count+1
    print str(count)+': added node '+newnode
    H.add_edge(oldnode,newnode)
    maxweight=0
    newnode=''
    oldnode=''
    if count ==20:
        break
root='Cyber security'

def treegetpos(G, root):
    depth=1
    da=[]
    maxdepth=0
    while len(da)<len(G.nodes()):
        if len(da)==0:
            da.append((root,depth,''))
        else:
            for node in da:
                if node[1]==depth-1:
                    for n in G.neighbors(node[0]):
                        if n!=node[2]:
                            da.append((n,depth,node[0]))
        maxdepth=depth
        depth=depth+1
    posit={}
    dq=[]
    c=0
    while c<maxdepth:
        dq.append(0)
        c=c+1
    for node in da:
        dq[node[1]-1]=dq[node[1]-1]+1
    dm1=0
    while dm1<len(dq):
        dc=0
        while dc<dq[dm1]:
            for node in da:
                if node[1]-1==dm1:
                    posit.update({node[0]:(6*dm1,2*(dc-(dq[dm1]/2)))})
                    dc=dc+1
        dm1=dm1+1
    return posit

positions=treegetpos(H,root)

nx.draw(H, pos=positions, with_labels=1, node_size=3,  width=.2, font_size=8)
plt.show()
plt.savefig('edges.png')
#


