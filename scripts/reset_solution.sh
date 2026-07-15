#!/usr/bin/env bash
# Reset one or more problems back to their NotImplementedError stub,
# discarding whatever is currently in the working file. Restores from
# stubs/, which mirrors the same category structure as the repo root.
# Prompts for confirmation before doing anything, since this is
# destructive (see scripts/save_solution.sh / `make save` to snapshot
# a solution first).
set -euo pipefail

usage() {
    echo "Usage: $(basename "$0") <all|category|problem-file-or-name>" >&2
    echo "  e.g. $(basename "$0") all" >&2
    echo "       $(basename "$0") strings_and_hashing" >&2
    echo "       $(basename "$0") strings_and_hashing/is_unique.py" >&2
    echo "       $(basename "$0") is_unique" >&2
    exit 1
}

[ $# -eq 1 ] || usage

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if [ ! -d stubs ]; then
    echo "error: stubs/ directory not found -- nothing to reset from" >&2
    exit 1
fi

target="$1"
targets=()

if [ "$target" = "all" ]; then
    while IFS= read -r -d '' f; do
        targets+=("${f#stubs/}")
    done < <(find stubs -type f -name '*.py' ! -name '__init__.py' -print0 | sort -z)
elif [ -d "stubs/$target" ]; then
    while IFS= read -r -d '' f; do
        targets+=("${f#stubs/}")
    done < <(find "stubs/$target" -type f -name '*.py' ! -name '__init__.py' -print0 | sort -z)
else
    input="$target"
    [[ "$input" == *.py ]] || input="${input}.py"

    if [ -f "stubs/$input" ]; then
        targets+=("$input")
    else
        matches=()
        while IFS= read -r -d '' f; do
            matches+=("${f#stubs/}")
        done < <(find stubs -mindepth 2 -maxdepth 2 -name "$(basename "$input")" -print0)

        case "${#matches[@]}" in
            0)
                echo "error: no problem found matching '$target'" >&2
                exit 1
                ;;
            1)
                targets+=("${matches[0]}")
                ;;
            *)
                echo "error: '$target' is ambiguous, matched:" >&2
                printf '  %s\n' "${matches[@]}" >&2
                exit 1
                ;;
        esac
    fi
fi

if [ ${#targets[@]} -eq 0 ]; then
    echo "error: nothing matched '$target'" >&2
    exit 1
fi

echo "This will reset the following problem(s) to NotImplementedError,"
echo "discarding whatever is currently in each file:"
printf '  %s\n' "${targets[@]}"
echo

read -r -p "Have you saved any solutions you want to keep (make save)? [y/N] " reply
case "$reply" in
    [yY]|[yY][eE][sS]) ;;
    *)
        echo "Aborted. Nothing was reset."
        exit 1
        ;;
esac

for t in "${targets[@]}"; do
    mkdir -p "$(dirname "$t")"
    cp "stubs/$t" "$t"
    echo "reset $t"
done
