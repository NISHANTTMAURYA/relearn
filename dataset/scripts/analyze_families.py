import sys
sys.path.insert(0, r"d:\relearn")
from dataset.scripts.curriculum_families import CURRICULUM_FAMILIES

print(f"Total families: {len(CURRICULUM_FAMILIES)}")
misc_set = set()
for i, f in enumerate(CURRICULUM_FAMILIES):
    misc_set.add(f["target_misc"])
    print(f"Fam {i:02d}: {f['family'][:35]:<35} | Misc: {f['target_misc'][:40]:<40} | MiscP: {len(f['misc_phrasings'])} | CorP: {len(f['correct_phrasings'])} | Stems: {len(f['stem_templates'])}")
print(f"\nTotal distinct target misconceptions: {len(misc_set)}")
