from pathlib import Path
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
REPOSITORIES = json.loads((ROOT / "repositories.json").read_text(encoding="utf-8"))
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")

assert len(PROJECTS) == 25
assert len({project["id"] for project in PROJECTS}) == len(PROJECTS)
assert len(REPOSITORIES) == 28
assert INDEX.count('class="project-row"') == len(PROJECTS)
assert README.count("| **") >= len(PROJECTS)
assert "tenderfit.co.uk" in INDEX + README
assert "tenderfit.eu" not in INDEX + README
assert "https://github.com/ElilmA/ai-client-delivery-portfolio" in INDEX + README

for project in PROJECTS:
    for field in ("id", "title", "category", "status", "eyebrow", "summary", "description", "order"):
        assert project.get(field), f"{project.get('id', '?')} missing {field}"
    if project.get("image"):
        assert (ROOT / project["image"]).is_file(), f"Missing image {project['image']}"
    if project.get("url"):
        assert project["url"].startswith("https://"), project["url"]
    if project.get("repo"):
        assert project["repo"].startswith("https://github.com/"), project["repo"]
    if project.get("case"):
        assert (ROOT / project["case"]).is_file(), f"Missing case {project['case']}"

public_text = "\n".join(
    path.read_text(encoding="utf-8")
    for path in [ROOT / "README.md", ROOT / "index.html", *sorted((ROOT / "case-studies").glob("*.md"))]
)
assert not re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", public_text, re.I)
for banned in ("portfolio-hub.png", "upwork-rag-live.png", "parking-reservations.png", "workforce-workflows.png", "legacy-commerce.png", "tenderfit-eu-live.png"):
    assert banned not in public_text, f"Generated asset still referenced: {banned}"

asset_files = sorted(path.name for path in (ROOT / "assets").iterdir() if path.is_file())
digests = {
    name: hashlib.sha256((ROOT / "assets" / name).read_bytes()).hexdigest().upper()
    for name in asset_files
}
result = {
    "projects": len(PROJECTS),
    "repositories": len(REPOSITORIES),
    "project_rows": INDEX.count('class="project-row"'),
    "assets": len(asset_files),
    "tenderfit_domain": "tenderfit.co.uk",
    "email_matches": 0,
    "generated_cover_references": 0,
    "asset_sha256": digests,
}
output = ROOT.parents[2] / ".ai/artifacts/portfolio-content-validation-20261030.json"
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
