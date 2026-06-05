# AI Studio Phase A Setup Guide (AIBugfix)

## 1) Organization
- Name: AIBugfix
- Default admin: superadmin@cosmos.local

## 2) Project Assets
- Repository URL: https://github.com/rammoorthyraju/ltts-bmw-aibugfix-test.git
- RCA input file: rca/APP-101.json
- Primary buggy file: src/ui/music_page.py

## 3) Phase A Agent Chain
1. component_mapper
2. code_understander
3. interface_analyst
4. bug_fixer
5. code_reviewer

## 4) Prompt Templates

### component_mapper
Given the RCA, return top relevant files.
Output JSON only:
{
  "relevant_files": ["..."],
  "module_path": "...",
  "confidence_notes": "..."
}

### code_understander
Analyze selected files and identify likely failure path.
Output JSON only:
{
  "code_summary": "...",
  "call_graph": {"...": ["..."]},
  "risk_areas": ["..."],
  "error_handling_map": {"...": "..."}
}

### interface_analyst
Assess whether fix may break public interfaces.
Output JSON only:
{
  "interface_contracts": {"...": "..."},
  "breaking_change_risk": "LOW|MEDIUM|HIGH"
}

### bug_fixer
Generate minimal unified diff for root cause only.
Output JSON only:
{
  "fix_diff": "--- a/...\\n+++ b/...\\n@@ ...",
  "fix_explanation": "...",
  "fix_confidence": 0.0
}

### code_reviewer
Review diff + static checks and decide approval.
Output JSON only:
{
  "review_status": "APPROVED|REQUEST_CHANGES",
  "review_comments": ["..."],
  "static_analysis_clean": true
}

## 5) Tool Calls to Register in AI Studio

Minimum set:
- repo_file_index(repo_url, branch)
- semantic_code_search(repo_path, query, top_k)
- fetch_file_content(repo_path, file_path)
- tree_sitter_parse(file_path, language)
- call_graph_builder(repo_path, entry_function, depth)
- clangd_diagnostics(file_path, repo_path) [optional for Python repos]
- generate_unified_diff(defect_id, root_cause, file_contents)
- git_apply_check(repo_path, diff)
- git_apply(repo_path, diff)
- ruff_check(repo_path)
- mypy_check(repo_path)
- bandit_check(repo_path)
- cppcheck_optional(file_path, repo_path)

## 6) Skills and Knowledge Base Usage

Skills:
- code_intelligence: for mapping + structural understanding
- fix_generation: for unified diff generation
- static_analysis: for reviewer decision

Knowledge Base collections:
- rca_history: store solved RCA cases
- codebase_chunks: optional code chunks for semantic retrieval
- review_findings: reviewer comments and outcomes

Suggested ingest metadata per RCA:
- defect_id
- root_cause
- fix_summary
- changed_files
- review_status

## 7) Dynamic Configuration from AI Studio UI

Configure these values in project settings (instead of hardcoding):
- target_repo_url
- default_branch
- target_profile (example: infotainment_rca)
- min_coverage_pct
- static_checks_enabled
- reviewer_threshold

Map UI settings to runtime config keys:
- target_repo_url -> runtime.target.repo_url
- target_profile -> runtime.target.profile
- min_coverage_pct -> runtime.gates.min_coverage_pct
- static_checks_enabled -> runtime.gates.static_checks_enabled
- reviewer_threshold -> runtime.gates.reviewer_confidence_threshold

## 8) Example Runtime Input for APP-101

{
  "defect_id": "APP-101",
  "root_cause": "selected_track can be None, but code accesses selected_track.title and selected_track.artist directly.",
  "target_repo_url": "https://github.com/rammoorthyraju/ltts-bmw-aibugfix-test.git",
  "target_profile": "infotainment_rca",
  "app_id": "",
  "ecu_id": ""
}

## 9) Expected Phase A Output Snapshot

{
  "relevant_files": ["src/ui/music_page.py"],
  "code_summary": "Null dereference in show_track_details when selected_track is None.",
  "breaking_change_risk": "LOW",
  "fix_diff": "--- a/src/ui/music_page.py\\n+++ b/src/ui/music_page.py\\n@@ ...",
  "review_status": "APPROVED"
}
