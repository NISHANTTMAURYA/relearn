# Builder script to assemble generate_complete_curriculum_datasets.py with all 25 curriculum families and 1000 sequences
import json
import os

target_file = r"d:\relearn\dataset\scripts\generate_complete_curriculum_datasets.py"

header = '''import json
import csv
import os
import random
import string

random.seed(42)

def safe_format(template_str, p):
    if not template_str or not isinstance(template_str, str) or "{" not in template_str:
        return template_str
    try:
        formatter = string.Formatter()
        fields = [fname for _, fname, _, _ in formatter.parse(template_str) if fname is not None]
        if not fields:
            return template_str
        
        p0 = p[0] if len(p) >= 1 else 10
        p1 = p[1] if len(p) >= 2 else 5
        p2 = p[2] if len(p) >= 3 else 2
        
        calc_div = p0 // p1 if p1 != 0 and p0 % p1 == 0 else round(p0 / p1, 1) if p1 != 0 else p0
        calc_mul = p0 * p1
        
        kwargs_pool = {
            "u": p0, "f": p1 if len(p) >= 2 else p0, "fp": p0,
            "d": p0, "t": p1, "v": p0, "m": p0, "M": p0, "h": p2,
            "V": p0, "I": p1, "R": p2 if len(p) >= 3 else p1,
            "misc_val": calc_mul,
            "cor_val": calc_div,
            "div_val": calc_div,
            "slip": round(p0 * 1.5, 1),
            "f_val": calc_mul
        }
        sub_kwargs = {k: kwargs_pool.get(k, 0) for k in fields}
        return template_str.format(**sub_kwargs)
    except Exception:
        return template_str

BASE_DIR = r"d:\\relearn\\dataset"
INDIV_DIR = os.path.join(BASE_DIR, "individual_response_dataset")
SEQ_DIR = os.path.join(BASE_DIR, "sequence_dataset")

os.makedirs(INDIV_DIR, exist_ok=True)
os.makedirs(SEQ_DIR, exist_ok=True)
'''

print("Builder initialized...")
