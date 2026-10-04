# Re:Learn 25 Core Physics Curriculum Families
# Fully grounded in NCERT Science Class 10, Class 9, and Secondary CBSE standards

CURRICULUM_FAMILIES = [
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
            "I'm not sure if half the image disappears or if it just becomes fuzzy.",
            "Maybe covering half the lens cuts off the rays, or maybe it just makes it dim?"
        ]
    },

    # 2. OPTICS: SCREEN REIFICATION
    {
        "family": "OPTICS_SCREEN_REIFICATION",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Real Image Formation in Space",
        "target_misc": "MISC-OPT-002: Screen Reification (Image Exists Only on Screen)",
        "misc_desc": "Believes a real image is a physical drawing that only exists if a physical screen is present to capture it; does not understand that rays intersect in space forming an aerial image.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Convex lens forming real image in air. Cardboard screen is removed, showing rays still converge at the focal plane.",
            "visual_elements": ["ConvexLens", "ConvergingRays", "AerialImagePlane", "ObserverEye"],
            "whiteboard_commands": [
                "draw_lens(type='convex', f=20)",
                "draw_converging_rays(focus_point=(40, 0))",
                "remove_screen()",
                "write_equation('Rays converge in space: aerial image exists independently of screen')"
            ]
        },
        "stem_templates": [
            "A convex lens of focal length {f} cm focuses the image of a candle on a white screen placed 40 cm away. If the screen is abruptly removed, does the image still exist in space at that location?",
            "A student forms a sharp real image on a viewing card using a lens of f = {f} cm. When the card is taken away, what happens to the real image?",
            "In an optics experiment with a converging lens (f = {f} cm), the screen is lifted out of the beam. Where does the image go?"
        ],
        "params": [(15,), (20,), (10,), (25,), (12,)],
        "correct_base": "The real inverted image still exists in empty space at that exact focal position (aerial image). The screen merely scatters light diffusely so observers can view it from all angles; the convergence of light rays occurs independently of the screen.",
        "misc_phrasings": [
            "The image disappears completely because an image cannot exist in thin air without a screen to catch it.",
            "Without the screen, there is no surface for the image to be drawn on, so no image is formed.",
            "Removing the screen destroys the image because real images only live on physical screens.",
            "The light rays just travel forward forever without forming any image since the screen is gone."
        ],
        "correct_phrasings": [
            "The image remains in empty space at that focal plane (aerial image). Light rays still intersect there regardless of whether a screen is present.",
            "The image still exists in space. A screen is only needed to scatter light diffusely to our eyes, not to create the image.",
            "The real image is formed in the air at the focal plane; it exists independently of any physical screen."
        ],
        "slip_phrasings": [
            "The aerial image still exists, but its position shifted from 40 cm to {slip} cm due to calculation slip.",
            "Image exists in space, but calculated magnification as +2.0 instead of -1.0."
        ],
        "unit_phrasings": [
            "Image distance in space is 40 Joules instead of cm.",
            "Focal plane location reported as 20 Amperes instead of cm."
        ],
        "unsure_phrasings": [
            "I know we always need a screen in class, so maybe the image vanishes without it?",
            "Can an image exist in empty space or does it need a physical wall?"
        ]
    },

    # 3. OPTICS: VIRTUAL RAY CONVERGENCE
    {
        "family": "OPTICS_VIRTUAL_RAY_CONVERGENCE",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Virtual Images & Mirrors",
        "target_misc": "MISC-OPT-003: Virtual Image Ray Convergence Fallacy",
        "misc_desc": "Believes virtual images behind a mirror or lens are formed by real physical light rays that penetrate the glass and intersect behind the surface.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Plane mirror reflecting light into eye, with dotted construction lines showing virtual image behind mirror.",
            "visual_elements": ["PlaneMirror", "IncidentRays", "ReflectedRays", "DottedExtensions", "VirtualImage"],
            "whiteboard_commands": [
                "draw_plane_mirror()",
                "draw_real_reflected_rays(diverging=True)",
                "draw_dotted_backward_extensions()",
                "write_equation('No light energy behind mirror; virtual intersection only')"
            ]
        },
        "stem_templates": [
            "An object is placed at distance {u} cm in front of a flat plane mirror. Do actual light rays pass through the mirror to form the virtual image?",
            "When you see your reflection in a plane mirror at distance {u} cm, what physical process happens behind the mirror glass?",
            "A convex mirror forms an erect virtual image of a vehicle at distance {u} m. Are light rays physically present at the image location behind the mirror?"
        ],
        "params": [(10,), (15,), (20,), (25,), (30,)],
        "correct_base": "No light rays actually pass through or intersect behind the mirror. Reflected rays diverge into the eye, and the human visual cortex projects them straight backward. Virtual images are formed by the apparent intersection of backward ray extensions, with zero physical light energy behind the mirror.",
        "misc_phrasings": [
            "Light rays penetrate through the mirror glass and physically focus {u} cm behind the surface.",
            "Actual light rays cross each other behind the mirror to create the reflection.",
            "Light travels into the silver coating and converges behind the mirror to project the image.",
            "Rays pass through the glass and meet at the virtual image position behind the mirror."
        ],
        "correct_phrasings": [
            "Zero light rays penetrate behind the mirror. The reflected rays diverge into the eye, and the virtual image is formed by the backward extrapolation of these rays.",
            "No physical rays exist behind the mirror; the virtual image is an apparent intersection of backward-projected rays.",
            "Virtual images contain no light energy; they are perceived because the eye traces diverging reflected rays backward."
        ],
        "slip_phrasings": [
            "No rays behind mirror, but calculated image distance as +{slip} cm instead of -{u} cm.",
            "Correctly identified virtual extension, but stated plane mirror magnification is +0.5 instead of +1.0."
        ],
        "unit_phrasings": [
            "Virtual image distance is {u} Watts instead of cm.",
            "Reported object distance in Newtons."
        ],
        "unsure_phrasings": [
            "It looks like light is behind the mirror, but I'm not sure if it is real light or just an illusion.",
            "Do rays go through the mirror or do they only bounce off the front?"
        ]
    },

    # 4. OPTICS: CARTESIAN SIGN CONVENTION
    {
        "family": "OPTICS_CARTESIAN_SIGN_CONVENTION",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "New Cartesian Sign Convention and Mirror/Lens Formulae",
        "target_misc": "MISC-OPT-004: Sign Convention Spatial Inversion",
        "misc_desc": "Treats distances as absolute scalar magnitudes; treats object distance u as positive or forgets that concave mirror focal length is negative.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Concave mirror with optical center at origin. Object at u = -30 cm, f = -15 cm. Image forms at v = -30 cm.",
            "visual_elements": ["ConcaveMirror", "PrincipalAxis", "Object(u=-30)", "Focus(f=-15)", "Image(v=-30)"],
            "whiteboard_commands": [
                "draw_axes(origin='Pole')",
                "set_sign_convention(incident_direction='positive_x')",
                "mark_point(x=-30, label='u = -30 cm')",
                "mark_point(x=-15, label='f = -15 cm')",
                "write_equation('1/v + 1/u = 1/f => 1/v = 1/(-15) - 1/(-30) => v = -30 cm')"
            ]
        },
        "stem_templates": [
            "An object is placed at a distance of {u} cm in front of a concave mirror of focal length {f} cm. Using the New Cartesian Sign Convention, determine the image distance v.",
            "A candle is located {u} cm from a concave mirror with focal length {f} cm. Calculate the image position v using the mirror formula with proper signs.",
            "Calculate image position v for an illuminated needle placed {u} cm before a concave spherical mirror having focal length {f} cm."
        ],
        "params": [(30, 15), (40, 20), (20, 10), (60, 20), (50, 25)],
        "correct_base": "Under New Cartesian Sign Convention: pole is origin, incident direction is positive. Object is in front: u = -{u} cm. Concave mirror focus is in front: f = -{f} cm. 1/v = 1/f - 1/u = -1/{f} - (-1/{u}). Image is real, inverted, at v = -{cor_val} cm in front of mirror.",
        "misc_phrasings": [
            "v = +{slip} cm because distances in real life cannot be negative numbers; I set u = +{u} and f = +{f}.",
            "1/v = 1/{f} - 1/{u} giving positive v, because the object is in front of the mirror.",
            "Since the image is formed on the same side, v is positive {u} cm.",
            "I used 1/v = 1/{f} + 1/{u} with positive values because distance is always positive."
        ],
        "correct_phrasings": [
            "With u = -{u} cm and f = -{f} cm: 1/v = 1/(-{f}) - 1/(-{u}) = -1/{f} + 1/{u}, which gives v = -{cor_val} cm (in front of mirror, real).",
            "By New Cartesian Convention: u = -{u} cm, f = -{f} cm. 1/v = -1/{f} - (-1/{u}) => v = -{cor_val} cm.",
            "Using proper signs: u=-{u}, f=-{f}. The mirror formula yields v = -{cor_val} cm, indicating a real inverted image."
        ],
        "slip_phrasings": [
            "Applied negative signs correctly (u=-{u}, f=-{f}), but slipped on fraction subtraction: computed v = -{slip} cm.",
            "Correct sign setup, but forgot to invert 1/v at the final step, reporting v = -1/{cor_val} cm."
        ],
        "unit_phrasings": [
            "Image distance v = -{cor_val} meters instead of centimeters.",
            "Reported focal length with units cm^2."
        ],
        "unsure_phrasings": [
            "I always get confused about whether concave mirror focal length is positive or negative.",
            "Do we make u negative for all mirrors, or only concave mirrors?"
        ]
    },

    # 5. OPTICS: GLASS SLAB REFRACTION
    {
        "family": "OPTICS_GLASS_SLAB_REFRACTION",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Refraction through a Rectangular Glass Slab",
        "target_misc": "MISC-OPT-005: Glass Slab Angular Deviation Fallacy",
        "misc_desc": "Believes light emerging from a rectangular glass slab is permanently bent at an angle, confusing lateral displacement with angular deviation (prism behavior).",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Rectangular glass slab showing incident ray at angle i, refraction at angle r, and emergent ray at angle e = i parallel to incident ray with lateral displacement d.",
            "visual_elements": ["GlassSlab(parallel_faces)", "IncidentRay(i=45)", "RefractedRay", "EmergentRay(e=45)", "LateralDisplacement(d)"],
            "whiteboard_commands": [
                "draw_rectangular_slab(thickness=15)",
                "draw_incident_ray(angle=45)",
                "draw_refracted_ray_towards_normal()",
                "draw_emergent_ray_parallel_to_incident()",
                "write_equation('i = e  =>  Emergent ray is parallel to incident ray (Lateral shift only)')"
            ]
        },
        "stem_templates": [
            "A light ray enters a rectangular glass slab with parallel opposite faces at an angle of incidence of 45°. Describe the direction of the emergent ray relative to the incident ray.",
            "Light passes through a flat rectangular glass block of thickness {u} cm. Does the ray exit permanently bent at an angle or parallel to its original path?",
            "In NCERT Activity 10.10, light refracts through a rectangular glass block. How does the angle of emergence e compare to the angle of incidence i?"
        ],
        "params": [(10,), (15,), (20,), (12,), (8,)],
        "correct_base": "The emergent ray is parallel to the incident ray (angle of emergence e equals angle of incidence i: e = i). The ray undergoes only a lateral displacement (sideways shift), not an angular deviation, because the opposing refracting surfaces are strictly parallel.",
        "misc_phrasings": [
            "The emergent ray exits bent at a permanent angle because glass bends light permanently like a prism.",
            "The ray leaves at a sharp angle to its original direction due to refraction at both surfaces.",
            "The light gets dispersed into different angles because refraction changes the beam's direction permanently.",
            "Angle of emergence is smaller than incidence angle, so the ray permanently diverges."
        ],
        "correct_phrasings": [
            "The emergent ray is strictly parallel to the incident ray (angle i = angle e), shifted sideways by a lateral displacement proportional to slab thickness.",
            "No angular deviation occurs; the ray emerges parallel to its incident direction with lateral shift because the refracting faces are parallel.",
            "i = e. The emergent ray is parallel to the incident ray; it only suffers lateral displacement."
        ],
        "slip_phrasings": [
            "Emergent ray is parallel, but calculated lateral displacement as {slip} cm due to arithmetic slip.",
            "Stated i = e correctly, but mislabeled refractive index formula as n = sin r / sin i."
        ],
        "unit_phrasings": [
            "Lateral displacement reported in degrees instead of centimeters.",
            "Emergence angle reported in radians without conversion."
        ],
        "unsure_phrasings": [
            "Does a glass slab bend light like a prism, or does it come out parallel?",
            "I know light bends entering glass, but does it bend back the same amount leaving?"
        ]
    },

    # 6. HUMAN EYE: VISION DEFECTS
    {
        "family": "HUMAN_EYE_VISION_DEFECTS",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Defects of Vision and Their Correction",
        "target_misc": "MISC-EYE-001: Vision Defect Corrective Inversion",
        "misc_desc": "Inverts corrective lenses; prescribes convex lens for myopia (short-sightedness) or concave lens for hypermetropia.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Myopic eye forming image in front of retina, with concave corrective lens diverging rays to focus exactly on retina.",
            "visual_elements": ["EyeBall", "CrystallineLens", "Retina", "MyopicFocus(in_front)", "ConcaveLens(diverging)"],
            "whiteboard_commands": [
                "draw_eyeball_with_lens()",
                "show_myopic_rays(converging_point='in_front_of_retina')",
                "insert_corrective_lens(type='concave')",
                "show_corrected_rays(converging_point='on_retina')",
                "write_equation('Myopia: Eye is too converging => Correct with Diverging (Concave) Lens')"
            ]
        },
        "stem_templates": [
            "A student cannot see distant objects clearly beyond {fp} cm but reads a textbook comfortably at 25 cm. Name the defect of vision and specify the type of corrective lens required.",
            "A person with myopia has a far point of {fp} cm. What type of corrective spectacle lens is needed to restore normal distant vision?",
            "An eye examination shows that parallel rays from infinity focus in front of the retina at {fp} cm. Which spherical lens will correct this defect?"
        ],
        "params": [(80,), (150,), (100,), (200,), (120,)],
        "correct_base": "The defect is Myopia (near-sightedness). The eye lens is too converging (or eyeball is elongated), causing distant rays to focus IN FRONT of the retina. A concave (diverging) lens is required to diverge the rays so they focus sharply on the retina.",
        "misc_phrasings": [
            "The defect is myopia and must be corrected using a convex lens to converge the light.",
            "A convex spectacles lens is needed because convex lenses help you see things far away.",
            "The person has hypermetropia and needs a concave lens to push the focus back.",
            "Needs a converging convex lens of power P = +1/f to strengthen the eye focus."
        ],
        "correct_phrasings": [
            "Defect is Myopia (nearsightedness); corrected using a concave (diverging) lens with focal length f = -{fp} cm.",
            "Myopia: rays focus in front of retina. A concave lens is needed to diverge incoming parallel rays so they appear to come from the far point.",
            "The student suffers from myopia; a diverging (concave) lens of focal length -{fp} cm restores vision."
        ],
        "slip_phrasings": [
            "Identified myopia and concave lens correctly, but calculated lens power as P = +{slip} D instead of -{slip} D.",
            "Stated concave lens correctly, but wrote far point equation with wrong sign: f = +{fp} cm."
        ],
        "unit_phrasings": [
            "Corrective lens power is -1.25 Joules instead of Dioptres.",
            "Reported focal length in units of Hertz."
        ],
        "unsure_phrasings": [
            "I always mix up whether myopia takes convex or concave.",
            "Is myopia nearsightedness or farsightedness? I forget which lens goes with which."
        ]
    },

    # 7. HUMAN EYE: PRISM DISPERSION
    {
        "family": "HUMAN_EYE_PRISM_DISPERSION",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Refraction of Light Through a Prism & Dispersion",
        "target_misc": "MISC-EYE-002: Prism Dispersion Speed and Deviation Inversion",
        "misc_desc": "Believes red light is deflected most or that red travels slowest in glass, inverting the Cauchy dispersion relation.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Equilateral glass prism with white light incident. Red refracts least (top of band), Violet refracts most (bottom of band).",
            "visual_elements": ["GlassPrism", "WhiteRay", "RedRay(least_deviated)", "VioletRay(most_deviated)", "SpectrumBand"],
            "whiteboard_commands": [
                "draw_prism(apex_angle=60)",
                "split_white_light_at_face1()",
                "draw_red_beam(deviation='minimum', color='red')",
                "draw_violet_beam(deviation='maximum', color='violet')",
                "write_equation('v_red > v_violet  =>  n_violet > n_red  =>  Violet deviates most')"
            ]
        },
        "stem_templates": [
            "A narrow beam of white light passes through a triangular glass prism. Which constituent color undergoes the greatest deviation from its original path?",
            "In the dispersion of white light by a glass prism, which color of light travels fastest in glass and which deviates the least?",
            "Compare the angles of deviation for red light versus violet light when passing through an equilateral glass prism."
        ],
        "params": [(1,)],
        "correct_base": "Violet light undergoes the greatest deviation. In glass, refractive index depends on wavelength (Cauchy's relation: n_violet > n_red). Red light travels fastest (v = c/n) and deviates least; violet travels slowest and bends most towards the prism base.",
        "misc_phrasings": [
            "Red light is deviated the most because red has the strongest and most intense color energy.",
            "Red bends at the greatest angle because it has the longest wavelength.",
            "Red light travels slowest in glass, so it gets pulled and bent the most by the prism.",
            "Violet deviates least because it is at the bottom of the VIBGYOR rainbow spectrum."
        ],
        "correct_phrasings": [
            "Violet light deviates the most because glass has a higher refractive index for violet than for red (n_violet > n_red; v_violet < v_red).",
            "Violet bends most and red bends least. Red has the longest wavelength, travels fastest in glass, and suffers minimum deviation.",
            "Violet suffers the greatest angle of deviation because it travels slowest in glass, experiencing the greatest refractive index."
        ],
        "slip_phrasings": [
            "Stated violet deviates most, but listed VIBGYOR order backwards in the wavelength formula.",
            "Correctly identified violet, but computed refractive index as n = v/c instead of c/v."
        ],
        "unit_phrasings": [
            "Angle of deviation reported in nanometers instead of degrees.",
            "Light speed in glass given with units m/s^2."
        ],
        "unsure_phrasings": [
            "I know red and violet are at the ends, but I forget which one bends more.",
            "Does longer wavelength bend more or less when entering a prism?"
        ]
    },

    # 8. HUMAN EYE: ATMOSPHERIC REFRACTION & TWINKLING
    {
        "family": "HUMAN_EYE_ATMOSPHERIC_TWINKLING",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Atmospheric Refraction (Twinkling of Stars)",
        "target_misc": "MISC-EYE-003: Star Twinkling Emission Artifact Fallacy",
        "misc_desc": "Believes stars twinkle because of physical flickering, burning bursts, or cloud obstruction, rather than atmospheric refraction of point sources.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Light from distant star passing through turbulent atmospheric layers of varying density into observer's eye.",
            "visual_elements": ["DistantStar(point_source)", "AtmosphereLayers(varying_density)", "WaveringRay", "ObserverEye"],
            "whiteboard_commands": [
                "draw_star_at_infinity()",
                "draw_atmosphere_gradient(temperature_fluctuations=True)",
                "waver_ray_path()",
                "write_equation('Apparent position & brightness waver due to fluctuating air refractive index')"
            ]
        },
        "stem_templates": [
            "Why do stars twinkle at night when viewed from Earth, whereas planets do not twinkle?",
            "An observer watches a star on a clear night. What physical process causes the rapid flickering in position and brightness?",
            "Astronauts on the Moon do not observe star twinkling. Why do stars appear to twinkle only from Earth's surface?"
        ],
        "params": [(1,)],
        "correct_base": "Twinkling is caused by atmospheric refraction through turbulent, continuously shifting air layers with fluctuating temperatures and refractive indices. Because stars are distant point sources, small refractive deflections cause noticeable wavering in apparent position and brightness. Planets are extended sources, so point fluctuations average out.",
        "misc_phrasings": [
            "Stars twinkle because nuclear explosions on the star surface turn the light on and off rapidly.",
            "Twinkling occurs because thin invisible clouds pass continuously in front of the star.",
            "Stars physically pulsate and expand/contract every second, producing the blinking appearance.",
            "Planets shine constantly because they are made of solid rock, while stars are flickering gas fires."
        ],
        "correct_phrasings": [
            "Twinkling is caused by atmospheric refraction. Shifting temperature and density in air layers continuously alter the refractive index, making the point-sized star image waver in position and brightness.",
            "Due to atmospheric turbulence, the refractive index of air fluctuates continually along the light path. Stars are point sources, so intensity wavers.",
            "Atmospheric refraction through fluctuating air density causes apparent brightness and position to waver; planets are extended disks, so fluctuations average to zero."
        ],
        "slip_phrasings": [
            "Correctly identified atmospheric refraction, but stated stars are extended sources and planets are point sources.",
            "Explained refractive wavering accurately, but attributed effect to the ozone layer specifically."
        ],
        "unit_phrasings": [
            "Fluctuation frequency given in kilograms instead of Hertz.",
            "Refractive index difference labeled with units of meters."
        ],
        "unsure_phrasings": [
            "Is twinkling caused by the air or is the star itself actually flickering?",
            "I'm not sure why planets don't twinkle if stars do."
        ]
    },

    # 9. HUMAN EYE: RAYLEIGH SCATTERING & SKY COLOUR
    {
        "family": "HUMAN_EYE_RAYLEIGH_SCATTERING",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Scattering of Light and Colour of the Sky",
        "target_misc": "MISC-EYE-004: Sky Colour Reflection Fallacy",
        "misc_desc": "Believes the sky is blue because it reflects ocean water, or confuses wavelength dependence in Rayleigh scattering.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Sunlight striking atmospheric gas molecules. Blue light scatters in all directions (I ~ 1/lambda^4); red transmits through.",
            "visual_elements": ["SunBeam(white)", "GasMolecules(sub_micron)", "BlueScatteredRays", "RedTransmittedRay", "Observer"],
            "whiteboard_commands": [
                "draw_incident_sunlight()",
                "draw_air_molecule_scattering()",
                "write_equation('Rayleigh Scattering: Intensity proportional to 1 / lambda^4')",
                "write_equation('lambda_blue < lambda_red  =>  Blue scatters ~16x more than Red')"
            ]
        },
        "stem_templates": [
            "Why does the clear daytime sky appear blue to an observer on the ground?",
            "What physical optical process is responsible for the blue color of the clear sky?",
            "In an atmosphere devoid of particles and gas molecules, what color would the daytime sky appear?"
        ],
        "params": [(1,)],
        "correct_base": "Rayleigh scattering by atmospheric gas molecules (N2, O2) whose size is smaller than visible wavelengths. The intensity of scattered light is inversely proportional to the fourth power of wavelength (I ~ 1/lambda^4). Shorter blue wavelengths scatter roughly 16 times more strongly than red, illuminating the sky blue from all directions.",
        "misc_phrasings": [
            "The sky is blue because it acts as a giant mirror reflecting the blue water of Earth's oceans.",
            "Water vapor droplets in the sky are blue, coloring the atmosphere.",
            "Oxygen gas molecules are inherently blue in color, absorbing all other colors.",
            "The ozone layer filters out all colors except blue by direct chemical absorption."
        ],
        "correct_phrasings": [
            "Fine air molecules scatter shorter blue wavelengths far more intensely than longer red wavelengths (Rayleigh Scattering: I ~ 1/lambda^4).",
            "Due to Rayleigh scattering by sub-micron air molecules, blue light is scattered in all directions throughout the atmosphere.",
            "Gas molecules scatter shorter wavelengths (blue) far more effectively than longer wavelengths (red); in absence of atmosphere, sky appears black."
        ],
        "slip_phrasings": [
            "Stated Rayleigh scattering correctly, but wrote scattering intensity as proportional to lambda^4 instead of 1/lambda^4.",
            "Correctly identified blue scattering, but stated red light has higher frequency than blue."
        ],
        "unit_phrasings": [
            "Wavelength of blue light stated as 400 MHz instead of nanometers.",
            "Scattering cross-section reported with units of Amperes."
        ],
        "unsure_phrasings": [
            "Does the sky reflect the ocean or does the ocean reflect the sky?",
            "Why doesn't the sky look violet if violet has an even shorter wavelength than blue?"
        ]
    },

    # 10. ELECTRICITY: CURRENT CONSERVATION
    {
        "family": "ELECTRICITY_CURRENT_CONSERVATION",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Electric Current in Series Circuits (Conservation of Charge)",
        "target_misc": "MISC-ELEC-001: Current Attenuation / Consumption Model",
        "misc_desc": "Believes electric current is consumed or attenuated by circuit elements like resistors and bulbs as it circulates.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_diagram",
            "diagram_description": "Series circuit with 6V battery and two identical bulbs. Three ammeters A1, A2, A3 are placed before, between, and after the bulbs.",
            "visual_elements": ["Battery(6V)", "Bulb1", "Bulb2", "Ammeter1(A1)", "Ammeter2(A2)", "Ammeter3(A3)"],
            "whiteboard_commands": [
                "draw_series_circuit(battery=6V, components=['A1', 'Bulb1', 'A2', 'Bulb2', 'A3'])",
                "label_ammeters(A1='0.90 A', A2='0.90 A', A3='0.90 A')",
                "write_equation('Conservation of Charge: I_in = I_out  =>  A1 = A2 = A3')",
                "write_equation('Current is NOT consumed; only electric potential energy drops')"
            ]
        },
        "stem_templates": [
            "Two identical bulbs B1 and B2 are connected in series with a 6V battery. An ammeter A1 measures current entering B1, and A2 measures current leaving B2. How do the ammeter readings compare?",
            "Three resistors are wired in series. A technician measures current before the first resistor (I1) and after the third resistor (I3). What is the relationship between I1 and I3?",
            "In a simple series closed loop containing a battery and a light bulb, does the electric current returning to the negative terminal equal the current leaving the positive terminal?"
        ],
        "params": [(1,)],
        "correct_base": "A1 = A2 (current is strictly identical at every point in a series circuit). Electric charge is conserved; electrons cannot accumulate, leak, or be destroyed in a closed loop. Bulbs consume electric potential ENERGY (which converts to heat and light), NOT electric current or electric charge.",
        "misc_phrasings": [
            "A1 > A2 because bulb B1 consumes some of the electric current to glow, leaving less for A2.",
            "Current decreases along the circuit as it gets used up powering the bulbs.",
            "A1 reads 1.2 A but A2 reads only 0.6 A because current is spent across the resistors.",
            "The current returning to the battery is nearly zero because the load uses up the electricity."
        ],
        "correct_phrasings": [
            "A1 = A2. In any series circuit, electric current is identical at all points by conservation of charge (I = const).",
            "I1 = I3. Current is not consumed; only electrical potential energy drops across the load.",
            "The readings are exactly equal: electric charge cannot vanish, so rate of flow is conserved throughout the entire loop."
        ],
        "slip_phrasings": [
            "A1 = A2, but calculated the total equivalent resistance as R/2 instead of 2R.",
            "Correctly stated currents are identical, but reported current unit as Volts."
        ],
        "unit_phrasings": [
            "Current measured as 0.90 Joules instead of Amperes.",
            "Rate of electron flow stated in Coulombs/sec^2."
        ],
        "unsure_phrasings": [
            "If current isn't used up, what makes the bulb light up and battery go flat?",
            "I think the second bulb gets less current because it is further downstream."
        ]
    },

    # 11. ELECTRICITY: BATTERY CONSTANT CURRENT SOURCE
    {
        "family": "ELECTRICITY_PARALLEL_BATTERY_DELIVERY",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Parallel Circuits and Source Potential Difference",
        "target_misc": "MISC-ELEC-002: Battery as Constant Current Source",
        "misc_desc": "Believes a battery produces a fixed constant total current regardless of what external resistance network is connected.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_diagram",
            "diagram_description": "Battery connected to Bulb 1. A second identical Bulb 2 is connected in parallel via a switch. Battery delivers twice the current when switch closes.",
            "visual_elements": ["Battery(V=constant)", "Branch1(Bulb1)", "Branch2(Bulb2_with_switch)", "MainAmmeter"],
            "whiteboard_commands": [
                "draw_parallel_circuit(branches=['Bulb1', 'Bulb2'])",
                "show_state1(switch='open', I_total='1.0 A', brightness='full')",
                "show_state2(switch='closed', I_total='2.0 A', brightness='full')",
                "write_equation('Battery maintains CONSTANT VOLTAGE V, not constant current')",
                "write_equation('R_eq halved => I_total doubles => Branch current unchanged')"
            ]
        },
        "stem_templates": [
            "A bulb B1 is connected alone across a 12V car battery. An identical bulb B2 is now connected in parallel with B1. How does the brightness of B1 change?",
            "In a domestic parallel household circuit, what happens to the current through a room lamp when a powerful electric heater is switched ON in parallel?",
            "A battery maintains potential difference V across a resistor R. If an identical resistor is added in parallel, what happens to total battery current and current in the first branch?"
        ],
        "params": [(1,)],
        "correct_base": "Brightness of B1 is UNCHANGED. The battery maintains a constant potential difference V across each parallel branch (V1 = V2 = V). Current in branch 1 remains I1 = V/R. Adding branch 2 lowers the total equivalent resistance (R_eq = R/2), so the battery supplies TWICE the total current (I_total = 2I).",
        "misc_phrasings": [
            "Bulb B1 dims to half brightness because the battery provides a fixed total current that must now be shared.",
            "B1 dims because the second bulb steals half the current from the first bulb.",
            "The battery has a set amount of amps, so adding another branch starves the first branch.",
            "Brightness drops by 50% because the total battery current is split equally between the two bulbs."
        ],
        "correct_phrasings": [
            "Brightness of B1 remains completely unchanged. In parallel, voltage across B1 is constant (V), so branch current I = V/R is constant; total battery current doubles.",
            "B1 stays at full brightness. The battery is a constant voltage source, not constant current; each parallel branch operates independently.",
            "No change in B1's brightness: V is identical across parallel branches. The battery simply delivers more total current to meet demand."
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

    # 13. ELECTRICITY: PARALLEL RESISTANCE ADDITION
    {
        "family": "ELECTRICITY_PARALLEL_RESISTANCE_ADDITION",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Equivalent Resistance in Parallel Networks",
        "target_misc": "MISC-ELEC-005: Parallel Resistance Addition Fallacy",
        "misc_desc": "Overgeneralizes series addition to parallel circuits, believing adding resistors in parallel increases the total equivalent resistance (R_eq = R1 + R2).",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_diagram",
            "diagram_description": "Two parallel branches with resistors R1 and R2 showing charge splitting into two pathways, resulting in R_eq smaller than either resistor.",
            "visual_elements": ["ParallelNetwork", "Branch1(R1)", "Branch2(R2)", "TotalCurrentArrow"],
            "whiteboard_commands": [
                "draw_parallel_resistors(r1=10, r2=10)",
                "write_equation('1 / R_eq = 1/R1 + 1/R2')",
                "write_equation('R_eq = (R1 * R2) / (R1 + R2) < min(R1, R2)')",
                "write_equation('Adding parallel branches ADDS conductive pathways => R_eq DECREASES')"
            ]
        },
        "stem_templates": [
            "Two resistors of {u} ohms and {f} ohms are connected in parallel. What is the equivalent resistance of the network?",
            "A student adds a second resistor of {f} ohms in parallel across an existing {u} ohm resistor. How does the total circuit resistance change?",
            "Calculate the combined resistance when R1 = {u} ohms and R2 = {f} ohms are connected in parallel across a supply."
        ],
        "params": [(10, 10), (20, 20), (6, 12), (4, 4), (10, 40)],
        "correct_base": "In parallel: 1/R_eq = 1/R1 + 1/R2, so R_eq = (R1 * R2) / (R1 + R2). Adding another resistor in parallel ALWAYS decreases equivalent resistance because it creates an additional pathway for charge to flow.",
        "misc_phrasings": [
            "The equivalent resistance is {u} + {f} = {misc_val} ohms because adding more resistors always increases total resistance.",
            "R_eq = {misc_val} ohms; resistors always add up linearly regardless of whether they are series or parallel.",
            "Total resistance increases because you are adding another resistive obstruction to the circuit.",
            "R_eq = {misc_val} ohms; two resistors together must resist more than one resistor alone."
        ],
        "correct_phrasings": [
            "1/R_eq = 1/{u} + 1/{f}, yielding R_eq = {cor_val} ohms. Parallel branches provide additional paths, decreasing net resistance.",
            "R_eq = ({u} * {f}) / ({u} + {f}) = {cor_val} ohms, which is strictly less than either individual resistor.",
            "The combined resistance decreases to {cor_val} ohms because adding parallel branches increases total conductance."
        ],
        "slip_phrasings": [
            "Used 1/R_eq = 1/{u} + 1/{f} correctly, but forgot to take the reciprocal at the end, reporting 1/{cor_val} ohms.",
            "Computed R_eq as {slip} ohms due to common denominator addition error."
        ],
        "unit_phrasings": [
            "Equivalent resistance is {cor_val} Watts instead of Ohms.",
            "Reported resistance with units of Amperes."
        ],
        "unsure_phrasings": [
            "Does parallel resistance add like regular numbers or do we invert them?",
            "I get mixed up between the series formula and parallel formula for resistors."
        ]
    },

    # 14. ELECTRICITY: POWER FORMULA MISSELECTION
    {
        "family": "ELECTRICITY_POWER_FORMULA_MISSELECTION",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Joule Heating and Electric Power in Parallel vs Series",
        "target_misc": "MISC-ELEC-006: Power Formula Mis-selection in Parallel vs Series",
        "misc_desc": "Blindly applies P = I^2*R to parallel circuits where V is constant, wrongly concluding that higher resistance produces more heat in parallel.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_diagram",
            "diagram_description": "Two bulbs of 60W and 100W in parallel across 220V mains. 100W bulb has lower resistance and glows brighter.",
            "visual_elements": ["MainsSupply(220V)", "Bulb1(R=high)", "Bulb2(R=low)", "CurrentArrows"],
            "whiteboard_commands": [
                "draw_parallel_bulbs(voltage=220)",
                "write_equation('In Parallel: V is CONSTANT across all branches')",
                "write_equation('P = V^2 / R  =>  Power is INVERSELY proportional to R')",
                "write_equation('Smaller R draws larger current I = V/R  =>  Glows brighter')"
            ]
        },
        "stem_templates": [
            "Two electric bulbs rated 60 W and 100 W (both at 220 V) are connected in parallel to a 220 V supply. Which bulb has lower resistance and which glows brighter?",
            "Two resistors R1 = {u} ohms and R2 = {f} ohms (R1 < R2) are connected in parallel across a constant voltage supply. Which resistor dissipates more heat per second?",
            "In a household parallel circuit with constant voltage, does a high-resistance heater or a low-resistance heater consume more electric power?"
        ],
        "params": [(10, 20, 12), (5, 10, 6), (20, 40, 24), (15, 30, 12)],
        "correct_base": "In parallel, voltage V is constant across both branches. By P = V^2 / R, electric power is inversely proportional to resistance. The smaller resistance draws more current (I = V/R) and dissipates MORE power, glowing brighter.",
        "misc_phrasings": [
            "The {f} ohm resistor produces more heat because P = I^2 * R, so higher resistance always means more power dissipated.",
            "By P = I^2 * R, the larger resistor generates more heat because heat is directly proportional to resistance.",
            "More resistance creates more friction for electrons, so higher R always yields more watts in parallel.",
            "The 60 W bulb glows brighter in parallel because it has higher resistance and P = I^2*R."
        ],
        "correct_phrasings": [
            "In parallel, V is identical across both loads. Using P = V^2 / R, the smaller resistance of {u} ohms draws larger current and dissipates more power.",
            "Since voltage is constant in parallel, P = V^2/R governs power: smaller resistance dissipates greater heat.",
            "The lower resistance resistor dissipates more power because it draws proportionally more current at the same voltage."
        ],
        "slip_phrasings": [
            "Used P = V^2/R correctly, but squared V incorrectly as {slip} instead of {misc_val}.",
            "Correctly stated smaller R gives more power, but inverted formula as P = R / V^2."
        ],
        "unit_phrasings": [
            "Power dissipated is {misc_val} Ohms instead of Watts.",
            "Reported heating rate in Volts."
        ],
        "unsure_phrasings": [
            "When do we use P = I^2*R and when do we use P = V^2/R? I am confused.",
            "Does high resistance make things hotter or does high current make things hotter?"
        ]
    },

    # 15. MAGNETIC EFFECTS: MAGNETIC POLE VS CHARGE
    {
        "family": "MAGNETIC_EFFECTS_POLE_CHARGE_EQUIVALENCE",
        "grade": "Class 10",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Nature of Magnetic Poles vs Electrostatic Charges",
        "target_misc": "MISC-MAG-001: Magnetic Pole = Electrostatic Charge Equivalence Fallacy",
        "misc_desc": "Conflates magnetic poles with electrostatic charges, believing North poles are positively charged and attract stationary electrons.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "field_lines",
            "diagram_description": "Stationary electron placed near North pole of bar magnet. Magnetic force F = q(v x B) = 0 because v = 0.",
            "visual_elements": ["BarMagnet(North)", "StationaryElectron(v=0)", "MagneticFieldLines(B)", "ZeroForceVector"],
            "whiteboard_commands": [
                "draw_bar_magnet(poles=['North', 'South'])",
                "place_stationary_charge(q='-e', v=0)",
                "write_equation('Lorentz Force: F = q * (v x B) = q * v * B * sin(theta)')",
                "write_equation('When v = 0: F = 0  =>  Stationary charges feel ZERO magnetic force')",
                "write_equation('Magnetic poles are NOT electric charges')"
            ]
        },
        "stem_templates": [
            "A stationary electron is placed at rest near the North pole of a strong permanent bar magnet. What is the magnitude of the magnetic force exerted on the electron?",
            "Can a stationary electric charge be attracted or repelled by a static magnetic field from a bar magnet?",
            "A student claims that the North pole of a magnet is equivalent to a positive electrostatic charge (+Q). Is this statement scientifically accurate?"
        ],
        "params": [(1,)],
        "correct_base": "Zero force. The magnetic force on a charged particle is given by the Lorentz force equation F = q * (v x B) = q * v * B * sin(theta). When the charge is stationary (velocity v = 0), the magnetic force is strictly zero. Magnetic poles are dipoles arising from moving charges/spins, not electrostatic monopoles.",
        "misc_phrasings": [
            "The stationary electron is strongly attracted to the North pole because the North pole is like a positive charge (+Q).",
            "The North pole pulls the negative electron inwards by electrostatic attraction.",
            "A strong magnetic pole always attracts stationary electric charges just like a charged balloon.",
            "The electron gets repelled because North poles push away negative charges."
        ],
        "correct_phrasings": [
            "The magnetic force is strictly 0 N. A magnetic field exerts force only on MOVING charges (F = q*v*B*sin theta); when v = 0, force is zero.",
            "Zero force. Magnetic poles are not electric charges, and magnetic fields do not interact with stationary charges.",
            "No force acts on the electron. Since velocity v = 0, Lorentz force F = q(v x B) = 0 N."
        ],
        "slip_phrasings": [
            "Stated force is zero, but claimed an electric current could exist without any moving charges.",
            "Force is zero, but wrote Lorentz formula as F = q * v / B."
        ],
        "unit_phrasings": [
            "Magnetic force reported as 0 Tesla instead of Newtons.",
            "Magnetic charge reported in Coulombs."
        ],
        "unsure_phrasings": [
            "Don't magnets attract electric charges since electricity and magnetism are related?",
            "Is the North pole positive or negative? I'm not sure."
        ]
    },

    # 16. MAGNETIC EFFECTS: FIELD LINES CROSSING
    {
        "family": "MAGNETIC_EFFECTS_FIELD_LINES_CROSSING",
        "grade": "Class 10",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Properties of Magnetic Field Lines",
        "target_misc": "MISC-MAG-004: Field Line Crossing Fallacy",
        "misc_desc": "Believes magnetic field lines can intersect or cross each other where fields are strong or between two opposing magnets.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "field_lines",
            "diagram_description": "Smooth, continuous, non-intersecting magnetic field lines curving from North to South outside a bar magnet.",
            "visual_elements": ["BarMagnet", "FieldLines(continuous_loops)", "CompassNeedle(unique_tangent)"],
            "whiteboard_commands": [
                "draw_bar_magnet()",
                "draw_curved_field_lines_no_intersections()",
                "place_compass_at_point()",
                "write_equation('Compass can only point in ONE direction at any point')",
                "write_equation('Field lines NEVER intersect')"
            ]
        },
        "stem_templates": [
            "Can two magnetic field lines ever cross or intersect each other in space? Explain your reasoning.",
            "A student draws magnetic field lines around two bar magnets and shows two lines crossing at point P. Is this diagram physically valid?",
            "Why is it impossible for magnetic lines of force to intersect at any point in a magnetic field?"
        ],
        "params": [(1,)],
        "correct_base": "No two magnetic field lines can ever cross each other. If they did, a magnetic compass placed at the point of intersection would have to point in two different directions at the same instant, which is physically impossible. The net magnetic field vector at any point has a single unique direction.",
        "misc_phrasings": [
            "Yes, field lines cross each other when two strong magnets are pushed close together.",
            "Lines intersect at the neutral point between opposing magnetic poles.",
            "Field lines can cross because multiple magnetic forces can act simultaneously at the same location.",
            "Lines overlap and cross where the magnetic field strength is extremely dense."
        ],
        "correct_phrasings": [
            "Field lines never intersect. If they crossed, a compass needle would have to point in two different directions simultaneously, which is impossible.",
            "No, magnetic field lines cannot cross; at every point in space, the net magnetic field has a unique vector tangent.",
            "Impossible: intersecting lines would imply two different directions for the magnetic force at a single point."
        ],
        "slip_phrasings": [
            "Correctly stated lines cannot cross, but claimed field lines start at South and end at North outside the magnet.",
            "Identified that lines do not cross, but stated field lines are straight parallel lines everywhere."
        ],
        "unit_phrasings": [
            "Field line density given in Volts instead of Tesla.",
            "Reported magnetic flux in Amperes."
        ],
        "unsure_phrasings": [
            "I think field lines can cross if two magnets push against each other, but not sure.",
            "Do lines touch each other when the field is very strong?"
        ]
    },

    # 17. MAGNETIC EFFECTS: FLEMING'S LEFT-HAND RULE
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
            "The magnetic force is perpendicular to both current and magnetic field, directed vertically upwards for positive charge and downwards for electrons.",
            "By Fleming's Left Hand Rule: Force is vertically upwards for conventional current, and downwards for negative charges."
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
            "Do we use left hand for motors and right hand for generators, or the other way?"
        ]
    },

    # 18. MAGNETIC EFFECTS: ELECTROMAGNETIC INDUCTION
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
                "write_equation('EMF = -N * dPhi/dt  (Faraday-Lenz Law)')"
            ]
        },
        "stem_templates": [
            "A coil of {u} turns is placed inside a constant steady magnetic field of {f} T. Is any EMF induced in the coil?",
            "A wire coil with {u} loops sits motionless inside a steady non-changing magnetic field. Does a galvanometer connected to it deflect?",
            "A {u}-turn coil is held stationary in a uniform magnetic field of {f} T. What EMF is induced across its terminals?"
        ],
        "params": [(100, 2), (200, 5), (50, 1), (150, 3), (300, 4)],
        "correct_base": "No EMF is induced (EMF = 0 V). Faraday's Law states EMF = -N * dPhi/dt. A constant (non-changing) magnetic field produces zero rate of change of magnetic flux (dPhi/dt = 0), so induced EMF is strictly zero.",
        "misc_phrasings": [
            "Yes, a steady EMF of {u} x {f} = {misc_val} V is induced because the field acts continuously on the coil.",
            "The coil experiences an EMF proportional to field strength times turns = {misc_val} V.",
            "A constant field of {f} T through {u} turns gives a continuous EMF because magnetic flux exists.",
            "The galvanometer deflects continuously because the magnetic field passes through the coil loops."
        ],
        "correct_phrasings": [
            "Zero EMF. Faraday's Law: EMF = -N * dPhi/dt = 0 because dPhi/dt = 0 for a constant field.",
            "No deflection. Only a changing magnetic flux induces an EMF; a static field induces nothing.",
            "EMF = 0 V. Electromagnetic induction requires relative motion or change in magnetic flux, not mere presence of a field."
        ],
        "slip_phrasings": [
            "Correctly identified EMF = 0, but miscalculated time constant as {slip} s.",
            "Gave correct answer (zero EMF) but confused Faraday's Law equation with Ampere's Law."
        ],
        "unit_phrasings": [
            "EMF reported as {u} Tesla instead of Volts.",
            "Rate of flux change reported in T instead of Wb/s (Volts)."
        ],
        "unsure_phrasings": [
            "I think EMF is induced whenever the field is present, but I'm not sure about constant vs changing.",
            "Does the number of turns matter if the field is constant?"
        ]
    },

    # ========================== CLASS 9 PHYSICS (FOUNDATIONAL MECHANICS) ==========================
    # 19. MOTION: SPEED, DISTANCE, TIME
    {
        "family": "MOTION_SPEED_DISTANCE_TIME",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Uniform Motion and Rate of Change of Motion",
        "target_misc": "MISC-MOT-001: Speed Distance Operation Inversion",
        "misc_desc": "Multiplies distance and time instead of dividing, or inverts velocity formula as v = t / d.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_graph",
            "diagram_description": "Distance-time graph for uniform straight-line motion. Slope equals speed (v = d/t).",
            "visual_elements": ["TimeAxis(x)", "DistanceAxis(y)", "LinearSlope", "SlopeTriangle"],
            "whiteboard_commands": [
                "draw_axes(x='Time (s)', y='Distance (m)')",
                "plot_line(slope=20, label='v = 20 m/s')",
                "write_equation('Speed = Distance / Time  =>  v = d / t')",
                "write_equation('Units: meters / seconds = m/s')"
            ]
        },
        "stem_templates": [
            "A runner covers a straight track of {d} meters in {t} seconds. Calculate the runner's average speed.",
            "An automobile travels a distance of {d} m in {t} s along a straight highway. What is its speed?",
            "A bicycle covers {d} meters in {t} seconds with uniform velocity. Determine the speed."
        ],
        "params": [(100, 5), (300, 15), (60, 3), (200, 10), (150, 5)],
        "correct_base": "Speed = Distance / Time = {d} m / {t} s = {cor_val} m/s.",
        "misc_phrasings": [
            "Speed is {misc_val} m/s because I multiplied distance by time ({d} * {t} = {misc_val}).",
            "I calculated speed = {d} * {t} = {misc_val} m/s.",
            "Speed = distance times time, so it equals {misc_val} m/s.",
            "v = t / d = {t} / {d} = {div_val} m/s because time comes first."
        ],
        "correct_phrasings": [
            "Average speed = Distance / Time = {d} / {t} = {cor_val} m/s.",
            "v = d / t = {d} / {t} = {cor_val} m/s along the straight track.",
            "Speed is rate of distance covered per unit time: {d} m / {t} s = {cor_val} m/s."
        ],
        "slip_phrasings": [
            "Set up formula correctly as {d} / {t}, but made arithmetic error: computed {slip} m/s.",
            "Divided correctly but wrote speed as {cor_val} km/h without converting units."
        ],
        "unit_phrasings": [
            "Speed = {cor_val} meters instead of m/s.",
            "Calculated {cor_val} seconds per meter."
        ],
        "unsure_phrasings": [
            "Do we multiply distance and time or divide distance by time for speed?",
            "I get confused about whether distance goes on top or bottom."
        ]
    },

    # 20. MOTION: SPEED VS ACCELERATION
    {
        "family": "MOTION_SPEED_VS_ACCELERATION",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Acceleration vs Constant Velocity",
        "target_misc": "MISC-MOT-002: Speed-Acceleration Conflation",
        "misc_desc": "Equates high speed with high acceleration; believes a vehicle moving at high constant speed must have large acceleration.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_graph",
            "diagram_description": "Velocity-time graph showing horizontal line for constant velocity v = 20 m/s. Slope a = dv/dt = 0.",
            "visual_elements": ["TimeAxis(x)", "VelocityAxis(y)", "HorizontalLine(v=20)", "ZeroSlopeLabel"],
            "whiteboard_commands": [
                "draw_axes(x='Time (s)', y='Velocity (m/s)')",
                "plot_horizontal_line(y=20, label='Constant Speed')",
                "write_equation('Acceleration = Change in Velocity / Time = (v - u) / t')",
                "write_equation('Since v = u = 20 m/s: a = (20 - 20) / 10 = 0 m/s^2')",
                "write_equation('High Speed does NOT equal High Acceleration!')"
            ]
        },
        "stem_templates": [
            "A high-speed train travels along a straight track at a steady, uniform velocity of {v} m/s for {t} seconds. What is the acceleration of the train during this time?",
            "An aircraft cruises at a constant speed of {v} m/s in a straight line for {t} s. Determine its acceleration.",
            "A sports car maintains a fixed speedometer reading of {v} m/s along a straight test track for {t} seconds. Find its acceleration."
        ],
        "params": [(20, 10), (50, 5), (30, 10), (100, 20), (25, 5)],
        "correct_base": "Acceleration is 0 m/s^2. Acceleration is the RATE OF CHANGE of velocity: a = (v - u) / t. Because velocity is constant and direction is unchanged, delta v = 0, so acceleration is strictly zero regardless of how high the speed is.",
        "misc_phrasings": [
            "Acceleration is {v} m/s^2 because the train is moving very fast at {v} m/s.",
            "Acceleration = {v} / {t} = {div_val} m/s^2 (divided speed by time without checking if speed was changing).",
            "The train accelerates at {v} m/s^2 to maintain its high speed.",
            "High speed means high acceleration, so it cannot be zero."
        ],
        "correct_phrasings": [
            "Acceleration is 0 m/s^2. Acceleration requires a change in velocity (a = delta v / delta t). Constant speed on a straight track means delta v = 0.",
            "0 m/s^2. Since velocity is uniform ({v} m/s), there is zero change in velocity, so acceleration is zero.",
            "Zero acceleration. A high speed does not imply acceleration unless velocity is changing."
        ],
        "slip_phrasings": [
            "Identified 0 m/s^2 acceleration, but computed distance traveled as {slip} m due to arithmetic slip.",
            "Correctly stated zero acceleration, but stated acceleration formula as a = v * t."
        ],
        "unit_phrasings": [
            "Acceleration is 0 m/s instead of m/s^2.",
            "Reported acceleration in Newtons."
        ],
        "unsure_phrasings": [
            "If an object is moving fast, doesn't it have acceleration?",
            "I'm not sure if acceleration is speed divided by time or change in speed divided by time."
        ]
    },

    # 21. FORCE: NEWTON'S FIRST LAW & IMPETUS
    {
        "family": "FORCE_NEWTON_FIRST_LAW",
        "grade": "Class 9",
        "chapter": "Force and Laws of Motion",
        "topic": "Newton's First Law of Motion and Inertia",
        "target_misc": "MISC-FOR-001: Impetus Theory (Force is Required to Sustain Motion)",
        "misc_desc": "Aristotelian impetus fallacy: believes an object moving at constant velocity requires a continuous forward net force to keep moving.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Hockey puck sliding at constant velocity on frictionless horizontal ice. Net horizontal force is zero.",
            "visual_elements": ["Puck(mass=m)", "VelocityVector(v=constant)", "FrictionlessSurface", "ZeroNetForce"],
            "whiteboard_commands": [
                "draw_puck_on_ice()",
                "draw_gravity_down(mg)",
                "draw_normal_up(N)",
                "note_horizontal_forces(none)",
                "write_equation('Newton First Law: F_net = 0  =>  Velocity remains CONSTANT')",
                "write_equation('No force is needed to sustain motion!')"
            ]
        },
        "stem_templates": [
            "A hockey puck of mass {m} kg glides across perfectly frictionless horizontal ice at a constant speed of {v} m/s. What net horizontal force is required to keep it moving at this speed?",
            "A space probe of mass {m} kg drifts through deep space far from any stars at constant velocity {v} m/s. What forward rocket thrust is needed to maintain its motion?",
            "An object of mass {m} kg slides on a frictionless horizontal plane at {v} m/s. What is the net horizontal force acting on the object?"
        ],
        "params": [(2, 10), (5, 4), (1, 20), (10, 5), (3, 15)],
        "correct_base": "Net horizontal force required is 0 N. By Newton's First Law of Motion (Law of Inertia), an object in uniform motion continues to move with constant velocity unless acted upon by an external net force. Force causes acceleration (change in motion), not motion itself.",
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

    # 22. FORCE: NEWTON'S THIRD LAW ACTION-REACTION
    {
        "family": "FORCE_NEWTON_THIRD_LAW_ACTION_REACTION",
        "grade": "Class 9",
        "chapter": "Force and Laws of Motion",
        "topic": "Newton's Third Law (Action and Reaction)",
        "target_misc": "MISC-FOR-002: Action-Reaction Self-Cancellation Fallacy",
        "misc_desc": "Believes action and reaction forces cancel each other out on the same body, preventing acceleration from occurring.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Horse pulling a cart. Action force is exerted on cart; reaction force is exerted on horse. Because they act on different bodies, they do not cancel.",
            "visual_elements": ["BodyA(Horse)", "BodyB(Cart)", "ForceAonB(on_cart)", "ForceBonA(on_horse)"],
            "whiteboard_commands": [
                "draw_horse_and_cart()",
                "draw_force_on_cart(arrow='forward', label='F_horse_on_cart')",
                "draw_force_on_horse(arrow='backward', label='F_cart_on_horse')",
                "write_equation('Newton Third Law: Action & Reaction act on DIFFERENT bodies')",
                "write_equation('They NEVER cancel each other on a single body!')"
            ]
        },
        "stem_templates": [
            "A horse pulls a cart forward. By Newton's Third Law, the cart pulls the horse backward with an equal and opposite force. Why doesn't the system remain stationary if the forces are equal and opposite?",
            "If every action force produces an equal and opposite reaction force, why do objects ever accelerate instead of canceling out to zero net force?",
            "When a soccer player kicks a ball, the ball pushes back on the foot with an equal and opposite force. Why does the ball accelerate forward?"
        ],
        "params": [(1,)],
        "correct_base": "Action and reaction forces never cancel each other because they ACT ON TWO DIFFERENT BODIES. The forward action force acts ON THE CART, while the backward reaction force acts ON THE HORSE. An object's acceleration depends solely on the net external force acting on THAT specific body.",
        "misc_phrasings": [
            "The forces cancel out to zero on the cart, so the horse must produce an action force greater than the reaction force to move.",
            "Third law only applies when objects are stationary; when moving, action becomes greater than reaction.",
            "Action and reaction balance each other on the cart, so friction has to break the tie.",
            "If forces are equal and opposite, net force is zero so nothing can ever accelerate."
        ],
        "correct_phrasings": [
            "Action and reaction act on two different bodies (horse on cart, cart on horse), so they cannot cancel each other. The cart accelerates due to the net force on the cart alone.",
            "They never cancel because they are applied to different objects; cancellation only occurs when opposing forces act on the same single body.",
            "Newton's third law pairs act on separate bodies: the force on the ball accelerates the ball; the force on the foot slows the foot."
        ],
        "slip_phrasings": [
            "Stated forces act on different bodies, but calculated net force on cart using mass of horse.",
            "Correctly identified different bodies, but referred to Newton's Second Law instead of Third Law."
        ],
        "unit_phrasings": [
            "Action force reported as 50 Joules instead of Newtons.",
            "Reaction force labeled with momentum units."
        ],
        "unsure_phrasings": [
            "If the forces are equal and opposite, why don't they cancel out like tug-of-war?",
            "How can a cart move if it pulls back with the same force the horse pulls forward?"
        ]
    },

    # 23. GRAVITATION: FREE FALL MASS INDEPENDENCE
    {
        "family": "GRAVITATION_FREE_FALL",
        "grade": "Class 9",
        "chapter": "Gravitation",
        "topic": "Free Fall and Acceleration Due to Gravity (Mass Independence)",
        "target_misc": "MISC-GRAV-001: Heavier Objects Fall Faster Fallacy",
        "misc_desc": "Aristotelian gravity fallacy: believes heavier objects accelerate faster and hit the ground first in free fall in a vacuum.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_graph",
            "diagram_description": "Evacuated glass vacuum tube. A heavy lead cannonball and a light feather dropped from height h hit the bottom at the exact same instant.",
            "visual_elements": ["VacuumTube", "HeavyBall(mass=M)", "Feather(mass=m)", "SimultaneousImpact"],
            "whiteboard_commands": [
                "draw_vacuum_chamber(pressure=0)",
                "drop_objects(mass1=M, mass2=m, height=h)",
                "write_equation('Gravitational Force: F = m * g  (depends on mass)')",
                "write_equation('Acceleration: a = F / m = (m * g) / m = g  (INDEPENDENT of mass!)')",
                "write_equation('All bodies fall with identical acceleration g in vacuum')"
            ]
        },
        "stem_templates": [
            "A heavy cannonball of mass {M} kg and a light feather of mass {m} g are dropped simultaneously from height {h} m inside an evacuated vacuum chamber. Which object reaches the ground first?",
            "In an Apollo 15 moon experiment without air, an astronaut drops a hammer (1.32 kg) and a falcon feather (0.03 kg) from the same height. Compare their landing times.",
            "Two spheres of masses {M} kg and {m} kg are released from rest from a tower of height {h} m in vacuum. Which hits the ground first?"
        ],
        "params": [(10, 5, 20), (50, 1, 10), (5, 2, 15), (20, 1, 30), (100, 10, 50)],
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

    # 24. WORK, ENERGY & POWER: DIRECTION DEPENDENCE
    {
        "family": "WORK_ENERGY_POWER_CLASS9",
        "grade": "Class 9",
        "chapter": "Work and Energy",
        "topic": "Work Done by Force: Direction Dependence",
        "target_misc": "MISC-WRK-001: Work Equals Force Times Distance Regardless of Direction",
        "misc_desc": "Applies W = F * d without considering the angle between force and displacement; believes work is done whenever force is applied even if perpendicular to motion.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Block pushed horizontally while normal force acts vertically — perpendicular force does zero work.",
            "visual_elements": ["Block(moving_right)", "Applied_Force(horizontal)", "Normal_Force(vertical)", "Weight(downward)"],
            "whiteboard_commands": [
                "draw_block_on_surface(displacement='right')",
                "draw_force_vector(direction='up', label='Normal Force N')",
                "draw_force_vector(direction='right', label='Applied Force F')",
                "write_equation('W = F * d * cos(theta)')",
                "write_equation('If theta=90 deg: W = F * d * cos(90 deg) = 0')"
            ]
        },
        "stem_templates": [
            "A porter carries a {m} kg bag on his head and walks horizontally for {v} m. How much work is done by the vertical holding force he exerts?",
            "A man carries a {m} kg load and walks {v} m on a flat road. Calculate work done by the vertical holding force.",
            "A force of {m} N acts vertically upward while an object moves horizontally for {v} m. What work is done by this force?"
        ],
        "params": [(10, 5), (20, 8), (15, 6), (25, 10), (12, 4)],
        "correct_base": "W = F * d * cos(theta). When force is perpendicular to displacement (theta = 90 deg), W = F * d * cos(90 deg) = 0 J. No work is done by a force perpendicular to the direction of motion.",
        "misc_phrasings": [
            "Work done = {m} * {v} = {misc_val} J because force times displacement = work, direction doesn't matter.",
            "The porter does {misc_val} J of work because he exerts a force of {m} N over {v} m.",
            "Work = F * d = {m} * {v} = {misc_val} J regardless of direction.",
            "Force of {m} N for {v} m always gives {misc_val} J of work done."
        ],
        "correct_phrasings": [
            "Work done = F * d * cos(90 deg) = {m} * {v} * 0 = 0 J. Force perpendicular to motion does zero work.",
            "0 J. The vertical holding force is perpendicular to horizontal displacement; W = 0.",
            "Zero joules. W = Fd cos theta where theta = 90 deg gives W = 0."
        ],
        "slip_phrasings": [
            "Correctly wrote W = Fd cos theta but computed cos(90 deg) = 1 instead of 0; got {misc_val} J.",
            "Identified zero work but miscalculated F * d as {slip} instead of {misc_val}."
        ],
        "unit_phrasings": [
            "Work = 0 Newtons instead of Joules.",
            "Work stated as {misc_val} kg*m instead of Joules."
        ],
        "unsure_phrasings": [
            "I know direction matters but I'm not sure how to apply cosine to this situation.",
            "Does carrying something count as work even if you don't move vertically?"
        ]
    },

    # 25. MOMENTUM: CONSERVATION IN COLLISIONS
    {
        "family": "MOMENTUM_CONSERVATION_CLASS9",
        "grade": "Class 9",
        "chapter": "Force and Laws of Motion",
        "topic": "Law of Conservation of Momentum",
        "target_misc": "MISC-MOM-001: Momentum Not Conserved When Object Stops",
        "misc_desc": "Believes momentum is destroyed or disappears when one object stops in a collision, rather than being transferred to another body.",
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
            "A {m} kg ball moving at {v} m/s collides head-on with an identical stationary ball. Ball 1 stops. What is the velocity of ball 2?",
            "Ball of mass {m} kg travelling at {v} m/s hits another ball of equal mass at rest and comes to complete stop. Find the speed of second ball.",
            "Two identical balls of mass {m} kg: first moves at {v} m/s, second is at rest. After collision, first stops. Using conservation of momentum, find second ball's velocity."
        ],
        "params": [(2, 5), (3, 4), (5, 6), (1, 8), (4, 3)],
        "correct_base": "By conservation of momentum: p_before = p_after. m*v + 0 = 0 + m*v2, so v2 = v. The second ball moves forward at the same speed ({v} m/s) the first ball originally possessed.",
        "misc_phrasings": [
            "Momentum is destroyed when ball 1 stops. Ball 2 receives no velocity since ball 1 has zero momentum at rest.",
            "When ball 1 stops, it loses its momentum. Ball 2 stays stationary.",
            "Ball 1 at rest means total momentum becomes zero; ball 2 remains at rest.",
            "The {m} kg ball stops so all {misc_val} kg m/s of momentum disappears — ball 2 has none."
        ],
        "correct_phrasings": [
            "By conservation of momentum: {m} * {v} = {m} * v2, so v2 = {v} m/s.",
            "Momentum is conserved: initial p = {misc_val} kg m/s = final p, so ball 2 moves at {v} m/s.",
            "v2 = {v} m/s because m1*v1 = m2*v2 and masses are equal."
        ],
        "slip_phrasings": [
            "Applied conservation correctly but computed {m} * {v} = {slip} due to arithmetic slip.",
            "Got v2 = {v} m/s correctly but stated units as m/s^2 instead of m/s."
        ],
        "unit_phrasings": [
            "Momentum stated as {misc_val} m/s instead of kg m/s.",
            "Velocity of ball 2 given as {v} Newtons instead of m/s."
        ],
        "unsure_phrasings": [
            "I think momentum is transferred somehow but I don't know the exact rule.",
            "Does ball 2 move with the same speed or different speed? I'm not sure."
        ]
    },

    # 26. OPTICS: MAGNIFICATION SIGN INTERPRETATION
    {
        "family": "OPTICS_MAGNIFICATION_SIGN_INTERPRETATION",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Linear Magnification by Spherical Mirrors and Lenses",
        "target_misc": "MISC-OPT-006: Magnification Negative Sign Magnitude Fallacy",
        "misc_desc": "Conflates the negative sign of magnification with size diminished, wrongly believing m = -2.0 means the image is smaller than the object because negative numbers are less than zero.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Concave mirror forming enlarged inverted real image. Magnification m = -2.0 indicates image is twice as large as object and inverted.",
            "visual_elements": ["ConcaveMirror", "Object(h=2cm)", "Image(h'=-4cm, inverted)", "PrincipalAxis"],
            "whiteboard_commands": [
                "draw_concave_mirror()",
                "draw_object_and_inverted_image(h=2, h_prime=-4)",
                "write_equation('m = h_prime / h = -4 / 2 = -2.0')",
                "write_equation('Minus sign indicates INVERTED (real) orientation')",
                "write_equation('|m| = 2.0 > 1  =>  Image is ENLARGED, not diminished!')"
            ]
        },
        "stem_templates": [
            "A spherical mirror produces an image with linear magnification m = -2.0. Is the image enlarged or diminished, and what is its orientation?",
            "A student computes the magnification of an optical setup as m = -1.5. Describe the size and nature of the image.",
            "If the magnification produced by a concave mirror is m = -3.0, does this mean the image is three times smaller or three times larger than the object?"
        ],
        "params": [(1,)],
        "correct_base": "The image is ENLARGED (twice the size of the object) and INVERTED (real). In optical magnification m = h'/h, the negative sign indicates inversion (real image). The absolute magnitude |m| determines size: |m| = 2.0 > 1 means enlarged.",
        "misc_phrasings": [
            "The image is diminished and smaller because -2 is a negative number and less than 1.",
            "Since magnification is negative (-2.0), the image must be smaller than the object.",
            "Negative magnification means the image shrinks below zero size.",
            "m = -1.5 means the image is smaller by 1.5 times because negative values mean reduction."
        ],
        "correct_phrasings": [
            "The image is enlarged and inverted. The minus sign denotes an inverted real image, while |m| = 2.0 > 1 proves the image height is twice the object height.",
            "Enlarged and inverted. In optics, sign indicates orientation (negative = inverted) and absolute value indicates size scaling (|m| > 1 is enlarged).",
            "The image is 2 times larger than the object and inverted. The negative sign only signifies inversion, not a reduction in size."
        ],
        "slip_phrasings": [
            "Stated enlarged and inverted, but calculated image distance as v = +u/m instead of v = -m*u.",
            "Correctly identified enlarged, but stated image is virtual."
        ],
        "unit_phrasings": [
            "Magnification is -2.0 cm instead of a dimensionless scalar.",
            "Magnification reported in Dioptres."
        ],
        "unsure_phrasings": [
            "Does negative magnification mean smaller or upside down? I am unsure.",
            "How can magnification be negative if length is positive?"
        ]
    },

    # 27. OPTICS: REFRACTIVE INDEX SPEED INVERSION
    {
        "family": "OPTICS_REFRACTIVE_INDEX_SPEED_INVERSION",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Refractive Index and Speed of Light in Media",
        "target_misc": "MISC-OPT-007: Refractive Index Speed Proportionality Inversion",
        "misc_desc": "Believes higher refractive index means light travels faster, inverting the formula n = c / v to v = n * c.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Light ray passing from air into glass (n=1.5). Light slows down from 3e8 m/s to 2e8 m/s.",
            "visual_elements": ["Boundary", "Air(n=1.0, v=3e8)", "Glass(n=1.5, v=2e8)", "RayBendingTowardsNormal"],
            "whiteboard_commands": [
                "draw_interface(medium1='Air', medium2='Glass')",
                "write_equation('n = c / v  =>  v = c / n')",
                "write_equation('Higher n  =>  SLOWER light speed')",
                "write_equation('In glass (n=1.5): v = 3e8 / 1.5 = 2.0e8 m/s')"
            ]
        },
        "stem_templates": [
            "The absolute refractive index of glass is 1.5. Calculate the speed of light in glass given c = 3.0 x 10^8 m/s.",
            "Medium A has refractive index 1.33 and Medium B has refractive index 1.65. In which medium does light travel faster?",
            "Given that diamond has a high refractive index of 2.42, does light travel faster or slower in diamond compared to water (n = 1.33)?"
        ],
        "params": [(1,)],
        "correct_base": "Speed of light v = c / n = (3.0 x 10^8) / 1.5 = 2.0 x 10^8 m/s. Refractive index is inversely proportional to speed; higher optical density (higher n) means light travels SLOWER.",
        "misc_phrasings": [
            "v = c * n = 3.0e8 * 1.5 = 4.5e8 m/s; light speeds up because glass has higher index 1.5.",
            "Light travels faster in medium B (n=1.65) because greater refractive index accelerates the light rays.",
            "Light travels fastest in diamond because it has the highest refractive index of 2.42.",
            "v = n * c because optical density boosts light velocity."
        ],
        "correct_phrasings": [
            "Speed in glass is v = c / n = 3.0e8 / 1.5 = 2.0e8 m/s. Higher refractive index corresponds to slower light propagation.",
            "Light travels faster in the medium with lower refractive index (Medium A, n=1.33) because v = c/n.",
            "Light travels much slower in diamond (v = c/2.42 = 1.24e8 m/s) because speed is inversely proportional to refractive index."
        ],
        "slip_phrasings": [
            "Divided correctly as 3e8 / 1.5, but wrote result as 2.0e7 m/s due to exponent error.",
            "Stated light slows down, but inverted ratio as n = v / c."
        ],
        "unit_phrasings": [
            "Speed of light in glass is 2.0e8 Newtons instead of m/s.",
            "Refractive index reported in m/s."
        ],
        "unsure_phrasings": [
            "Does high refractive index mean light is faster or slower?",
            "I forget whether we multiply or divide c by n to get speed."
        ]
    },

    # 28. OPTICS: CONCAVE LENS REAL IMAGE FALLACY
    {
        "family": "OPTICS_CONCAVE_LENS_REAL_IMAGE_FALLACY",
        "grade": "Class 10",
        "chapter": "Light – Reflection and Refraction",
        "topic": "Image Formation by Concave (Diverging) Lenses",
        "target_misc": "MISC-OPT-008: Concave Lens Real Image Fallacy",
        "misc_desc": "Believes a concave lens can form a real inverted image on a screen if the object is placed far away beyond 2F.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Concave lens diverging incident parallel rays. Virtual erect diminished image formed between optical center and focus.",
            "visual_elements": ["ConcaveLens", "DivergingRays", "VirtualFocus(F1)", "VirtualImage(erect)"],
            "whiteboard_commands": [
                "draw_concave_lens()",
                "draw_diverging_refracted_rays()",
                "show_virtual_intersection_at_F()",
                "write_equation('Concave lens ALWAYS forms VIRTUAL, ERECT, DIMINISHED images')",
                "write_equation('Can NEVER project an image on a real screen')"
            ]
        },
        "stem_templates": [
            "A student places an illuminated object 50 cm in front of a concave lens of focal length 20 cm. Can a sharp image be formed on a screen placed on the other side?",
            "Under what object distance conditions can a concave (diverging) spherical lens form a real inverted image?",
            "Can a concave lens project a real image of a lighted candle onto a white wall?"
        ],
        "params": [(1,)],
        "correct_base": "No, a concave lens can NEVER form a real image on a screen under any circumstances. A concave lens is a diverging lens that always causes refracted rays to spread outward. It always forms an erect, diminished, virtual image on the same side as the object, which cannot be captured on a screen.",
        "misc_phrasings": [
            "Yes, if the object is placed beyond 2F (at 50 cm), a real inverted image will be formed on the screen.",
            "A real image forms on the screen as long as the screen is positioned at the focal distance 20 cm.",
            "Concave lenses produce real images when objects are far away, just like concave mirrors.",
            "Screen will show a real magnified image on the opposite side."
        ],
        "correct_phrasings": [
            "No screen can capture an image: a concave lens always diverges light and forms only virtual, erect, diminished images.",
            "Never. Regardless of object distance, a concave lens always produces a virtual image located between the optical center and focus on the same side.",
            "No image can be focused on a screen because diverging lenses never bring light rays to a real physical convergence."
        ],
        "slip_phrasings": [
            "Stated virtual image correctly, but computed image distance with wrong sign as v = +14.3 cm.",
            "Correctly stated virtual, but claimed magnification is greater than 1."
        ],
        "unit_phrasings": [
            "Virtual image distance is -14.3 Volts instead of cm.",
            "Power of concave lens reported with units of Amperes."
        ],
        "unsure_phrasings": [
            "Can a concave lens form a real image if you move it far enough?",
            "I get confused between concave mirrors and concave lenses."
        ]
    },

    # 29. HUMAN EYE: SUNSET RED SCATTERING
    {
        "family": "HUMAN_EYE_SUNSET_RED_SCATTERING",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Colour of the Sun at Sunrise and Sunset",
        "target_misc": "MISC-EYE-005: Sunset Red Absorption / Temperature Fallacy",
        "misc_desc": "Believes the Sun appears reddish at sunset because the Sun physically cools down, or because red light is absorbed by clouds.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Sun near horizon traversing longer atmospheric path. Blue light is scattered away; least scattered red light reaches observer.",
            "visual_elements": ["EarthAtmosphere", "SunAtNoon(short_path)", "SunAtHorizon(long_path)", "ScatteredBlueRays", "TransmittedRedRay"],
            "whiteboard_commands": [
                "draw_earth_with_atmosphere()",
                "draw_sun_at_horizon(path='long')",
                "scatter_blue_light_away(I_proportional_to_1_over_lambda4)",
                "transmit_red_light_directly_to_eye()",
                "write_equation('Longest wavelength Red scatters least  =>  Reaches observer directly')"
            ]
        },
        "stem_templates": [
            "Why does the Sun appear reddish during sunrise and sunset, whereas it appears white at noon?",
            "What optical phenomenon causes the reddish appearance of the Sun near the horizon?",
            "Explain why the setting sun looks deep red while the daytime overhead sun looks bright white."
        ],
        "params": [(1,)],
        "correct_base": "Near the horizon, sunlight must pass through a much thicker layer of the atmosphere. By Rayleigh scattering (I ~ 1/lambda^4), shorter wavelengths (blue and violet) are scattered away in all directions before reaching the observer. Only the longer, least-scattered red wavelengths penetrate the thick path directly into our eyes.",
        "misc_phrasings": [
            "The Sun looks red at sunset because it cools down at the end of the day, lowering its temperature.",
            "Red appearance happens because evening clouds absorb all red light and reflect it down.",
            "Dust particles at ground level only produce red light by chemical reaction at sunset.",
            "The Sun burns red fuel in the evening when it moves closer to the horizon."
        ],
        "correct_phrasings": [
            "At sunset, sunlight travels through a longer atmospheric path. Shorter blue wavelengths are scattered away, leaving the least-scattered red light to reach our eyes.",
            "Due to Rayleigh scattering, blue light is scattered out of the line of sight over the long horizon path; red light with longer wavelength penetrates directly.",
            "Red light has the longest visible wavelength and scatters least, so it survives the long atmospheric distance at sunrise and sunset."
        ],
        "slip_phrasings": [
            "Explained Rayleigh scattering correctly, but claimed red light scatters more than blue light.",
            "Correct mechanism, but stated the sun looks red due to total internal reflection in raindrops."
        ],
        "unit_phrasings": [
            "Atmospheric path length is 500 Kilowatts instead of kilometers.",
            "Scattering wavelength given in Hertz."
        ],
        "unsure_phrasings": [
            "Does the Sun change color because of dust or because the atmosphere bends it?",
            "Why doesn't the noon sun look red if it has the same light?"
        ]
    },

    # 30. HUMAN EYE: ADVANCED SUNRISE & DELAYED SUNSET
    {
        "family": "HUMAN_EYE_ADVANCED_SUNRISE_DELAYED_SUNSET",
        "grade": "Class 10",
        "chapter": "The Human Eye and the Colourful World",
        "topic": "Atmospheric Refraction (Advanced Sunrise and Delayed Sunset)",
        "target_misc": "MISC-EYE-006: Horizon Straight-Line Geometric Fallacy",
        "misc_desc": "Believes the Sun is visible 2 minutes before actual sunrise because light travels in perfectly straight lines and Earth rotates faster in the morning.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "ray_diagram",
            "diagram_description": "Sun below actual horizon. Rays entering atmosphere bend downwards towards normal into observer's eye, lifting apparent position above horizon.",
            "visual_elements": ["EarthCurvature", "AtmosphereGradient", "ActualSun(below_horizon)", "ApparentSun(above_horizon)", "BentRayPath"],
            "whiteboard_commands": [
                "draw_earth_horizon()",
                "place_sun_below_horizon(angle='0.5_deg')",
                "bend_light_ray_downwards(denser_air_near_ground)",
                "trace_straight_backward_to_apparent_sun()",
                "write_equation('Atmospheric Refraction bends rays around curvature => 2 min early sunrise, 2 min late sunset')"
            ]
        },
        "stem_templates": [
            "Why is the Sun visible to an observer on Earth about 2 minutes before the actual sunrise and 2 minutes after actual sunset?",
            "What causes the apparent daily lengthening of daylight time by approximately 4 minutes?",
            "If Earth had no atmosphere at all, how would the time of sunrise and sunset be affected?"
        ],
        "params": [(1,)],
        "correct_base": "Atmospheric refraction. As light from the Sun (below the geometric horizon) enters Earth's atmosphere, it travels from rarer to progressively denser air layers, bending continuously downwards towards the normal. The eye traces these rays backward along a straight tangent, making the Sun appear raised above the horizon about 2 minutes early.",
        "misc_phrasings": [
            "The Sun is visible early because light travels in straight lines and the Earth rotates faster in the morning.",
            "We see the Sun early because clouds act as mirrors and reflect the Sun over the curvature.",
            "The 2-minute difference is caused by clocks running slower due to gravitational time dilation.",
            "Early sunrise is due to the Sun expanding in volume at dawn."
        ],
        "correct_phrasings": [
            "Atmospheric refraction bends light rays downwards around Earth's curvature, shifting the Sun's apparent position above the horizon by about 0.5 degrees (2 minutes).",
            "Continuous refraction through air layers of increasing optical density curves light towards the ground, making the Sun visible before it crosses the geometric horizon.",
            "Without an atmosphere, there would be no atmospheric refraction; sunrise would occur 2 minutes later and sunset 2 minutes earlier, shortening daylight by 4 minutes."
        ],
        "slip_phrasings": [
            "Correctly stated atmospheric refraction, but computed total daylight extension as 2 minutes instead of 4 minutes (2 + 2).",
            "Attributed the bending to dispersion instead of atmospheric density gradient."
        ],
        "unit_phrasings": [
            "Angular shift of the sun is 0.5 Hours instead of degrees.",
            "Refraction time shift given in Joules."
        ],
        "unsure_phrasings": [
            "Does the atmosphere make the day longer or does the Sun rise earlier naturally?",
            "How can we see something that is below the horizon?"
        ]
    },

    # 31. ELECTRICITY: VOLTAGE-CURRENT CONFLATION
    {
        "family": "ELECTRICITY_VOLTAGE_CURRENT_CONFLATION",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Electric Potential Difference vs Electric Current",
        "target_misc": "MISC-ELEC-004: Voltage-Current Conflation / Voltage as Flowing Entity",
        "misc_desc": "Conflates voltage with current, stating that 'voltage flows through the wire' or that voltage is consumed by resistors.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_diagram",
            "diagram_description": "Circuit with voltmeter across resistor (measuring across two points) and ammeter in series (measuring through one line).",
            "visual_elements": ["Resistor(R)", "Voltmeter(across_terminals)", "Ammeter(in_series)", "ChargeFlow"],
            "whiteboard_commands": [
                "draw_resistor_with_voltmeter_across()",
                "draw_ammeter_in_series()",
                "write_equation('CURRENT (I) flows THROUGH a component')",
                "write_equation('VOLTAGE (V) is the potential difference ACROSS two points')",
                "write_equation('Voltage does NOT flow; it drives the flow of current!')"
            ]
        },
        "stem_templates": [
            "A student says: 'In this circuit, 12 volts of electricity is flowing through the 4-ohm resistor.' What conceptual error has the student made?",
            "Explain the fundamental operational difference between electric current and potential difference in a circuit.",
            "Why is an ammeter connected in series while a voltmeter must be connected in parallel across a circuit component?"
        ],
        "params": [(1,)],
        "correct_base": "Voltage does NOT flow. Voltage (electric potential difference) exists ACROSS two points and represents the work done per unit charge (V = W/Q) driving the circuit. Current (I) is the actual physical flow of electric charge THROUGH a conductor. Current flows through; voltage is applied across.",
        "misc_phrasings": [
            "Voltage flows through the resistor and gets consumed just like water pressure flows through a pipe.",
            "There is no error; voltage and current are two names for the same flowing electricity.",
            "The 12 volts flows through the wire and becomes 0 volts on the other side because voltage gets used up.",
            "Current stays at the battery while voltage travels around the circuit."
        ],
        "correct_phrasings": [
            "Voltage does not flow; it is a potential difference measured ACROSS two points that pushes charge. Electric current is what flows THROUGH the component.",
            "The error is treating voltage as a flowing substance. Current (charge/time) flows through; voltage (energy/charge) exists across terminals.",
            "Current flows through a branch (measured in series); voltage is the potential difference across two points (measured in parallel)."
        ],
        "slip_phrasings": [
            "Correctly distinguished across vs through, but stated 1 Volt = 1 Coulomb / Joule instead of Joule / Coulomb.",
            "Identified current flows, but calculated I = V * R instead of V / R."
        ],
        "unit_phrasings": [
            "Potential difference stated as 12 Amperes instead of Volts.",
            "Current stated in Volts per second."
        ],
        "unsure_phrasings": [
            "Does voltage travel through the wire or does it stay in the battery?",
            "What is the difference between volts and amps in everyday language?"
        ]
    },

    # 32. ELECTRICITY: RESISTIVITY VS RESISTANCE
    {
        "family": "ELECTRICITY_RESISTIVITY_VS_RESISTANCE",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Factors on which the Resistance of a Conductor Depends (Resistivity)",
        "target_misc": "MISC-ELEC-007: Resistivity Dimensional Dependence Fallacy",
        "misc_desc": "Believes resistivity (rho) depends on the dimensions (length or area) of a wire, wrongly concluding that cutting a wire in half halves its resistivity.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_diagram",
            "diagram_description": "Cylindrical copper wire of length L and cross-section A cut in half into length L/2. Resistance is halved (R/2); resistivity rho remains strictly identical.",
            "visual_elements": ["OriginalWire(L, A, rho)", "CutWire(L/2, A, rho)", "ResistanceLabel(R/2)", "ResistivityLabel(rho=const)"],
            "whiteboard_commands": [
                "draw_cylindrical_wire(length='L', area='A')",
                "cut_wire_in_half(new_length='L/2')",
                "write_equation('Resistance: R = rho * L / A  =>  R is HALVED (R/2)')",
                "write_equation('Resistivity (rho): Intrinsic material property  =>  UNCHANGED')",
                "write_equation('Resistivity depends only on material and temperature, NOT geometry!')"
            ]
        },
        "stem_templates": [
            "A cylindrical copper wire of resistance R and resistivity rho is cut into two equal halves. What are the resistance and resistivity of each half?",
            "A wire of length L and uniform cross-section A has resistivity rho. If the wire is stretched to double its length, how does its resistivity change?",
            "How does the resistivity of a metal wire change when its radius is doubled at constant temperature?"
        ],
        "params": [(1,)],
        "correct_base": "Resistance is halved (R' = R/2) because R is directly proportional to length (R = rho * L / A). However, resistivity rho remains STRICTLY UNCHANGED. Resistivity is an intrinsic material property that depends only on the chemical nature of the substance and temperature, not on length, area, or shape.",
        "misc_phrasings": [
            "Both resistance and resistivity are halved (R' = R/2 and rho' = rho/2) because cutting the wire cuts everything in half.",
            "Resistivity doubles when length doubles because rho = R * A / L.",
            "Resistivity decreases because a shorter wire has less material to resist.",
            "Resistivity of copper changes whenever the wire geometry or thickness changes."
        ],
        "correct_phrasings": [
            "Resistance becomes R/2, but resistivity rho remains completely unchanged because resistivity is an intrinsic material property independent of dimensions.",
            "R decreases by half (R' = R/2), while resistivity rho is constant. Resistivity depends only on the material and temperature.",
            "Resistivity does not change at all; only the resistance depends on length and cross-sectional area (R = rho*L/A)."
        ],
        "slip_phrasings": [
            "Stated rho is unchanged, but calculated new resistance of stretched wire as 2R instead of 4R (neglecting volume conservation).",
            "Stated resistivity is constant, but gave unit of resistivity as Ohm / meter instead of Ohm-meter."
        ],
        "unit_phrasings": [
            "Resistivity is measured in Ohms instead of Ohm-meters (Omega*m).",
            "Reported resistance in Ohm-meters."
        ],
        "unsure_phrasings": [
            "Is resistivity the same thing as resistance, or do they change differently?",
            "Does cutting a wire make its resistivity smaller?"
        ]
    },

    # 33. ELECTRICITY: SHORT CIRCUIT BYPASS FALLACY
    {
        "family": "ELECTRICITY_SHORT_CIRCUIT_FALLACY",
        "grade": "Class 10",
        "chapter": "Electricity",
        "topic": "Short Circuit and Parallel Branch Current Distribution",
        "target_misc": "MISC-ELEC-008: Zero-Resistance Short Circuit Current Sharing Fallacy",
        "misc_desc": "Believes current continues to divide equally through a bulb when a zero-resistance wire is connected in parallel across it, failing to recognize complete bypass (short circuit).",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "circuit_diagram",
            "diagram_description": "Bulb connected to battery. An ideal zero-resistance jumper wire connects the two terminals of the bulb. All current bypasses the bulb, so it turns off completely.",
            "visual_elements": ["Battery", "Bulb", "BypassWire(R=0)", "CurrentArrows(bypassing_bulb)"],
            "whiteboard_commands": [
                "draw_circuit_with_bulb()",
                "draw_short_circuit_jumper_across_bulb()",
                "write_equation('R_branch1 = R_bulb, R_branch2 = 0')",
                "write_equation('Current follows path of least resistance: I_bulb = 0, I_wire = I_total')",
                "write_equation('Bulb turns OFF completely (Short-circuited)')"
            ]
        },
        "stem_templates": [
            "A lighted bulb is connected to a battery. A thick copper wire of negligible resistance is now connected directly across the two terminals of the bulb. What happens to the bulb?",
            "In a circuit with a bulb glowing brightly, an ideal conducting wire (R = 0) is connected in parallel with the bulb. Does the bulb remain lit?",
            "Explain what occurs when a zero-resistance shunt wire is connected across an active resistive component in a DC circuit."
        ],
        "params": [(1,)],
        "correct_base": "The bulb turns OFF completely (goes dark). The ideal wire has virtually zero resistance (R = 0). In parallel, current divides inversely proportional to resistance (I_bulb / I_wire = R_wire / R_bulb = 0). Practically 100% of the current flows through the bypass wire, short-circuiting the bulb so zero current flows through its filament.",
        "misc_phrasings": [
            "The bulb stays on at half brightness because parallel branches always split the current equally.",
            "The bulb glows brighter because adding an extra wire provides an easier path for energy to reach it.",
            "The current divides 50/50 between the wire and the bulb, so the bulb stays illuminated.",
            "The bypass wire has no effect because current has already entered the bulb socket."
        ],
        "correct_phrasings": [
            "The bulb turns completely off because the zero-resistance bypass creates a short circuit, causing all current to bypass the filament.",
            "The bulb goes dark. Current takes the path of negligible resistance, so the potential difference across the bulb drops to zero (V = I*R_wire = 0).",
            "Short-circuited: all current flows through the zero-resistance wire, leaving zero current for the bulb filament."
        ],
        "slip_phrasings": [
            "Stated bulb goes dark, but claimed total battery current drops to zero instead of spiking to maximum.",
            "Correctly identified short circuit, but stated bulb burns out due to infinite voltage."
        ],
        "unit_phrasings": [
            "Bypass current reported in Volts instead of Amperes.",
            "Filament resistance reported with power units."
        ],
        "unsure_phrasings": [
            "Doesn't electricity share between all connected paths even if one is a wire?",
            "Why would a wire turn a light bulb off if the battery is still connected?"
        ]
    },

    # 34. MAGNETIC EFFECTS: UNIVERSAL METALLIC MAGNETISM
    {
        "family": "MAGNETIC_EFFECTS_UNIVERSAL_METALLIC_MAGNETISM",
        "grade": "Class 10",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Magnetic vs Non-Magnetic Materials",
        "target_misc": "MISC-MAG-002: Universal Metallic Magnetism Fallacy",
        "misc_desc": "Believes all metals (including copper, aluminum, silver, brass, and gold) are attracted to permanent magnets, confusing electrical conductivity with ferromagnetism.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "field_lines",
            "diagram_description": "Strong bar magnet near copper sheet and iron nail. Iron nail is strongly attracted; copper sheet experiences zero static magnetic attraction.",
            "visual_elements": ["BarMagnet", "IronNail(attracted)", "CopperBlock(no_attraction)", "MagneticDomains"],
            "whiteboard_commands": [
                "draw_bar_magnet()",
                "show_attraction(material='Iron / Nickel / Cobalt')",
                "show_no_attraction(material='Copper / Aluminum / Gold')",
                "write_equation('Electrical Conductors != Ferromagnetic Materials!')",
                "write_equation('Copper and Aluminum are NOT attracted by static permanent magnets')"
            ]
        },
        "stem_templates": [
            "A student brings a strong permanent bar magnet near a clean sheet of pure copper. Will the copper sheet be attracted to the magnet?",
            "Can an electromagnet or permanent bar magnet be used in a scrap yard to separate aluminum cans from iron scrap? Explain why or why not.",
            "Are all metallic conductors attracted by a magnetic field? Justify using examples of common metals."
        ],
        "params": [(1,)],
        "correct_base": "No, copper is NOT attracted to the magnet. Only ferromagnetic materials (such as Iron, Nickel, Cobalt, and certain alloys like Steel) are strongly attracted to permanent magnets. Pure copper is diamagnetic, and aluminum is weakly paramagnetic; neither exhibits perceptible static attraction to a magnet. High electrical conductivity does not imply ferromagnetism.",
        "misc_phrasings": [
            "Yes, copper is strongly attracted because copper is a metal and magnets attract all metals.",
            "Copper is a great conductor of electricity, so it naturally attracts magnetic fields strongly.",
            "The magnet will pick up the aluminum cans because all shiny metals are magnetic.",
            "Any metallic object placed near a magnet gets magnetized and pulled in."
        ],
        "correct_phrasings": [
            "No, pure copper is not attracted to a magnet. Magnets attract ferromagnetic materials (iron, nickel, cobalt), not all metallic conductors.",
            "An electromagnet attracts iron scrap but leaves aluminum cans untouched because aluminum is non-ferromagnetic.",
            "No: metals like copper, aluminum, and gold are non-magnetic under static fields; electrical conductivity is distinct from magnetic susceptibility."
        ],
        "slip_phrasings": [
            "Correctly stated copper is not attracted, but confused eddy currents in moving conductors with static ferromagnetism.",
            "Stated iron is magnetic, but claimed stainless steel is always strongly ferromagnetic."
        ],
        "unit_phrasings": [
            "Magnetic susceptibility labeled with units of Tesla/meter.",
            "Attraction force reported in Coulombs."
        ],
        "unsure_phrasings": [
            "I thought all metals stick to magnets, does copper really not stick?",
            "Why is iron magnetic but aluminum isn't if both are metals?"
        ]
    },

    # 35. MAGNETIC EFFECTS: MAGNETIC FORCE COLLINEAR FALLACY
    {
        "family": "MAGNETIC_EFFECTS_FORCE_COLLINEAR",
        "grade": "Class 10",
        "chapter": "Magnetic Effects of Electric Current",
        "topic": "Force on a Current-Carrying Conductor in a Magnetic Field",
        "target_misc": "MISC-MAG-003: Magnetic Force Collinear / Parallel Fallacy",
        "misc_desc": "Believes the magnetic force on a current-carrying wire acts parallel to the magnetic field lines, failing to understand that magnetic force is strictly perpendicular to both field and current.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "field_lines",
            "diagram_description": "Horizontal wire in horizontal magnetic field. Magnetic force F acts vertically (perpendicular to both I and B via cross product).",
            "visual_elements": ["FieldLines_B(horizontal)", "Current_I(horizontal)", "ForceVector_F(vertical_up)"],
            "whiteboard_commands": [
                "draw_magnetic_field_vector(direction='Right')",
                "draw_current_vector(direction='Into_Page')",
                "draw_force_vector(direction='Upwards')",
                "write_equation('F = I * (L x B) = I * L * B * sin(theta)')",
                "write_equation('Magnetic force is strictly PERPENDICULAR to B, NEVER parallel!')"
            ]
        },
        "stem_templates": [
            "A straight wire carrying current is placed inside a uniform magnetic field. Can the magnetic force on the wire ever be in the same direction as the magnetic field lines?",
            "A magnetic field points horizontally towards the North. An electric current flows horizontally towards the East. In which direction does the magnetic force act?",
            "Why does a current-carrying conductor experience zero magnetic force when aligned parallel to the magnetic field?"
        ],
        "params": [(1,)],
        "correct_base": "No, the magnetic force is NEVER parallel to the magnetic field lines. By the Lorentz force rule F = I * (L x B) = I * L * B * sin(theta), the magnetic force is mutually perpendicular to both the conductor (current) and the magnetic field. When current is parallel to field (theta = 0), sin(0) = 0, so force is zero.",
        "misc_phrasings": [
            "The magnetic force pushes the wire directly along the magnetic field lines towards the North.",
            "Magnetic force always pulls objects in the same direction that the magnetic field is pointing.",
            "The wire accelerates parallel to the field lines just like a charge moves along electric field lines.",
            "Maximum magnetic force occurs when the wire is parallel to the magnetic field lines."
        ],
        "correct_phrasings": [
            "The magnetic force is strictly perpendicular to both current and magnetic field; it can never act parallel to the field lines.",
            "Force is directed vertically upwards (perpendicular to both North and East) by Fleming's Left-Hand Rule; it is never in the direction of B.",
            "When wire is parallel to field, theta = 0, giving F = ILB sin(0) = 0 N. Magnetic force is perpendicular to B, never parallel."
        ],
        "slip_phrasings": [
            "Identified perpendicular direction, but wrote force formula as F = I * L / B.",
            "Stated force is vertical, but forgot to reverse direction for negative current carriers."
        ],
        "unit_phrasings": [
            "Magnetic force magnitude reported in Tesla instead of Newtons.",
            "Magnetic field B reported in Joules."
        ],
        "unsure_phrasings": [
            "Doesn't a force always push in the direction the field is pointing?",
            "Why is magnetic force sideways instead of in the direction of the field?"
        ]
    },

    # 36. MOTION: DISTANCE VS DISPLACEMENT
    {
        "family": "MOTION_DISTANCE_VS_DISPLACEMENT",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Describing Motion: Distance and Displacement",
        "target_misc": "MISC-MOT-003: Distance Equals Displacement Fallacy",
        "misc_desc": "Believes distance and displacement are always identical scalar quantities, failing to understand that displacement is a vector from initial to final position and can be zero after a round trip.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_graph",
            "diagram_description": "Athlete running one complete circular lap of radius r = 7 m. Total distance is 2*pi*r = 44 m; net displacement is strictly 0 m.",
            "visual_elements": ["CircularTrack(r=7m)", "StartingPoint(A)", "LapPath", "ZeroDisplacementVector"],
            "whiteboard_commands": [
                "draw_circular_track(radius=7)",
                "mark_start_and_end_point(A=(0, 7))",
                "write_equation('Distance = Total path length = 2 * pi * r = 2 * (22/7) * 7 = 44 m')",
                "write_equation('Displacement = Shortest straight-line distance from start to end = 0 m')",
                "write_equation('Displacement can be zero even when distance is non-zero!')"
            ]
        },
        "stem_templates": [
            "An athlete completes one round of a circular track of radius 7 m in 40 seconds. What are the total distance covered and the net displacement at the end of the round?",
            "A farmer moves along the boundary of a square field of side 10 m and returns to his starting corner. What is the magnitude of his displacement?",
            "A person walks 4 km East, then turns and walks 4 km West back to the starting point. Compare the total distance traveled with the final displacement."
        ],
        "params": [(1,)],
        "correct_base": "Distance = 44 m (circumference = 2 * pi * r = 2 * (22/7) * 7 = 44 m). Displacement = 0 m. Distance is the total scalar path length traveled. Displacement is the vector shortest straight-line distance from initial position to final position; because the runner finishes at the starting point, displacement is exactly zero.",
        "misc_phrasings": [
            "Both distance and displacement are 44 m because distance and displacement are the same thing.",
            "Displacement cannot be zero because the athlete ran hard for 44 meters.",
            "The displacement is 44 m because displacement is how far you ran.",
            "Displacement equals distance traveled, so both are 8 km for the round trip."
        ],
        "correct_phrasings": [
            "Distance is 44 m, but displacement is 0 m because the initial and final positions coincide.",
            "Displacement is 0 m (net change in position is zero), while total distance covered is 44 m (circumference).",
            "Distance is scalar path length (44 m); displacement is vector change in position (0 m for a complete closed loop)."
        ],
        "slip_phrasings": [
            "Correctly identified displacement as 0 m, but calculated circumference as 2 * pi * r^2 = 308 m.",
            "Stated displacement is 0 m, but labeled it with units of seconds."
        ],
        "unit_phrasings": [
            "Displacement reported in m/s instead of meters.",
            "Distance reported as 44 kg."
        ],
        "unsure_phrasings": [
            "How can displacement be zero if someone actually ran a distance?",
            "Is displacement distance in a straight line or total distance?"
        ]
    },

    # 37. MOTION: NEGATIVE ACCELERATION VS DECELERATION
    {
        "family": "MOTION_NEGATIVE_ACCELERATION_DECELERATION",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Acceleration: Sign of Acceleration and Direction of Motion",
        "target_misc": "MISC-MOT-004: Negative Acceleration Equals Deceleration Fallacy",
        "misc_desc": "Equates negative acceleration strictly with slowing down (deceleration), failing to realize that an object moving in the negative direction with negative acceleration is speeding up.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_graph",
            "diagram_description": "Car moving in negative x direction with velocity v = -10 m/s and acceleration a = -5 m/s^2. Velocity magnitude increases to -20 m/s (speeding up in negative direction).",
            "visual_elements": ["Axis_X", "Vehicle(moving_left)", "VelocityVector(left, v=-10)", "AccelVector(left, a=-5)"],
            "whiteboard_commands": [
                "draw_number_line(positive='Right', negative='Left')",
                "draw_car_moving_left(v=-10, a=-5)",
                "write_equation('v and a have SAME sign (both negative)  =>  Object is SPEEDING UP!')",
                "write_equation('Deceleration occurs when v and a have OPPOSITE signs, not just when a < 0')"
            ]
        },
        "stem_templates": [
            "A car travels towards the West (chosen as negative direction) with velocity -15 m/s and has an acceleration of -3 m/s^2. Is the car speeding up or slowing down?",
            "Does a negative acceleration always mean an object is slowing down? Explain using an example of motion along a chosen coordinate axis.",
            "An elevator moving downwards (negative direction) accelerates downwards at -2 m/s^2. Describe what happens to its speed."
        ],
        "params": [(1,)],
        "correct_base": "The car is SPEEDING UP. Whether an object speeds up or slows down depends on the relative signs of velocity and acceleration, not the sign of acceleration alone. When velocity and acceleration have the SAME sign (both negative), the object speeds up in the negative direction. Deceleration (slowing down) occurs ONLY when velocity and acceleration have OPPOSITE signs.",
        "misc_phrasings": [
            "The car is slowing down because acceleration is negative (-3 m/s^2), and negative acceleration always means braking.",
            "Negative acceleration is deceleration by definition, so the car must be coming to a stop.",
            "Any negative sign on acceleration means the speed is decreasing.",
            "The elevator slows down because acceleration has a minus sign."
        ],
        "correct_phrasings": [
            "The car is speeding up. Because velocity and acceleration share the same negative direction (both negative), its speed increases from 15 m/s to 18 m/s.",
            "No: negative acceleration does not always mean slowing down. If an object moves in the negative direction, negative acceleration increases its speed.",
            "Speeding up in the downward direction: when velocity and acceleration are parallel (same sign), speed increases."
        ],
        "slip_phrasings": [
            "Correctly stated speeding up, but calculated final speed as -15 + (-3) * 2 = -24 m/s instead of -21 m/s.",
            "Identified speeding up, but wrote acceleration units as m/s instead of m/s^2."
        ],
        "unit_phrasings": [
            "Acceleration reported in m/s.",
            "Speed reported in Newtons."
        ],
        "unsure_phrasings": [
            "I thought deceleration and negative acceleration were the exact same thing.",
            "Can something speed up with a negative acceleration?"
        ]
    },

    # 38. MOTION: AVERAGE SPEED ARITHMETIC MEAN FALLACY
    {
        "family": "MOTION_AVERAGE_SPEED_ARITHMETIC_MEAN",
        "grade": "Class 9",
        "chapter": "Motion",
        "topic": "Average Speed for Equal Distance Intervals",
        "target_misc": "MISC-MOT-005: Average Speed Arithmetic Mean Fallacy",
        "misc_desc": "Calculates average speed for equal distances as the simple arithmetic average (v1 + v2) / 2 instead of total distance divided by total time (harmonic mean 2*v1*v2 / (v1 + v2)).",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_graph",
            "diagram_description": "Car travels distance d at 60 km/h, returns distance d at 40 km/h. Average speed is 2*60*40/(60+40) = 48 km/h, not 50 km/h.",
            "visual_elements": ["TripOut(d, v=60km/h, t1=d/60)", "TripReturn(d, v=40km/h, t2=d/40)", "TotalDistance(2d)"],
            "whiteboard_commands": [
                "draw_two_way_trip(out_speed=60, return_speed=40)",
                "calculate_time(t1='d/60', t2='d/40', t_total='5d/120')",
                "write_equation('v_avg = Total Distance / Total Time = 2d / (d/60 + d/40)')",
                "write_equation('v_avg = (2 * 60 * 40) / (60 + 40) = 48 km/h  (NOT 50 km/h!)')"
            ]
        },
        "stem_templates": [
            "A car travels from town A to town B at an average speed of 60 km/h and returns from B to A along the same route at 40 km/h. What is the average speed for the entire round trip?",
            "A student walks to school at 4 km/h and runs back home along the same path at 6 km/h. Find the average speed for the whole journey.",
            "An automobile covers the first half of a total distance at 30 km/h and the second half of the distance at 60 km/h. Calculate its average speed."
        ],
        "params": [(1,)],
        "correct_base": "Average speed = Total Distance / Total Time = 2d / (d/60 + d/40) = 2*60*40 / (60+40) = 4800 / 100 = 48 km/h. Average speed is NOT the arithmetic average (60+40)/2 = 50 km/h, because more time is spent traveling at the slower speed.",
        "misc_phrasings": [
            "Average speed is (60 + 40) / 2 = 50 km/h because you simply take the average of the two numbers.",
            "Average speed = (4 + 6) / 2 = 5 km/h, just add them and divide by 2.",
            "It is 50 km/h because 50 is halfway between 40 and 60.",
            "v_avg = (30 + 60) / 2 = 45 km/h (arithmetic mean of the two speeds)."
        ],
        "correct_phrasings": [
            "Average speed = Total Distance / Total Time = 2*v1*v2 / (v1 + v2) = (2 * 60 * 40) / 100 = 48 km/h (harmonic mean).",
            "48 km/h. Since equal distances are traveled, more time is spent at 40 km/h than at 60 km/h, weighting the true average speed closer to 40 km/h.",
            "Average speed is 48 km/h: v_avg = total distance / total time = 2d / (d/60 + d/40) = 48 km/h, strictly less than the arithmetic mean."
        ],
        "slip_phrasings": [
            "Set up harmonic mean formula correctly, but computed 4800 / 100 as 4.8 km/h due to decimal slip.",
            "Calculated total time correctly, but forgot to double distance for the round trip."
        ],
        "unit_phrasings": [
            "Average speed is 48 km instead of km/h.",
            "Reported speed in m/s^2."
        ],
        "unsure_phrasings": [
            "Can't we just average the two speeds like normal numbers?",
            "Why isn't average speed just the middle of 40 and 60?"
        ]
    },

    # 39. FORCE: MASS VS WEIGHT
    {
        "family": "FORCE_MASS_VS_WEIGHT",
        "grade": "Class 9",
        "chapter": "Gravitation",
        "topic": "Mass and Weight",
        "target_misc": "MISC-FOR-003: Mass-Weight Equivalence Fallacy",
        "misc_desc": "Conflates mass and weight, believing that an object's mass changes when taken to the Moon, or treating weight as a scalar intrinsic property measured in kilograms.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Astronaut on Earth (m=60 kg, W=588 N) and on Moon (m=60 kg, W=98 N). Mass is invariant; weight is location-dependent force.",
            "visual_elements": ["EarthSurface(g=9.8)", "MoonSurface(g=1.63)", "Astronaut(mass=60kg)", "WeightVector_Earth(588N)", "WeightVector_Moon(98N)"],
            "whiteboard_commands": [
                "draw_astronaut_on_earth()",
                "draw_astronaut_on_moon()",
                "write_equation('Mass (m) = 60 kg on Earth AND 60 kg on Moon (Invariant matter quantity)')",
                "write_equation('Weight (W = m*g): Earth W = 60*9.8 = 588 N, Moon W = 60*1.63 = 98 N')",
                "write_equation('Mass is in kg; Weight is a force in Newtons!')"
            ]
        },
        "stem_templates": [
            "An astronaut has a mass of 60 kg on Earth. What will be the astronaut's mass and weight on the surface of the Moon, where acceleration due to gravity is 1/6th of Earth's (g_moon = 1.63 m/s^2)?",
            "A rock weighs 30 N on Earth. What is its mass on Earth and what will be its mass on the Moon?",
            "Explain the difference between mass and weight, and describe which quantity changes when an object is taken to outer space."
        ],
        "params": [(1,)],
        "correct_base": "Mass on Moon = 60 kg (UNCHANGED). Weight on Moon = m * g_moon = 60 * 1.63 = 98 N (or 588 / 6 = 98 N). Mass is the measure of inertia and quantity of matter; it is strictly invariant everywhere in the universe. Weight is the gravitational force exerted on the object (W = mg), which varies with local gravity.",
        "misc_phrasings": [
            "The astronaut's mass on the Moon is 10 kg because mass becomes 1/6th on the Moon (60 / 6 = 10 kg).",
            "Mass drops to 10 kg because there is less gravity to hold the mass together.",
            "Weight and mass are the same thing; both become 10 kg on the Moon.",
            "The rock's mass changes to zero in outer space because weight is zero."
        ],
        "correct_phrasings": [
            "Mass remains exactly 60 kg (mass is invariant). Weight becomes W = 60 * 1.63 = 98 N (one-sixth of Earth weight 588 N).",
            "Mass is invariant (60 kg everywhere). Weight is a force (W = mg) that changes to 98 N on the Moon.",
            "Mass measures matter content and remains 60 kg; weight is the gravitational force and decreases to 98 N."
        ],
        "slip_phrasings": [
            "Correctly stated mass is 60 kg, but multiplied by 6 instead of dividing: weight = 3528 N.",
            "Stated 60 kg mass, but gave Moon weight as 98 kg instead of 98 N."
        ],
        "unit_phrasings": [
            "Weight on Moon is 98 kg instead of Newtons.",
            "Mass reported in Newtons."
        ],
        "unsure_phrasings": [
            "Doesn't someone weigh less on the Moon because their mass gets lighter?",
            "Why do bathroom scales measure weight in kilograms if weight is a force?"
        ]
    },

    # 40. GRAVITATION: INVERSE SQUARE LAW SCALING
    {
        "family": "GRAVITATION_INVERSE_SQUARE_FALLACY",
        "grade": "Class 9",
        "chapter": "Gravitation",
        "topic": "Universal Law of Gravitation (Inverse Square Dependence)",
        "target_misc": "MISC-GRAV-002: Inverse Square Distance Linearity Fallacy",
        "misc_desc": "Treats gravitational force as inversely proportional to distance (1/r) rather than distance squared (1/r^2), wrongly concluding that doubling distance cuts force in half.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Two masses separated by distance r (force F). When separation is increased to 2r, force drops to F/4.",
            "visual_elements": ["Mass1(M)", "Mass2(m)", "Separation(r, Force=F)", "Separation(2r, Force=F/4)"],
            "whiteboard_commands": [
                "draw_mass_pair(distance='r', force='F')",
                "draw_mass_pair(distance='2r', force='F/4')",
                "write_equation('Universal Law of Gravitation: F = G * M * m / r^2')",
                "write_equation('When r -> 2r: F_new = G * M * m / (2r)^2 = F / 4')",
                "write_equation('Doubling distance cuts force to ONE-FOURTH, not half!')"
            ]
        },
        "stem_templates": [
            "The gravitational force between two identical spheres separated by distance r is 100 N. If the distance between their centers is doubled to 2r, what is the new gravitational force?",
            "How does the gravitational force between two planets change if the distance between them is tripled?",
            "According to Newton's Universal Law of Gravitation, if distance between two objects is halved (r/2), how does the gravitational attraction change?"
        ],
        "params": [(1,)],
        "correct_base": "The new force is 25 N (one-fourth of the original force: F' = F / 4 = 100 / 4 = 25 N). Gravitation obeys the inverse-square law: F = G * M * m / r^2. Replacing r with 2r gives (2r)^2 = 4r^2 in the denominator, reducing the force by a factor of 4, NOT 2.",
        "misc_phrasings": [
            "The new force is 50 N because doubling the distance cuts the gravitational pull in half (100 / 2 = 50 N).",
            "Force is inversely proportional to distance, so 2 times the distance means half the force.",
            "Tripling the distance cuts the force to 1/3rd because distance is tripled.",
            "Halving distance doubles the force to 200 N instead of multiplying by 4."
        ],
        "correct_phrasings": [
            "New force is 25 N: F is inversely proportional to r^2, so doubling separation divides force by 2^2 = 4 (100 / 4 = 25 N).",
            "Force becomes one-fourth (25 N) by the inverse-square law: F proportional to 1/r^2.",
            "F' = F / (2^2) = 100 / 4 = 25 N. Inverse square law dictates that doubling distance reduces force to 25%."
        ],
        "slip_phrasings": [
            "Correctly identified 1/r^2 dependence, but calculated 2^2 as 8: got 12.5 N.",
            "Computed 100 / 4 = 20 N due to mental division slip."
        ],
        "unit_phrasings": [
            "New force is 25 Joules instead of Newtons.",
            "Gravitational constant G reported with units of kg/m."
        ],
        "unsure_phrasings": [
            "Does distance square or just distance matter for gravity?",
            "I'm not sure if doubling distance makes gravity half or a quarter."
        ]
    },

    # 41. WORK & ENERGY: KINETIC ENERGY VELOCITY SQUARING
    {
        "family": "ENERGY_KINETIC_VELOCITY_LINEARITY",
        "grade": "Class 9",
        "chapter": "Work and Energy",
        "topic": "Kinetic Energy and Velocity Dependence",
        "target_misc": "MISC-ENG-001: Kinetic Energy Velocity Linearity Fallacy",
        "misc_desc": "Believes kinetic energy is directly proportional to velocity (linear) rather than velocity squared (quadratic), wrongly concluding that doubling speed doubles kinetic energy.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "motion_graph",
            "diagram_description": "Car moving at speed v (kinetic energy E_k). When speed doubles to 2v, kinetic energy increases fourfold (4*E_k), requiring 4x the braking distance.",
            "visual_elements": ["CarAtSpeed_v(Ek=1000J)", "CarAtSpeed_2v(Ek=4000J)", "BrakingDistanceGraph"],
            "whiteboard_commands": [
                "draw_vehicle_at_speed(v='v', Ek='Ek')",
                "draw_vehicle_at_speed(v='2v', Ek='4*Ek')",
                "write_equation('Kinetic Energy: E_k = (1/2) * m * v^2')",
                "write_equation('When v -> 2v: E_k_new = (1/2) * m * (2v)^2 = 4 * E_k')",
                "write_equation('Doubling velocity QUADRUPLES the kinetic energy!')"
            ]
        },
        "stem_templates": [
            "A moving automobile of mass 1000 kg has a kinetic energy of 50,000 J at 10 m/s. If its speed is doubled to 20 m/s, what is its new kinetic energy?",
            "How does the kinetic energy of a moving runner change if their speed increases by a factor of 3?",
            "Why does a car traveling at 60 km/h require four times the braking distance of the same car traveling at 30 km/h?"
        ],
        "params": [(1,)],
        "correct_base": "The new kinetic energy is 200,000 J (quadrupled: 4 * 50,000 J = 200,000 J). Kinetic energy is proportional to the SQUARE of velocity: E_k = (1/2) * m * v^2. Doubling speed multiplies kinetic energy by 2^2 = 4, which is why braking distance also quadruples.",
        "misc_phrasings": [
            "New kinetic energy is 100,000 J because doubling speed doubles kinetic energy (2 * 50,000 = 100,000 J).",
            "Kinetic energy is directly proportional to speed, so 2 times speed means 2 times the energy.",
            "Tripling speed gives 3 times the kinetic energy (linear scaling).",
            "Braking distance doubles when speed doubles because energy doubles."
        ],
        "correct_phrasings": [
            "New kinetic energy is 200,000 J: E_k is proportional to v^2, so doubling velocity increases energy by 2^2 = 4 times (4 * 50,000 J).",
            "E_k quadruples (4x) to 200,000 J because kinetic energy scales with the square of speed: E_k = 0.5 * m * v^2.",
            "200 kJ. By E_k = 0.5*m*v^2, doubling v gives (2)^2 = 4 times greater kinetic energy."
        ],
        "slip_phrasings": [
            "Correctly identified 4x factor, but calculated 4 * 50,000 as 20,000 J due to missing zero.",
            "Wrote E_k formula as m * v^2 without the 1/2 factor."
        ],
        "unit_phrasings": [
            "Kinetic energy is 200,000 Watts instead of Joules.",
            "Reported kinetic energy in Newtons."
        ],
        "unsure_phrasings": [
            "Is energy multiplied by speed or speed squared? I get mixed up with momentum.",
            "Why does speed have an exponent of 2 in kinetic energy?"
        ]
    },

    # 42. WORK & ENERGY: ZERO WORK IN CIRCULAR ORBITS
    {
        "family": "WORK_ENERGY_ZERO_WORK_CIRCULAR_ORBIT",
        "grade": "Class 9",
        "chapter": "Work and Energy",
        "topic": "Work Done by Centripetal / Gravitational Force in Circular Motion",
        "target_misc": "MISC-WRK-002: Circular Orbit Gravitational Work Fallacy",
        "misc_desc": "Believes gravitational force does continuous positive work on a planet or satellite in a circular orbit to keep it moving around the Sun/Earth.",
        "diagram_meta": {
            "has_diagram": True,
            "diagram_type": "force_diagram",
            "diagram_description": "Satellite orbiting Earth in circular orbit. Gravitational force points towards center; instantaneous displacement is tangential (theta = 90 deg). Net work is 0 J.",
            "visual_elements": ["Earth(center)", "Satellite(orbiting)", "CentripetalForceVector(radial_inward)", "DisplacementVector(tangential)", "RightAngle(90deg)"],
            "whiteboard_commands": [
                "draw_circular_orbit()",
                "draw_gravitational_force_vector(direction='Center')",
                "draw_displacement_vector(direction='Tangent')",
                "show_angle(theta=90)",
                "write_equation('W = F * d * cos(90 deg) = F * d * 0 = 0 J')",
                "write_equation('Gravitational force does ZERO work on circular satellite!')"
            ]
        },
        "stem_templates": [
            "A satellite orbits the Earth in a circular path at a constant speed of 7 km/s. What is the total work done by Earth's gravitational force on the satellite in one complete revolution?",
            "Does the gravitational force of the Sun do work on the Earth as it moves in its approximately circular orbit?",
            "Explain why the kinetic energy and speed of an artificial satellite in a circular orbit remain constant over time."
        ],
        "params": [(1,)],
        "correct_base": "Work done is strictly 0 J. Gravitational force acts radially inward towards Earth's center, while the instantaneous displacement of the satellite is tangential along the circle. The angle between force and displacement is always 90 degrees. Since W = F * d * cos(90 deg) = 0, gravity does zero work on the satellite, keeping its kinetic energy constant.",
        "misc_phrasings": [
            "Gravity does huge work to keep the satellite moving around the circle for millions of meters.",
            "Work done = F_gravity * 2*pi*r, force times the circumference traveled.",
            "Gravity does positive work because without gravity the satellite would fly away.",
            "Work is done continuously to sustain the 7 km/s orbital velocity."
        ],
        "correct_phrasings": [
            "Zero work (0 J): gravitational force is always perpendicular to tangential displacement (theta = 90 deg), so W = Fd cos(90 deg) = 0.",
            "0 Joules. The centripetal gravitational pull is orthogonal to the direction of motion at every instant, doing zero work.",
            "No work is done by gravity (W = 0). Since work is zero, the work-energy theorem dictates that kinetic energy and speed remain constant."
        ],
        "slip_phrasings": [
            "Stated 0 J work, but computed centripetal acceleration as v^2 * r instead of v^2 / r.",
            "Identified 0 work, but claimed satellite has zero kinetic energy."
        ],
        "unit_phrasings": [
            "Work done is 0 Newtons instead of Joules.",
            "Orbital velocity given in m/s^2."
        ],
        "unsure_phrasings": [
            "If gravity is pulling it the whole time, why is work done equal to zero?",
            "Doesn't moving a satellite require work against space resistance?"
        ]
    }

]
