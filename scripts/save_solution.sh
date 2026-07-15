#!/usr/bin/env bash
# Copy a solved problem's source file into solutions/, mirroring its
# category path (e.g. strings_and_hashing/is_unique.py ->
# solutions/strings_and_hashing/is_unique.py). solutions/ is gitignored,
# so this is just a private snapshot you can keep before resetting a
# stub back to NotImplementedError to practice it again.
set -euo pipefail

usage() {
    echo "Usage: $(basename "$0") <problem-file-or-name>" >&2
    echo "  e.g. $(basename "$0") strings_and_hashing/is_unique.py" >&2
    echo "       $(basename "$0") is_unique" >&2
    exit 1
}

[ $# -eq 1 ] || usage

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

input="$1"
[[ "$input" == *.py ]] || input="${input}.py"

if [ -f "$input" ]; then
    src="$input"
else
    # Bare problem name: search category directories for a matching file.
    matches=()
    while IFS= read -r -d '' f; do
        matches+=("${f#./}")
    done < <(find . -mindepth 2 -maxdepth 2 -name "$(basename "$input")" \
                 -not -path "./solutions/*" -not -path "./tests/*" -print0)

    case "${#matches[@]}" in
        0)
            echo "error: no problem file found matching '$1'" >&2
            exit 1
            ;;
        1)
            src="${matches[0]}"
            ;;
        *)
            echo "error: '$1' is ambiguous, matched:" >&2
            printf '  %s\n' "${matches[@]}" >&2
            exit 1
            ;;
    esac
fi

dest="solutions/$src"
mkdir -p "$(dirname "$dest")"
cp "$src" "$dest"

echo "saved $src -> $dest"
