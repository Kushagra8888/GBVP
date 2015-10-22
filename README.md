# GBVP

Implementation of the Graph Based Vertical Paritioning Algorithm

## Terminologies used

* **primitive cycle**: denotes any cycle in the affinity graph.
* **affinity cycle**: denotes a primitive cycle that contains a cycle node. Assumption: cycle means an affinity cycle.
* **cycle completing edge**: “to be selected” edge that would complete a cycle.
* **cycle node**: is that node of the cycle completing edge, which was selected earlier.
* **former edge**: an edge that was selected between the last cut and the cycle node.
* **cycle edge**: any of the edges forming a cycle.
* **extension of a cycle**: a cycle being extended by pivoting at the cycle node

## Important Conditions

### Possibility of a cycle
 no former edge exists, or p(former edge) <= p(al1 the cycle edges).

### Possibility of extension
p(edge being constiered or cycle completing edge) > = p(any one of the cycle
  edges).

