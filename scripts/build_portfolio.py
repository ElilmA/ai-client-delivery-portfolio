from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
REPOSITORIES = json.loads((ROOT / "repositories.json").read_text(encoding="utf-8"))

CATEGORY_LABELS = {
    "live": "Live",
    "client": "Client",
    "ai": "AI product",
    "tool": "Tool",
    "lab": "Lab",
}


def esc(value: str | None) -> str:
    return html.escape(value or "", quote=True)


def project_link(project: dict) -> str | None:
    return project.get("url") or project.get("repo") or project.get("case")


def render_link(label: str, href: str) -> str:
    return f'<a href="{esc(href)}">{esc(label)}</a>'


def render_product_card(project: dict) -> str:
    wide = " product-card-wide" if project["category"] == "live" and project["order"] == 1 else ""
    image = ""
    if project.get("image"):
        image = (
            f'<a class="product-image" href="{esc(project_link(project))}">'
            f'<img src="{esc(project["image"])}" alt="{esc(project.get("imageAlt"))}" loading="lazy">'
            "</a>"
        )
    links = []
    if project.get("url"):
        links.append(render_link("Open live product", project["url"]))
    if project.get("repo"):
        links.append(render_link("Source", project["repo"]))
    if project.get("case"):
        links.append(
            render_link(
                "Read case",
                "https://github.com/ElilmA/ai-client-delivery-portfolio/blob/main/"
                + project["case"],
            )
        )
    return f"""
          <article class="product-card{wide}">
            {image}
            <div class="product-copy">
              <p class="kicker">{esc(project.get("eyebrow"))}</p>
              <h3>{esc(project["title"])}</h3>
              <p>{esc(project["summary"])}</p>
              <div class="card-links">{''.join(links)}</div>
            </div>
          </article>
"""


def render_case_card(project: dict) -> str:
    image = ""
    if project.get("image"):
        image = (
            f'<img src="{esc(project["image"])}" '
            f'alt="{esc(project.get("imageAlt"))}" loading="lazy">'
        )
    link = project_link(project) or "#"
    return f"""
          <a class="case-card" href="{esc(link)}" data-category="{esc(project["category"])}">
            {image}
            <span class="case-number">{int(project["order"]):02d}</span>
            <h3>{esc(project["title"])}</h3>
            <p>{esc(project["summary"])}</p>
          </a>
"""


def render_project_row(project: dict) -> str:
    links = []
    if project.get("url"):
        links.append(render_link("Live", project["url"]))
    if project.get("repo"):
        links.append(render_link("Source", project["repo"]))
    if project.get("case"):
        links.append(
            render_link(
                "Case",
                "https://github.com/ElilmA/ai-client-delivery-portfolio/blob/main/"
                + project["case"],
            )
        )
    chips = "".join(f"<li>{esc(item)}</li>" for item in project.get("stack", [])[:4])
    thumb = ""
    main_class = "project-main"
    if project.get("image"):
        main_class += " has-image"
        thumb = (
            f'<img class="project-thumb" src="{esc(project["image"])}" '
            f'alt="{esc(project.get("imageAlt"))}" loading="lazy">'
        )
    return f"""
          <article class="project-row" data-category="{esc(project["category"])}">
            <span class="project-number">{int(project["order"]):02d}</span>
            <div class="{main_class}">
              <div>
                <p class="project-meta">{esc(CATEGORY_LABELS.get(project["category"]))} / {esc(project["status"])}</p>
                <h3>{esc(project["title"])}</h3>
                <p>{esc(project["summary"])}</p>
                <ul class="project-stack" aria-label="Technology">{chips}</ul>
              </div>
              {thumb}
            </div>
            <div class="project-links">{''.join(links)}</div>
          </article>
"""


def render_html() -> str:
    live = [p for p in PROJECTS if p["category"] == "live" and p.get("featured")]
    client = [p for p in PROJECTS if p["category"] == "client"][:3]
    live_cards = "".join(render_product_card(p) for p in live)
    client_cards = "".join(render_case_card(p) for p in client)
    project_rows = "".join(render_project_row(p) for p in PROJECTS)
    filters = [
        ("all", "All work"),
        ("live", "Live"),
        ("client", "Client"),
        ("ai", "AI"),
        ("tool", "Tools"),
        ("lab", "Labs"),
    ]
    filter_buttons = "".join(
        f'<button type="button" data-filter="{key}" class="filter-button'
        f'{" is-active" if key == "all" else ""}">{esc(label)}</button>'
        for key, label in filters
    )
    return f"""
      <section class="section" id="live" aria-labelledby="live-title">
        <div class="section-heading">
          <div>
            <p class="section-tag">Open the actual products</p>
            <h2 id="live-title">Live products, not just descriptions.</h2>
          </div>
          <p>Every featured entry opens a running product or a concrete product preview. Images are real screenshots from the deployed UI.</p>
        </div>
        <div class="product-grid">{live_cards}</div>
      </section>

      <section class="section section-dark" id="client-work" aria-labelledby="client-title">
        <div class="section-heading">
          <div>
            <p class="section-tag">Sanitized client delivery</p>
            <h2 id="client-title">Complex systems, explained without leaking the client.</h2>
          </div>
          <p>Client code, branding, private screenshots, and customer data stay private. The selected screenshots below show only the project UI without exposing customer records.</p>
        </div>
        <div class="case-grid">{client_cards}</div>
      </section>

      <section class="section all-work" id="all-work" aria-labelledby="all-work-title">
        <div class="section-heading">
          <div>
            <p class="section-tag">The full archive</p>
            <h2 id="all-work-title">Every product, client system, tool, and lab.</h2>
          </div>
          <p>{len(PROJECTS)} selected builds, ordered by product maturity. Projects without a usable public screenshot are listed without an image rather than illustrated with a mockup.</p>
        </div>
        <div class="project-filters" role="group" aria-label="Filter projects">{filter_buttons}</div>
        <div class="project-index">{project_rows}</div>
      </section>
"""


def render_markdown() -> str:
    live = [p for p in PROJECTS if p["category"] == "live" and p.get("featured")]
    client = [p for p in PROJECTS if p["category"] == "client"]
    lines = ["## Selected live products", ""]
    for project in live:
        lines.extend(
            [
                f"### [{project['title']}]({project_link(project)})",
                "",
                f"**{project['eyebrow']}** · {project['status']}",
                "",
                project["summary"],
                "",
                f"Stack: `{'` · `'.join(project.get('stack', []))}`",
                "",
            ]
        )
        if project.get("image"):
            lines.extend([f"![{project['imageAlt']}]({project['image']})", ""])
        links = []
        if project.get("url"):
            links.append(f"[Live]({project['url']})")
        if project.get("repo"):
            links.append(f"[Source]({project['repo']})")
        if project.get("case"):
            links.append(f"[Case study]({project['case']})")
        lines.extend([" · ".join(links), ""])

    lines.extend(["## Client systems", ""])
    for project in client:
        link = project_link(project)
        link_text = f"[{project['title']}]({link})" if link else project["title"]
        lines.extend(
            [
                f"### {link_text}",
                "",
                f"**{project['eyebrow']}** · {project['status']}",
                "",
                project["summary"],
                "",
                f"Stack: `{'` · `'.join(project.get('stack', []))}`",
                "",
            ]
        )
        if project.get("image"):
            lines.extend([f"![{project['imageAlt']}]({project['image']})", ""])
        if link:
            lines.extend([f"[Open project]({link})", ""])
    lines.append("")

    visual_tools = [
        project
        for project in PROJECTS
        if (
            project["category"] in {"ai", "tool"}
            or (project["category"] == "live" and not project.get("featured"))
        )
        and project.get("image")
    ]
    lines.extend(["## Product and tool projects", ""])
    for project in visual_tools:
        link = project_link(project)
        link_text = f"[{project['title']}]({link})" if link else project["title"]
        lines.extend(
            [
                f"### {link_text}",
                "",
                f"**{project['eyebrow']}** · {project['status']}",
                "",
                project["summary"],
                "",
                f"![{project['imageAlt']}]({project['image']})",
                "",
                f"Stack: `{'` · `'.join(project.get('stack', []))}`",
                "",
            ]
        )
        if link:
            lines.extend([f"[Open project]({link})", ""])

    lines.extend(["## Complete project index", "", "| Project | Type | Status | Links |", "|---|---|---|---|"])
    for project in PROJECTS:
        links = []
        if project.get("url"):
            links.append(f"[Live]({project['url']})")
        if project.get("repo"):
            links.append(f"[Source]({project['repo']})")
        if project.get("case"):
            links.append(f"[Case]({project['case']})")
        lines.append(
            f"| **{project['title']}** — {project['summary']} | "
            f"{CATEGORY_LABELS.get(project['category'], project['category'])} | "
            f"{project['status']} | {' · '.join(links) or '—'} |"
        )

    lines.extend(["", "## Public repositories", "", "| Repository | Type | Description |", "|---|---|---|"])
    for repo in sorted(REPOSITORIES, key=lambda item: item["name"].lower()):
        repo_type = "Customized fork" if repo.get("fork") else "Original"
        description = (repo.get("description") or "No description").replace("|", "\\|")
        lines.append(
            f"| [{repo['name']}]({repo['html_url']}) | {repo_type} | {description} |"
        )
    lines.append("")
    return "\n".join(lines)


def replace_region(path: Path, start: str, end: str, content: str) -> None:
    text = path.read_text(encoding="utf-8")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    path.write_text(f"{before}{start}\n{content.strip()}\n{end}{after}", encoding="utf-8")


def main() -> None:
    replace_region(
        ROOT / "index.html",
        "<!-- PROJECTS:START -->",
        "<!-- PROJECTS:END -->",
        render_html(),
    )
    replace_region(
        ROOT / "README.md",
        "<!-- PROJECTS:START -->",
        "<!-- PROJECTS:END -->",
        render_markdown(),
    )
    print(f"Rendered {len(PROJECTS)} projects and {len(REPOSITORIES)} repositories")


if __name__ == "__main__":
    main()
