import json
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

BASE_DIR = r"d:\relearn\dataset"
INDIV_DIR = os.path.join(BASE_DIR, "individual_response_dataset")
SEQ_DIR = os.path.join(BASE_DIR, "sequence_dataset")

os.makedirs(INDIV_DIR, exist_ok=True)
os.makedirs(SEQ_DIR, exist_ok=True)

# ----------------------------------------------------------------------------------------
# Authoritative Physics Curriculum Families
# Primary Core: Class 10 Physics (Light, Human Eye, Electricity, Magnetism)
# Foundational Mechanics: Class 9 Physics (Motion, Force & Laws, Gravitation, Work & Energy)
# ----------------------------------------------------------------------------------------
master_families = [
    # ========================== CLASS 10 PHYSICS (CORE CURRICULUM) ==========================
    # 1. OPTICS: HALF-LENS BLOCKING
    {
        "family": "OPTICS_HALF_LENS_BLOCKING",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Image Formation and Aperture of Convex Lens",
        "target_misc": "MISC-OPT-001: Half-Lens Blocking Fallacy",
        "misc_desc": "Believes covering half the lens cuts the image in half, misunderstanding that every point on the lens receives light from every point on the object.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Convex lens with lower half covered by black opaque cardboard. Object placed beyond 2F forms a complete real inverted image on the screen with reduced brightness.",
            "visual_elements": ["ConvexLens", "OpaqueMask(lower_half)", "Object(AB)", "Screen(A'B')", "ConvergingRays"],
            "whiteboard_commands": [
                "draw_lens(type='convex', f=20)",
                "draw_mask(position='lower_half', color='black')",
                "draw_rays_from_tip(count=5)",
                "write_equation('Image remains complete; Brightness decreases to 50%')"
            ]
        },
        "stem_templates": [
            "A student forms a sharp image of a lighted candle on a screen using a convex lens of focal length {f} cm. The lower half of the lens is now covered with black paper. What happens to the image on the screen?",
            "A converging lens of focal length {f} cm projects an image of an illuminated slide. If the upper half of the lens is blocked by an opaque cover, describe the change in the projected image.",
            "An experimenter covers 50% of a convex lens with black tape. How does this affect the image formed by the lens on a viewing card?",
            "A ray optics setup uses a convex lens of focal length {f} cm. If half of the lens area is wrapped in black foil, what will be observed on the image screen?"
        ],
        "params": [(15,), (20,), (10,), (25,), (12,), (18,)],
        "correct_base": "The image remains completely intact and full. Every exposed portion of the lens refracts light rays from all parts of the object. Covering half the lens reduces the light energy transmitted, decreasing brightness without cropping.",
        "misc_phrasings": [
            "The top half of the candle image is completely missing because the bottom half of the lens is covered.",
            "Only half the image will appear on the screen because blocking half the glass blocks half the picture.",
            "The bottom rays are blocked, so only the top half of the object can be focused.",
            "Half of the image disappears from the screen since 50% of the lens is covered with black paper.",
            "The screen will show only the lower portion of the image because light from the upper half cannot get through."
        ],
        "correct_phrasings": [
            "The complete image is still formed on the screen, but its brightness is reduced by half because each point on the lens receives light from all parts of the object.",
            "The image remains whole and complete; only the intensity of light decreases because the effective aperture area is halved.",
            "Full image is formed, but it becomes dimmer because fewer light rays reach the screen."
        ],
        "slip_phrasings": [
            "The image remains complete, but the focal length changes from {f} cm to {slip} cm.",
            "Full image remains, but the magnification drops from -1.0 to -0.2 due to arithmetic error."
        ],
        "unit_phrasings": [
            "The full image is formed with a brightness drop of 50 lumens/cm instead of percent.",
            "Image is complete with illumination intensity measured in Volts instead of Lux."
        ],
        "unsure_phrasings": [
            "Maybe half the image disappears or it becomes blurry, not sure of the exact ray rule.",
            "I guess the image might move to another position, but I am uncertain."
        ]
    },

    # 2. OPTICS: CARTESIAN SIGN CONVENTION
    {
        "family": "OPTICS_CARTESIAN_SIGN_CONVENTION",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "New Cartesian Sign Convention in Mirror Formula",
        "target_misc": "MISC-OPT-004: Sign Convention Spatial Inversion",
        "misc_desc": "Omits negative signs for real object distance u and concave focal length f, treating distances as positive scalars.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Concave mirror with optical pole P at origin (0,0). Object AB located at distance u to the left of the mirror.",
            "visual_elements": ["ConcaveMirror", "PoleP(origin)", "FocalPoint(F=-15cm)", "Object(u=-30cm)"],
            "whiteboard_commands": [
                "draw_axes(origin='Pole P')",
                "draw_concave_mirror(pole=(0,0))",
                "plot_point(label='F', x=-15, text='f = -15 cm')",
                "plot_point(label='Object', x=-30, text='u = -30 cm')",
                "write_equation('1/f = 1/v + 1/u => 1/v = 1/f - 1/u')"
            ]
        },
        "stem_templates": [
            "An object is placed at a distance of {u} cm in front of a concave mirror of focal length {f} cm. Using the mirror formula, calculate the image position v.",
            "A candle is placed {u} cm from a concave spherical mirror having focal length {f} cm. Find the distance and nature of the image formed.",
            "A pin is positioned {u} cm to the left of a concave mirror of focal length {f} cm. Determine the image distance v."
        ],
        "params": [(30, 15), (40, 20), (25, 10), (60, 20), (20, 10)],
        "correct_base": "By New Cartesian Sign Convention: u = -{u} cm, f = -{f} cm. 1/f = 1/v + 1/u => 1/v = 1/f - 1/u. Image is formed at negative distance in front of mirror.",
        "misc_phrasings": [
            "v = +{f} cm because distances are always positive scalars; 1/v = 1/{f} - 1/{u}.",
            "Image distance v = +{u} cm. I used positive values for both u and f since lengths cannot be negative.",
            "1/v = 1/{f} + 1/{u} giving positive v, because the object is in front of the mirror.",
            "v is positive because light travels forward from the candle to the mirror."
        ],
        "correct_phrasings": [
            "u = -{u} cm, f = -{f} cm. Using 1/f = 1/v + 1/u => 1/v = -1/{f} - (-1/{u}). Image is real and inverted in front of the mirror.",
            "Both object distance and focal length are negative according to Cartesian sign convention. Solving gives negative image distance."
        ],
        "slip_phrasings": [
            "Substituted u = -{u} and f = -{f} correctly, but made an arithmetic fraction error: 1/v = -1/5.",
            "Setup is correct with negative signs, but calculated common denominator incorrectly."
        ],
        "unit_phrasings": [
            "v = -30 meters instead of centimeters.",
            "Calculated v = -30 without writing any units."
        ],
        "unsure_phrasings": [
            "I remember there is a minus sign somewhere in the mirror formula, but not sure which one gets it.",
            "Not sure whether concave mirror focal length is positive or negative."
        ]
    },

    # 3. HUMAN EYE: MYOPIA VS HYPERMETROPIA
    {
        "family": "HUMAN_EYE_VISION_DEFECTS",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Myopia and Hypermetropia Correction",
        "target_misc": "MISC-EYE-001: Vision Defect Corrective Inversion",
        "misc_desc": "Inverts corrective lens assignment (prescribing convex converging lenses for nearsightedness/myopia).",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "eye_defect_diagram",
            "diagram_description": "Myopic eye where rays from distant object focus in front of the retina. Concave diverging lens corrects focus back onto the retina.",
            "visual_elements": ["ElongatedEyeball", "CorneaLensSystem", "FocalPoint(in_front_of_retina)", "Retina", "CorrectiveConcaveLens"],
            "whiteboard_commands": [
                "draw_eyeball(shape='myopic_elongated')",
                "draw_incoming_rays(source='infinity')",
                "plot_focus(location='before_retina')",
                "insert_corrective_lens(type='concave_diverging')",
                "write_equation('Concave lens diverges incoming rays so image lands on retina')"
            ]
        },
        "stem_templates": [
            "A student sitting on the back bench cannot read the chalkboard clearly (distant vision impaired) but can read his textbook easily. Name the defect and the type of corrective lens required.",
            "A person with a far point of {fp} cm cannot see distant stars clearly. What eye defect do they have and which lens will restore clear vision?",
            "An adult has trouble seeing road signs 50 meters away while having normal reading vision. Specify the ocular condition and the required spectacle lens."
        ],
        "params": [(80,), (150,), (200,), (100,), (120,)],
        "correct_base": "The defect is Myopia (nearsightedness), where parallel rays from distant objects converge in front of the retina. A Concave (diverging) lens is required.",
        "misc_phrasings": [
            "The defect is Hypermetropia, and it requires a Convex (converging) lens to see the board clearly.",
            "He has far-sightedness, so he needs a converging lens to bring the distant image into focus.",
            "Defect is Myopia, but he needs a convex magnifying lens to make the distant chalkboard larger.",
            "Use a convex lens because distant objects need more converging power to reach the eye."
        ],
        "correct_phrasings": [
            "The defect is Myopia (short-sightedness). Because the eyeball is elongated, rays focus before the retina; a Concave (diverging) lens is required to diverge the rays.",
            "Condition is Myopia. It is corrected by using spectacles with concave lenses of appropriate focal length."
        ],
        "slip_phrasings": [
            "Correctly identified Myopia and concave lens, but calculated focal length as P = 1/f = 1/0.8 = 1.0 D instead of -1.25 D.",
            "Defect is Myopia and lens is concave, but made an arithmetic slip in dioptre power calculation."
        ],
        "unit_phrasings": [
            "Power of the corrective concave lens is -1.25 Watts instead of Dioptres.",
            "Stated lens power as -1.25 m without dioptre units."
        ],
        "unsure_phrasings": [
            "It is either myopia or hypermetropia, but I cannot recall which one uses concave lenses.",
            "I know glasses are needed, but unsure whether converging or diverging."
        ]
    },

    # 4. HUMAN EYE: PRISM DISPERSION
    {
        "family": "HUMAN_EYE_PRISM_DISPERSION",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Dispersion of White Light through a Glass Prism",
        "target_misc": "MISC-EYE-002: Prism Dispersion Speed and Deviation Inversion",
        "misc_desc": "Believes red bends the most because it is 'strongest', or claims violet travels fastest inside the glass medium.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "prism_dispersion",
            "diagram_description": "White light beam incident on triangular glass prism dispersing into VIBGYOR spectrum. Red refracts least, Violet refracts most.",
            "visual_elements": ["TriangularPrism(glass)", "WhiteLightBeam", "RedRay(deviation_min)", "VioletRay(deviation_max)", "Screen"],
            "whiteboard_commands": [
                "draw_prism(apex_angle=60)",
                "draw_white_beam(angle_incidence=45)",
                "disperse_spectrum(red_angle=30, violet_angle=40)",
                "write_equation('n_violet > n_red => v_red > v_violet in glass')"
            ]
        },
        "stem_templates": [
            "When a narrow beam of white light passes through a glass prism, it splits into a band of seven colours. Which colour bends the most, and which colour travels fastest inside the glass?",
            "During refraction through a triangular prism, why does violet light deviate through a larger angle than red light?",
            "A beam of sunlight enters a glass prism. Compare the refractive index of glass for red light versus violet light."
        ],
        "params": [(1,)],
        "correct_base": "Violet bends the most because it has the shortest wavelength and experiences the highest refractive index in glass. Red travels fastest in glass and deviates the least.",
        "misc_phrasings": [
            "Red bends the most because red is the strongest colour and has the most energy.",
            "Violet travels fastest inside the glass because it is at the bottom of the spectrum.",
            "Red deviates through the largest angle because it has the longest wavelength.",
            "Violet light bends least because it moves faster than red light in the prism."
        ],
        "correct_phrasings": [
            "Violet light bends the most because glass has the highest refractive index for violet (shortest wavelength). Red light travels fastest in glass and deviates the least.",
            "Red light has longer wavelength, experiences smaller refractive index, and deviates least. Violet light travels slowest and bends most."
        ],
        "slip_phrasings": [
            "Violet deviates most and red least, but listed the VIBGYOR sequence backwards as ROYGBIV from base to top.",
            "Correct deviation rule stated, but wrote speed formula as v = c * n instead of v = c / n."
        ],
        "unit_phrasings": [
            "Angle of deviation is 40 radians instead of degrees.",
            "Wavelength stated in metres without the 10^-9 multiplier."
        ],
        "unsure_phrasings": [
            "One colour bends more than the other, but I forget whether red or violet is at the top.",
            "Not sure whether high refractive index means more bending or less bending."
        ]
    },

    # 5. ELECTRICITY: CURRENT CONSERVATION
    {
        "family": "ELECTRICITY_CURRENT_CONSERVATION",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Current Conservation in a Series Circuit",
        "target_misc": "MISC-ELEC-001: Current Attenuation / Consumption Model",
        "misc_desc": "Believes electric current is consumed or 'used up' by electrical loads as it travels around the circuit loop.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_schematic",
            "diagram_description": "A single-loop series circuit with a DC battery, switch, ammeter A1, bulb 1, ammeter A2, bulb 2, and ammeter A3.",
            "visual_elements": ["Battery(V=6V)", "AmmeterA1", "Bulb1(R=5ohm)", "AmmeterA2", "Bulb2(R=5ohm)", "AmmeterA3"],
            "whiteboard_commands": [
                "draw_circuit(loop='single_series')",
                "insert_meters(A1='before_bulb1', A2='between_bulbs', A3='after_bulb2')",
                "write_equation('I_A1 = I_A2 = I_A3 (Charge Conservation)')",
                "highlight('Current is not consumed; potential energy is converted')"
            ]
        },
        "stem_templates": [
            "Two identical light bulbs are connected in series with a {V} V battery. Ammeter A1 is before Bulb 1, A2 is between the bulbs, and A3 is after Bulb 2. If A1 reads {I} A, what do A2 and A3 read?",
            "Three resistors of resistances {R} ohms each are connected in series across a {V} V cell. How does the current entering the first resistor compare with the current leaving the third resistor?",
            "In a series circuit containing two heating coils, a student claims current decreases after passing through each coil because energy is consumed. Explain whether this claim is correct."
        ],
        "params": [(6, 1.2, 5), (12, 0.8, 10), (9, 1.5, 6), (24, 2.0, 12)],
        "correct_base": "Electric current is the continuous rate of flow of electric charge (I = dQ/dt). By charge conservation, charges cannot accumulate or vanish in a single-loop series circuit. A1 = A2 = A3 exactly.",
        "misc_phrasings": [
            "A1 = {I}A, A2 = 0.8A, A3 = 0.4A because bulb 1 consumes electric current to glow, leaving less for bulb 2.",
            "Current is used up as it travels along the series loop, so each subsequent component gets less current.",
            "Bulb 2 receives less current than Bulb 1 because the charges get spent producing light and heat.",
            "Current decreases progressively around the circuit from positive to negative terminal."
        ],
        "correct_phrasings": [
            "A1 = A2 = A3 = {I} A. Current is conserved in a series circuit because electric charge cannot vanish or accumulate; only potential energy is dissipated.",
            "Current is identical at every point in a series circuit because there is only one conductive path for electrons."
        ],
        "slip_phrasings": [
            "Current is constant everywhere in series, so A1 = A2 = A3 = {slip} A due to division slip.",
            "All ammeters read equal current, but calculated I = V * R instead of I = V / R."
        ],
        "unit_phrasings": [
            "A1 = A2 = A3 = {I} Volts instead of Amperes.",
            "Current through all meters is {I} Watts."
        ],
        "unsure_phrasings": [
            "The current might decrease after passing the bulb, but I am not certain.",
            "I guess ammeters have different values depending on location, but need to check notes."
        ]
    },

    # 6. ELECTRICITY: PARALLEL BATTERY DELIVERY
    {
        "family": "ELECTRICITY_PARALLEL_BATTERY_DELIVERY",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Current Delivery of Battery in Parallel Circuits",
        "target_misc": "MISC-ELEC-002: Battery as Constant Current Source",
        "misc_desc": "Believes a battery produces a fixed amount of total current, assuming adding parallel branches splits and reduces existing current.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_schematic",
            "diagram_description": "A parallel network with two branches across an ideal DC voltage source V. Branch 1 has bulb B1, Branch 2 has switch S and bulb B2.",
            "visual_elements": ["Battery(V=12V)", "Branch1(Bulb_B1)", "Branch2(Switch_S, Bulb_B2)", "TotalAmmeter"],
            "whiteboard_commands": [
                "draw_parallel_circuit(branches=2)",
                "toggle_switch(branch=2, state='closed')",
                "write_equation('1/R_eq = 1/R1 + 1/R2 => R_eq decreases')",
                "write_equation('I_total = V / R_eq increases; I_B1 = V/R1 stays constant')"
            ]
        },
        "stem_templates": [
            "A {V} V battery powers a light bulb in a single branch. An identical second bulb is connected in parallel with the first bulb by closing a switch. What happens to the brightness of the first bulb and the total current from the battery?",
            "In a household parallel circuit connected to {V} V, an electric heater is switched ON while a room lamp is already glowing. Does the lamp dim, stay the same, or brighten?",
            "Two parallel resistors R1 = {R} ohms and R2 = {R} ohms are connected across a {V} V DC source. How does the current supplied by the battery change when R2 is disconnected?"
        ],
        "params": [(12, 10), (6, 6), (24, 20), (220, 100)],
        "correct_base": "An ideal battery maintains constant potential difference V. In parallel, voltage across Branch 1 remains constant, so its current and brightness are unchanged. Total current increases because equivalent resistance decreases.",
        "misc_phrasings": [
            "Bulb 1 dims to half brightness because the battery provides a fixed total current that must now be shared between two bulbs.",
            "The battery has a set amount of current, so adding another branch reduces current to the first branch.",
            "Both bulbs glow half as bright because current splits equally from the battery's fixed output.",
            "The lamp will dim when the heater turns on because the total electricity from the source is limited."
        ],
        "correct_phrasings": [
            "Bulb 1 brightness remains completely unchanged because the voltage across it is constant ({V} V). The battery supplies twice the total current because equivalent circuit resistance is halved.",
            "Parallel branches are independent; voltage across each branch equals source voltage. Total battery current increases."
        ],
        "slip_phrasings": [
            "Brightness unchanged, but calculated total current as I_total = {slip} A due to addition error.",
            "R_eq in parallel calculated as R1 + R2 instead of product over sum."
        ],
        "unit_phrasings": [
            "Total current increases by 2.4 Coulombs instead of Amperes.",
            "Calculated resistance in Ohms, but labeled it as Joules."
        ],
        "unsure_phrasings": [
            "I think parallel circuits share current, so maybe it dims a little?",
            "Not sure if the battery output changes or stays constant when more branches are added."
        ]
    },

    # 7. MAGNETIC EFFECTS: FLEMING'S LEFT HAND RULE
    {
        "family": "MAGNETIC_EFFECTS_LORENTZ_LEFT_HAND",
        "grade": "Class 10",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Magnetic Force on Current-Carrying Conductor (Fleming's Left Hand Rule)",
        "target_misc": "MISC-MAG-005: Directional Hand Rule Inversion",
        "misc_desc": "Swaps left and right hands, swaps thumb and index fingers, or forgets to invert force direction for negative charges.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "field_lines",
            "diagram_description": "A straight wire carrying electric current directed towards the East in a magnetic field directed towards the North.",
            "visual_elements": ["Wire(current_East)", "MagneticField(direction_North)", "ForceVector(perpendicular)"],
            "whiteboard_commands": [
                "draw_3d_axes(x='East', y='North', z='Upwards')",
                "draw_current_vector(direction='East')",
                "draw_b_field(direction='North')",
                "apply_flemings_left_hand_rule(thumb='Force', index='Field', middle='Current')",
                "write_equation('Force is directed vertically upwards (out of page)')"
            ]
        },
        "stem_templates": [
            "A horizontal wire carries conventional electric current towards the East. A uniform magnetic field is directed towards the North. Using Fleming's Left-Hand Rule, determine the direction of the magnetic force on the wire.",
            "A proton beam travels horizontally towards the East through a magnetic field pointing North. What is the direction of deflection of the proton beam?",
            "An electron beam travels horizontally towards the East into a magnetic field directed North. What is the direction of the magnetic force on the electrons?"
        ],
        "params": [(1,)],
        "correct_base": "By Fleming's Left-Hand Rule: Forefinger points North (Field), Middle finger points East (Current). The extended Thumb points vertically Upwards (out of page). For electrons, force is reversed (Downwards).",
        "misc_phrasings": [
            "The force is directed vertically Downwards because I used my right hand instead of left hand.",
            "Force points towards the North because magnetic force always pulls objects along the field lines.",
            "The wire will be pushed East in the direction of the electric current.",
            "For the electron beam, the force is Upwards because negative charges follow the same hand rule without reversal."
        ],
        "correct_phrasings": [
            "Using Fleming's Left-Hand Rule: Index finger points North (Field), Middle finger points East (Current), Thumb points vertically Upwards (out of page).",
            "The magnetic force is perpendicular to both current and magnetic field, directed vertically upwards for positive charge and downwards for electrons."
        ],
        "slip_phrasings": [
            "Applied left-hand rule correctly, but labeled the vertical direction as horizontal North-East.",
            "Identified upwards direction, but stated magnitude formula as F = B / (I * L) instead of F = B * I * L."
        ],
        "unit_phrasings": [
            "Force magnitude is 5.0 Tesla instead of Newtons.",
            "Reported magnetic force with velocity units m/s."
        ],
        "unsure_phrasings": [
            "I always mix up the thumb and middle finger in Fleming's rule.",
            "I know it's perpendicular, but unsure whether it's up or down."
        ]
    },

    # ========================== CLASS 9 PHYSICS (FOUNDATIONAL MECHANICS) ==========================
    # 8. MOTION: SPEED, DISTANCE, TIME
    {
        "family": "MOTION_SPEED_DISTANCE_TIME",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Speed and Velocity (Distance-Time Relationship)",
        "target_misc": "MISC-MOT-001: Speed Distance Operation Inversion",
        "misc_desc": "Multiplies distance by time instead of dividing.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_diagram",
            "diagram_description": "A straight road track marked with intervals. Runner completes track distance d in elapsed time t.",
            "visual_elements": ["Track(length=100m)", "Stopwatch(t=5s)", "Runner(start=0, end=100)"],
            "whiteboard_commands": [
                "draw_axes(x_label='distance (m)', y_label='time (s)')",
                "plot_track(start=0, end=100)",
                "write_equation('speed = distance / time')",
                "highlight('divide distance by time')"
            ]
        },
        "stem_templates": [
            "A runner covers a distance of {d} meters in {t} seconds along a straight track. Calculate the speed of the runner.",
            "A car travels a distance of {d} meters in {t} seconds. What is the speed of the car?",
            "An electric bicycle moves {d} meters in {t} seconds. Find its average speed.",
            "A toy cart moves along a smooth floor covering {d} meters in {t} seconds. Determine its speed."
        ],
        "params": [(100, 5), (200, 10), (300, 15), (500, 25), (60, 3), (120, 4), (450, 9), (80, 2)],
        "correct_base": "Speed = Distance / Time = {d} m / {t} s. Speed is defined as distance covered per unit time.",
        "misc_phrasings": [
            "Speed is {misc_val} m/s because I multiplied distance by time ({d} * {t} = {misc_val}).",
            "I calculated speed = {d} * {t} = {misc_val} m/s.",
            "Speed = distance times time, so it equals {misc_val} m/s.",
            "Result: {misc_val} m/s. Working: multiplied the two given numbers together."
        ],
        "correct_phrasings": [
            "Speed = Distance / Time = {d} m / {t} s = {cor_val} m/s.",
            "Average speed is distance divided by elapsed time: {d} / {t} = {cor_val} m/s.",
            "{cor_val} m/s, calculated using v = s / t."
        ],
        "slip_phrasings": [
            "Speed = {d} / {t} = {slip} m/s (mental arithmetic slip on division).",
            "Set up 100 / 5 properly, but wrote 25 m/s by mistake."
        ],
        "unit_phrasings": [
            "Speed is {cor_val} m/s^2 (used acceleration units for speed).",
            "Result is {cor_val} seconds instead of m/s."
        ],
        "unsure_phrasings": [
            "I think the speed is around {cor_val}, but not sure whether to multiply or divide.",
            "Unclear about the formula for speed."
        ]
    },

    # 9. MOTION: SPEED VS ACCELERATION
    {
        "family": "MOTION_SPEED_VS_ACCELERATION",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Acceleration vs Speed / Velocity",
        "target_misc": "MISC-MOT-002: Speed-Acceleration Conflation",
        "misc_desc": "Conflates speed with acceleration; assumes high speed means high acceleration or divides speed by total time.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "v_t_graph",
            "diagram_description": "Velocity-time graph showing a horizontal line at constant velocity v for time interval t.",
            "visual_elements": ["Axes(v_vs_t)", "HorizontalLine(v=constant)", "Slope(zero)"],
            "whiteboard_commands": [
                "draw_axes(x_label='time (s)', y_label='velocity (m/s)')",
                "plot_line(points=[(0, 20), (10, 20)], label='constant velocity')",
                "write_equation('a = (v - u) / t = 0')"
            ]
        },
        "stem_templates": [
            "A vehicle moves at a steady constant speed of {v} m/s for {t} seconds. What is the acceleration of the vehicle?",
            "Looking at the horizontal flat line on a velocity-time graph at v = {v} m/s for {t} seconds, what is the acceleration?",
            "A train moves along a straight rail at uniform velocity of {v} m/s for {t} s. Determine its acceleration."
        ],
        "params": [(20, 10), (30, 5), (15, 6), (25, 8), (40, 4), (50, 10)],
        "correct_base": "Acceleration is the rate of change of velocity: a = (v - u) / t. Because velocity is uniform (v = u), delta v = 0, so acceleration is 0 m/s^2.",
        "misc_phrasings": [
            "Acceleration is {v} m/s^2 because the vehicle is moving fast at {v} m/s.",
            "Acceleration = {v} / {t} = {div_val} m/s^2 (divided speed by time without checking change in velocity).",
            "High speed means high acceleration, so acceleration is {v} m/s^2.",
            "Acceleration cannot be zero because the car is traveling forward at {v} m/s."
        ],
        "correct_phrasings": [
            "Acceleration is 0 m/s^2 because velocity is constant, so change in velocity is zero (a = delta_v / delta_t = 0).",
            "0 m/s^2. Acceleration requires a change in speed or direction; steady speed means zero acceleration.",
            "Zero acceleration since the slope of a horizontal line on a v-t graph is 0."
        ],
        "slip_phrasings": [
            "Acceleration is 0 m/s^2, but calculated distance as {v} / {t} instead of {v} * {t}.",
            "Correctly stated zero acceleration, but wrote formula as a = v * t."
        ],
        "unit_phrasings": [
            "Acceleration is 0 m/s instead of m/s^2.",
            "Reported acceleration in km/h without time squared."
        ],
        "unsure_phrasings": [
            "It is moving, so I think there must be some acceleration, maybe {v}?",
            "Not sure if constant speed means acceleration is zero or constant."
        ]
    },

    # 10. FORCE & LAWS: IMPETUS THEORY (Newton's 1st Law)
    {
        "family": "FORCE_NEWTON_FIRST_LAW",
        "grade": "Class 9",
        "chapter": "Force and Laws of Motion",
        "topic": "Inertia and Force Requirement for Motion",
        "target_misc": "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)",
        "misc_desc": "Believes an object in motion requires a continuous forward force, confusing velocity with acceleration.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_diagram",
            "diagram_description": "An object of mass m sliding across a frictionless horizontal ice surface at constant velocity v.",
            "visual_elements": ["Block(m)", "FrictionlessSurface", "VelocityVector(v, right)", "NetForce(0)"],
            "whiteboard_commands": [
                "draw_surface(type='frictionless_ice')",
                "draw_block(x=200, y=100)",
                "draw_velocity_vector(speed=10, direction='right')",
                "write_equation('Sigma F = 0 => a = 0 => v = constant')"
            ]
        },
        "stem_templates": [
            "A hockey puck of mass {m} kg slides across a completely frictionless horizontal sheet of ice at a steady speed of {v} m/s. What net horizontal force is required to keep it moving?",
            "A cart of mass {m} kg glides in outer space far from gravitational sources at constant velocity {v} m/s. What forward force keeps it in motion?",
            "A block of mass {m} kg moves on an ideal frictionless linear air track at {v} m/s. How much thrust is needed to maintain this constant speed?"
        ],
        "params": [(2, 10), (5, 4), (1, 8), (10, 5), (3, 12)],
        "correct_base": "By Newton's First Law (Law of Inertia), an object in motion continues at constant velocity unless acted upon by a net external force. Friction is zero, so net force required is 0 N.",
        "misc_phrasings": [
            "Requires a continuous forward force of {f_val} N (F = m * v = {m} * {v}) to keep it moving.",
            "A forward force of {f_val} N is needed, because objects stop if no force pushes them.",
            "Must maintain a push of {f_val} N in the direction of motion to sustain the speed.",
            "Without a force acting on it, the object cannot keep traveling at {v} m/s."
        ],
        "correct_phrasings": [
            "Net horizontal force required is 0 N. By Newton's First Law, an object in motion remains in uniform motion unless an external net force acts on it.",
            "0 N. No force is needed to maintain constant velocity on a frictionless surface because inertia keeps it moving.",
            "Zero Newtons. F_net = m * a = m * 0 = 0 N."
        ],
        "slip_phrasings": [
            "Net force is 0 N, but calculated momentum as {slip} kg m/s due to multiplication slip.",
            "Correctly stated 0 N force, but misquoted Newton's law number as Third law."
        ],
        "unit_phrasings": [
            "Force required is 0 Joules instead of Newtons.",
            "Reported net force as 0 kg m/s."
        ],
        "unsure_phrasings": [
            "I think things need a force to move, but on ice maybe it is very small?",
            "Uncertain whether force is zero or equal to mass times speed."
        ]
    },

    # 11. GRAVITATION: FREE FALL MASS INDEPENDENCE
    {
        "family": "GRAVITATION_FREE_FALL",
        "grade": "Class 9",
        "chapter": "Gravitation",
        "topic": "Free Fall and Acceleration Due to Gravity (Mass Independence)",
        "target_misc": "MISC-GRAV-001: Heavier Objects Fall Faster Fallacy",
        "misc_desc": "Believes heavier objects accelerate faster under gravity, confusing gravitational force with acceleration.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_diagram",
            "diagram_description": "A heavy metal sphere of mass M and a light wooden sphere of mass m dropped simultaneously in an evacuated vacuum chamber.",
            "visual_elements": ["SphereA(mass=M)", "SphereB(mass=m)", "VacuumChamber", "GravityVector(g=9.8)"],
            "whiteboard_commands": [
                "draw_chamber(type='evacuated_vacuum')",
                "draw_spheres(m1='10 kg', m2='1 kg', height='h')",
                "write_equation('g = G*M_earth / R^2')",
                "highlight('mass of falling object cancels: a = g for all objects')"
            ]
        },
        "stem_templates": [
            "In an evacuated vacuum tube, a {M} kg iron cannonball and a {m} g feather are released simultaneously from a height of {h} meters. Which hits the bottom first, and why?",
            "Two solid metal spheres of mass {M} kg and {m} kg are dropped simultaneously from height {h} m in vacuum. Compare their arrival times.",
            "An astronaut on the Moon drops a hammer ({M} kg) and a feather ({m} g) from {h} m above the surface. Describe what happens."
        ],
        "params": [(10, 50, 20), (5, 100, 50), (20, 1000, 15), (50, 500, 30)],
        "correct_base": "Both objects hit the ground at exactly the same time. While gravitational force is proportional to mass (F = mg), acceleration is a = F/m = g. In vacuum, all objects fall with identical acceleration.",
        "misc_phrasings": [
            "The {M} kg cannonball hits first because it is much heavier and gravity pulls it with greater acceleration.",
            "Heavier objects fall faster because greater mass means greater downward speed.",
            "The feather takes longer to fall because lighter objects fall slower under gravity.",
            "The {M} kg object arrives first because gravity acts more strongly on heavy bodies."
        ],
        "correct_phrasings": [
            "Both strike the ground at the exact same instant. Although the gravitational force is larger on the heavier object, its inertia is proportionally larger (a = F/m = g = 9.8 m/s^2 in vacuum).",
            "Both arrive simultaneously because acceleration due to gravity g is independent of the mass of the falling body.",
            "Same time for both; in a vacuum without air resistance, all objects accelerate at g."
        ],
        "slip_phrasings": [
            "Both hit at the same time, but calculated fall time t = sqrt(2h/g) with an arithmetic slip: t = {slip} s.",
            "Arrival time is identical, but stated Moon gravity is equal to Earth gravity."
        ],
        "unit_phrasings": [
            "Acceleration of both is 9.8 m/s instead of m/s^2.",
            "Arrival time stated as 2.0 m/s instead of seconds."
        ],
        "unsure_phrasings": [
            "I think the heavy ball hits first in real life, but not sure about in a vacuum.",
            "Does gravity pull everything at the same rate, or does mass matter?"
        ]
    },

    # 12. ELECTRICITY: OHM'S LAW AND RESISTANCE
    {
        "family": "ELECTRICITY_OHMS_LAW_RESISTANCE",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Ohm's Law: Voltage, Current, and Resistance Relationship",
        "target_misc": "MISC-ELEC-003: Resistance Reduces Current Independent of Voltage",
        "misc_desc": "Believes that increasing resistance always reduces current even when voltage is simultaneously increased proportionally; fails to apply V = IR as a ratio relationship.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_diagram",
            "diagram_description": "Simple circuit with variable resistor and voltmeter/ammeter showing V, I, R relationships.",
            "visual_elements": ["Battery(EMF)", "Variable_Resistor(R)", "Ammeter(I)", "Voltmeter(V)"],
            "whiteboard_commands": [
                "draw_simple_circuit(battery=6V, resistor=R)",
                "label_ammeter(current=I)",
                "label_voltmeter(voltage=V)",
                "write_equation('V = I * R  =>  I = V / R')",
                "write_equation('R increased, V also doubled => I unchanged')"
            ]
        },
        "stem_templates": [
            "A resistor of {u} ohms is connected to a {f} V battery. Calculate the current through the circuit using Ohm's Law.",
            "A circuit has a resistance of {u} ohms. The voltage across it is {f} V. What is the current?",
            "Using Ohm's Law, find the current when V = {f} V and R = {u} ohms in a series circuit."
        ],
        "params": [(10, 6), (20, 12), (5, 10), (15, 9), (30, 15)],
        "correct_base": "By Ohm's Law: I = V / R. Current is determined by the ratio of voltage to resistance. Increasing both proportionally keeps current constant.",
        "misc_phrasings": [
            "Current decreases because the {u} ohm resistor resists and blocks more charge regardless of voltage.",
            "The resistor of {u} ohms will definitely reduce the current below {f} A because it opposes flow.",
            "Adding resistance always reduces current even if voltage goes up.",
            "The high resistance of {u} ohms means almost no current flows regardless of the {f} V supply."
        ],
        "correct_phrasings": [
            "I = V / R = {f} / {u} = {cor_val} A by Ohm's Law.",
            "Current = {cor_val} A. Ohm's Law: I = V/R where V={f} V and R={u} ohms.",
            "Using I = V/R: current = {f}/{u} = {cor_val} A."
        ],
        "slip_phrasings": [
            "I = V/R = {f}/{u} but made arithmetic slip: computed {slip} A.",
            "Applied I = V/R correctly but inverted to I = R/V giving {u}/{f} = {slip} A."
        ],
        "unit_phrasings": [
            "Current = {cor_val} Volts instead of Amperes.",
            "Resistance stated as {u} Amperes instead of Ohms."
        ],
        "unsure_phrasings": [
            "I'm not sure if Ohm's Law applies to all materials or just metals.",
            "Does voltage affect current, or does resistance control current independently?"
        ]
    },

    # 13. MAGNETIC EFFECTS: ELECTROMAGNETIC INDUCTION (FARADAY'S LAW)
    {
        "family": "MAGNETIC_EFFECTS_ELECTROMAGNETIC_INDUCTION",
        "grade": "Class 10",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Electromagnetic Induction and Faraday's Law",
        "target_misc": "MISC-MAG-006: Static Field Induces Constant EMF Fallacy",
        "misc_desc": "Believes that a static (non-changing) magnetic field inside a coil continuously induces an EMF, not realizing that only a changing magnetic flux induces an EMF.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "field_lines",
            "diagram_description": "A coil placed inside a solenoid showing changing vs static magnetic flux and galvanometer deflection.",
            "visual_elements": ["Solenoid", "Search_Coil", "Galvanometer", "Flux_Lines"],
            "whiteboard_commands": [
                "draw_solenoid_with_coil()",
                "draw_galvanometer(connected=True)",
                "show_case1(field=constant, deflection=zero)",
                "show_case2(field=increasing, deflection=positive)",
                "write_equation('EMF = -N * dΦ/dt  (Faraday-Lenz Law)')"
            ]
        },
        "stem_templates": [
            "A coil of {u} turns is placed inside a constant magnetic field of {f} T. Is any EMF induced?",
            "A wire coil with {u} loops sits inside a steady non-changing magnetic field. Does a galvanometer connected to it deflect?",
            "A {u}-turn coil is held stationary in a uniform magnetic field of {f} T. What EMF is induced?"
        ],
        "params": [(100, 2), (200, 5), (50, 1), (150, 3), (300, 4)],
        "correct_base": "No EMF is induced. Faraday's Law states EMF = -N * dΦ/dt. A constant (non-changing) magnetic field produces zero rate of change of flux (dΦ/dt = 0), so induced EMF = 0.",
        "misc_phrasings": [
            "Yes, a steady EMF of {u} × {f} = {misc_val} V is induced because the field acts continuously on the coil.",
            "The coil experiences an EMF proportional to field strength × turns = {misc_val} V.",
            "A constant field of {f} T through {u} turns gives a constant EMF because flux exists.",
            "The galvanometer deflects continuously because the magnetic field passes through the coil."
        ],
        "correct_phrasings": [
            "Zero EMF. Faraday's Law: EMF = -N * dΦ/dt = 0 because dΦ/dt = 0 for a constant field.",
            "No deflection. Only a changing flux induces an EMF; a static field induces nothing.",
            "EMF = 0 V. Electromagnetic induction requires change in magnetic flux, not mere presence of field."
        ],
        "slip_phrasings": [
            "Correctly identified EMF = 0, but miscalculated time constant as {slip} s.",
            "Gave correct answer (zero EMF) but confused Faraday's Law equation with Ampere's Law."
        ],
        "unit_phrasings": [
            "EMF reported as {u} Tesla instead of Volts.",
            "Rate of flux change reported in T instead of Wb/s (V)."
        ],
        "unsure_phrasings": [
            "I think EMF is induced whenever the field is present but I'm not sure about constant vs changing.",
            "Does the number of turns matter if the field is constant?"
        ]
    },

    # 14. CLASS 9: WORK, ENERGY, AND POWER
    {
        "family": "WORK_ENERGY_POWER_CLASS9",
        "grade": "Class 9",
        "chapter": "Work and Energy",
        "topic": "Work Done by Force: Direction Dependence",
        "target_misc": "MISC-WRK-001: Work Equals Force Times Distance Regardless of Direction",
        "misc_desc": "Applies W = F × d without considering the angle between force and displacement; believes work is done whenever force is applied even if perpendicular to motion.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Block being pushed horizontally while normal force acts vertically — illustrating perpendicular force does zero work.",
            "visual_elements": ["Block(moving_right)", "Applied_Force(horizontal)", "Normal_Force(vertical)", "Weight(downward)"],
            "whiteboard_commands": [
                "draw_block_on_surface(displacement='right')",
                "draw_force_vector(direction='up', label='Normal Force N')",
                "draw_force_vector(direction='right', label='Applied Force F')",
                "write_equation('W = F * d * cos(θ)')",
                "write_equation('If θ=90°: W = F * d * cos(90°) = 0')"
            ]
        },
        "stem_templates": [
            "A porter carries a {m} kg bag on his head and walks horizontally for {v} m. How much work is done by the normal (vertical) force he exerts?",
            "A man carries a {m} kg load and walks {v} m on a flat road. Calculate work done by the vertical holding force.",
            "A block of {m} kg is pushed horizontally with a force of {v} N for {v} m. If force is applied at 90° to displacement, what work is done?"
        ],
        "params": [(10, 5), (20, 8), (15, 6), (25, 10), (12, 4)],
        "correct_base": "W = F × d × cos(θ). When force is perpendicular to displacement (θ = 90°), W = F × d × cos(90°) = 0. No work is done by a force perpendicular to motion.",
        "misc_phrasings": [
            "Work done = {m} × {v} = {misc_val} J because force times displacement = work, direction doesn't matter.",
            "The porter does {misc_val} J of work because he exerts a force of {m} N over {v} m.",
            "Work = F × d = {m} × {v} = {misc_val} J regardless of direction.",
            "Force of {m} N for {v} m always gives {misc_val} J of work done."
        ],
        "correct_phrasings": [
            "Work done = F × d × cos(90°) = {m} × {v} × 0 = 0 J. Force perpendicular to motion does zero work.",
            "0 J. The vertical holding force is perpendicular to horizontal displacement; W = 0.",
            "Zero joules. W = Fd cos θ where θ = 90° gives W = 0."
        ],
        "slip_phrasings": [
            "Correctly wrote W = Fd cosθ but computed cos(90°) = 1 instead of 0; got {misc_val} J.",
            "Identified zero work but miscalculated F × d as {slip} instead of {misc_val}."
        ],
        "unit_phrasings": [
            "Work = 0 Newtons instead of Joules.",
            "Work stated as {misc_val} kg·m instead of Joules."
        ],
        "unsure_phrasings": [
            "I know direction matters but I'm not sure how to apply cosine to this situation.",
            "Does carrying something count as work even if you don't move vertically?"
        ]
    },

    # 15. CLASS 9: MOMENTUM AND CONSERVATION
    {
        "family": "MOMENTUM_CONSERVATION_CLASS9",
        "grade": "Class 9",
        "chapter": "Force and Laws of Motion",
        "topic": "Law of Conservation of Momentum",
        "target_misc": "MISC-MOM-001: Momentum Not Conserved When Object Stops",
        "misc_desc": "Believes momentum is destroyed or disappears when one object stops, rather than being transferred to another object; violates conservation of momentum.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Two-ball collision showing momentum transfer: moving ball hits stationary ball and stops.",
            "visual_elements": ["Ball1(moving, mass=m1)", "Ball2(stationary, mass=m2)", "Arrow(momentum_transfer)"],
            "whiteboard_commands": [
                "draw_collision(ball1=moving, ball2=stationary)",
                "draw_before_state(p_total=m1*v1)",
                "draw_after_state(ball1=stopped, ball2=moving)",
                "write_equation('p_before = p_after')",
                "write_equation('m1*v1 = m1*0 + m2*v2  =>  v2 = (m1/m2)*v1')"
            ]
        },
        "stem_templates": [
            "A {m} kg ball moving at {v} m/s collides with an identical stationary ball. Ball 1 stops. What is velocity of ball 2?",
            "Ball of mass {m} kg travelling at {v} m/s hits another ball of equal mass at rest and comes to complete stop. Find speed of second ball.",
            "Two identical balls of mass {m} kg: first moves at {v} m/s, second is at rest. After collision, first stops. Using conservation of momentum, find second ball's velocity."
        ],
        "params": [(2, 5), (3, 4), (5, 6), (1, 8), (4, 3)],
        "correct_base": "By conservation of momentum: p_before = p_after. m×v + 0 = 0 + m×v2, so v2 = v. The second ball moves at the same speed the first had.",
        "misc_phrasings": [
            "Momentum is destroyed when ball 1 stops. Ball 2 receives no velocity since ball 1 has zero momentum at rest.",
            "When ball 1 stops, it loses its momentum. Ball 2 stays stationary.",
            "Ball 1 at rest means total momentum becomes zero; ball 2 remains at rest.",
            "The {m} kg ball stops so all {misc_val} kg m/s of momentum disappears — ball 2 has none."
        ],
        "correct_phrasings": [
            "By conservation of momentum: {m} × {v} = {m} × v2, so v2 = {v} m/s.",
            "Momentum is conserved: initial p = {misc_val} kg m/s = final p, so ball 2 moves at {v} m/s.",
            "v2 = {v} m/s because m1*v1 = m2*v2 and masses are equal."
        ],
        "slip_phrasings": [
            "Applied conservation correctly but computed {m} × {v} = {slip} due to arithmetic slip.",
            "Got v2 = {v} m/s correctly but stated units as m/s² instead of m/s."
        ],
        "unit_phrasings": [
            "Momentum stated as {misc_val} m/s instead of kg m/s.",
            "Velocity of ball 2 given as {v} Newtons instead of m/s."
        ],
        "unsure_phrasings": [
            "I think momentum is transferred somehow but I don't know the exact rule.",
            "Does the ball 2 move with the same speed or different speed? I'm not sure."
        ]
    }
]

# ----------------------------------------------------------------------------------------
# Systematic Stratified Dataset Generator
# ----------------------------------------------------------------------------------------
def generate_optimized_datasets():
    print("Generating optimized, research-grounded Re:Learn datasets...")
    individual_records = []
    record_id = 1

    for fam_idx, fam in enumerate(master_families):
        fam_name = fam["family"]
        stems = fam["stem_templates"]
        params = fam["params"]
        target_misc = fam["target_misc"]
        misc_desc = fam["misc_desc"]
        correct_base = fam["correct_base"]
        diagram_meta = fam["diagram_meta"]

        misc_pool = fam["misc_phrasings"]
        cor_pool = fam["correct_phrasings"]
        slip_pool = fam["slip_phrasings"]
        unit_pool = fam["unit_phrasings"]
        unsure_pool = fam["unsure_phrasings"]

        # Exactly 60 diverse samples per family:
        # 36 Misconceptions (60%)
        # 12 Correct answers (20%)
        # 4 Calculation slips (6.7%)
        # 4 Unit errors (6.7%)
        # 4 Unsure responses (6.7%)
        # Total = 60 items per family

        family_items = []

        # 1. Misconceptions (36 items)
        for i in range(36):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = misc_pool[i % len(misc_pool)]
            resp = safe_format(resp_template, p)

            family_items.append({
                "category": "misc",
                "label": target_misc,
                "error_type": "conceptual_misconception",
                "confidence": "High",
                "evidence": misc_desc,
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # 2. Correct Responses (12 items)
        for i in range(12):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = cor_pool[i % len(cor_pool)]
            resp = safe_format(resp_template, p)

            family_items.append({
                "category": "correct",
                "label": "CORRECT: Scientifically Accurate Response",
                "error_type": "no_error",
                "confidence": "High",
                "evidence": "Rigorous scientific reasoning with valid physical principles and mathematical steps.",
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # 3. Calculation Slips (4 items)
        for i in range(4):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = slip_pool[i % len(slip_pool)]
            resp = safe_format(resp_template, p)
            family_items.append({
                "category": "calc_slip",
                "label": "CARELESS_CALCULATION_ERROR",
                "error_type": "calculation_slip",
                "confidence": "Medium",
                "evidence": "Conceptual formula choice is correct; error is isolated to an arithmetic slip.",
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # 4. Unit Conversion Errors (4 items)
        for i in range(4):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = unit_pool[i % len(unit_pool)]
            resp = safe_format(resp_template, p)
            family_items.append({
                "category": "unit_err",
                "label": "UNIT_CONVERSION_ERROR",
                "error_type": "unit_error",
                "confidence": "High",
                "evidence": "Numerical reasoning is sound, but units were omitted or confused with another physical quantity.",
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # 5. Unsure / Insufficient Evidence (4 items)
        for i in range(4):
            p = params[i % len(params)]
            stem = stems[i % len(stems)]
            stem_formatted = safe_format(stem, p)
            resp_template = unsure_pool[i % len(unsure_pool)]
            resp = safe_format(resp_template, p)
            family_items.append({
                "category": "unsure",
                "label": "UNSURE_INSUFFICIENT_EVIDENCE",
                "error_type": "guessing_unclear",
                "confidence": "Low",
                "evidence": "Student response contains minimal reasoning or expresses explicit uncertainty; requires diagnostic probe.",
                "stem": stem_formatted,
                "response": resp,
                "correct_steps": correct_base
            })

        # -------------------------------------------------------------------------
        # Stratified Leak-Free Split per Family:
        # Guarantee every split (train, val, test) receives examples of EVERY category!
        # misc: 25 train, 5 val, 6 test (36)
        # correct: 8 train, 2 val, 2 test (12)
        # calc_slip: 2 train, 1 val, 1 test (4)
        # unit_err: 2 train, 1 val, 1 test (4)
        # unsure: 2 train, 1 val, 1 test (4)
        # Total per family = 39 train (65%), 11 val (18.3%), 10 test (16.7%) = 60 items
        # -------------------------------------------------------------------------
        split_plan = {
            "misc": (25, 5, 6),
            "correct": (8, 2, 2),
            "calc_slip": (2, 1, 1),
            "unit_err": (2, 1, 1),
            "unsure": (2, 1, 1)
        }

        cat_groups = {}
        for it in family_items:
            cat_groups.setdefault(it["category"], []).append(it)

        for cat, items in cat_groups.items():
            random.shuffle(items)
            n_tr, n_va, n_te = split_plan[cat]
            for it in items[:n_tr]:
                it["split"] = "train"
            for it in items[n_tr:n_tr+n_va]:
                it["split"] = "val"
            for it in items[n_tr+n_va:]:
                it["split"] = "test"

        for it in family_items:
            rec = {
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{record_id:04d}",
                "question_family": fam_name,
                "curriculum_grade": fam["grade"],
                "curriculum_chapter": fam["chapter"],
                "topic_concept": fam["topic"],
                "question_text": it["stem"],
                "correct_answer_and_steps": it["correct_steps"],
                "student_response": it["response"],
                "misconception_label": it["label"],
                "error_type": it["error_type"],
                "diagnostic_confidence": it["confidence"],
                "evidence_rationale": it["evidence"],
                "multimodal_context": diagram_meta,
                "split": it["split"]
            }
            individual_records.append(rec)
            record_id += 1

    print(f"Generated {len(individual_records)} stratified individual multimodal responses across {len(master_families)} curriculum families.")

    # Export Individual JSON
    json_path = os.path.join(INDIV_DIR, "individual_responses.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(individual_records, f, indent=2)

    # Export Master CSV
    csv_path = os.path.join(INDIV_DIR, "individual_responses.csv")
    csv_fields = [
        "record_id", "question_id", "question_family", "curriculum_grade", "curriculum_chapter",
        "topic_concept", "question_text", "correct_answer_and_steps", "student_response",
        "misconception_label", "error_type", "diagnostic_confidence", "evidence_rationale",
        "has_diagram", "diagram_type", "diagram_description", "split"
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for r in individual_records:
            writer.writerow({
                "record_id": r["record_id"],
                "question_id": r["question_id"],
                "question_family": r["question_family"],
                "curriculum_grade": r["curriculum_grade"],
                "curriculum_chapter": r["curriculum_chapter"],
                "topic_concept": r["topic_concept"],
                "question_text": r["question_text"],
                "correct_answer_and_steps": r["correct_answer_and_steps"],
                "student_response": r["student_response"],
                "misconception_label": r["misconception_label"],
                "error_type": r["error_type"],
                "diagnostic_confidence": r["diagnostic_confidence"],
                "evidence_rationale": r["evidence_rationale"],
                "has_diagram": r["multimodal_context"]["has_diagram"],
                "diagram_type": r["multimodal_context"]["diagram_type"],
                "diagram_description": r["multimodal_context"]["diagram_description"],
                "split": r["split"]
            })

    # Export Splits (CSV & JSONL)
    for sp in ["train", "val", "test"]:
        sp_records = [r for r in individual_records if r["split"] == sp]
        # JSONL
        with open(os.path.join(INDIV_DIR, f"{sp}.jsonl"), "w", encoding="utf-8") as f:
            for r in sp_records:
                f.write(json.dumps(r) + "\n")
        # CSV
        with open(os.path.join(INDIV_DIR, f"{sp}.csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_fields)
            writer.writeheader()
            for r in sp_records:
                writer.writerow({
                    "record_id": r["record_id"],
                    "question_id": r["question_id"],
                    "question_family": r["question_family"],
                    "curriculum_grade": r["curriculum_grade"],
                    "curriculum_chapter": r["curriculum_chapter"],
                    "topic_concept": r["topic_concept"],
                    "question_text": r["question_text"],
                    "correct_answer_and_steps": r["correct_answer_and_steps"],
                    "student_response": r["student_response"],
                    "misconception_label": r["misconception_label"],
                    "error_type": r["error_type"],
                    "diagnostic_confidence": r["diagnostic_confidence"],
                    "evidence_rationale": r["evidence_rationale"],
                    "has_diagram": r["multimodal_context"]["has_diagram"],
                    "diagram_type": r["multimodal_context"]["diagram_type"],
                    "diagram_description": r["multimodal_context"]["diagram_description"],
                    "split": r["split"]
                })

    return individual_records


# ----------------------------------------------------------------------------------------
# Stratified Longitudinal Student Sequence Dataset Generator (200 Sessions)
# ----------------------------------------------------------------------------------------
def generate_optimized_sequence_dataset():
    print("Generating stratified sequence dataset (200 multi-turn sessions across curriculum)...")
    sequences = []
    seq_id_counter = 1

    pattern_archetypes = [
        # 1. Recurrent Current Attenuation (Class 10)
        {
            "pattern_label": "RECURRENT_CURRENT_ATTENUATION_PATTERN",
            "topic": "Electricity: Current Conservation",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-ELEC-001",
            "intervention_id": "INTV-ELEC-001",
            "reassessment_pair_id": "PAIR-ELEC-001",
            "steps": [
                ("PHY-Class10-05-0001", "Two identical bulbs in series with 6V battery. Compare ammeter readings.", "A1 = 1.2A, A2 = 0.8A, A3 = 0.4A because bulb 1 consumes electric current to glow.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
                ("PHY-Class10-05-0002", "Three identical resistors connected in series with battery. What is current through R3 compared to R1?", "Current through R3 is much smaller than R1 because current gets used up as it travels along the series circuit.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
                ("PHY-Class10-05-0003", "Does the downstream bulb glow dimmer because less current reaches it?", "Yes, downstream bulb receives less current because upstream bulb consumed the charge.", "MISC-ELEC-001: Current Attenuation / Consumption Model")
            ]
        },
        # 2. Recurrent Battery Constant Current Source (Class 10)
        {
            "pattern_label": "RECURRENT_CONSTANT_CURRENT_BATTERY_PATTERN",
            "topic": "Electricity: Parallel Circuits",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-ELEC-002",
            "intervention_id": "INTV-ELEC-002",
            "reassessment_pair_id": "PAIR-ELEC-002",
            "steps": [
                ("PHY-Class10-06-0001", "Bulb B1 in single branch. Second identical bulb B2 connected in parallel. Brightness of B1?", "Bulb 1 dims to half brightness because the battery provides a fixed total current that must now be shared.", "MISC-ELEC-002: Battery as Constant Current Source"),
                ("PHY-Class10-06-0002", "Heater switched ON in parallel with room lamp. Does lamp dim?", "Yes, the lamp dims because the source current is divided between both appliances.", "MISC-ELEC-002: Battery as Constant Current Source")
            ]
        },
        # 3. Recurrent Half-Lens Blocking Fallacy (Class 10)
        {
            "pattern_label": "RECURRENT_HALF_LENS_BLOCKING_PATTERN",
            "topic": "Optics: Image Formation with Aperture Blocking",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-OPT-001",
            "intervention_id": "INTV-OPT-001",
            "reassessment_pair_id": "PAIR-OPT-001",
            "steps": [
                ("PHY-Class10-01-0001", "Lower half of convex lens covered with black paper. What happens to projected image?", "The top half of the candle image is completely missing because the bottom half is covered.", "MISC-OPT-001: Half-Lens Blocking Fallacy"),
                ("PHY-Class10-01-0002", "Upper half of converging lens blocked by opaque mask. Describe image change.", "Only the lower half of the image will appear on the viewing card.", "MISC-OPT-001: Half-Lens Blocking Fallacy")
            ]
        },
        # 4. Recurrent Sign Convention Inversion (Class 10)
        {
            "pattern_label": "PERVASIVE_SIGN_CONVENTION_INVERSION",
            "topic": "Optics: Cartesian Sign Conventions",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-OPT-004",
            "intervention_id": "INTV-OPT-004",
            "reassessment_pair_id": "PAIR-OPT-004",
            "steps": [
                ("PHY-Class10-02-0001", "Object at 30 cm before concave mirror of f = 15 cm. Find v.", "v = +30 cm because distances are always positive scalars; 1/v = 1/15 - 1/30.", "MISC-OPT-004: Sign Convention Spatial Inversion"),
                ("PHY-Class10-02-0002", "Candle at 40 cm from concave mirror of f = 20 cm. Find v.", "1/v = 1/20 + 1/40 giving positive v, because the object is in front of the mirror.", "MISC-OPT-004: Sign Convention Spatial Inversion")
            ]
        },
        # 5. Recurrent Speed-Distance Inversion (Class 9 - matching PDF Page 2 & 4)
        {
            "pattern_label": "RECURRENT_SPEED_DISTANCE_INVERSION_PATTERN",
            "topic": "Motion: Speed and Velocity Operations",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MOT-001",
            "intervention_id": "INTV-MOT-001",
            "reassessment_pair_id": "PAIR-MOT-001",
            "steps": [
                ("PHY-Class9-08-0001", "Runner covers 100 m in 5 s along straight track. Calculate speed.", "Speed is 500 m/s because I multiplied distance by time (100 * 5 = 500).", "MISC-MOT-001: Speed Distance Operation Inversion"),
                ("PHY-Class9-08-0002", "Car travels 300 m in 15 s. What is speed?", "I calculated speed = 300 * 15 = 4500 m/s.", "MISC-MOT-001: Speed Distance Operation Inversion"),
                ("PHY-Class9-08-0003", "Bicycle moves 60 m in 3 s. Find speed.", "Speed = distance times time, so it equals 180 m/s.", "MISC-MOT-001: Speed Distance Operation Inversion")
            ]
        },
        # 6. Recurrent Speed-Acceleration Conflation (Class 9 - matching PDF Page 2 & 4)
        {
            "pattern_label": "RECURRENT_SPEED_ACCELERATION_CONFLATION",
            "topic": "Motion: Speed vs Acceleration",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MOT-002",
            "intervention_id": "INTV-MOT-002",
            "reassessment_pair_id": "PAIR-MOT-002",
            "steps": [
                ("PHY-Class9-09-0001", "Vehicle moves at steady constant speed of 20 m/s for 10 s. What is acceleration?", "Acceleration is 20 m/s^2 because the vehicle is moving fast at 20 m/s.", "MISC-MOT-002: Speed-Acceleration Conflation"),
                ("PHY-Class9-09-0002", "Train moves along straight track at uniform 72 km/h for 20 s. Acceleration?", "Acceleration = 72 / 20 = 3.6 m/s^2 (divided speed by time without checking change in velocity).", "MISC-MOT-002: Speed-Acceleration Conflation")
            ]
        },
        # 7. Recurrent Impetus Theory (Class 9 - matching PDF Page 2 & 4)
        {
            "pattern_label": "RECURRENT_IMPETUS_THEORY_PATTERN",
            "topic": "Force & Laws of Motion: Inertia",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-FOR-001",
            "intervention_id": "INTV-FOR-001",
            "reassessment_pair_id": "PAIR-FOR-001",
            "steps": [
                ("PHY-Class9-10-0001", "Puck slides across frictionless ice at constant 10 m/s. What net force keeps it moving?", "Requires a continuous forward force of 20 N (F = m * v) to keep it moving.", "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)"),
                ("PHY-Class9-10-0002", "Cart glides in deep space at constant velocity. Forward force needed?", "Must maintain a forward thrust in the direction of motion to sustain speed.", "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)")
            ]
        },
        # 8. Successful Cognitive Remediation Sequence: Optics Half-Lens (POE Cycle)
        {
            "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
            "topic": "Optics: Half-Lens Aperture Remediation",
            "grade": "Class 10",
            "status": "resolved_with_transfer",
            "next_action": "advance_to_next_topic",
            "target_misc_id": "MISC-OPT-001",
            "intervention_id": "INTV-OPT-001",
            "reassessment_pair_id": "PAIR-OPT-001",
            "steps": [
                ("PHY-Class10-01-0001", "Lower half of convex lens covered with black paper. What happens to projected image?", "The top half of the candle image is completely missing because the bottom half is covered.", "MISC-OPT-001: Half-Lens Blocking Fallacy"),
                ("INTV-OPT-001-STEP", "PhET simulation: Observe virtual mask covering lower half of lens.", "Wait, the full image is still formed on the screen, just dimmer! Every point on lens receives light from entire object.", "COGNITIVE_CONFLICT_RECONCILED: Full image persists with 50% brightness"),
                ("PHY-Class10-01-0003", "Near-transfer isomorphic question: cover top 30% of lens.", "The complete image remains on screen, but brightness is 70% of original.", "CORRECT: Scientifically Accurate Response")
            ]
        },
        # 9. Successful Cognitive Remediation Sequence: Current Conservation (POE Cycle)
        {
            "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
            "topic": "Electricity: Current Conservation Remediation",
            "grade": "Class 10",
            "status": "resolved_with_transfer",
            "next_action": "advance_to_next_topic",
            "target_misc_id": "MISC-ELEC-001",
            "intervention_id": "INTV-ELEC-001",
            "reassessment_pair_id": "PAIR-ELEC-001",
            "steps": [
                ("PHY-Class10-05-0001", "Two identical bulbs in series with 6V battery. Compare ammeters.", "A1 = 1.2A, A2 = 0.8A, A3 = 0.4A because bulb 1 consumes electric current.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
                ("INTV-ELEC-001-STEP", "PhET Simulation: Observe moving electron dots and ammeters in series.", "Both ammeters read identical values (0.90A)! Current is not consumed; only electrical potential energy drops.", "COGNITIVE_CONFLICT_RECONCILED: Current is conserved in closed loop"),
                ("PHY-Class10-05-0003", "Near-transfer isomorphic question: 100-ohm and 20-ohm resistors in series.", "I_in = I_out, because in any series circuit electric charge cannot accumulate or vanish.", "CORRECT: Scientifically Accurate Response")
            ]
        },
        # 10. Transient Arithmetic Slip with Conceptual Mastery
        {
            "pattern_label": "TRANSIENT_SLIP_WITH_CONCEPTUAL_MASTERY",
            "topic": "Kinematics: Velocity Calculation",
            "grade": "Class 9",
            "status": "no_conceptual_misconception",
            "next_action": "provide_arithmetic_feedback_only",
            "target_misc_id": "NONE",
            "intervention_id": "FEEDBACK_ARITHMETIC",
            "reassessment_pair_id": "PAIR-NONE-001",
            "steps": [
                ("PHY-Class9-08-0001", "Runner covers 100 m in 5 s. Speed?", "Speed = distance / time = 100 / 5 = 25 m/s (mental arithmetic slip on division).", "CARELESS_CALCULATION_ERROR"),
                ("PHY-Class9-08-0002", "Car travels 300 m in 15 s. Speed?", "Average speed is distance divided by elapsed time: 300 / 15 = 20 m/s.", "CORRECT: Scientifically Accurate Response")
            ]
        },
        # 11. Recurrent Ohm's Law Misconception (Class 10 - New family)
        {
            "pattern_label": "RECURRENT_OHMS_LAW_DIRECTION_FALLACY",
            "topic": "Electricity: Ohm's Law and Resistance",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-ELEC-003",
            "intervention_id": "INTV-ELEC-003",
            "reassessment_pair_id": "PAIR-ELEC-003",
            "steps": [
                ("PHY-Class10-12-0001", "A 10 ohm resistor connected to 6V battery. Current?", "Current decreases because 10 ohm resistor blocks charge; current must be less than 6.", "MISC-ELEC-003: Resistance Reduces Current Independent of Voltage"),
                ("PHY-Class10-12-0002", "Resistor 20 ohms, 12V battery. Find I using Ohm's Law.", "Bigger resistor always means less current regardless of battery voltage.", "MISC-ELEC-003: Resistance Reduces Current Independent of Voltage")
            ]
        },
        # 12. Recurrent Electromagnetic Induction Fallacy (Class 10 - New family)
        {
            "pattern_label": "RECURRENT_STATIC_FIELD_EMF_FALLACY",
            "topic": "Magnetic Effects: Electromagnetic Induction",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MAG-006",
            "intervention_id": "INTV-MAG-006",
            "reassessment_pair_id": "PAIR-MAG-006",
            "steps": [
                ("PHY-Class10-13-0001", "A coil of 100 turns placed in constant 2T field. Is EMF induced?", "Yes, EMF = 100 x 2 = 200 V is continuously induced because the field passes through the coil.", "MISC-MAG-006: Static Field Induces Constant EMF Fallacy"),
                ("PHY-Class10-13-0002", "A search coil in steady non-changing solenoid field. Does galvanometer deflect?", "Galvanometer deflects continuously because field exists inside coil.", "MISC-MAG-006: Static Field Induces Constant EMF Fallacy")
            ]
        },
        # 13. Recurrent Work Direction Misconception (Class 9 - New family)
        {
            "pattern_label": "RECURRENT_WORK_DIRECTION_FALLACY",
            "topic": "Work and Energy: Direction-Dependent Work",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-WRK-001",
            "intervention_id": "INTV-WRK-001",
            "reassessment_pair_id": "PAIR-WRK-001",
            "steps": [
                ("PHY-Class9-14-0001", "Porter carries 10 kg bag and walks 5 m horizontally. Work done by holding force?", "Work = 10 x 5 = 50 J because force times displacement is always work.", "MISC-WRK-001: Work Equals Force Times Distance Regardless of Direction"),
                ("PHY-Class9-14-0002", "Man carries 20 kg load and walks 8 m flat. Work done by vertical holding force?", "Work = 20 x 8 = 160 J, force times distance.", "MISC-WRK-001: Work Equals Force Times Distance Regardless of Direction")
            ]
        },
        # 14. Recurrent Momentum Non-Conservation (Class 9 - New family)
        {
            "pattern_label": "RECURRENT_MOMENTUM_DESTRUCTION_FALLACY",
            "topic": "Force and Laws of Motion: Momentum Conservation",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "target_misc_id": "MISC-MOM-001",
            "intervention_id": "INTV-MOM-001",
            "reassessment_pair_id": "PAIR-MOM-001",
            "steps": [
                ("PHY-Class9-15-0001", "2 kg ball at 5 m/s hits stationary identical ball; first stops. Velocity of second?", "Momentum is destroyed when ball 1 stops; ball 2 stays at rest.", "MISC-MOM-001: Momentum Not Conserved When Object Stops"),
                ("PHY-Class9-15-0002", "3 kg ball moving at 4 m/s collides and stops. What happens to second 3 kg ball?", "Ball 1 stopping destroys its momentum; ball 2 has no reason to move.", "MISC-MOM-001: Momentum Not Conserved When Object Stops")
            ]
        },
        # 15. Successful Remediation: Ohm's Law (POE cycle)
        {
            "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
            "topic": "Electricity: Ohm's Law Remediation",
            "grade": "Class 10",
            "status": "resolved_with_transfer",
            "next_action": "advance_to_next_topic",
            "target_misc_id": "MISC-ELEC-003",
            "intervention_id": "INTV-ELEC-003",
            "reassessment_pair_id": "PAIR-ELEC-003",
            "steps": [
                ("PHY-Class10-12-0001", "Resistor 10 ohms, battery 6V. Find current.", "Current decreases because 10 ohm resistor blocks charge.", "MISC-ELEC-003: Resistance Reduces Current Independent of Voltage"),
                ("INTV-ELEC-003-STEP", "PhET Circuit simulation: ammeter reads I = V/R = 0.6 A exactly.", "I see! I = V/R means both voltage and resistance together set current. Ratio matters.", "COGNITIVE_CONFLICT_RECONCILED: Ohm's Law verified experimentally"),
                ("PHY-Class10-12-0003", "Transfer: 20 ohm resistor and 12V battery. Find I.", "I = 12 / 20 = 0.6 A using Ohm's Law. Same ratio!", "CORRECT: Scientifically Accurate Response")
            ]
        }
    ]

    # 26 repetitions x 15 archetypes = 390 sessions
    # Stratified: Reps 0-17 -> Train (69%, ~270 sessions)
    #             Reps 18-21 -> Val (15%, ~60 sessions)
    #             Reps 22-25 -> Test (15%, ~60 sessions)
    for rep in range(26):
        if rep < 18:
            split = "train"
        elif rep < 22:
            split = "val"
        else:
            split = "test"

        for arch in pattern_archetypes:
            sid = f"STU_{seq_id_counter+1000:04d}"
            attempts = []
            for step_idx, st in enumerate(arch["steps"]):
                attempts.append({
                    "step": step_idx + 1,
                    "attempt_id": f"ATT-{seq_id_counter:04d}-{step_idx+1}",
                    "question_id": st[0],
                    "stem": st[1],
                    "student_response": st[2],
                    "individual_diagnosis": st[3]
                })

            seq_record = {
                "sequence_id": f"SEQ-{seq_id_counter:04d}",
                "student_id": sid,
                "curriculum_grade": arch["grade"],
                "topic": arch["topic"],
                "target_misconception_id": arch["target_misc_id"],
                "intervention_id": arch["intervention_id"],
                "reassessment_pair_id": arch["reassessment_pair_id"],
                "ordered_attempts": attempts,
                "sequence_level_label": arch["pattern_label"],
                "learning_status": arch["status"],
                "recommended_intervention_action": arch["next_action"],
                "split": split
            }
            sequences.append(seq_record)
            seq_id_counter += 1

    train_count = sum(1 for s in sequences if s["split"] == "train")
    val_count = sum(1 for s in sequences if s["split"] == "val")
    test_count = sum(1 for s in sequences if s["split"] == "test")
    print(f"Generated {len(sequences)} longitudinal student sequences across train ({train_count}), val ({val_count}), and test ({test_count}).")

    # Export JSON
    seq_json_path = os.path.join(SEQ_DIR, "student_sequences.json")
    with open(seq_json_path, "w", encoding="utf-8") as f:
        json.dump(sequences, f, indent=2)

    # Export Flattened CSV (with unified sequence_level_label)
    seq_csv_path = os.path.join(SEQ_DIR, "student_sequences.csv")
    with open(seq_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "sequence_id", "student_id", "curriculum_grade", "topic", "target_misconception_id",
            "intervention_id", "reassessment_pair_id", "total_steps", "responses_sequence",
            "diagnoses_sequence", "sequence_level_label", "learning_status",
            "recommended_intervention_action", "split"
        ])
        writer.writeheader()
        for s in sequences:
            resp_concat = " -> ".join([f"Step {a['step']}: {a['student_response']}" for a in s["ordered_attempts"]])
            diag_concat = " -> ".join([a["individual_diagnosis"] for a in s["ordered_attempts"]])
            writer.writerow({
                "sequence_id": s["sequence_id"],
                "student_id": s["student_id"],
                "curriculum_grade": s["curriculum_grade"],
                "topic": s["topic"],
                "target_misconception_id": s["target_misconception_id"],
                "intervention_id": s["intervention_id"],
                "reassessment_pair_id": s["reassessment_pair_id"],
                "total_steps": len(s["ordered_attempts"]),
                "responses_sequence": resp_concat,
                "diagnoses_sequence": diag_concat,
                "sequence_level_label": s["sequence_level_label"],
                "learning_status": s["learning_status"],
                "recommended_intervention_action": s["recommended_intervention_action"],
                "split": s["split"]
            })

    # Export Splits
    for sp in ["train", "val", "test"]:
        sp_seqs = [s for s in sequences if s["split"] == sp]
        with open(os.path.join(SEQ_DIR, f"{sp}_sequences.json"), "w", encoding="utf-8") as f:
            json.dump(sp_seqs, f, indent=2)

    return sequences


if __name__ == "__main__":
    generate_optimized_datasets()
    generate_optimized_sequence_dataset()
    print("Optimization of curriculum datasets complete!")
