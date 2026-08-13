import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRY = json.loads((ROOT / "catalog" / "plugins.json").read_text(
    encoding="utf-8"))["plugins"][0]


def test_catalog_identifies_the_real_repository_and_release():
    assert ENTRY["repository"].endswith("/rom-hub-cdromance")
    assert ENTRY["install"] == ENTRY["repository"]
    assert ENTRY["ref"] in ENTRY["download"]


def test_catalog_does_not_claim_a_standalone_provider():
    assert ENTRY["capabilities"] == []
    assert ENTRY["search_only"] is True
    assert not (ROOT / "manifest.toml").exists()


def test_catalog_points_to_the_browser_assisted_path():
    assert "BROWSER-ASSISTED" in ENTRY["description"]
    assert "Capture" in ENTRY["comments"]
