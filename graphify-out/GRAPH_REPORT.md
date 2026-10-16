# Graph Report - roboflow-plugin-roboflow-computer-vision-openai  (2026-10-16)

## Corpus Check
- 2 files · ~2,482 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 28 nodes · 28 edges · 5 communities (4 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7d8257fc`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]

## God Nodes (most connected - your core abstractions)
1. `AeroSight` - 10 edges
2. `QueryPredicate` - 4 edges
3. `model_labels()` - 3 edges
4. `infer_jpeg()` - 3 edges
5. `Run locally` - 3 edges
6. `get_model()` - 2 edges
7. `infer_socket()` - 2 edges
8. `Project structure` - 2 edges
9. `What you can do` - 1 edges
10. `How it works` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (5 total, 1 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.22
Nodes (8): AeroSight, Features, How it works, Licensing, Model and application licensing, Test a video, Try a video, What you can do

### Community 1 - "Community 1"
Cohesion: 0.43
Nodes (4): get_model(), infer_jpeg(), infer_socket(), model_labels()

### Community 2 - "Community 2"
Cohesion: 0.29
Nodes (5): _Protocol, QueryPredicate, Python bindings to the Tree-sitter parsing library., A custom query predicate that runs on a pattern., Parameters         ----------          predicate : str             The name

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (3): code:powershell (python -m pip install -r requirements.txt), code:powershell ($env:YOLO_MODEL = 'C:\path\to\best.pt'), Run locally

## Knowledge Gaps
- **13 isolated node(s):** `What you can do`, `How it works`, `code:powershell (python -m pip install -r requirements.txt)`, `code:powershell ($env:YOLO_MODEL = 'C:\path\to\best.pt')`, `Try a video` (+8 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AeroSight` connect `Community 0` to `Community 3`, `Community 4`?**
  _High betweenness centrality (0.211) - this node is a cross-community bridge._
- **Why does `Run locally` connect `Community 3` to `Community 0`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **What connects `What you can do`, `How it works`, `code:powershell (python -m pip install -r requirements.txt)` to the rest of the system?**
  _13 weakly-connected nodes found - possible documentation gaps or missing edges._