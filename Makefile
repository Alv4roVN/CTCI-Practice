.PHONY: save reset

# Snapshot a solved problem into solutions/, mirroring its category path.
# Usage: make save FILE=strings_and_hashing/is_unique.py
#        make save FILE=is_unique
save:
	@bash scripts/save_solution.sh $(FILE)

# Reset problem(s) back to their NotImplementedError stub. Prompts for
# confirmation first -- save anything you want to keep before running this.
# Usage: make reset TARGET=all
#        make reset TARGET=strings_and_hashing
#        make reset TARGET=strings_and_hashing/is_unique.py
#        make reset TARGET=is_unique
reset:
	@bash scripts/reset_solution.sh $(TARGET)
