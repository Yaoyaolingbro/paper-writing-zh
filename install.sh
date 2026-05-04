#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_DIR="${CODEX_SKILLS_DIR:-$HOME/.agents/skills}"

usage() {
  cat <<'USAGE'
Install paper-writing-zh Codex skills.

Usage:
  ./install.sh [--dry-run] [--dest DIR]

Environment:
  CODEX_SKILLS_DIR  Override destination directory. Defaults to ~/.agents/skills.

Examples:
  ./install.sh
  ./install.sh --dry-run
  ./install.sh --dest "$HOME/.codex/skills"
USAGE
}

DRY_RUN=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --dest)
      if [[ $# -lt 2 ]]; then
        echo "error: --dest requires a directory" >&2
        exit 2
      fi
      DEST_DIR="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "error: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

skill_dirs=(
  "$ROOT_DIR/ai-paper-writing-zh"
  "$ROOT_DIR/reference-verifier"
)

for skill_dir in "${skill_dirs[@]}"; do
  if [[ ! -f "$skill_dir/SKILL.md" ]]; then
    echo "error: missing skill entry: $skill_dir/SKILL.md" >&2
    exit 1
  fi
done

if [[ ${#skill_dirs[@]} -eq 0 ]]; then
  echo "error: no skills configured for installation" >&2
  exit 1
fi

echo "Destination: $DEST_DIR"

if [[ "$DRY_RUN" -eq 0 ]]; then
  mkdir -p "$DEST_DIR"
fi

for skill_dir in "${skill_dirs[@]}"; do
  skill_name="$(basename "$skill_dir")"
  target_dir="$DEST_DIR/$skill_name"

  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "Would install: $skill_name -> $target_dir"
    continue
  fi

  mkdir -p "$target_dir"
  rsync -a --delete \
    --exclude '.git' \
    --exclude '.DS_Store' \
    "$skill_dir/" "$target_dir/"
  echo "Installed: $skill_name -> $target_dir"
done

echo "Done."
