"""Core workflow for Proteomics Normalizer by Red@."""

PROJECT_NAME = "Proteomics Normalizer"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
