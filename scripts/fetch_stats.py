import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "thomasvandongen.dev", **(headers or {})})
    time.sleep(1)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == 4:
                raise
            time.sleep(2 ** attempt)


def stars(repo):
    headers = {}
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    return get(f"https://api.github.com/repos/{repo}", headers)["stargazers_count"]


def pypi_downloads(package):
    key = os.environ.get("PEPY_API_KEY")
    if not key:
        return None
    return get(f"https://api.pepy.tech/api/v2/projects/{package}", {"X-API-Key": key})["total_downloads"]


def crate_downloads(crate):
    return get(f"https://crates.io/api/v1/crates/{crate}")["crate"]["downloads"]


def main():
    projects = yaml.safe_load((ROOT / "data" / "projects.yaml").read_text())
    stats_path = ROOT / "data" / "stats.json"
    stats = json.loads(stats_path.read_text()) if stats_path.exists() else {}
    for project in projects:
        entry = {}
        try:
            if repo := project.get("repo"):
                entry["stars"] = stars(repo)
            downloads = None
            if pypi := project.get("pypi"):
                downloads = pypi_downloads(pypi)
            elif crate := project.get("crate"):
                downloads = crate_downloads(crate)
            if downloads is not None:
                entry["downloads"] = downloads
        except Exception as exc:
            print(f"{project['name']}: {exc}", file=sys.stderr)
        if entry:
            stats[project["name"]] = {**stats.get(project["name"], {}), **entry}
    stats_path.write_text(json.dumps(stats, indent=2) + "\n")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
