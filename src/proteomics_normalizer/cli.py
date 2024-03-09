import argparse
from proteomics_normalizer.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalization and export helpers for proteomics abundance tables.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
