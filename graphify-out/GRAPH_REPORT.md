# Graph Report - roboflow-plugin-roboflow-computer-vision-openai  (2026-10-16)

## Corpus Check
- 2 files · ~2,006 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 22 nodes · 22 edges · 4 communities
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]

## God Nodes (most connected - your core abstractions)
1. `AeroSight` - 5 edges
2. `QueryPredicate` - 4 edges
3. `model_labels()` - 3 edges
4. `infer_jpeg()` - 3 edges
5. `Run locally` - 3 edges
6. `get_model()` - 2 edges
7. `infer_socket()` - 2 edges
8. `Features` - 1 edges
9. `code:powershell (python -m pip install -r requirements.txt)` - 1 edges
10. `code:powershell ($env:YOLO_MODEL = 'C:\path\to\best.pt')` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (4 total, 0 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.43
Nodes (4): get_model(), infer_jpeg(), infer_socket(), model_labels()

### Community 1 - "Community 1"
Cohesion: 0.29
Nodes (5): _Protocol, QueryPredicate, Python bindings to the Tree-sitter parsing library., A custom query predicate that runs on a pattern., Parameters         ----------          predicate : str             The name

### Community 2 - "Community 2"
Cohesion: 0.4
Nodes (4): AeroSight, Features, Model and application licensing, Test a video

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (3): code:powershell (python -m pip install -r requirements.txt), code:powershell ($env:YOLO_MODEL = 'C:\path\to\best.pt'), Run locally

## Knowledge Gaps
- **8 isolated node(s):** `Features`, `code:powershell (python -m pip install -r requirements.txt)`, `code:powershell ($env:YOLO_MODEL = 'C:\path\to\best.pt')`, `Test a video`, `Model and application licensing` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AeroSight` connect `Community 2` to `Community 3`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Why does `Run locally` connect `Community 3` to `Community 2`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **What connects `Features`, `code:powershell (python -m pip install -r requirements.txt)`, `code:powershell ($env:YOLO_MODEL = 'C:\path\to\best.pt')` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._