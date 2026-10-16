# Graph Report - roboflow-plugin-roboflow-computer-vision-openai  (2026-10-16)

## Corpus Check
- 2 files · ~2,529 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 30 nodes · 32 edges · 4 communities
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `541cf366`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]

## God Nodes (most connected - your core abstractions)
1. `AeroSight` - 11 edges
2. `Run locally` - 4 edges
3. `QueryPredicate` - 4 edges
4. `model_labels()` - 3 edges
5. `infer_jpeg()` - 3 edges
6. `Project structure` - 3 edges
7. `get_model()` - 2 edges
8. `infer_socket()` - 2 edges
9. `Model provenance` - 2 edges
10. `code:text (models/uav-persons-detection-3-yolo11n-t1/weights.pt)` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (4 total, 0 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.22
Nodes (8): AeroSight, Features, How it works, Licensing, Model and application licensing, Test a video, Try a video, What you can do

### Community 1 - "Community 1"
Cohesion: 0.43
Nodes (4): get_model(), infer_jpeg(), infer_socket(), model_labels()

### Community 2 - "Community 2"
Cohesion: 0.29
Nodes (7): code:text (models/uav-persons-detection-3-yolo11n-t1/weights.pt), code:powershell (python -m pip install -r requirements.txt), code:powershell ($env:YOLO_MODEL = 'C:\path\to\weights.pt'), code:text (app.py                              FastAPI server, WebSocke), Model provenance, Project structure, Run locally

### Community 3 - "Community 3"
Cohesion: 0.29
Nodes (5): _Protocol, QueryPredicate, Python bindings to the Tree-sitter parsing library., A custom query predicate that runs on a pattern., Parameters         ----------          predicate : str             The name

## Knowledge Gaps
- **12 isolated node(s):** `Features`, `code:powershell (python -m pip install -r requirements.txt)`, `Test a video`, `code:text (app.py                              FastAPI server, WebSocke)`, `Licensing` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AeroSight` connect `Community 0` to `Community 2`?**
  _High betweenness centrality (0.224) - this node is a cross-community bridge._
- **Why does `Run locally` connect `Community 2` to `Community 0`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Why does `Project structure` connect `Community 2` to `Community 0`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **What connects `Features`, `code:powershell (python -m pip install -r requirements.txt)`, `Test a video` to the rest of the system?**
  _12 weakly-connected nodes found - possible documentation gaps or missing edges._