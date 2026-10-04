"""
Linguistic Diversity & Student Persona Augmentation Module for Re:Learn
Simulates authentic Class 9 & 10 Indian student communication styles:
1. Vernacular / CBSE Indian English (conversational idioms, "sir", "na", "bhai", "obviously")
2. Shorthand & Texting (bcz, coz, cant, diff, u, img, vel, acc)
3. Terse & Formulaic (direct declarations, equation-first)
4. Intuitive / Hesitant / Rambling (first-person reasoning, conversational justification)
5. Typographic Noise (minor realistic spelling variations)
6. Realistic Abstention / Negatives ("idk", "skip", "forgot formula", "guess")
"""

import random
import re

INDIAN_ENGLISH_PREFIXES = [
    "sir according to me, ",
    "sir ",
    "actually ",
    "obviously ",
    "bhai ",
    "as per rule, ",
    "in my opinion, ",
    "clearly, ",
    "sir in this case ",
    "arre sir ",
    "bhai listen, ",
    "bro honestly, ",
    "wait sir, ",
    "from what I studied, ",
    ""
]

INDIAN_ENGLISH_SUFFIXES = [
    " na",
    " sir",
    " only",
    " obviously",
    " na sir",
    " basically",
    " pakka",
    " 100%",
    ""
]

SLANG_REPLACEMENTS = {
    r"\bbecause\b": ["bcz", "coz", "bcuz", "since", "as"],
    r"\bcannot\b": ["cant", "cannot", "can't"],
    r"\bcan not\b": ["cant", "cannot"],
    r"\bdoes not\b": ["doesnt", "doesn't", "dont"],
    r"\bdo not\b": ["dont", "don't"],
    r"\bimage\b": ["img", "image", "picture"],
    r"\bfocal length\b": ["focal len", "f", "focus length", "focal length"],
    r"\bcurrent\b": ["curnt", "current", "I"],
    r"\bresistance\b": ["res", "resistance", "R"],
    r"\bvoltage\b": ["volt", "voltage", "potential diff", "V"],
    r"\bvelocity\b": ["vel", "velocity", "v", "speed"],
    r"\bacceleration\b": ["acc", "acceleration", "a"],
    r"\brefraction\b": ["refraction", "refrction", "bending"],
    r"\breflection\b": ["reflection", "reflction", "bouncing"],
    r"\bcompletely\b": ["fully", "completely", "totally", "100%"],
    r"\bapproximately\b": ["approx", "around", "nearly"],
    r"\byou\b": ["u", "you"],
    r"\bplease\b": ["pls", "please"],
    r"\bthrough\b": ["thru", "through"],
    r"\bdistance\b": ["dist", "distance"],
    r"\bgravitational\b": ["grav", "gravity", "gravitational"],
    r"\bperpendicular\b": ["perp", "at 90 deg", "perpendicular"],
    r"\bstraight\b": ["str", "straight"]
}

TYPO_PROBABILITIES = {
    "disappears": ["dissapears", "disapears", "disappears"],
    "decreases": ["decreeses", "decreass", "decreases"],
    "increases": ["increeses", "increass", "increases"],
    "half": ["halve", "half"],
    "parallel": ["paralel", "parallel"],
    "separate": ["seperate", "separate"],
    "deflection": ["deflecion", "deflection"],
    "resistance": ["resistence", "resistance"]
}

UNSURE_STUDENT_RESPONSES = [
    "sir I don't know this formula, please explain",
    "idk forgot the chapter formulas",
    "skip this question for now",
    "not sure sir, maybe option A or B?",
    "haven't studied this topic yet",
    "random guess, not confident at all",
    "pass, question seems tricky",
    "sir can you give a hint?",
    "idk maybe it doubles or halves?",
    "no idea honestly",
    "sir please tell the correct steps",
    "confused between current and voltage here",
    "skip",
    "idk"
]

def apply_vernacular_cbse(text, rng=None):
    r = rng if rng else random
    prefix = r.choice(INDIAN_ENGLISH_PREFIXES)
    suffix = r.choice(INDIAN_ENGLISH_SUFFIXES)
    res = prefix + text[0].lower() + text[1:]
    res = res.rstrip(".") + suffix + "."
    return res.strip()

def apply_shorthand_texting(text, rng=None):
    r = rng if rng else random
    res = text
    for pattern, repls in SLANG_REPLACEMENTS.items():
        if r.random() < 0.6:
            res = re.sub(pattern, r.choice(repls), res, flags=re.IGNORECASE)
    # lowercase sometimes
    if r.random() < 0.4:
        res = res.lower()
    return res.strip()

def apply_terse_formulaic(text, rng=None):
    r = rng if rng else random
    # Extract core clauses or make it direct
    res = text
    res = res.replace("The reason is that ", "")
    res = res.replace("We know that ", "")
    res = res.replace("According to the theory, ", "")
    res = res.replace("Because of this, ", "=> ")
    res = res.replace("therefore ", "=> ")
    res = res.replace("hence ", "=> ")
    return res.strip()

def apply_intuitive_rambling(text, rng=None):
    r = rng if rng else random
    openers = [
        "I feel like ",
        "Basically what happens is ",
        "From what I understood, ",
        "If you think about it practically, ",
        "My intuition says "
    ]
    return r.choice(openers) + text[0].lower() + text[1:]

def apply_typo_noise(text, rng=None):
    r = rng if rng else random
    res = text
    for word, typos in TYPO_PROBABILITIES.items():
        if word in res and r.random() < 0.5:
            res = res.replace(word, r.choice(typos))
    return res

def augment_student_response(text, persona_id, seed=None):
    """
    persona_id:
      0: Clean Academic / Textbook (as is)
      1: Indian Vernacular / CBSE English
      2: Shorthand / Texting
      3: Terse / Direct
      4: Intuitive / Rambling
      5: Vernacular + Shorthand blend
    """
    rng = random.Random(seed) if seed is not None else random
    if persona_id == 0:
        return text
    elif persona_id == 1:
        return apply_vernacular_cbse(text, rng)
    elif persona_id == 2:
        return apply_shorthand_texting(text, rng)
    elif persona_id == 3:
        return apply_terse_formulaic(text, rng)
    elif persona_id == 4:
        return apply_intuitive_rambling(text, rng)
    elif persona_id == 5:
        step1 = apply_vernacular_cbse(text, rng)
        step2 = apply_shorthand_texting(step1, rng)
        return apply_typo_noise(step2, rng)
    return text
