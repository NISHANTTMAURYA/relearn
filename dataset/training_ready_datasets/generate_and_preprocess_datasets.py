import json
import csv
import os
import random

random.seed(42)

OUTPUT_DIR_INDIV = r"d:\relearn\dataset\training_ready_datasets\individual_response_dataset"
OUTPUT_DIR_SEQ = r"d:\relearn\dataset\training_ready_datasets\sequence_dataset"

os.makedirs(OUTPUT_DIR_INDIV, exist_ok=True)
os.makedirs(OUTPUT_DIR_SEQ, exist_ok=True)

# -------------------------------------------------------------
# Comprehensive Master Question Templates
# -------------------------------------------------------------
question_templates = [
    # 1. SERIES BULBS & CURRENT CONSERVATION
    {
        "question_id": "PHY-ELEC-001",
        "family": "SERIES_BULBS_CURRENT",
        "chapter": "Electricity",
        "topic": "Current Conservation in Series Circuit",
        "question_text": "A 6V battery is connected in series with two identical bulbs, Bulb 1 and Bulb 2. Ammeters A1, A2, and A3 are placed before Bulb 1, between Bulb 1 and Bulb 2, and after Bulb 2 respectively. Compare the ammeter readings.",
        "correct_answer_and_steps": "A1 = A2 = A3. In a single series loop, charge is strictly conserved (I = dQ/dt is uniform). Bulbs convert electrical potential energy to light and heat, but current is identical throughout.",
        "responses": [
            {
                "student_response": "A1 = 1.2A, A2 = 0.8A, A3 = 0.4A. Bulb 1 consumes some current to light up, and Bulb 2 consumes the rest.",
                "misconception_label": "MISC-ELEC-001: Current Attenuation / Consumption Model",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Working explicitly states current is consumed by bulbs sequentially.",
                "alternative_cause": "MISC-ELEC-004: Voltage exhaustion"
            },
            {
                "student_response": "A1 = A2 = A3 = 1.2A. Electric current is the flow of charge and charge cannot be lost in a closed series loop.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Accurate conservation principle stated.",
                "alternative_cause": None
            },
            {
                "student_response": "A1 and A3 are 1.2A, but A2 is 0.5A because current gets bottlenecked when squeezing through the filament.",
                "misconception_label": "MISC-ELEC-004: Voltage-Current Conflation / Local Bottleneck",
                "error_type": "conceptual_misconception",
                "confidence": "Medium",
                "evidence": "Treats resistor as a localized temporary speed bottleneck rather than systemic loop impedance.",
                "alternative_cause": "MISC-ELEC-001"
            },
            {
                "student_response": "A1 = 6A, A2 = 4A, A3 = 2A because V = 6V.",
                "misconception_label": "CARELESS_CALCULATION_ERROR",
                "error_type": "calculation_slip",
                "confidence": "Medium",
                "evidence": "Arbitrarily copied voltage number into current values without formula.",
                "alternative_cause": "UNSURE_INSUFFICIENT_EVIDENCE"
            },
            {
                "student_response": "I think Bulb 2 is dimmer.",
                "misconception_label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "error_type": "guessing_unclear",
                "confidence": "Low",
                "evidence": "Vague qualitative claim without specifying ammeter readings or physical reasoning.",
                "alternative_cause": "MISC-ELEC-001"
            }
        ]
    },

    # 2. PARALLEL RESISTANCE & BATTERY BEHAVIOR
    {
        "question_id": "PHY-ELEC-002",
        "family": "PARALLEL_BRANCH_ADDITION",
        "chapter": "Electricity",
        "topic": "Parallel Resistor Combination & Battery Delivery",
        "question_text": "A 12V battery is connected across a 6-ohm resistor R1. A second resistor R2 of 3 ohms is connected in parallel across R1. What happens to the total current drawn from the battery?",
        "correct_answer_and_steps": "Initially I = 12/6 = 2A. In parallel: 1/R_eq = 1/6 + 1/3 = 1/2 => R_eq = 2 ohms. Total current I_total = 12/2 = 6A (increases from 2A to 6A).",
        "responses": [
            {
                "student_response": "Total current stays 2A. A 12V battery has a fixed current rating that cannot change no matter what you connect.",
                "misconception_label": "MISC-ELEC-002: Battery as Constant Current Source",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Explicitly assumes battery outputs invariant current regardless of external load.",
                "alternative_cause": None
            },
            {
                "student_response": "Total resistance is 6 + 3 = 9 ohms. Current is 12 / 9 = 1.33A, so current decreases.",
                "misconception_label": "MISC-ELEC-005: Parallel Resistance Addition Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Calculates parallel resistance by adding resistances linearly (R_eq = R1 + R2).",
                "alternative_cause": None
            },
            {
                "student_response": "1/R = 1/6 + 1/3 = 3/6 = 1/2, so R = 2 ohms. Total current = 12V / 2 ohms = 6A. Current increases from 2A to 6A.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Flawless parallel Ohm's law calculation.",
                "alternative_cause": None
            },
            {
                "student_response": "1/R = 1/6 + 1/3 = 3/6 = 0.5. Total current = 12 * 0.5 = 6V.",
                "misconception_label": "UNIT_CONVERSION_ERROR",
                "error_type": "unit_error",
                "confidence": "Medium",
                "evidence": "Labeled current with Volts instead of Amperes.",
                "alternative_cause": "CARELESS_CALCULATION_ERROR"
            }
        ]
    },

    # 3. PARALLEL CURRENT DIVISION
    {
        "question_id": "PHY-ELEC-003",
        "family": "PARALLEL_CURRENT_DIVISION",
        "chapter": "Electricity",
        "topic": "Current Division across Unequal Parallel Branches",
        "question_text": "A total current of 6A enters a parallel junction splitting into two branches of resistance 2 ohms and 4 ohms. What is the current in each branch?",
        "correct_answer_and_steps": "V = I_total * R_p = 6A * (4/3) ohms = 8V. I_1 = 8V / 2 ohms = 4A. I_2 = 8V / 4 ohms = 2A. Or I_1/I_2 = R_2/R_1 = 4/2 = 2 => I_1 = 4A, I_2 = 2A.",
        "responses": [
            {
                "student_response": "Current splits equally at the junction, so each branch gets 6A / 2 = 3A.",
                "misconception_label": "MISC-ELEC-003: Shared Current / Equal Division Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Divides total current equally, ignoring branch resistance difference.",
                "alternative_cause": None
            },
            {
                "student_response": "The 4-ohm resistor gets 4A and the 2-ohm resistor gets 2A because higher resistance draws more current.",
                "misconception_label": "MISC-ELEC-004: Voltage-Current Conflation / Direct Ratio Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Inverts Ohm's law, believing current is directly proportional to resistance.",
                "alternative_cause": "CARELESS_CALCULATION_ERROR"
            },
            {
                "student_response": "I1 = 4A, I2 = 2A. V across both is 8V, so I1 = 8/2 = 4A and I2 = 8/4 = 2A.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Correct branch calculation using constant branch voltage.",
                "alternative_cause": None
            }
        ]
    },

    # 4. POWER IN PARALLEL
    {
        "question_id": "PHY-ELEC-004",
        "family": "DOMESTIC_BULB_POWER",
        "chapter": "Electricity",
        "topic": "Power Dissipation & Resistance in Parallel",
        "question_text": "Two electric bulbs rated 220V, 100W and 220V, 40W are connected in parallel to a 220V household supply. Which bulb has greater resistance, and which glows brighter?",
        "correct_answer_and_steps": "R = V^2 / P. R_100 = 220^2 / 100 = 484 ohms; R_40 = 220^2 / 40 = 1210 ohms. 40W bulb has greater resistance. In parallel across 220V, 100W bulb consumes 100W and glows brighter.",
        "responses": [
            {
                "student_response": "The 100W bulb has more resistance because P = I^2 * R means power is directly proportional to resistance. The 100W bulb glows brighter.",
                "misconception_label": "MISC-ELEC-006: Power Formula Mis-selection in Parallel vs Series",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Applied P = I^2*R to parallel circuit instead of P = V^2/R.",
                "alternative_cause": None
            },
            {
                "student_response": "The 40W bulb glows brighter because it has higher resistance and higher resistance produces more heat.",
                "misconception_label": "MISC-ELEC-006: Power Formula Mis-selection in Parallel vs Series",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Assumes higher resistance always produces greater brightness regardless of connection.",
                "alternative_cause": "MISC-ELEC-004"
            },
            {
                "student_response": "R = V^2 / P. 40W bulb has 1210 ohms, 100W has 484 ohms. In parallel, 100W bulb draws more current and glows brighter.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Correct formula selection P = V^2/R for constant voltage.",
                "alternative_cause": None
            }
        ]
    },

    # 5. WIRE STRETCHING RESISTANCE
    {
        "question_id": "PHY-ELEC-005",
        "family": "WIRE_STRETCHING_RESISTANCE",
        "chapter": "Electricity",
        "topic": "Factors Affecting Resistance (Length & Area)",
        "question_text": "A wire of resistance R is stretched uniformly until its length is doubled. What is its new resistance?",
        "correct_answer_and_steps": "Volume is constant: V = L * A = (2L) * (A/2). Since length doubles and area is halved, R' = rho * (2L) / (A/2) = 4 * (rho * L / A) = 4R.",
        "responses": [
            {
                "student_response": "R' = 2R because resistance is directly proportional to length (R = rho * L / A).",
                "misconception_label": "MISC-ELEC-004: Area Neglect in Volume Conservation",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Fails to conserve volume, ignoring that stretching halves cross-sectional area.",
                "alternative_cause": "CARELESS_CALCULATION_ERROR"
            },
            {
                "student_response": "R' = 4R. Doubling length halves cross-sectional area because volume is conserved, so R' = 4R.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Accurate application of volume conservation to R formula.",
                "alternative_cause": None
            },
            {
                "student_response": "R' = R because the material resistivity rho did not change.",
                "misconception_label": "MISC-ELEC-004: Resistivity vs Resistance Conflation",
                "error_type": "conceptual_misconception",
                "confidence": "Medium",
                "evidence": "Conflates material property (resistivity) with geometry-dependent property (resistance).",
                "alternative_cause": None
            }
        ]
    },

    # 6. CONVEX LENS HALF COVERED
    {
        "question_id": "PHY-OPT-001",
        "family": "HALF_LENS_COVERED",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Image Formation by Convex Lens Aperture",
        "question_text": "A convex lens forms a sharp real image of a candle flame on a screen. If the bottom half of the lens is covered with black cardboard, describe what happens to the image on the screen.",
        "correct_answer_and_steps": "The entire image remains intact and complete in the same position, but its intensity (brightness) decreases to approximately half because all object points emit rays to the uncovered upper half.",
        "responses": [
            {
                "student_response": "The bottom half of the candle image is blocked and disappears from the screen.",
                "misconception_label": "MISC-OPT-001: Half-Lens Blocking Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Believes the bottom half of the lens corresponds 1:1 to the bottom half of the image.",
                "alternative_cause": "MISC-OPT-006"
            },
            {
                "student_response": "The top half disappears because the image formed by a convex lens is inverted.",
                "misconception_label": "MISC-OPT-001: Half-Lens Blocking Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Considers inversion but still applies 1:1 geometric stencil blocking.",
                "alternative_cause": None
            },
            {
                "student_response": "The image disappears completely because the principal rays cannot pass.",
                "misconception_label": "MISC-OPT-006: Special Ray Exclusivity / Ray Reification",
                "error_type": "conceptual_misconception",
                "confidence": "Medium",
                "evidence": "Thinks image formation strictly requires textbook construction rays.",
                "alternative_cause": "MISC-OPT-001"
            },
            {
                "student_response": "The complete image is still formed on the screen, but it becomes dimmer because fewer rays from each point reach the screen.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Understands that every point radiates a cone of rays across the entire aperture.",
                "alternative_cause": None
            }
        ]
    },

    # 7. CARTESIAN SIGN CONVENTION
    {
        "question_id": "PHY-OPT-002",
        "family": "CARTESIAN_SIGN_CONVENTION",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Cartesian Sign Convention in Mirror Formula",
        "question_text": "An object is placed 20 cm in front of a concave mirror of focal length 15 cm. Calculate the image distance v and state whether the image is real or virtual.",
        "correct_answer_and_steps": "By Cartesian convention: u = -20 cm, f = -15 cm. 1/f = 1/v + 1/u => 1/v = 1/(-15) - 1/(-20) = -1/15 + 1/20 = -1/60 => v = -60 cm. Image is real and inverted.",
        "responses": [
            {
                "student_response": "u = 20, f = 15. 1/15 = 1/v + 1/20 => 1/v = 1/15 - 1/20 = 1/60 => v = +60 cm. The image is virtual and erect.",
                "misconception_label": "MISC-OPT-004: Cartesian Sign Convention Spatial Inversion",
                "error_type": "sign_inversion",
                "confidence": "High",
                "evidence": "Substituted positive scalar distances for u and f.",
                "alternative_cause": None
            },
            {
                "student_response": "u = -20, f = -15. 1/v = 1/(-15) - 1/(-20) = -1/15 + 1/20 = -1/60 => v = -60 cm. Real and inverted image in front of mirror.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Correct Cartesian signs and fraction arithmetic.",
                "alternative_cause": None
            },
            {
                "student_response": "u = -20, f = -15. 1/v = 1/(-15) + 1/(-20) = -7/60 => v = -8.57 cm.",
                "misconception_label": "CARELESS_CALCULATION_ERROR",
                "error_type": "calculation_slip",
                "confidence": "High",
                "evidence": "Used lens formula 1/f = 1/v - 1/u instead of mirror formula 1/f = 1/v + 1/u.",
                "alternative_cause": "MISC-OPT-004"
            },
            {
                "student_response": "v is roughly -60.",
                "misconception_label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "error_type": "guessing_unclear",
                "confidence": "Low",
                "evidence": "Gives isolated number without working or nature of image.",
                "alternative_cause": None
            }
        ]
    },

    # 8. GLASS SLAB REFRACTION
    {
        "question_id": "PHY-OPT-003",
        "family": "GLASS_SLAB_REFRACTION",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Refraction through Parallel Glass Slab",
        "question_text": "A ray of light enters a rectangular glass slab with parallel faces at an angle of 45 degrees. What is the direction of the emergent ray relative to the incident ray?",
        "correct_answer_and_steps": "Angle of incidence equals angle of emergence (i = e). The emergent ray is strictly parallel to the incident ray, shifted sideways by lateral displacement with zero angular deviation.",
        "responses": [
            {
                "student_response": "The emergent ray is permanently bent at an angle towards the normal, deviating by 15 degrees from its original path.",
                "misconception_label": "MISC-OPT-005: Glass Slab Emergent Ray Angular Deviation Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Confuses parallel glass slab with triangular prism deviation.",
                "alternative_cause": None
            },
            {
                "student_response": "The emergent ray travels parallel to the original incident ray, but with a lateral displacement.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Correctly states parallelism and lateral shift.",
                "alternative_cause": None
            }
        ]
    },

    # 9. MYOPIA CORRECTION
    {
        "question_id": "PHY-EYE-001",
        "family": "MYOPIA_CORRECTION",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Defects of Vision (Myopia)",
        "question_text": "A student cannot clearly see the blackboard located 5 meters away, but reads their textbook at 25 cm without difficulty. Name the vision defect and specify the lens required for correction.",
        "correct_answer_and_steps": "The student has Myopia (near-sightedness). Parallel rays from distant objects converge in front of the retina. A concave (diverging) lens is required to diverge the rays so they focus on the retina.",
        "responses": [
            {
                "student_response": "The student has Myopia. They need a convex lens because distant things look small and a convex magnifying glass will make them bigger.",
                "misconception_label": "MISC-EYE-001: Vision Defect Corrective Lens Inversion",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Prescribes convex lens for myopia based on magnification intuition.",
                "alternative_cause": None
            },
            {
                "student_response": "The defect is Hypermetropia, corrected with a convex lens.",
                "misconception_label": "MISC-EYE-001: Vision Defect Corrective Lens Inversion",
                "error_type": "conceptual_misconception",
                "confidence": "Medium",
                "evidence": "Confuses myopia and hypermetropia definitions.",
                "alternative_cause": None
            },
            {
                "student_response": "Myopia (near-sightedness), corrected using a concave lens of appropriate focal length.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Correct defect identification and diverging lens prescription.",
                "alternative_cause": None
            }
        ]
    },

    # 10. PRISM DISPERSION
    {
        "question_id": "PHY-EYE-002",
        "family": "PRISM_DISPERSION",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Dispersion of White Light through a Prism",
        "question_text": "When white light passes through a glass prism, which colour deviates the most, and which colour travels fastest inside the glass?",
        "correct_answer_and_steps": "Violet light has the shortest wavelength, experiences the highest refractive index in glass, travels the slowest, and suffers the greatest deviation. Red light travels fastest in glass and deviates the least.",
        "responses": [
            {
                "student_response": "Red deviates the most because red is the strongest color with highest energy. Violet travels fastest because it is sharp.",
                "misconception_label": "MISC-EYE-002: Prism Dispersion Speed & Deviation Inversion",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Inverts wavelength, speed, and deviation relationships based on colloquial energy concepts.",
                "alternative_cause": None
            },
            {
                "student_response": "Violet deviates the most because it travels slowest in glass. Red travels fastest and deviates the least.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Accurate dispersion mechanism cited.",
                "alternative_cause": None
            }
        ]
    },

    # 11. ATMOSPHERIC OPTICS & SCATTERING
    {
        "question_id": "PHY-EYE-003",
        "family": "ATMOSPHERIC_SCATTERING",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Scattering of Light & Sky Colour",
        "question_text": "Why does the clear daytime sky appear blue to an observer on Earth, but appears black to an astronaut on the Moon?",
        "correct_answer_and_steps": "Earth has an atmosphere containing molecules smaller than visible light wavelengths, which cause Rayleigh scattering (intensity proportional to 1/lambda^4). Blue light is scattered most. The Moon has no atmosphere, so no light is scattered into an observer's eyes, making the sky appear dark/black.",
        "responses": [
            {
                "student_response": "The sky is blue because Earth's blue oceans reflect sunlight upward into the air. The Moon has no water so it looks black.",
                "misconception_label": "MISC-EYE-004: Sky Colour Reflection / Ocean Reflection Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Believes blue sky is an optical mirror reflection of oceans.",
                "alternative_cause": None
            },
            {
                "student_response": "On Earth, air molecules scatter short blue wavelengths in all directions (Rayleigh scattering). On the Moon, there is no atmosphere to scatter light, so space looks pitch black.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Correctly explains Rayleigh scattering and absence of scattering medium.",
                "alternative_cause": None
            }
        ]
    },

    # 12. MAGNETIC POLE & CHARGE CONFLATION
    {
        "question_id": "PHY-MAG-001",
        "family": "MAGNETIC_POLE_CHARGE",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Interaction of Magnetic Field with Stationary Charge",
        "question_text": "A stationary positive charge (proton) is placed at rest between the North and South poles of a strong horseshoe magnet. What is the magnetic force acting on the proton?",
        "correct_answer_and_steps": "F = q * v * B * sin(theta). Since the proton is stationary, its velocity v = 0 m/s. Therefore, the magnetic force is identically zero (0 N). Magnetic fields do not exert force on stationary charges.",
        "responses": [
            {
                "student_response": "The proton feels an attractive force pulling it towards the South pole because positive charges attract negative magnetic poles.",
                "misconception_label": "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Equivalence Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Equates magnetic North/South poles to electrostatic positive/negative charges.",
                "alternative_cause": "MISC-MAG-003"
            },
            {
                "student_response": "The force is 0 N because a static magnetic field exerts force only on moving charges (v = 0 implies F = 0).",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Correct Lorentz velocity dependence recognized.",
                "alternative_cause": None
            },
            {
                "student_response": "The proton accelerates parallel along the field lines towards the South pole.",
                "misconception_label": "MISC-MAG-003: Magnetic Force Collinear / Parallel Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "Medium",
                "evidence": "Assumes magnetic force is collinear with field lines like gravity or electrostatic force.",
                "alternative_cause": "MISC-MAG-001"
            }
        ]
    },

    # 13. FLEMING'S LEFT-HAND RULE
    {
        "question_id": "PHY-MAG-002",
        "family": "FLEMINGS_LEFT_HAND_RULE",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Direction of Force on Moving Electron (Fleming's Left-Hand Rule)",
        "question_text": "An electron moves horizontally from West to East into a magnetic field directed vertically downwards. In which direction is the magnetic force on the electron?",
        "correct_answer_and_steps": "Electron moves West to East, so conventional current I is East to West. Magnetic field B is downwards. Using Fleming's Left-Hand Rule: Forefinger (Field) = Down, Center finger (Current) = West => Thumb (Force) points South.",
        "responses": [
            {
                "student_response": "Force is directed towards North. I used Fleming's rule with current pointing West to East.",
                "misconception_label": "MISC-MAG-005: Directional Hand Rule Inversion Fallacy",
                "error_type": "sign_inversion",
                "confidence": "High",
                "evidence": "Failed to invert conventional current direction for a negative charge (electron).",
                "alternative_cause": None
            },
            {
                "student_response": "Force points South. Since electron moves West to East, conventional current is East to West. Left hand rule gives South.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Accurate negative charge reversal and Fleming's left hand application.",
                "alternative_cause": None
            }
        ]
    },

    # 14. SOLENOID MAGNETIC FIELD
    {
        "question_id": "PHY-MAG-003",
        "family": "SOLENOID_FIELD_PROPERTIES",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Magnetic Field of a Current-Carrying Solenoid",
        "question_text": "Describe the pattern of magnetic field lines inside a long current-carrying solenoid, and explain what this pattern indicates about field strength.",
        "correct_answer_and_steps": "Inside the solenoid, magnetic field lines are straight, parallel, and equidistant. This indicates that the magnetic field is uniform at all points inside the solenoid.",
        "responses": [
            {
                "student_response": "Field lines are zero inside because all magnetic fields stay strictly outside a coil.",
                "misconception_label": "MISC-MAG-004: Magnetic Field Line Discontinuous Loop Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Believes field lines only exist outside, ignoring closed loop nature.",
                "alternative_cause": None
            },
            {
                "student_response": "Field lines cross each other in the middle of the solenoid creating a magnetic knot.",
                "misconception_label": "MISC-MAG-004: Magnetic Field Line Crossing Fallacy",
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": "Believes magnetic field lines can intersect.",
                "alternative_cause": None
            },
            {
                "student_response": "They are parallel straight lines, indicating that the magnetic field is uniform throughout the interior of the solenoid.",
                "misconception_label": "CORRECT",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Accurate description of uniform field inside solenoid.",
                "alternative_cause": None
            }
        ]
    }
]

# -------------------------------------------------------------
# Generate Individual Records with Leak-Free Family Split
# -------------------------------------------------------------
individual_records = []
resp_counter = 1

families = list(set(q["family"] for q in question_templates))
random.shuffle(families)
n_train = int(len(families) * 0.70)
n_val = int(len(families) * 0.15)

train_families = set(families[:n_train])
val_families = set(families[n_train:n_train + n_val])
test_families = set(families[n_train + n_val:])

for q in question_templates:
    fam = q["family"]
    if fam in train_families:
        split = "train"
    elif fam in val_families:
        split = "val"
    else:
        split = "test"

    for r in q["responses"]:
        rec = {
            "response_id": f"RESP-{resp_counter:04d}",
            "question_id": q["question_id"],
            "question_family": q["family"],
            "chapter": q["chapter"],
            "topic_concept": q["topic"],
            "question_text": q["question_text"],
            "correct_answer_and_steps": q["correct_answer_and_steps"],
            "student_response": r["student_response"],
            "misconception_label": r["misconception_label"],
            "error_type": r["error_type"],
            "confidence_evidence": r["confidence"],
            "evidence_details": r["evidence"],
            "alternative_cause": r["alternative_cause"],
            "response_origin": "curated_per_literature" if r["error_type"] == "conceptual_misconception" else "authored_clean_sample",
            "split": split
        }
        individual_records.append(rec)
        resp_counter += 1

# Write individual_responses.json and CSV
json_indiv_path = os.path.join(OUTPUT_DIR_INDIV, "individual_responses.json")
with open(json_indiv_path, "w", encoding="utf-8") as f:
    json.dump(individual_records, f, indent=2)

csv_indiv_path = os.path.join(OUTPUT_DIR_INDIV, "individual_responses.csv")
with open(csv_indiv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(individual_records[0].keys()))
    writer.writeheader()
    writer.writerows(individual_records)

# Write split files (train, val, test)
for s in ["train", "val", "test"]:
    s_recs = [r for r in individual_records if r["split"] == s]
    with open(os.path.join(OUTPUT_DIR_INDIV, f"{s}.jsonl"), "w", encoding="utf-8") as f:
        for r in s_recs:
            f.write(json.dumps(r) + "\n")
    with open(os.path.join(OUTPUT_DIR_INDIV, f"{s}.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(individual_records[0].keys()))
        writer.writeheader()
        writer.writerows(s_recs)

print(f"Generated {len(individual_records)} individual response records across {len(families)} question families.")

# -------------------------------------------------------------
# Generate Comprehensive Sequence Dataset (10 Ordered Attempts)
# -------------------------------------------------------------
student_sequences = [
    {
        "sequence_id": "SEQ-001",
        "student_id": "STU_101",
        "topic": "Electricity: Current Conservation",
        "ordered_attempts": [
            {
                "step": 1,
                "question_id": "PHY-ELEC-001",
                "question_stem": "Two bulbs in series with ammeters A1, A2, A3.",
                "student_response": "A1 = 1.2A, A2 = 0.8A, A3 = 0.4A. Bulb 1 consumes some current, and Bulb 2 consumes the rest.",
                "individual_diagnosis": "MISC-ELEC-001: Current Attenuation / Consumption Model",
                "confidence": 0.95
            },
            {
                "step": 2,
                "question_id": "PHY-ELEC-001-VAR",
                "question_stem": "Three identical resistors in series with ammeters before and after each resistor.",
                "student_response": "Current drops from 3A to 2A after the first resistor, then drops to 1A after the second resistor.",
                "individual_diagnosis": "MISC-ELEC-001: Current Attenuation / Consumption Model",
                "confidence": 0.98
            },
            {
                "step": 3,
                "question_id": "PROBE-ELEC-001",
                "question_stem": "Diagnostic Probe: If we swap the order of a 10-ohm and 2-ohm resistor in series, what happens to current?",
                "student_response": "The first resistor in line will always get the most current because current is depleted as it travels.",
                "individual_diagnosis": "MISC-ELEC-001: Current Attenuation / Consumption Model",
                "confidence": 0.99
            }
        ],
        "sequence_level_label": "RECURRENT_CURRENT_ATTENUATION_PATTERN",
        "evidence_summary": [
            "Q1: Student explicitly asserts current consumed by bulbs sequentially",
            "Q2: Replicated linear current drop across 3-resistor series configuration",
            "Q3: Probe confirmed student ignores resistance value and relies strictly on spatial sequence order"
        ],
        "confidence": "High",
        "status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
        "split": "train"
    },
    {
        "sequence_id": "SEQ-002",
        "student_id": "STU_102",
        "topic": "Electricity: Parallel Resistance and Battery Behavior",
        "ordered_attempts": [
            {
                "step": 1,
                "question_id": "PHY-ELEC-002",
                "question_stem": "Adding a 3-ohm resistor in parallel across a 6-ohm resistor powered by 12V battery.",
                "student_response": "Total current stays 2A because the 12V battery always outputs 2A.",
                "individual_diagnosis": "MISC-ELEC-002: Battery as Constant Current Source",
                "confidence": 0.92
            },
            {
                "step": 2,
                "question_id": "PROBE-ELEC-002",
                "question_stem": "If we connect 5 more resistors in parallel, does the battery current change?",
                "student_response": "No, battery current is fixed by the battery.",
                "individual_diagnosis": "MISC-ELEC-002: Battery as Constant Current Source",
                "confidence": 0.96
            }
        ],
        "sequence_level_label": "RECURRENT_CONSTANT_CURRENT_BATTERY_PATTERN",
        "evidence_summary": [
            "Q1: Asserts battery delivers constant current despite branch addition",
            "Q2: Reaffirms invariant battery current under multi-branch load"
        ],
        "confidence": "High",
        "status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
        "split": "train"
    },
    {
        "sequence_id": "SEQ-003",
        "student_id": "STU_103",
        "topic": "Light: Convex Lens Aperture & Image Formation (Pre-to-Post Intervention)",
        "ordered_attempts": [
            {
                "step": 1,
                "question_id": "PHY-OPT-001",
                "question_stem": "Convex lens forms real candle image on screen; lower half covered with black cardboard.",
                "student_response": "Bottom half of the flame disappears from the screen.",
                "individual_diagnosis": "MISC-OPT-001: Half-Lens Blocking Fallacy",
                "confidence": 0.94
            },
            {
                "step": 2,
                "question_id": "INTV-OPT-001-POE",
                "question_stem": "PhET Simulation: Student manipulates rays and covers half of lens.",
                "student_response": "I see that rays from the top and bottom of the arrow still hit the open top half and meet at the screen. The image is whole, just darker!",
                "individual_diagnosis": "COGNITIVE_CONFLICT_RECONCILED",
                "confidence": 0.90
            },
            {
                "step": 3,
                "question_id": "REASSESS-OPT-001",
                "question_stem": "Reassessment: Circular coin taped over center 20% of concave mirror.",
                "student_response": "The entire tree image will still be seen on the wall, but its brightness will be slightly reduced because light from all parts of the tree reflects off the rest of the mirror.",
                "individual_diagnosis": "CORRECT",
                "confidence": 0.98
            }
        ],
        "sequence_level_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
        "evidence_summary": [
            "Q1: Demonstrated classic half-lens blocking fallacy",
            "Step 2: Interactive POE simulation induced conceptual shift",
            "Step 3: Flawless isomorphic near-transfer to concave mirror"
        ],
        "confidence": "High",
        "status": "RESOLVED_MISCONCEPTION_WITH_TRANSFER",
        "split": "val"
    },
    {
        "sequence_id": "SEQ-004",
        "student_id": "STU_104",
        "topic": "Magnetism: Magnetic Forces on Charges",
        "ordered_attempts": [
            {
                "step": 1,
                "question_id": "PHY-MAG-001",
                "question_stem": "Stationary proton placed between North and South poles of magnet.",
                "student_response": "Proton is attracted to South pole because positive attracts negative.",
                "individual_diagnosis": "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Equivalence Fallacy",
                "confidence": 0.95
            },
            {
                "step": 2,
                "question_id": "PROBE-MAG-001",
                "question_stem": "What if an electron at rest is placed near the North pole?",
                "student_response": "Electron will be attracted to the positive North pole.",
                "individual_diagnosis": "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Equivalence Fallacy",
                "confidence": 0.97
            }
        ],
        "sequence_level_label": "RECURRENT_MAGNETIC_ELECTROSTATIC_CONFLATION",
        "evidence_summary": [
            "Q1: Equates South pole with negative charge",
            "Q2: Reaffirms North pole with positive charge for electron"
        ],
        "confidence": "High",
        "status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
        "split": "test"
    },
    {
        "sequence_id": "SEQ-005",
        "student_id": "STU_105",
        "topic": "Electricity: Calculation Slip vs Misconception Disambiguation",
        "ordered_attempts": [
            {
                "step": 1,
                "question_id": "PHY-ELEC-002",
                "question_stem": "Parallel branch addition: 6 ohm and 3 ohm across 12V.",
                "student_response": "1/R = 1/6 + 1/3 = 3/6 = 0.5. Total current = 12 * 0.5 = 6V.",
                "individual_diagnosis": "UNIT_CONVERSION_ERROR",
                "confidence": 0.85
            },
            {
                "step": 2,
                "question_id": "PHY-ELEC-003",
                "question_stem": "Current split in 2-ohm and 4-ohm parallel branches for 6A.",
                "student_response": "I1 = 4 Amps, I2 = 2 Amps.",
                "individual_diagnosis": "CORRECT",
                "confidence": 0.95
            }
        ],
        "sequence_level_label": "TRANSIENT_SLIP_WITH_CONCEPTUAL_MASTERY",
        "evidence_summary": [
            "Q1: Calculation slip with inverted resistance / unit label",
            "Q2: Perfect branch current calculation demonstrates underlying Ohm's law mastery"
        ],
        "confidence": "High",
        "status": "NO_CONCEPTUAL_MISCONCEPTION",
        "split": "val"
    },
    {
        "sequence_id": "SEQ-006",
        "student_id": "STU_106",
        "topic": "Human Eye: Vision Defect Remediation",
        "ordered_attempts": [
            {
                "step": 1,
                "question_id": "PHY-EYE-001",
                "question_stem": "Cannot see blackboard clearly at 5m, reads book clearly at 25cm. Name defect and corrective lens.",
                "student_response": "Myopia, corrected with convex lens so distant letters are magnified.",
                "individual_diagnosis": "MISC-EYE-001: Vision Defect Corrective Lens Inversion",
                "confidence": 0.94
            },
            {
                "step": 2,
                "question_id": "INTV-EYE-001-POE",
                "question_stem": "Simulation showing myopic eye over-converging rays in front of retina.",
                "student_response": "Oh! The eye lens is already bending the rays too much. A convex lens makes it bend even earlier! We need a concave lens to diverge them back onto the retina.",
                "individual_diagnosis": "COGNITIVE_CONFLICT_RECONCILED",
                "confidence": 0.92
            },
            {
                "step": 3,
                "question_id": "REASSESS-EYE-001",
                "question_stem": "A patient cannot see objects beyond 1.5m. What lens power and type should be prescribed?",
                "student_response": "Diverging concave lens of focal length -1.5m, power P = -0.67 D.",
                "individual_diagnosis": "CORRECT",
                "confidence": 0.98
            }
        ],
        "sequence_level_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
        "evidence_summary": [
            "Q1: Inverted lens prescription based on magnification analogy",
            "Step 2: Ray trace simulation clarified over-convergence",
            "Step 3: Correct numerical prescription and concave lens choice"
        ],
        "confidence": "High",
        "status": "RESOLVED_MISCONCEPTION_WITH_TRANSFER",
        "split": "train"
    },
    {
        "sequence_id": "SEQ-007",
        "student_id": "STU_107",
        "topic": "Optics: Sign Convention Consistency across Mirrors and Lenses",
        "ordered_attempts": [
            {
                "step": 1,
                "question_id": "PHY-OPT-002",
                "question_stem": "Concave mirror u = 20cm, f = 15cm. Find v.",
                "student_response": "1/15 = 1/v + 1/20 => v = +60cm, virtual image.",
                "individual_diagnosis": "MISC-OPT-004: Cartesian Sign Convention Spatial Inversion",
                "confidence": 0.96
            },
            {
                "step": 2,
                "question_id": "PHY-OPT-002-LENS",
                "question_stem": "Convex lens u = 20cm, f = 15cm. Find v.",
                "student_response": "1/15 = 1/v - 1/20 => v = +8.57cm.",
                "individual_diagnosis": "MISC-OPT-004: Cartesian Sign Convention Spatial Inversion",
                "confidence": 0.95
            }
        ],
        "sequence_level_label": "PERVASIVE_SIGN_CONVENTION_INVERSION",
        "evidence_summary": [
            "Q1: Plugged scalar positive u = 20 into mirror formula",
            "Q2: Plugged scalar positive u = 20 into lens formula without coordinate origin"
        ],
        "confidence": "High",
        "status": "UNRESOLVED_PERSISTENT_MISCONCEPTION",
        "split": "test"
    }
]

# Write student_sequences.json and splits
json_seq_path = os.path.join(OUTPUT_DIR_SEQ, "student_sequences.json")
with open(json_seq_path, "w", encoding="utf-8") as f:
    json.dump(student_sequences, f, indent=2)

for s in ["train", "val", "test"]:
    s_seqs = [seq for seq in student_sequences if seq["split"] == s]
    with open(os.path.join(OUTPUT_DIR_SEQ, f"{s}_sequences.json"), "w", encoding="utf-8") as f:
        json.dump(s_seqs, f, indent=2)

print(f"Generated {len(student_sequences)} multi-attempt sequence records across train/val/test splits.")
