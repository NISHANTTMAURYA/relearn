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
    }
]
