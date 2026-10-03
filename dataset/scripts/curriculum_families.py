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
    }
]


