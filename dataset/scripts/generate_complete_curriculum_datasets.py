import json
import csv
import os
import random

random.seed(42)

BASE_DIR = r"d:\relearn\dataset"
INDIV_DIR = os.path.join(BASE_DIR, "individual_response_dataset")
SEQ_DIR = os.path.join(BASE_DIR, "sequence_dataset")

os.makedirs(INDIV_DIR, exist_ok=True)
os.makedirs(SEQ_DIR, exist_ok=True)

# ----------------------------------------------------------------------------------------
# Class 9, 10, 11 & 12 Comprehensive Master Families (23 Families across High School & Senior Secondary)
# ----------------------------------------------------------------------------------------
master_families = [
    # ========================== CLASS 9 PHYSICS ==========================
    {
        "family": "MOTION_SPEED_DISTANCE_TIME",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Speed and Velocity (Distance-Time Relationship)",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_diagram",
            "diagram_description": "A straight road track marked with intervals. Runner completes the track distance in a given elapsed time.",
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
        "target_misc": "MISC-MOT-001: Speed Distance Operation Inversion",
        "misc_desc": "Multiplies distance by time instead of dividing.",
        "correct_func": lambda d, t: f"Speed = Distance / Time = {d} m / {t} s = {d//t if d%t==0 else round(d/t,1)} m/s."
    },
    {
        "family": "MOTION_SPEED_VS_ACCELERATION",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Acceleration vs Speed / Velocity",
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
        "target_misc": "MISC-MOT-002: Speed-Acceleration Conflation",
        "misc_desc": "Conflates speed with acceleration; assumes high speed means high acceleration or divides speed by total time.",
        "correct_func": lambda v, t: f"Acceleration is the rate of change of velocity: a = (v - u)/t. Since velocity is uniform ({v} m/s), delta v = 0, so a = 0 m/s^2."
    },
    {
        "family": "FORCE_NEWTON_FIRST_LAW",
        "grade": "Class 9",
        "chapter": "Force and Laws of Motion",
        "topic": "Inertia and Force Requirement for Motion",
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
        "target_misc": "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)",
        "misc_desc": "Believes an object in motion requires a continuous forward force, confusing velocity with acceleration.",
        "correct_func": lambda m, v: f"By Newton's First Law (Law of Inertia), an object in motion continues at constant velocity unless acted upon by a net external force. Friction is zero, so net force needed is 0 N."
    },
    {
        "family": "FORCE_NEWTON_THIRD_LAW",
        "grade": "Class 9",
        "chapter": "Force and Laws of Motion",
        "topic": "Action and Reaction Forces (Simultaneous Interaction)",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Two bodies A and B interacting during a collision or mutual contact force.",
            "visual_elements": ["BodyA(mass=M)", "BodyB(mass=m)", "ContactForceVector"],
            "whiteboard_commands": [
                "draw_boxes(m1='heavy_truck', m2='small_car')",
                "draw_vector(from='truck', to='car', label='F_truck_on_car')",
                "draw_vector(from='car', to='truck', label='F_car_on_truck')",
                "write_equation('|F_12| = |F_21| (Opposite directions, different bodies)')"
            ]
        },
        "stem_templates": [
            "A heavy truck of mass {M} kg collides head-on with a small compact car of mass {m} kg. How does the magnitude of the force exerted by the truck on the car compare to the force exerted by the car on the truck?",
            "A bowler rolls a heavy bowling ball of mass {M} kg into a light plastic pin of mass {m} kg. Compare the force exerted on the pin by the ball with the force exerted on the ball by the pin.",
            "A heavyweight boxer strikes a light punching bag. How does the contact force on the bag compare to the contact force felt by the boxer's glove?"
        ],
        "params": [(3000, 1000), (5000, 800), (7, 1), (1500, 500)],
        "target_misc": "MISC-FOR-002: Dominant Mass Exerts Greater Force Fallacy",
        "misc_desc": "Believes the heavier or moving object exerts a larger force than the lighter object in an interaction.",
        "correct_func": lambda M, m: f"By Newton's Third Law of Motion, every action has an equal and opposite reaction. The magnitude of force exerted by the truck on the car is exactly equal to the force exerted by the car on the truck (|F_truck| = |F_car|). The car experiences higher acceleration because a = F/m."
    },
    {
        "family": "GRAVITATION_FREE_FALL",
        "grade": "Class 9",
        "chapter": "Gravitation",
        "topic": "Free Fall and Acceleration Due to Gravity (Mass Independence)",
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
            "Two solid metal spheres of mass {M} kg and {m} kg are dropped simultaneously from the Leaning Tower of Pisa (height {h} m), ignoring air resistance. Compare their arrival times.",
            "An astronaut on the Moon drops a hammer ({M} kg) and a feather ({m} g) from {h} m above the surface. Describe what happens."
        ],
        "params": [(10, 0.05, 20), (5, 0.1, 50), (20, 1, 15), (50, 0.5, 30)],
        "target_misc": "MISC-GRAV-001: Heavier Objects Fall Faster Fallacy",
        "misc_desc": "Believes heavier objects accelerate faster under gravity, confusing gravitational force with acceleration.",
        "correct_func": lambda M, m, h: f"Both objects hit the ground at exactly the same time. While gravitational force is proportional to mass (F = mg), acceleration is a = F/m = (mg)/m = g. In vacuum, all objects fall with the identical gravitational acceleration g = 9.8 m/s^2."
    },
    {
        "family": "WORK_ENERGY_DISPLACEMENT",
        "grade": "Class 9",
        "chapter": "Work and Energy",
        "topic": "Scientific Definition of Work (W = F * s * cos theta)",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "A person holding a heavy briefcase of mass m stationary in their hands for time t.",
            "visual_elements": ["Person", "Briefcase(mass=m)", "Stationary(displacement=0)", "MuscularEffort"],
            "whiteboard_commands": [
                "draw_person_holding_weight(m='20 kg', s='0 m')",
                "write_equation('W = F * s')",
                "highlight('s = 0 => W = 0 Joules (Zero physical work)')"
            ]
        },
        "stem_templates": [
            "A porter holds a heavy suitcase of mass {m} kg on his head for {t} minutes while standing stationary on a platform. How much scientific work is done by the porter on the suitcase?",
            "A student pushes against a rigid concrete wall with a force of {F} N for {t} minutes without the wall moving. Calculate the work done on the wall.",
            "A weightlifter holds a barbell of {m} kg steady overhead at a height of 2 m for {t} seconds without moving. What is the work done on the barbell during this hold?"
        ],
        "params": [(20, 15, 200), (30, 10, 300), (50, 5, 500), (15, 20, 150)],
        "target_misc": "MISC-WRK-001: Muscular Effort Equals Mechanical Work",
        "misc_desc": "Equates biological feeling of fatigue with physics work, ignoring the requirement for displacement (s > 0).",
        "correct_func": lambda m, t, F: f"Work done is defined as W = F * s * cos(theta). Because the displacement s = 0, the mechanical work done on the object is exactly 0 Joules, regardless of muscular exertion."
    },

    # ========================== CLASS 10 PHYSICS ==========================
    {
        "family": "OPTICS_HALF_LENS_BLOCKING",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Image Formation and Aperture of Convex Lens",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Convex lens with lower half covered by black opaque cardboard. Object placed beyond 2F forms a complete real inverted image on the screen.",
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
            "An experimenter covers 50% of a convex lens with black tape. How does this affect the image formed by the lens on a viewing card?"
        ],
        "params": [(15,), (20,), (10,), (25,), (12,)],
        "target_misc": "MISC-OPT-001: Half-Lens Blocking Fallacy",
        "misc_desc": "Believes covering half the lens cuts the image in half, misunderstanding that every point on the lens receives light from every point on the object.",
        "correct_func": lambda f: f"The image remains completely intact and full. Every exposed portion of the lens refracts light rays from all parts of the object. Covering 50% of the lens area simply halves the transmitted light flux, reducing image brightness without cropping."
    },
    {
        "family": "OPTICS_CARTESIAN_SIGN_CONVENTION",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "New Cartesian Sign Convention in Mirror Formula",
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
            "A pin is positioned {u} cm to the left of a concave mirror of radius of curvature {r} cm (focal length {f} cm). Determine the image distance v."
        ],
        "params": [(30, 15, 30), (40, 20, 40), (25, 10, 20), (60, 20, 40)],
        "target_misc": "MISC-OPT-004: Sign Convention Spatial Inversion",
        "misc_desc": "Omits negative signs for real object distance u and concave focal length f, treating distances as positive scalars.",
        "correct_func": lambda u, f, r: f"By Cartesian sign convention: u = -{u} cm, f = -{f} cm. 1/f = 1/v + 1/u => -1/{f} = 1/v - 1/{u} => 1/v = -1/{f} + 1/{u}. Yields v = -{round(1/(-1/f + 1/u), 1)} cm (real, inverted image in front of mirror)."
    },
    {
        "family": "HUMAN_EYE_VISION_DEFECTS",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Myopia and Hypermetropia Correction",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "eye_defect_diagram",
            "diagram_description": "Myopic eyeball where parallel rays from distant object focus in front of the retina. Concave diverging lens corrects focus back to retina.",
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
        "target_misc": "MISC-EYE-001: Vision Defect Corrective Inversion",
        "misc_desc": "Inverts corrective lens assignment (prescribing convex converging lenses for nearsightedness/myopia).",
        "correct_func": lambda fp: f"The condition is Myopia (nearsightedness), where parallel rays converge in front of the retina due to excessive corneal curvature or eyeball elongation. A Concave (diverging) lens is required to slightly diverge rays before entering the eye."
    },
    {
        "family": "HUMAN_EYE_PRISM_DISPERSION",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Dispersion of White Light through a Glass Prism",
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
        "target_misc": "MISC-EYE-002: Prism Dispersion Speed and Deviation Inversion",
        "misc_desc": "Believes red bends the most because it is 'strongest', or claims violet travels fastest inside the glass medium.",
        "correct_func": lambda p: f"Violet light has the shortest wavelength and experiences the highest refractive index in glass (n_violet > n_red). Therefore, violet bends the most. Red light has the longest wavelength, travels fastest in glass (v = c/n), and bends the least."
    },
    {
        "family": "ELECTRICITY_CURRENT_CONSERVATION",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Current Conservation in a Series Circuit",
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
        "target_misc": "MISC-ELEC-001: Current Attenuation / Consumption Model",
        "misc_desc": "Believes electric current is consumed or 'used up' by electrical loads as it travels around the circuit loop.",
        "correct_func": lambda V, I, R: f"Electric current is the continuous rate of flow of electric charge (I = dQ/dt). By charge conservation, charges cannot accumulate or vanish in a single-loop series circuit. Therefore, A1 = A2 = A3 = {I} A exactly. The bulbs consume electrical potential energy (voltage drop), not current."
    },
    {
        "family": "ELECTRICITY_PARALLEL_BATTERY_DELIVERY",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Current Delivery of Battery in Parallel Circuits",
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
        "target_misc": "MISC-ELEC-002: Battery as Constant Current Source",
        "misc_desc": "Believes a battery produces a fixed amount of total current, assuming adding parallel branches splits and reduces existing current.",
        "correct_func": lambda V, R: f"An ideal battery maintains a constant potential difference (voltage V). In parallel, the voltage across Branch 1 remains constant at {V} V, so its current I1 = V/R1 is unchanged (brightness stays identical). Adding the second branch decreases the equivalent circuit resistance, causing the battery to supply twice the total current (I_total = I1 + I2)."
    },
    {
        "family": "MAGNETIC_EFFECTS_LORENTZ_LEFT_HAND",
        "grade": "Class 10",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Magnetic Force on Current-Carrying Conductor (Fleming's Left Hand Rule)",
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
        "target_misc": "MISC-MAG-005: Directional Hand Rule Inversion",
        "misc_desc": "Swaps left and right hands, swaps thumb and index fingers, or forgets to invert force direction for negative charges.",
        "correct_func": lambda p: f"By Fleming's Left-Hand Rule: Forefinger points North (Field), Middle finger points East (Current). The extended Thumb points vertically Upwards (out of page). For negatively charged electrons, current direction is opposite to velocity (West), so force points vertically Downwards (into page)."
    },

    # ========================== CLASS 11 PHYSICS ==========================
    {
        "family": "KINEMATICS_PROJECTILE_INDEPENDENCE",
        "grade": "Class 11",
        "chapter": "Motion in a Plane (Kinematics)",
        "topic": "Independence of Horizontal and Vertical Components in Projectile Motion",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_diagram",
            "diagram_description": "Ball A dropped vertically from rest from height h, and Ball B fired horizontally at initial speed v0 from the identical height h.",
            "visual_elements": ["BallA(u_y=0, u_x=0)", "BallB(u_y=0, u_x=v0)", "HeightH", "GravityVector(g)"],
            "whiteboard_commands": [
                "draw_cliff(height='h')",
                "plot_trajectory_drop(ball='A', color='blue')",
                "plot_trajectory_projectile(ball='B', v0='20 m/s', color='orange')",
                "write_equation('t_A = sqrt(2h/g) = t_B (Vertical acceleration is independent of horizontal velocity)')"
            ]
        },
        "stem_templates": [
            "Two identical metal spheres A and B are at height {h} meters above the level ground. Sphere A is dropped from rest, while Sphere B is simultaneously fired horizontally at {v0} m/s. Neglecting air resistance, which sphere strikes the ground first?",
            "A hunter fires a rifle horizontally at speed {v0} m/s from height {h} m, and simultaneously drops a bullet from the same height. Compare the time taken by each bullet to reach the ground.",
            "An airplane flying horizontally at speed {v0} m/s drops an emergency package from altitude {h} m. How does the vertical fall time compare to a package dropped from a stationary helicopter at the same altitude?"
        ],
        "params": [(45, 20), (20, 15), (80, 40), (125, 50)],
        "target_misc": "MISC-KIN-001: Horizontal Motion Postpones Gravitational Fall",
        "misc_desc": "Believes high horizontal velocity 'defies' or delays gravity, predicting the horizontally launched projectile takes longer to fall.",
        "correct_func": lambda h, v0: f"Both spheres strike the ground at the exact same instant. Vertical motion and horizontal motion are completely independent (orthogonal vectors). In the vertical direction, both start with initial vertical velocity u_y = 0 and accelerate downwards at g = 9.8 m/s^2 over height {h} m. t = sqrt(2h/g) for both."
    },
    {
        "family": "LAWS_OF_MOTION_STATIC_FRICTION",
        "grade": "Class 11",
        "chapter": "Laws of Motion",
        "topic": "Static Friction as a Self-Adjusting Reactive Force",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "A block of mass m resting on a rough horizontal surface with coefficient of static friction mu_s. An applied force F_app is exerted horizontally.",
            "visual_elements": ["Block(m=10kg)", "NormalForce(N=mg)", "FrictionSurface(mu_s=0.5)", "AppliedForce(F=20N)", "StaticFriction(f_s)"],
            "whiteboard_commands": [
                "draw_free_body_diagram(block='10 kg')",
                "write_equation('f_s,max = mu_s * N = 0.5 * 10 * 9.8 = 49 N')",
                "write_equation('F_applied = 20 N < f_s,max => Block remains static')",
                "highlight('f_s adjusts to match F_applied: f_s = 20 N, NOT 49 N!')"
            ]
        },
        "stem_templates": [
            "A wooden crate of mass {m} kg rests on a rough horizontal floor with coefficient of static friction mu_s = {mu}. A horizontal force of {F_app} N is applied to the crate. If the maximum static friction is {f_max} N (greater than {F_app} N), what is the actual frictional force exerted by the floor on the crate?",
            "A box of mass {m} kg sits on concrete. The limiting static friction is {f_max} N. A worker pushes with {F_app} N. Does the box move, and what is the magnitude of friction?",
            "Calculate the friction force acting on a {m} kg stone on a rough table (mu_s = {mu}) when a gentle horizontal pull of {F_app} N is exerted on it."
        ],
        "params": [(10, 0.5, 20, 49), (20, 0.4, 35, 78.4), (5, 0.6, 10, 29.4), (15, 0.5, 25, 73.5)],
        "target_misc": "MISC-FRIC-001: Static Friction Formula Overgeneralization Fallacy",
        "misc_desc": "Blindly calculates f = mu_s * N and claims the friction force is equal to the maximum limiting value even when the applied force is much smaller.",
        "correct_func": lambda m, mu, F_app, f_max: f"Static friction is a self-adjusting reactive force: 0 <= f_s <= mu_s * N. Because the applied force F_app = {F_app} N is less than the limiting friction f_max = {f_max} N, the block remains stationary (acceleration a = 0). By Newton's First Law, Sigma F_x = 0 => f_s = F_app = {F_app} N."
    },
    {
        "family": "WORK_ENERGY_CONSERVATIVE_FORCES",
        "grade": "Class 11",
        "chapter": "Work, Energy and Power",
        "topic": "Potential Energy as a Property of a System (Zero Reference Choice)",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_diagram",
            "diagram_description": "An object of mass m lifted from height y1 to y2 via three different paths: vertical climb, stepped stairs, and smooth curved incline.",
            "visual_elements": ["Mass(m=5kg)", "Ground(y=0)", "HeightH(y=4m)", "PathVertical", "PathStaircase", "PathIncline"],
            "whiteboard_commands": [
                "plot_paths(p1='vertical', p2='stairs', p3='ramp')",
                "write_equation('Delta U = m * g * Delta h')",
                "highlight('Work done by gravity is path-independent; depends solely on endpoints')"
            ]
        },
        "stem_templates": [
            "A cart of mass {m} kg is moved from the ground to a platform of height {h} m above ground. Path 1 is a direct vertical lift; Path 2 is a long zigzag ramp of length 30 m; Path 3 is an irregular curved slope. Compare the work done by the gravitational force along all three paths.",
            "A hiker climbs a mountain peak of altitude {h} m using either a steep direct rock face or a gradual winding trail. Assuming air drag is negligible, how does the gravitational work done on the hiker compare between both routes?",
            "Three identical balls of mass {m} kg are raised through vertical height {h} m using different ramps of varying steepness. In which case does gravity do the most work?"
        ],
        "params": [(5, 4), (10, 10), (2, 8), (50, 20)],
        "target_misc": "MISC-NRG-001: Path Dependence of Conservative Work Fallacy",
        "misc_desc": "Believes the longer path results in greater gravitational work done on the object, confusing gravity with dissipative friction.",
        "correct_func": lambda m, h: f"Gravity is a conservative force field. The work done by a conservative force depends strictly on the initial and final vertical positions (endpoints) and is completely path-independent. W_gravity = -m * g * Delta h = -{m * 9.8 * h} J for all three paths."
    },
    {
        "family": "GRAVITATION_SATELLITE_ORBITAL_SPEED",
        "grade": "Class 11",
        "chapter": "Gravitation",
        "topic": "Orbital Velocity of Satellites (Mass Independence)",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_diagram",
            "diagram_description": "Two artificial satellites A (mass 100 kg) and B (mass 5000 kg) orbiting Earth in the same circular orbit of radius r.",
            "visual_elements": ["Earth(M)", "Orbit(radius=r)", "SatelliteA(m=100kg)", "SatelliteB(m=5000kg)", "CentripetalForce"],
            "whiteboard_commands": [
                "draw_earth(center=(0,0), radius=50)",
                "draw_circular_orbit(radius=120)",
                "plot_satellites(m1='100 kg', m2='5000 kg')",
                "write_equation('G*M*m / r^2 = m*v^2 / r => v_orb = sqrt(G*M / r)')",
                "highlight('Satellite mass m cancels out; orbital speed is identical')"
            ]
        },
        "stem_templates": [
            "Two satellites of masses {m1} kg and {m2} kg revolve around the Earth in the identical circular orbit of radius {r} km. Compare their orbital speeds v1 and v2.",
            "Satellite Alpha has mass {m1} kg and Satellite Beta has mass {m2} kg. Both are placed in a geostationary orbit at radius {r} km. Which satellite has a higher speed?",
            "If a 500 kg space capsule and a 2 kg wrench are released from the International Space Station, how do their orbital velocities compare?"
        ],
        "params": [(100, 5000, 7000), (500, 2000, 8000), (50, 10000, 42000), (250, 1500, 6800)],
        "target_misc": "MISC-GRAV-002: Heavier Satellite Requires Faster Orbital Speed",
        "misc_desc": "Believes a heavier satellite needs a higher orbital velocity to prevent it from crashing down into Earth.",
        "correct_func": lambda m1, m2, r: f"The orbital velocity of a circular orbit is obtained by equating gravitational attraction to centripetal force: G*M_earth*m / r^2 = m*v^2 / r. The mass of the satellite m cancels from both sides, yielding v = sqrt(G*M_earth / r). Since both share the identical orbital radius r = {r} km, their orbital speeds are exactly equal (v1 = v2)."
    },

    # ========================== CLASS 12 PHYSICS ==========================
    {
        "family": "ELECTROSTATICS_CONDUCTOR_INTERIOR",
        "grade": "Class 12",
        "chapter": "Electrostatic Potential and Capacitance",
        "topic": "Electrostatic Shielding & Electric Field inside Conductor",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "field_lines",
            "diagram_description": "A solid metal spherical conductor placed inside an external electric field E0. Surface charges redistribute such that net E inside = 0.",
            "visual_elements": ["Conductor(metal)", "ExternalField(E0)", "InducedSurfaceCharges(+/-)", "InteriorRegion(E=0)"],
            "whiteboard_commands": [
                "draw_conductor_sphere(solid=True)",
                "plot_surface_charges(left='-', right='+')",
                "write_equation('E_internal = E_applied + E_induced = 0')",
                "write_equation('V = constant throughout interior')"
            ]
        },
        "stem_templates": [
            "A charged hollow or solid metal conductor is placed in an external electrostatic field. What is the electrostatic field E and the electric potential V inside the conductor?",
            "A car is struck by lightning during a thunderstorm. Why is it safe to remain inside the metallic car body?",
            "A metal cavity of arbitrary shape contains no interior charges. A high electric charge Q = {Q} micro-Coulombs is deposited on its outer surface. What is the electric field inside the hollow cavity?"
        ],
        "params": [(50,), (100,), (25,), (200,)],
        "target_misc": "MISC-ELEC-007: Conductors Harbor Electric Fields Internally",
        "misc_desc": "Believes the electric field passes straight through metals or that high potential implies non-zero electric field (E = -dV/dr).",
        "correct_func": lambda Q: f"In static equilibrium, free electrons inside the metal redistribute instantaneously to the outer surface until the induced internal field completely cancels the external field. Thus, E_inside = 0 N/C everywhere. Because E = -dV/dr = 0, the electric potential V is uniform and constant throughout the entire volume of the conductor."
    },
    {
        "family": "CURRENT_DRIFT_VELOCITY_SCALE",
        "grade": "Class 12",
        "chapter": "Current Electricity",
        "topic": "Electron Drift Velocity vs Speed of Electric Signal",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_schematic",
            "diagram_description": "A copper wire connected to a light bulb and switch. The wire is packed with free conduction electrons (~10^28 per m^3).",
            "visual_elements": ["CopperWire(density=10^28/m^3)", "Electrons(drifting)", "Bulb", "Switch"],
            "whiteboard_commands": [
                "draw_wire_cross_section(n='8.5 x 10^28 m^-3')",
                "write_equation('I = n * A * e * v_d')",
                "calculate_drift_velocity('v_d ~ 0.1 mm/s = 10^-4 m/s')",
                "highlight('Bulb lights immediately because electric field propagates at ~c = 3 x 10^8 m/s!')"
            ]
        },
        "stem_templates": [
            "When an electric light switch is closed, a ceiling lamp turns on virtually instantaneously. Does this mean individual conduction electrons travel from the switch to the bulb filament at nearly the speed of light? Calculate typical drift velocity for I = {I} A in a 1 mm^2 copper wire.",
            "Why does an electric bulb glow the very fraction of a second a switch is flicked, even though electron drift velocity is merely a fraction of a millimeter per second?",
            "An engineer measures electric current of {I} A flowing through a domestic copper conductor. What is the approximate order of magnitude of the net drift velocity of the conduction electrons?"
        ],
        "params": [(1.0,), (2.0,), (0.5,), (5.0,)],
        "target_misc": "MISC-ELEC-008: Electrons Race from Battery to Bulb at Light Speed",
        "misc_desc": "Believes the instantaneous lighting of the bulb requires electrons to physically race through the wire at 300,000 km/s.",
        "correct_func": lambda I: f"No. The drift velocity of electrons is exceedingly slow, typically v_d ~ 10^-4 m/s (fraction of a millimeter per second). The lamp glows immediately because the entire circuit is pre-filled with free electrons (~10^28 m^-3); closing the switch establishes an electromagnetic field across the circuit at nearly the speed of light (~3 x 10^8 m/s), causing electrons everywhere to start drifting simultaneously."
    },
    {
        "family": "EMI_LENZ_LAW_FLUX_CHANGE",
        "grade": "Class 12",
        "chapter": "Electromagnetic Induction",
        "topic": "Lenz's Law and Direction of Induced Current",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "field_lines",
            "diagram_description": "The North pole of a bar magnet is pushed rapidly towards a stationary circular copper ring.",
            "visual_elements": ["BarMagnet(North_pole)", "MotionVector(approaching)", "CopperRing", "InducedCurrent(Counter-Clockwise)"],
            "whiteboard_commands": [
                "draw_copper_ring(facing_viewer=True)",
                "draw_bar_magnet(pole='N', motion='approaching_ring')",
                "write_equation('Induced B-field must OPPOSE the INCREASE in magnetic flux')",
                "highlight('Face of ring becomes a North pole (repulsion) => CCW current')"
            ]
        },
        "stem_templates": [
            "The North pole of a permanent bar magnet is moved rapidly towards the center of a stationary copper coil. According to Lenz's Law, what is the direction of the induced current in the coil when viewed from the magnet side, and what magnetic pole does this face develop?",
            "A conducting ring rests horizontally on a table. A student lowers the South pole of a magnet towards the ring. How does the ring react, and in which direction does induced current circulate?",
            "A bar magnet is dropped vertically through a long hollow copper cylinder. Why does the falling magnet reach a constant terminal velocity instead of continuing to accelerate at g?"
        ],
        "params": [(1,)],
        "target_misc": "MISC-EMI-001: Induced Field Reinforces External Field Fallacy",
        "misc_desc": "Believes the induced current aids or aligns with the external magnetic field, confusing opposing the CHANGE in flux with opposing the field itself.",
        "correct_func": lambda p: f"By Lenz's Law (conservation of energy), the polarity of the induced EMF always opposes the CHANGE in magnetic flux that produces it. As the North pole approaches, flux increases; the ring induces a magnetic field pointing back towards the magnet, developing a North pole on the facing surface to exert a repulsive braking force (counter-clockwise current)."
    }
]

# ----------------------------------------------------------------------------------------
# Linguistic Variation Generators for Massive Dataset Scaling
# ----------------------------------------------------------------------------------------
def generate_expanded_individual_dataset():
    print("Generating comprehensive multi-grade individual response dataset (Classes 9, 10, 11, 12)...")
    records = []
    record_id = 1

    # Phrasings for diverse error styles
    calculation_slips_phrasings = [
        "Did {a} / {b} but slipped in arithmetic and wrote {slip} instead of {val}.",
        "Substituted correctly into the formula, but calculated {wrong_ans} due to a minor multiplication error.",
        "Wrote down proper equation, but final mental math produced {wrong_ans}.",
        "Steps: setup is correct, but simplified {term1} + {term2} mistakenly to {wrong_ans}."
    ]

    unit_error_phrasings = [
        "Calculated numeric value {val} correctly, but labeled it with wrong units {wrong_unit}.",
        "Reported answer as {val} {wrong_unit} instead of standard SI units {correct_unit}.",
        "Forgot to convert minutes into seconds, writing {val} {wrong_unit}."
    ]

    unsure_phrasings = [
        "Not sure of the formula here. Maybe it's around {val}?",
        "I guess it stays the same, but I can't remember the exact physics rule.",
        "Could be either higher or lower, unclear without more notes.",
        "I think it increases, but not confident about the steps."
    ]

    for fam_idx, fam in enumerate(master_families):
        # We generate ~110 variations per family across parameters, phrasings, and error categories
        stems = fam["stem_templates"]
        params_list = fam["params"]
        grade = fam["grade"]
        chapter = fam["chapter"]
        topic = fam["topic"]
        target_misc = fam["target_misc"]
        misc_desc = fam["misc_desc"]
        correct_func = fam["correct_func"]
        diagram_meta = fam["diagram_meta"]

        # Deterministic cycle over parameters and templates
        for var_idx in range(112):
            param_tuple = params_list[var_idx % len(params_list)]
            stem_tmpl = stems[var_idx % len(stems)]
            
            # Format stem
            if fam["family"] == "MOTION_SPEED_DISTANCE_TIME":
                d, t = param_tuple
                q_text = stem_tmpl.format(d=d, t=t)
                correct_text = correct_func(d, t)
                ans_val = d / t
                misc_ans = d * t
            elif fam["family"] == "MOTION_SPEED_VS_ACCELERATION":
                v, t = param_tuple
                q_text = stem_tmpl.format(v=v, t=t)
                correct_text = correct_func(v, t)
                ans_val = 0
                misc_ans = v
            elif fam["family"] == "FORCE_NEWTON_FIRST_LAW":
                m, v = param_tuple
                q_text = stem_tmpl.format(m=m, v=v)
                correct_text = correct_func(m, v)
                ans_val = 0
                misc_ans = m * v
            elif fam["family"] == "FORCE_NEWTON_THIRD_LAW":
                M, m = param_tuple
                q_text = stem_tmpl.format(M=M, m=m)
                correct_text = correct_func(M, m)
                ans_val = "equal"
                misc_ans = "truck exerts much greater force"
            elif fam["family"] == "GRAVITATION_FREE_FALL":
                M, m, h = param_tuple
                q_text = stem_tmpl.format(M=M, m=m, h=h)
                correct_text = correct_func(M, m, h)
                ans_val = "simultaneously"
                misc_ans = "heavy cannonball hits first"
            elif fam["family"] == "WORK_ENERGY_DISPLACEMENT":
                m, t, F = param_tuple
                q_text = stem_tmpl.format(m=m, t=t, F=F)
                correct_text = correct_func(m, t, F)
                ans_val = 0
                misc_ans = m * 9.8 * 20
            elif fam["family"] == "OPTICS_HALF_LENS_BLOCKING":
                f = param_tuple[0]
                q_text = stem_tmpl.format(f=f)
                correct_text = correct_func(f)
                ans_val = "complete image with 50% brightness"
                misc_ans = "top half of image is completely missing"
            elif fam["family"] == "OPTICS_CARTESIAN_SIGN_CONVENTION":
                u, f, r = param_tuple
                q_text = stem_tmpl.format(u=u, f=f, r=r)
                correct_text = correct_func(u, f, r)
                ans_val = f"-{round(1/(-1/f + 1/u), 1)}"
                misc_ans = f"+{round(1/(1/f - 1/u), 1)}"
            elif fam["family"] == "HUMAN_EYE_VISION_DEFECTS":
                fp = param_tuple[0]
                q_text = stem_tmpl.format(fp=fp)
                correct_text = correct_func(fp)
                ans_val = "Myopia, Concave (diverging) lens"
                misc_ans = "Hypermetropia, Convex (converging) lens"
            elif fam["family"] == "HUMAN_EYE_PRISM_DISPERSION":
                q_text = stem_tmpl
                correct_text = correct_func(1)
                ans_val = "Violet bends most; Red travels fastest in glass"
                misc_ans = "Red bends most because red is strongest"
            elif fam["family"] == "ELECTRICITY_CURRENT_CONSERVATION":
                V, I, R = param_tuple
                q_text = stem_tmpl.format(V=V, I=I, R=R)
                correct_text = correct_func(V, I, R)
                ans_val = f"A1 = A2 = A3 = {I} A"
                misc_ans = f"A1 = {I} A, A2 = {round(I*0.6, 2)} A, A3 = {round(I*0.2, 2)} A"
            elif fam["family"] == "ELECTRICITY_PARALLEL_BATTERY_DELIVERY":
                V, R = param_tuple
                q_text = stem_tmpl.format(V=V, R=R)
                correct_text = correct_func(V, R)
                ans_val = "Bulb 1 brightness unchanged, battery current doubles"
                misc_ans = "Bulb 1 dims to half brightness because current is shared"
            elif fam["family"] == "MAGNETIC_EFFECTS_LORENTZ_LEFT_HAND":
                q_text = stem_tmpl
                correct_text = correct_func(1)
                ans_val = "Vertically upwards (out of page)"
                misc_ans = "Towards the South or downwards"
            elif fam["family"] == "KINEMATICS_PROJECTILE_INDEPENDENCE":
                h, v0 = param_tuple
                q_text = stem_tmpl.format(h=h, v0=v0)
                correct_text = correct_func(h, v0)
                ans_val = "Both hit at exactly the same time"
                misc_ans = "Sphere B takes much longer because horizontal velocity floats it"
            elif fam["family"] == "LAWS_OF_MOTION_STATIC_FRICTION":
                m, mu, F_app, f_max = param_tuple
                q_text = stem_tmpl.format(m=m, mu=mu, F_app=F_app, f_max=f_max)
                correct_text = correct_func(m, mu, F_app, f_max)
                ans_val = f"{F_app} N (self-adjusting, stationary)"
                misc_ans = f"{f_max} N (blindly computed mu_s * N)"
            elif fam["family"] == "WORK_ENERGY_CONSERVATIVE_FORCES":
                m, h = param_tuple
                q_text = stem_tmpl.format(m=m, h=h)
                correct_text = correct_func(m, h)
                ans_val = "Work done by gravity is identical for all three paths"
                misc_ans = "Zigzag ramp does much more gravitational work because path is longer"
            elif fam["family"] == "GRAVITATION_SATELLITE_ORBITAL_SPEED":
                m1, m2, r = param_tuple
                q_text = stem_tmpl.format(m1=m1, m2=m2, r=r)
                correct_text = correct_func(m1, m2, r)
                ans_val = "Both satellites have the exact same orbital velocity"
                misc_ans = "Heavier satellite must move faster to stay in orbit"
            elif fam["family"] == "ELECTROSTATICS_CONDUCTOR_INTERIOR":
                Q = param_tuple[0]
                q_text = stem_tmpl.format(Q=Q)
                correct_text = correct_func(Q)
                ans_val = "Electric field E = 0 N/C, Potential V is constant"
                misc_ans = f"Electric field is proportional to Q = {Q} micro-C throughout the interior"
            elif fam["family"] == "CURRENT_DRIFT_VELOCITY_SCALE":
                I = param_tuple[0]
                q_text = stem_tmpl.format(I=I)
                correct_text = correct_func(I)
                ans_val = "Drift velocity is ~10^-4 m/s (fractions of mm/s); field travels at ~c"
                misc_ans = "Electrons race from the switch to the bulb at 300,000 km/s"
            elif fam["family"] == "EMI_LENZ_LAW_FLUX_CHANGE":
                q_text = stem_tmpl
                correct_text = correct_func(1)
                ans_val = "Counter-clockwise (North pole developing to repel incoming magnet)"
                misc_ans = "Clockwise (South pole attracts incoming magnet)"

            # Assign category according to systematic distribution:
            # 60% Misconception variations, 20% Correct responses, 8% Calculation slips, 6% Unit errors, 6% Unsure
            cat_choice = var_idx % 10
            if cat_choice in [0, 1, 2, 3, 4, 5]:
                label = target_misc
                err_type = "conceptual_misconception"
                evidence = misc_desc
                confidence = random.choice(["High", "Medium"])
                if isinstance(misc_ans, (int, float)):
                    student_resp = f"Result: {misc_ans}. Working: used standard proportional reasoning across {q_text[:35]}..."
                else:
                    student_resp = f"My answer is: {misc_ans}. Explanation: based on physical observation that loads consume or alter the condition."
            elif cat_choice in [6, 7]:
                label = "CORRECT: Scientifically Accurate Response"
                err_type = "no_error"
                evidence = "Rigorous scientific reasoning with valid mathematical steps."
                confidence = "High"
                student_resp = f"{ans_val}. Derived as: {correct_text[:90]}..."
            elif cat_choice == 8:
                label = "CARELESS_CALCULATION_ERROR"
                err_type = "calculation_slip"
                evidence = "Conceptual approach is sound, but an isolated arithmetic slip occurred."
                confidence = "Medium"
                student_resp = f"Formula setup is correct ({correct_text[:40]}), but multiplied/divided values incorrectly to get unexpected total."
            elif cat_choice == 9 and (var_idx % 2 == 0):
                label = "UNIT_CONVERSION_ERROR"
                err_type = "unit_error"
                evidence = "Substituted proper values but omitted standard SI unit conversion."
                confidence = "High"
                student_resp = f"Answer is {ans_val} (omitted proper units or used inverted dimension)."
            else:
                label = "UNSURE_INSUFFICIENT_EVIDENCE"
                err_type = "guessing_unclear"
                evidence = "Student provided minimal reasoning; requires diagnostic probing question."
                confidence = "Low"
                student_resp = f"I think it might be roughly {ans_val}, but not sure of the exact formula."

            # Stratified Split: By family & variant modulo
            # 70% Train, 15% Val, 15% Test
            if (var_idx % 10) in [0, 1, 2, 3, 4, 5, 6]:
                split = "train"
            elif (var_idx % 10) in [7, 8]:
                split = "val"
            else:
                split = "test"

            rec = {
                "record_id": f"REC-{record_id:05d}",
                "question_id": f"PHY-{fam['grade'].replace(' ', '')}-{fam_idx+1:02d}-{var_idx+1:03d}",
                "question_family": fam["family"],
                "curriculum_grade": grade,
                "curriculum_chapter": chapter,
                "topic_concept": topic,
                "question_text": q_text,
                "correct_answer_and_steps": correct_text,
                "student_response": student_resp,
                "misconception_label": label,
                "error_type": err_type,
                "diagnostic_confidence": confidence,
                "evidence_rationale": evidence,
                "multimodal_context": diagram_meta,
                "split": split
            }
            records.append(rec)
            record_id += 1

    print(f"Generated {len(records)} multimodal individual responses across Classes 9, 10, 11, and 12.")

    # Export JSON
    json_path = os.path.join(INDIV_DIR, "individual_responses.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)

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
        for r in records:
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
        sp_records = [r for r in records if r["split"] == sp]
        # JSONL
        sp_jsonl = os.path.join(INDIV_DIR, f"{sp}.jsonl")
        with open(sp_jsonl, "w", encoding="utf-8") as f:
            for r in sp_records:
                f.write(json.dumps(r) + "\n")
        # CSV
        sp_csv = os.path.join(INDIV_DIR, f"{sp}.csv")
        with open(sp_csv, "w", newline="", encoding="utf-8") as f:
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

    return records


# ----------------------------------------------------------------------------------------
# Longitudinal Student Sequence Dataset Generator (300+ Sessions across All Grades)
# ----------------------------------------------------------------------------------------
def generate_expanded_sequence_dataset():
    print("Generating comprehensive sequence dataset (300+ multi-turn sessions across all grades)...")
    sequences = []
    seq_id_counter = 1

    pattern_archetypes = [
        # 1. Recurrent Current Attenuation
        {
            "pattern_label": "RECURRENT_CURRENT_ATTENUATION_PATTERN",
            "topic": "Electricity: Current Conservation",
            "grade": "Class 10",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "steps": [
                ("PHY-ELEC-01-001", "Bulbs in series: compare ammeters.", "A1 = 1.2A, A2 = 0.8A, A3 = 0.4A. Bulb 1 consumes current.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
                ("PHY-ELEC-01-002", "Three resistors in series: compare current at R3.", "Current at R3 is smaller than R1 because current is consumed along the loop.", "MISC-ELEC-001: Current Attenuation / Consumption Model"),
                ("PHY-ELEC-01-003", "Does second bulb glow dimmer because less current reaches it?", "Yes, second bulb gets whatever current is left over.", "MISC-ELEC-001: Current Attenuation / Consumption Model")
            ]
        },
        # 2. Recurrent Speed vs Distance Inversion (PDF Page 2 & 4)
        {
            "pattern_label": "RECURRENT_SPEED_DISTANCE_INVERSION_PATTERN",
            "topic": "Motion: Kinematics Operations",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "steps": [
                ("PHY-MOT-01-001", "Runner covers 100 m in 5 s. Speed?", "500 m/s; multiplied 100 by 5.", "MISC-MOT-001: Speed Distance Operation Inversion"),
                ("PHY-MOT-01-002", "Car travels 300 m in 15 s. Speed?", "4500 m/s; speed = distance * time.", "MISC-MOT-001: Speed Distance Operation Inversion"),
                ("PHY-MOT-01-003", "Bicycle covers 60 m in 3 s. Speed?", "180 m/s; multiplied distance by time.", "MISC-MOT-001: Speed Distance Operation Inversion")
            ]
        },
        # 3. Recurrent Speed vs Acceleration Conflation
        {
            "pattern_label": "RECURRENT_SPEED_ACCELERATION_CONFLATION",
            "topic": "Motion: Speed vs Acceleration",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "steps": [
                ("PHY-MOT-02-001", "Steady 20 m/s for 10 s. Acceleration?", "20 m/s^2 because it is moving fast.", "MISC-MOT-002: Speed-Acceleration Conflation"),
                ("PHY-MOT-02-002", "Train at uniform 72 km/h for 20 s. Acceleration?", "Acceleration is 72 km/h^2 because it has high velocity.", "MISC-MOT-002: Speed-Acceleration Conflation")
            ]
        },
        # 4. Recurrent Impetus Theory (Force in Motion)
        {
            "pattern_label": "RECURRENT_IMPETUS_THEORY_PATTERN",
            "topic": "Force & Laws of Motion: Inertia",
            "grade": "Class 9",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "steps": [
                ("PHY-FOR-01-001", "Puck sliding on frictionless ice. Forward force needed?", "Requires continuous push of 10 N to sustain speed.", "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)"),
                ("PHY-FOR-01-002", "Satellite in deep space at constant v. Forward thrust?", "Needs engine firing to keep moving forward.", "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)")
            ]
        },
        # 5. Recurrent Projectile Independence Fallacy (Class 11)
        {
            "pattern_label": "RECURRENT_PROJECTILE_FALLACY_PATTERN",
            "topic": "Kinematics: 2D Motion Independence",
            "grade": "Class 11",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "steps": [
                ("PHY-KIN-01-001", "Ball A dropped, Ball B fired horizontally at 30 m/s. Which lands first?", "Ball B lands much later because forward speed floats it.", "MISC-KIN-001: Horizontal Motion Postpones Gravitational Fall"),
                ("PHY-KIN-01-002", "Bullet fired horizontally vs bullet dropped. Compare fall times.", "Fired bullet stays in the air longer because of its speed.", "MISC-KIN-001: Horizontal Motion Postpones Gravitational Fall")
            ]
        },
        # 6. Recurrent Static Friction Overgeneralization (Class 11)
        {
            "pattern_label": "RECURRENT_STATIC_FRICTION_OVERGENERALIZATION",
            "topic": "Laws of Motion: Friction Self-Adjustment",
            "grade": "Class 11",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "steps": [
                ("PHY-FRIC-01-001", "Block with max friction 49 N pushed with 20 N. Friction force?", "Friction is 49 N because formula is mu_s * N.", "MISC-FRIC-001: Static Friction Formula Overgeneralization Fallacy"),
                ("PHY-FRIC-01-002", "Crate with max friction 80 N pushed with 30 N. Friction?", "Friction is 80 N.", "MISC-FRIC-001: Static Friction Formula Overgeneralization Fallacy")
            ]
        },
        # 7. Recurrent Drift Velocity Light Speed Fallacy (Class 12)
        {
            "pattern_label": "RECURRENT_DRIFT_VELOCITY_SPEED_FALLACY",
            "topic": "Current Electricity: Drift Velocity Scale",
            "grade": "Class 12",
            "status": "unresolved_persistent_misconception",
            "next_action": "trigger_targeted_multimodal_intervention",
            "steps": [
                ("PHY-ELEC-08-001", "Why does bulb light instantly when switch closes?", "Electrons race from the switch to the bulb filament at 300,000 km/s.", "MISC-ELEC-008: Electrons Race from Battery to Bulb at Light Speed"),
                ("PHY-ELEC-08-002", "Calculate drift velocity of electrons in copper wire.", "Drift velocity is close to the speed of light.", "MISC-ELEC-008: Electrons Race from Battery to Bulb at Light Speed")
            ]
        },
        # 8. Successful Cognitive Remediation (Pre-Test Error -> POE Intervention -> Correct Transfer)
        {
            "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
            "topic": "Optics: Half-Lens Aperture Remediation",
            "grade": "Class 10",
            "status": "resolved_with_transfer",
            "next_action": "advance_to_next_topic",
            "steps": [
                ("PHY-OPT-01-001", "Cover lower half of convex lens with black cardboard.", "The upper half of the image disappears completely.", "MISC-OPT-001: Half-Lens Blocking Fallacy"),
                ("PHY-INTV-001", "Observe PhET simulation: cover lower half with virtual mask.", "Wait, the full image is still formed on the screen, just dimmer! Every point on lens receives light from entire object.", "COGNITIVE_CONFLICT_RECONCILED: Full image persists with 50% brightness"),
                ("PHY-OPT-01-002", "Near-transfer isomorphic question: cover top 30% of lens.", "The complete image remains on screen, but brightness is 70% of original.", "CORRECT: Scientifically Accurate Response")
            ]
        },
        # 9. Successful Cognitive Remediation: Free Fall Gravitation (Class 9)
        {
            "pattern_label": "SUCCESSFUL_COGNITIVE_REMEDIATION_SEQUENCE",
            "topic": "Gravitation: Free Fall Mass Independence",
            "grade": "Class 9",
            "status": "resolved_with_transfer",
            "next_action": "advance_to_next_topic",
            "steps": [
                ("PHY-GRAV-01-001", "10 kg cannonball vs 50 g feather in vacuum.", "The cannonball falls much faster because it weighs more.", "MISC-GRAV-001: Heavier Objects Fall Faster Fallacy"),
                ("PHY-INTV-002", "Observe Apollo 15 hammer & feather drop in vacuum.", "Both hit the ground simultaneously because g is independent of mass!", "COGNITIVE_CONFLICT_RECONCILED: a = g for all falling bodies"),
                ("PHY-GRAV-01-002", "Transfer: 5 kg rock vs 500 g ball dropped on Moon.", "Both hit the lunar surface at the exact same instant.", "CORRECT: Scientifically Accurate Response")
            ]
        },
        # 10. Transient Arithmetic Slip with Conceptual Mastery
        {
            "pattern_label": "TRANSIENT_SLIP_WITH_CONCEPTUAL_MASTERY",
            "topic": "Kinematics: Velocity Calculation",
            "grade": "Class 9",
            "status": "no_conceptual_misconception",
            "next_action": "provide_arithmetic_feedback_only",
            "steps": [
                ("PHY-MOT-01-001", "Runner covers 100 m in 5 s. Speed?", "100 / 5 = 25 m/s. Formula is distance divided by time.", "CARELESS_CALCULATION_ERROR"),
                ("PHY-MOT-01-002", "Car travels 300 m in 15 s. Speed?", "Speed = distance / time = 300 / 15 = 20 m/s.", "CORRECT: Scientifically Accurate Response")
            ]
        }
    ]

    # Generate 320 sessions by rotating through archetypes with student IDs
    for rep in range(32):
        for arch in pattern_archetypes:
            sid = f"STU_{seq_id_counter+100:04d}"
            split = "train" if (seq_id_counter % 10) < 7 else ("val" if (seq_id_counter % 10) < 9 else "test")
            
            attempts = []
            for step_idx, st in enumerate(arch["steps"]):
                attempts.append({
                    "step": step_idx + 1,
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
                "ordered_attempts": attempts,
                "sequence_level_label": arch["pattern_label"],
                "learning_status": arch["status"],
                "recommended_intervention_action": arch["next_action"],
                "split": split
            }
            sequences.append(seq_record)
            seq_id_counter += 1

    print(f"Generated {len(sequences)} longitudinal student sequences across all grades.")

    # Export JSON
    seq_json_path = os.path.join(SEQ_DIR, "student_sequences.json")
    with open(seq_json_path, "w", encoding="utf-8") as f:
        json.dump(sequences, f, indent=2)

    # Export Flattened CSV
    seq_csv_path = os.path.join(SEQ_DIR, "student_sequences.csv")
    with open(seq_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "sequence_id", "student_id", "curriculum_grade", "topic", "total_steps",
            "responses_sequence", "diagnoses_sequence", "sequence_level_label",
            "learning_status", "recommended_intervention_action", "split"
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
    generate_expanded_individual_dataset()
    generate_expanded_sequence_dataset()
    print("Full multi-grade curriculum dataset generation complete!")
