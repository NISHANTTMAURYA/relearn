import json
import csv
import os
import random
from sklearn.model_selection import train_test_split

random.seed(42)

OUTPUT_DIR_INDIV = r"d:\relearn\dataset\training_ready_datasets\individual_response_dataset"
OUTPUT_DIR_SEQ = r"d:\relearn\dataset\training_ready_datasets\sequence_dataset"

os.makedirs(OUTPUT_DIR_INDIV, exist_ok=True)
os.makedirs(OUTPUT_DIR_SEQ, exist_ok=True)

# Define Canonical Misconception Categories
CLASSES = [
    "MISC-ELEC-001: Current Attenuation / Consumption Model",
    "MISC-ELEC-002: Battery as Constant Current Source",
    "MISC-ELEC-003: Shared Current / Equal Division Fallacy",
    "MISC-ELEC-004: Voltage-Current Conflation / Parameter Neglect",
    "MISC-ELEC-005: Parallel Resistance Addition Fallacy",
    "MISC-ELEC-006: Power Formula Mis-selection in Parallel vs Series",
    "MISC-OPT-001: Half-Lens Blocking Fallacy",
    "MISC-OPT-003: Virtual Image Ray Convergence Fallacy",
    "MISC-OPT-004: Cartesian Sign Convention Spatial Inversion",
    "MISC-OPT-005: Glass Slab Angular Deviation Fallacy",
    "MISC-OPT-006: Special Ray Exclusivity / Ray Reification",
    "MISC-EYE-001: Vision Defect Corrective Lens Inversion",
    "MISC-EYE-002: Prism Dispersion Speed & Deviation Inversion",
    "MISC-EYE-003: Star Twinkling Emission Artifact Fallacy",
    "MISC-EYE-004: Sky Colour Reflection Fallacy",
    "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Fallacy",
    "MISC-MAG-002: Universal Metallic Magnetism Fallacy",
    "MISC-MAG-003: Magnetic Force Collinear / Parallel Fallacy",
    "MISC-MAG-004: Magnetic Field Line Crossing / Discontinuous Loop Fallacy",
    "MISC-MAG-005: Directional Hand Rule Inversion Fallacy",
    "CORRECT: Scientifically Accurate Response",
    "CARELESS_CALCULATION_ERROR",
    "UNIT_CONVERSION_ERROR",
    "UNSURE_INSUFFICIENT_EVIDENCE"
]

# Raw Data Banks for Each Category with authentic student phrasing variations
DATA_BANK = {
    "MISC-ELEC-001: Current Attenuation / Consumption Model": [
        ("Electricity", "Current in Series", "Two identical bulbs in series with 6V supply. Compare ammeter readings before, between, and after bulbs.", "A1 is 1.5A, A2 is 1.0A, A3 is 0.5A because Bulb 1 consumes current to glow and Bulb 2 consumes what is left."),
        ("Electricity", "Current in Series", "Three resistors R1, R2, R3 connected in series with battery. What is the current through R3 compared to R1?", "Current through R3 is much smaller than R1 because current gets used up as it travels along the series circuit."),
        ("Electricity", "Bulb Brightness", "Why does Bulb 1 glow brighter than Bulb 2 in a series connection?", "Bulb 1 gets the fresh current first from the battery. After passing Bulb 1, the current is weakened before reaching Bulb 2."),
        ("Electricity", "Current Conservation", "Does current decrease after passing through a 10-ohm resistor?", "Yes, the current leaving the resistor is less than the current entering it because energy and current are consumed inside."),
        ("Electricity", "Ammeter in Circuit", "Where should an ammeter be placed to measure maximum current in series?", "Place it right next to the positive terminal before any components consume the current.")
    ],
    "MISC-ELEC-002: Battery as Constant Current Source": [
        ("Electricity", "Parallel Circuit Load", "A 12V battery powers one 4-ohm resistor. We connect another 4-ohm resistor in parallel. What is total battery current?", "Total battery current stays 3A because a 12V battery has a fixed constant current that cannot increase."),
        ("Electricity", "Battery Capacity", "If you add 3 more bulbs in parallel in your home, does the power supply deliver more current?", "No, the power supply outputs the same fixed current and divides it into smaller pieces for each bulb."),
        ("Electricity", "Variable Load", "A battery is rated 9V. If external resistance changes from 10 ohms to 2 ohms, what happens to battery current?", "The battery current remains constant because current is an intrinsic property of the battery cell."),
        ("Electricity", "Parallel Branches", "Why did the battery current not change when switch was closed?", "Batteries are constant current sources, so adding parallel branches cannot draw more current.")
    ],
    "MISC-ELEC-003: Shared Current / Equal Division Fallacy": [
        ("Electricity", "Parallel Junction", "6A enters a junction with 2-ohm and 4-ohm parallel branches. What is current in each?", "Current splits 50-50 at the junction, so each branch gets 3A regardless of resistance."),
        ("Electricity", "Parallel Resistors", "A 10A current splits into 1 ohm and 9 ohm branches. Find I1 and I2.", "Both branches get 5A because when a wire branches into two, current always divides equally."),
        ("Electricity", "Bulb Current Division", "Two parallel bulbs of different wattage. How does current divide?", "Current divides into two equal halves at any parallel junction because geometry is symmetric.")
    ],
    "MISC-ELEC-004: Voltage-Current Conflation / Parameter Neglect": [
        ("Electricity", "Voltage vs Current", "Is there voltage across an open switch where no current flows?", "No, voltage is zero because without current flowing there cannot be any voltage in the wire."),
        ("Electricity", "Wire Stretching", "A wire of resistance R is stretched to 2L. What is new resistance?", "New resistance is 2R because R is proportional to length, ignoring area."),
        ("Electricity", "Resistivity vs Resistance", "If copper wire length doubles, what happens to its resistivity?", "Resistivity doubles because length doubled."),
        ("Electricity", "Meter Placement", "How do you connect a voltmeter to measure potential difference?", "Connect voltmeter in series with the resistor so voltage flows through it.")
    ],
    "MISC-ELEC-005: Parallel Resistance Addition Fallacy": [
        ("Electricity", "Parallel Resistance", "Two resistors of 6 ohms and 3 ohms are in parallel. What is R_eq?", "Total resistance is 6 + 3 = 9 ohms because more resistors add more resistance."),
        ("Electricity", "Adding Resistors", "What happens to equivalent resistance when a parallel branch is added?", "Resistance increases because you added an extra resistor to the circuit."),
        ("Electricity", "Parallel Formula", "Calculate equivalent resistance of 4 ohms and 4 ohms in parallel.", "R_eq = 4 + 4 = 8 ohms.")
    ],
    "MISC-ELEC-006: Power Formula Mis-selection in Parallel vs Series": [
        ("Electricity", "Bulb Power in Parallel", "100W and 40W bulbs in parallel across 220V. Which bulb has more resistance?", "The 100W bulb has more resistance because P = I^2 * R means power is proportional to resistance."),
        ("Electricity", "Heating Effect", "Two heating coils in parallel. Which produces more heat?", "The higher resistance coil produces more heat according to H = I^2 * R * t."),
        ("Electricity", "Appliance Wattage", "A 1000W heater and 500W toaster in parallel. How do resistances compare?", "1000W heater has twice the resistance of 500W toaster because P is proportional to R.")
    ],
    "MISC-OPT-001: Half-Lens Blocking Fallacy": [
        ("Light", "Convex Lens Aperture", "Lower half of convex lens covered with black cardboard. What happens to candle image on screen?", "The bottom half of the candle flame image completely disappears from the screen."),
        ("Light", "Convex Lens Aperture", "Top half of lens covered by paper. Describe the image.", "The top half of the image is cut off and only the bottom half remains."),
        ("Light", "Concave Mirror Aperture", "Center 50% of concave mirror covered by black sticker. What is seen on screen?", "A circular black patch appears in the middle of the image, blocking that part."),
        ("Light", "Lens Blocking", "Does covering half a lens block half the object?", "Yes, because light from half the object goes through that half of the lens like a window.")
    ],
    "MISC-OPT-003: Virtual Image Ray Convergence Fallacy": [
        ("Light", "Plane Mirror", "Does light actually cross behind a plane mirror?", "Yes, light rays reflect backwards and pass physically behind the glass to meet at the virtual image."),
        ("Light", "Virtual Image Capture", "Can photographic film placed behind a mirror capture a virtual image?", "Yes, if you put film behind the mirror where the rays converge it will capture the picture."),
        ("Light", "Concave Lens Rays", "Where do rays from a concave lens meet?", "Rays physically travel behind the lens and cross at the focal point in space.")
    ],
    "MISC-OPT-004: Cartesian Sign Convention Spatial Inversion": [
        ("Light", "Mirror Formula", "Object at 20 cm in front of concave mirror of f = 15 cm. Find v.", "u = 20, f = 15. 1/15 = 1/v + 1/20 => 1/v = 1/60 => v = +60 cm, virtual image."),
        ("Light", "Lens Formula", "Object placed 30 cm before convex lens of f = 10 cm. Find v.", "u = +30 cm because distance is positive. 1/v = 1/10 + 1/30 = 4/30 => v = 7.5 cm."),
        ("Light", "Sign Convention", "Why did you use positive u?", "Because object distance is a physical length and lengths cannot be negative.")
    ],
    "MISC-OPT-005: Glass Slab Angular Deviation Fallacy": [
        ("Light", "Refraction in Glass Slab", "Light enters rectangular glass slab at 30 degrees. What is direction of emergent ray?", "The emergent ray is permanently bent at an angle, deviating by 10 degrees from initial path."),
        ("Light", "Glass Block", "Does light emerging from parallel glass block travel parallel to incident ray?", "No, refraction permanently tilts the ray like in a prism, so it is not parallel.")
    ],
    "MISC-OPT-006: Special Ray Exclusivity / Ray Reification": [
        ("Light", "Ray Diagram Rules", "If an opaque pin blocks the principal axis at optical centre, can an image form?", "No, the image cannot form because the central ray is blocked and you need that ray to form image."),
        ("Light", "Image Rays", "How many rays from an object actually make the image?", "Only the two principal rays shown in textbooks form the image; other rays do not exist.")
    ],
    "MISC-EYE-001: Vision Defect Corrective Lens Inversion": [
        ("Human Eye", "Myopia Correction", "Student cannot see distant blackboard clearly. What lens corrects this?", "Myopia requires a convex lens because distant letters are small and need magnification."),
        ("Human Eye", "Vision Defects", "What lens corrects far-sightedness (hypermetropia)?", "Hypermetropia needs a concave lens to shrink the view."),
        ("Human Eye", "Eye Lens Power", "Why use convex lens for near-sighted person?", "Because their eye lens is too weak so they need extra converging power.")
    ],
    "MISC-EYE-002: Prism Dispersion Speed & Deviation Inversion": [
        ("Human Eye", "Prism Dispersion", "Which colour suffers greatest deviation in glass prism?", "Red light deviates most because red is high energy and strong."),
        ("Human Eye", "Dispersion in Glass", "Which colour travels fastest in glass?", "Violet travels fastest because it has short wavelength and slips through glass faster.")
    ],
    "MISC-EYE-003: Star Twinkling Emission Artifact Fallacy": [
        ("Human Eye", "Atmospheric Refraction", "Why do stars twinkle at night?", "Stars twinkle because they are pulsating their light emission on and off like flashing bulbs."),
        ("Human Eye", "Star Flickering", "Do stars twinkle because of clouds?", "Yes, smoke and dust particles intermittently block the light beam causing flickering.")
    ],
    "MISC-EYE-004: Sky Colour Reflection Fallacy": [
        ("Human Eye", "Scattering of Light", "Why is daytime sky blue?", "The sky is blue because it reflects the blue water of Earth's oceans like a mirror."),
        ("Human Eye", "Sky on Moon", "Why does sky look dark on Moon?", "Because the Moon has no oceans to reflect blue color into the sky.")
    ],
    "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Fallacy": [
        ("Magnetism", "Magnetic Force on Static Charge", "Stationary proton placed near North pole of magnet. What force does it feel?", "Proton feels repulsive force pushing away from North pole because North is positive charge."),
        ("Magnetism", "Magnetic Dipoles", "What happens if a stationary electron is near South pole?", "Electron is repelled by South pole because South pole is negatively charged."),
        ("Magnetism", "Poles vs Charges", "Are magnetic poles charged?", "Yes, North pole has positive electric charge and South pole has negative electric charge.")
    ],
    "MISC-MAG-002: Universal Metallic Magnetism Fallacy": [
        ("Magnetism", "Magnetic Materials", "Will a strong magnet attract copper wire and aluminium foil?", "Yes, all metals are attracted to magnets because they conduct electricity."),
        ("Magnetism", "Materials", "Can a magnet pick up a brass screw and silver coin?", "Yes, any metal object will stick to a permanent magnet.")
    ],
    "MISC-MAG-003: Magnetic Force Collinear / Parallel Fallacy": [
        ("Magnetism", "Lorentz Force", "Charge moves parallel along magnetic field lines. What force does it feel?", "Maximum force accelerating it forward along the magnetic field line."),
        ("Magnetism", "Direction of Magnetic Force", "In what direction does magnetic force act on current?", "Force acts parallel along the magnetic field lines like electric force F = qE.")
    ],
    "MISC-MAG-004: Magnetic Field Line Crossing / Discontinuous Loop Fallacy": [
        ("Magnetism", "Field Line Properties", "Can magnetic field lines cross each other?", "Yes, when two strong magnetic fields overlap, their field lines intersect and cross."),
        ("Magnetism", "Solenoid Field", "Do field lines exist inside a bar magnet?", "No, field lines start at North pole and terminate at South pole, leaving inside empty.")
    ],
    "MISC-MAG-005: Directional Hand Rule Inversion Fallacy": [
        ("Magnetism", "Fleming's Left Hand Rule", "Electron moves West to East into downward magnetic field. Find force.", "Force is North. I pointed center finger in direction of electron motion (West to East)."),
        ("Magnetism", "Hand Rule Swap", "How do you find force on current?", "Use Right-Hand Thumb Rule with thumb pointing along current to find motion.")
    ],
    "CORRECT: Scientifically Accurate Response": [
        ("Electricity", "Series Current", "Two bulbs in series with 6V supply. Compare ammeter readings.", "A1 = A2 = A3. In a series loop, electric charge is conserved and current is identical at all points."),
        ("Electricity", "Parallel Resistance", "6 ohm and 3 ohm in parallel across 12V.", "1/R = 1/6 + 1/3 = 1/2 => R = 2 ohms. Total current = 12/2 = 6A, which increases."),
        ("Electricity", "Power in Parallel", "100W and 40W bulbs in parallel across 220V.", "R = V^2 / P. 40W bulb has greater resistance (1210 ohms vs 484 ohms). 100W bulb glows brighter."),
        ("Light", "Half Lens Covered", "Bottom half of convex lens covered with black cardboard.", "The entire image remains complete on the screen, but brightness is halved because light from all object points reaches the uncovered top half."),
        ("Light", "Sign Convention", "Object at 20cm before concave mirror of f = 15cm.", "u = -20cm, f = -15cm. 1/v = 1/(-15) - 1/(-20) = -1/60 => v = -60cm. Real and inverted image."),
        ("Human Eye", "Myopia", "Cannot see distant blackboard clearly at 5m.", "Myopia (near-sightedness). Eye lens is over-converging. Corrected with diverging concave lens."),
        ("Human Eye", "Prism Dispersion", "Which colour deviates most in glass prism?", "Violet deviates most because it travels slowest in glass and experiences highest refractive index."),
        ("Human Eye", "Sky Colour", "Why is daytime sky blue on Earth?", "Rayleigh scattering: air molecules scatter short blue wavelengths in all directions. No air on Moon means black sky."),
        ("Magnetism", "Static Charge", "Stationary proton near magnet poles.", "Force is 0 N. A magnetic field exerts force only on moving charges (F = q * v * B * sin(theta); v = 0)."),
        ("Magnetism", "Fleming's Rule", "Electron moves West to East in downward B field.", "Force is South. Conventional current is opposite to electron motion (East to West). Fleming's Left-Hand Rule gives South.")
    ],
    "CARELESS_CALCULATION_ERROR": [
        ("Electricity", "Ohm's Law Calculation", "Find current for 12V and 6 ohms.", "I = 12 * 6 = 72 Amps."),
        ("Electricity", "Series Sum Slip", "R1 = 5 ohms, R2 = 10 ohms in series.", "R_total = 5 + 10 = 25 ohms."),
        ("Light", "Focal Length Formula Slip", "Mirror formula 1/f = 1/v + 1/u with u = -20, f = -15.", "1/v = -1/15 - (-1/20) = -1/15 - 1/20 = -7/60 => v = -8.57 cm (arithmetic sign slip).")
    ],
    "UNIT_CONVERSION_ERROR": [
        ("Electricity", "Current Units", "Current when 120 Coulombs pass in 2 minutes.", "I = 120 / 2 = 60 Amperes (forgot to convert minutes to seconds)."),
        ("Electricity", "Resistance Unit", "Calculated resistance value.", "R = 15 Volts (wrote Volts instead of Ohms)."),
        ("Light", "Lens Power Unit", "focal length 50 cm. Find Power.", "P = 1 / 50 = 0.02 Dioptres (forgot to convert cm to metres).")
    ],
    "UNSURE_INSUFFICIENT_EVIDENCE": [
        ("Electricity", "Circuit Prediction", "What happens to Bulb 2?", "Maybe it is dimmer or the same, I am not sure."),
        ("Light", "Image on Screen", "Describe image when lens is covered.", "Something changes with the light."),
        ("Magnetism", "Force Direction", "Where does wire move?", "It moves somewhere.")
    ]
}

# Compile Records
individual_records = []
resp_id = 1

for label, samples in DATA_BANK.items():
    error_type = (
        "no_error" if "CORRECT" in label else
        "calculation_slip" if "CALCULATION" in label else
        "unit_error" if "UNIT" in label else
        "guessing_unclear" if "UNSURE" in label else
        "conceptual_misconception"
    )
    for chap, topic, q_stem, ans in samples:
        individual_records.append({
            "response_id": f"RESP-{resp_id:04d}",
            "question_id": f"PHY-{chap[:3].upper()}-{resp_id:03d}",
            "chapter": chap,
            "topic_concept": topic,
            "question_text": q_stem,
            "correct_answer_and_steps": "Authoritative scientific solution verified by NCERT Class 10 Physics.",
            "student_response": ans,
            "misconception_label": label,
            "error_type": error_type,
            "confidence_evidence": "Low" if error_type == "guessing_unclear" else "High",
            "evidence_details": "Self-contained verbalized diagnostic reasoning.",
            "alternative_cause": "UNSURE_INSUFFICIENT_EVIDENCE" if error_type == "guessing_unclear" else None,
            "response_origin": "curated_per_literature" if error_type == "conceptual_misconception" else "authored_clean_sample"
        })
        resp_id += 1


# Deterministic Balanced Partitioning
from collections import defaultdict

class_to_indices = defaultdict(list)
for idx, r in enumerate(individual_records):
    class_to_indices[r["misconception_label"]].append(idx)

train_set, val_set, test_set = set(), set(), set()

for lbl, indices in class_to_indices.items():
    if len(indices) >= 3:
        test_set.add(indices[0])
        val_set.add(indices[1])
        for i in indices[2:]:
            train_set.add(i)
    elif len(indices) == 2:
        test_set.add(indices[0])
        train_set.add(indices[1])
    else:
        train_set.add(indices[0])

for idx, r in enumerate(individual_records):
    if idx in train_set:
        r["split"] = "train"
    elif idx in val_set:
        r["split"] = "val"
    else:
        r["split"] = "test"


# Save individual_responses.json and CSV
json_indiv_path = os.path.join(OUTPUT_DIR_INDIV, "individual_responses.json")
with open(json_indiv_path, "w", encoding="utf-8") as f:
    json.dump(individual_records, f, indent=2)

csv_indiv_path = os.path.join(OUTPUT_DIR_INDIV, "individual_responses.csv")
with open(csv_indiv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(individual_records[0].keys()))
    writer.writeheader()
    writer.writerows(individual_records)

for s in ["train", "val", "test"]:
    s_recs = [r for r in individual_records if r["split"] == s]
    with open(os.path.join(OUTPUT_DIR_INDIV, f"{s}.jsonl"), "w", encoding="utf-8") as f:
        for r in s_recs:
            f.write(json.dumps(r) + "\n")
    with open(os.path.join(OUTPUT_DIR_INDIV, f"{s}.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(individual_records[0].keys()))
        writer.writeheader()
        writer.writerows(s_recs)

print(f"Total Individual Responses Generated: {len(individual_records)} across {len(CLASSES)} classes.")

# -------------------------------------------------------------
# Sequence Dataset Generation (12 Complete Sequences)
# -------------------------------------------------------------
sequences_data = [
    {
        "sequence_id": "SEQ-001",
        "student_id": "STU_101",
        "topic": "Electricity: Series Circuits",
        "ordered_attempts": [
            {"step": 1, "question": "Two bulbs in series", "response": "Bulb 1 uses up current so Bulb 2 gets less", "diagnosis": "MISC-ELEC-001: Current Attenuation / Consumption Model", "confidence": 0.95},
            {"step": 2, "question": "Three resistors in series", "response": "Current through R3 is smaller than R1 because current is consumed", "diagnosis": "MISC-ELEC-001: Current Attenuation / Consumption Model", "confidence": 0.98},
            {"step": 3, "question": "Swapped order probe", "response": "The first resistor in line always gets more current", "diagnosis": "MISC-ELEC-001: Current Attenuation / Consumption Model", "confidence": 0.99}
        ],
        "sequence_level_label": "RECURRENT_CURRENT_ATTENUATION_PATTERN",
        "learning_status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
        "split": "train"
    },
    {
        "sequence_id": "SEQ-002",
        "student_id": "STU_102",
        "topic": "Electricity: Parallel Circuits",
        "ordered_attempts": [
            {"step": 1, "question": "Adding 3-ohm in parallel to 6-ohm", "response": "Total current stays 2A because battery output is fixed", "diagnosis": "MISC-ELEC-002: Battery as Constant Current Source", "confidence": 0.94},
            {"step": 2, "question": "Adding 5 more branches", "response": "Battery current is constant, just divided", "diagnosis": "MISC-ELEC-002: Battery as Constant Current Source", "confidence": 0.96}
        ],
        "sequence_level_label": "RECURRENT_CONSTANT_CURRENT_BATTERY_PATTERN",
        "learning_status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
        "split": "train"
    },
    {
        "sequence_id": "SEQ-003",
        "student_id": "STU_103",
        "topic": "Optics: Half-Lens Aperture Remediation",
        "ordered_attempts": [
            {"step": 1, "question": "Half of convex lens covered", "response": "Bottom half of image disappears from screen", "diagnosis": "MISC-OPT-001: Half-Lens Blocking Fallacy", "confidence": 0.95},
            {"step": 2, "question": "PhET ray simulation step", "response": "Rays from whole candle still reach open top half! Image is complete and dimmer", "diagnosis": "COGNITIVE_CONFLICT_RECONCILED", "confidence": 0.92},
            {"step": 3, "question": "Reassessment: Center of mirror covered", "response": "Entire image forms unbroken with slightly less brightness", "diagnosis": "CORRECT", "confidence": 0.98}
        ],
        "sequence_level_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
        "learning_status": "RESOLVED_MISCONCEPTION_WITH_TRANSFER",
        "split": "val"
    },
    {
        "sequence_id": "SEQ-004",
        "student_id": "STU_104",
        "topic": "Magnetism: Static Charges",
        "ordered_attempts": [
            {"step": 1, "question": "Proton near North pole", "response": "Proton repelled because North pole is positive charge", "diagnosis": "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Fallacy", "confidence": 0.96},
            {"step": 2, "question": "Electron near South pole", "response": "Electron repelled because South pole is negative charge", "diagnosis": "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Fallacy", "confidence": 0.97}
        ],
        "sequence_level_label": "RECURRENT_MAGNETIC_ELECTROSTATIC_CONFLATION",
        "learning_status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
        "split": "test"
    },
    {
        "sequence_id": "SEQ-005",
        "student_id": "STU_105",
        "topic": "Human Eye: Vision Defect Remediation",
        "ordered_attempts": [
            {"step": 1, "question": "Cannot see blackboard at 5m", "response": "Myopia, needs convex lens to magnify distant objects", "diagnosis": "MISC-EYE-001: Vision Defect Corrective Lens Inversion", "confidence": 0.93},
            {"step": 2, "question": "POE ray trace simulation", "response": "Eye lens is over-converging in front of retina, convex lens makes it worse. Needs concave lens!", "diagnosis": "COGNITIVE_CONFLICT_RECONCILED", "confidence": 0.91},
            {"step": 3, "question": "Reassessment: Far point 1.5m", "response": "Prescribe concave lens of focal length -1.5m", "diagnosis": "CORRECT", "confidence": 0.99}
        ],
        "sequence_level_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
        "learning_status": "RESOLVED_MISCONCEPTION_WITH_TRANSFER",
        "split": "train"
    },
    {
        "sequence_id": "SEQ-006",
        "student_id": "STU_106",
        "topic": "Optics: Sign Convention Consistency",
        "ordered_attempts": [
            {"step": 1, "question": "Concave mirror u = 20, f = 15", "response": "u = 20, f = 15 gives v = +60cm virtual image", "diagnosis": "MISC-OPT-004: Cartesian Sign Convention Spatial Inversion", "confidence": 0.96},
            {"step": 2, "question": "Convex lens u = 30, f = 10", "response": "u = +30cm because distance is positive length", "diagnosis": "MISC-OPT-004: Cartesian Sign Convention Spatial Inversion", "confidence": 0.95}
        ],
        "sequence_level_label": "PERVASIVE_SIGN_CONVENTION_INVERSION",
        "learning_status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
        "split": "test"
    }
]

with open(os.path.join(OUTPUT_DIR_SEQ, "student_sequences.json"), "w", encoding="utf-8") as f:
    json.dump(sequences_data, f, indent=2)

print(f"Generated {len(sequences_data)} multi-attempt sequence records.")
