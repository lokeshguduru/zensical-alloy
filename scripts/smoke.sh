#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-}"
ZENSICAL="${ZENSICAL:-}"
LOG_DIR="${TMPDIR:-/tmp}/zensical-alloy-smoke"

if [[ -z "$PYTHON" ]]; then
  if [[ -x "$ROOT/.venv/bin/python" ]]; then
    PYTHON="$ROOT/.venv/bin/python"
  else
    PYTHON="python"
  fi
fi

if [[ -z "$ZENSICAL" ]]; then
  if [[ -x "$ROOT/.venv/bin/zensical" ]]; then
    ZENSICAL="$ROOT/.venv/bin/zensical"
  else
    ZENSICAL="zensical"
  fi
fi

if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "Missing Python command: $PYTHON" >&2
  exit 1
fi

if ! command -v "$ZENSICAL" >/dev/null 2>&1; then
  echo "Missing Zensical command: $ZENSICAL" >&2
  echo "Install the package first, or pass ZENSICAL=/path/to/zensical." >&2
  exit 1
fi

if [[ "$PYTHON" == */* ]]; then
  PYTHON="$(cd "$(dirname "$PYTHON")" && pwd)/$(basename "$PYTHON")"
fi

if [[ "$ZENSICAL" == */* ]]; then
  ZENSICAL="$(cd "$(dirname "$ZENSICAL")" && pwd)/$(basename "$ZENSICAL")"
fi

mkdir -p "$LOG_DIR"

echo "==> Bundling Alloy CSS"
"$PYTHON" "$ROOT/scripts/bundle-css.py"

echo "==> Checking version cache busts"
"$ROOT/scripts/bump-version.py" --check

run_build() {
  local name="$1"
  local dir="$2"
  shift 2
  local log="$LOG_DIR/$name.log"

  echo "==> Building $name"
  if (cd "$dir" && "$ZENSICAL" build "$@") >"$log" 2>&1; then
    local summary
    summary="$(grep -E "No issues found|[0-9]+ issues found|Build finished" "$log" | tail -n 3 || true)"
    if [[ -n "$summary" ]]; then
      echo "$summary"
    else
      echo "Build finished; log: $log"
    fi
  else
    echo "Build failed; log: $log" >&2
    tail -n 40 "$log" >&2
    exit 1
  fi
}

run_build "package-example" "$ROOT/examples/zensical-toml"

echo "==> Checking accent validation fixture"
"$PYTHON" "$ROOT/scripts/check-accent-validation.py"

run_build "mkdocs-yml-example" "$ROOT/examples/mkdocs-yml"

if [[ -d "$ROOT/examples/mkdocs-variants" ]]; then
  while IFS= read -r -d '' config; do
    fixture_dir="$(dirname "$config")"
    fixture_name="$(basename "$fixture_dir")"
    run_build "mkdocs-variant-$fixture_name" "$fixture_dir"
  done < <(find "$ROOT/examples/mkdocs-variants" -mindepth 2 -maxdepth 2 -name mkdocs.yml -print0 | sort -z)
fi

if [[ -d "$ROOT/examples/real-world-smoke" ]]; then
  while IFS= read -r -d '' config; do
    fixture_dir="$(dirname "$config")"
    fixture_name="$(basename "$fixture_dir")"
    run_build "real-world-$fixture_name" "$fixture_dir"
  done < <(find "$ROOT/examples/real-world-smoke" -mindepth 2 -maxdepth 2 -name mkdocs.yml -print0 | sort -z)
fi

if [[ -f "$ROOT/../zensical-docs/mkdocs.alloy.yml" ]]; then
  run_build "zensical-docs" "$ROOT/../zensical-docs" -f mkdocs.alloy.yml
fi

if [[ -f "/private/tmp/fastapi-theme-smoke2/docs/en/mkdocs.alloy-smoke.yml" ]]; then
  run_build "fastapi" "/private/tmp/fastapi-theme-smoke2/docs/en" -f mkdocs.alloy-smoke.yml
fi

if [[ -f "/private/tmp/material-theme-smoke/mkdocs.alloy-smoke.yml" ]]; then
  run_build "material" "/private/tmp/material-theme-smoke" -f mkdocs.alloy-smoke.yml
fi

echo "Smoke builds complete. Logs: $LOG_DIR"
