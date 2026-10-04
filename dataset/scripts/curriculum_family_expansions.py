"""
Authoritative Curriculum Expansions for Re:Learn
Provides comprehensive reasoning traces, diverse student phrasings,
vernacular colloquialisms, and edge cases across all 42 NCERT Curriculum Families.
"""

EXPANDED_CURRICULUM_PHRASINGS = {
    # 0. OPTICS: HALF-LENS BLOCKING
    "OPTICS_HALF_LENS_BLOCKING": {
        "misc_expansions": [
            "If the lower half of the lens is covered, then light from the top half of the candle cannot reach the screen, so only the bottom half of the image is visible.",
            "Only half image is projected because the black sheet blocks 50% of the object's rays from reaching the viewing screen.",
            "Covering bottom half will cut off the bottom part of image, leaving only the upper inverted half.",
            "Since light travels in straight lines, blocking the lower half of the lens physically cuts the image in half.",
            "The screen will only display the bottom portion of the candle flame because half of the lens aperture is blocked by paper."
        ],
        "correct_expansions": [
            "The image will remain completely intact and full, but its brightness will be cut in half because all parts of the object send rays through the remaining uncovered portion of the lens.",
            "A full, complete image continues to form on the screen; only the overall illumination decreases since fewer total rays are collected.",
            "Covering half the lens does not truncate the image at all. Every point on the lens forms a complete image; reducing lens area simply decreases the light intensity.",
            "The entire image of the candle remains on the screen, just with 50% less brightness due to the halved aperture area."
        ],
        "slip_expansions": [
            "The image remains complete, but the focal length changes from {f} cm to {slip} cm due to the mask.",
            "Full image is formed, but calculated image distance as {slip} cm instead of 2f due to addition error."
        ],
        "unit_expansions": [
            "The full image is formed with a brightness drop of 50 Amperes instead of percentage.",
            "Image is complete with illumination measured in Newtons instead of Lumens."
        ],
        "unsure_expansions": [
            "sir I know either brightness decreases or the image gets cut in half, but forgot which one NCERT says",
            "not sure if covering half the glass blocks half the image or just dims it"
        ],
        "stem_expansions": [
            "In a school laboratory experiment, a student places a black cardboard covering the bottom half of a convex lens (f = {f} cm). What will be observed on the white screen?",
            "A converging lens of focal length {f} cm projects a real inverted image. If the bottom 50% of the lens is painted with opaque black ink, what happens to the image?"
        ],
        "param_expansions": [(16,), (22,), (14,)]
    },

    # 1. OPTICS: SCREEN REIFICATION
    "OPTICS_SCREEN_REIFICATION": {
        "misc_expansions": [
            "The image vanishes completely into thin air because without a physical screen there is nowhere for the picture to be displayed.",
            "Real images only exist on physical surfaces like walls or screens, so pulling the screen away immediately destroys the image.",
            "If there is no screen, the rays just fly off into space without forming any image at that spot.",
            "An image cannot hang in empty space; it requires a screen to reflect the picture into our eyes, so no image exists once the screen is removed.",
            "Removing the screen removes the image because a real image is literally drawn on the screen surface."
        ],
        "correct_expansions": [
            "The real image still exists in empty space at that exact position (aerial image) because light rays still converge and intersect there independently of any screen.",
            "The image remains present in space at the focal plane; a screen is only a diffuse scatterer that allows viewing from wide angles, not a prerequisite for image formation.",
            "The intersection of refracted rays in three-dimensional space forms a real aerial image regardless of whether an opaque screen is present to capture it.",
            "Light rays physically converge at that spatial coordinate to form a real image in air; the screen merely scatters those rays into our eyes."
        ],
        "slip_expansions": [
            "The aerial image remains in space, but calculated position as {slip} cm due to arithmetic slip.",
            "Aerial image exists, but calculated magnification as -0.5 instead of -1.0."
        ],
        "unit_expansions": [
            "Aerial image exists at distance 40 Watts instead of cm.",
            "Image position is 30 Volts from the optical center."
        ],
        "unsure_expansions": [
            "sir can an image exist in empty air without a screen or does it vanish?",
            "idk if real images need a screen to exist in reality"
        ],
        "stem_expansions": [
            "A convex lens (f = {f} cm) produces a sharp image on a screen. If the screen is suddenly removed while looking towards the lens along the axis, does the image still exist in space?",
            "In NCERT Chapter 10, when a real inverted image is formed by a convex lens, does the convergence of light depend on the physical presence of a cardboard screen?"
        ],
        "param_expansions": [(18,), (24,), (16,)]
    },

    # 2. OPTICS: VIRTUAL RAY CONVERGENCE
    "OPTICS_VIRTUAL_RAY_CONVERGENCE": {
        "misc_expansions": [
            "Virtual images are formed because light rays actually penetrate inside the mirror and physically intersect behind the glass.",
            "The rays pass through the silvering of the plane mirror and meet at the point where we see the virtual image.",
            "Light rays travel behind the mirror surface and physically converge there to make the virtual image visible.",
            "Virtual image means real light rays go behind the mirror and focus at that point in space behind the wall.",
            "The rays actually cross behind the mirror, which is why our eyes can perceive the image behind the glass."
        ],
        "correct_expansions": [
            "No light rays actually pass behind or intersect behind the mirror; reflected rays diverge in front and only appear to diverge from a virtual point behind the mirror when projected backward.",
            "Virtual images are formed by the apparent divergence of reflected light rays; rays do not physically penetrate or meet behind the reflective surface.",
            "Virtual images cannot be captured on a screen because they are formed by imaginary backward extensions of real diverging rays, not actual physical intersection of light.",
            "The reflected rays enter the observer's eye diverging; the brain projects these rays straight backward, creating an optical perception of an image where no light actually exists."
        ],
        "slip_expansions": [
            "Virtual rays only appear to intersect, but calculated image distance as -{slip} cm instead of -{u} cm.",
            "Divergent rays projected backward, but miscalculated magnification as +2.0 instead of +1.0."
        ],
        "unit_expansions": [
            "Virtual image formed at virtual distance {u} Joules behind mirror.",
            "Apparent image location is {u} Amperes behind the reflective surface."
        ],
        "unsure_expansions": [
            "confused whether virtual rays actually go behind the mirror or are just imaginary lines",
            "sir do real photons travel behind the plane mirror or not?"
        ],
        "stem_expansions": [
            "When you view your reflection in a plane mirror at distance {u} cm, do physical light rays actually exist behind the glass surface where the image appears?",
            "Explain the physical nature of light rays forming a virtual image in a concave mirror when the object is placed between the pole and principal focus (u < f)."
        ],
        "param_expansions": [(8,), (14,), (6,)]
    },

    # 3. OPTICS: CARTESIAN SIGN CONVENTION
    "OPTICS_CARTESIAN_SIGN_CONVENTION": {
        "misc_expansions": [
            "Distances in real life cannot be negative numbers, so object distance u must always be taken as positive {u} cm in the mirror formula.",
            "Since the object is in front of the mirror where real things are, u is positive and focal length of concave mirror is also positive {f} cm.",
            "I used positive signs for both u and f because negative distance makes no physical sense.",
            "In mirror formula 1/f = 1/v + 1/u, we just substitute positive numbers u={u} and f={f} without any negative signs.",
            "Object distance is positive because the object is physically present on the left."
        ],
        "correct_expansions": [
            "According to the New Cartesian Sign Convention, distances measured against the direction of incident light (to the left of pole) are negative: u = -{u} cm and concave mirror focal length is f = -{f} cm.",
            "The pole is taken as the origin; since the incident rays travel left to right, all positions to the left (including object u and concave focus f) must have negative signs: u = -{u}, f = -{f}.",
            "By NCERT sign convention, object distance is always negative (u = -{u} cm), and a concave mirror has a negative focal length (f = -{f} cm), yielding a real image distance v with a negative sign.",
            "Using Cartesian coordinate rules: incident direction is +x. The object lies in the -x direction (u = -{u} cm) and concave focal point lies in -x direction (f = -{f} cm)."
        ],
        "slip_expansions": [
            "Correct signs u=-{u}, f=-{f}, but 1/v = -1/{f} - (-1/{u}) calculated as -1/{slip} due to common denominator error.",
            "Applied negative signs properly, but wrote v = -{slip} cm due to arithmetic slip."
        ],
        "unit_expansions": [
            "Image distance v = -{cor_val} Newtons instead of centimeters.",
            "Focal length written as -{f} Volts in Cartesian convention."
        ],
        "unsure_expansions": [
            "sir I always get confused whether u is negative or positive for concave mirrors",
            "not sure about the sign convention rules for mirrors"
        ],
        "stem_expansions": [
            "An object is placed at distance {u} cm in front of a concave mirror of focal length {f} cm. State the correct New Cartesian signs for u and f and calculate image position v.",
            "According to the New Cartesian Sign Convention in NCERT Class 10, what are the sign assignments for an object placed at {u} cm from a concave mirror (f = {f} cm)?"
        ],
        "param_expansions": [(45, 15), (35, 10), (25, 10)]
    },

    # 4. OPTICS: GLASS SLAB REFRACTION
    "OPTICS_GLASS_SLAB_REFRACTION": {
        "misc_expansions": [
            "The light ray emerging from a rectangular glass slab exits permanently bent at an angle, exactly like what happens in a triangular glass prism.",
            "Refraction at both parallel faces causes a cumulative angular deviation, so the emergent ray permanently deviates from the incident direction.",
            "Because light bends towards normal at entry and away at exit, the final emergent ray permanently diverges at a noticeable angle.",
            "The ray does not come out parallel; it exits at an angle because glass bends light permanently.",
            "Angle of emergence e is different from incidence angle i, producing a permanent angular deflection."
        ],
        "correct_expansions": [
            "The emergent ray is strictly parallel to the incident ray (angle of emergence e equals angle of incidence i); the beam undergoes only a lateral displacement (sideways parallel shift) because opposite faces are parallel.",
            "Because the opposing refracting surfaces of a rectangular slab are parallel, the bending away from normal at the second surface exactly cancels the bending towards normal at the first surface, resulting in zero angular deviation.",
            "In a rectangular glass slab, e = i, meaning the emergent ray emerges in the identical direction as the incident ray, shifted only sideways by a lateral displacement d.",
            "Unlike a triangular prism with non-parallel faces, a rectangular block has parallel faces, so the net angular deviation is exactly zero degrees; only lateral shift occurs."
        ],
        "slip_expansions": [
            "Emergent ray is parallel (e = i), but calculated lateral displacement as {slip} cm instead of {u} cm due to trig slip.",
            "Zero angular deviation, but stated lateral shift is {slip} mm due to multiplication slip."
        ],
        "unit_expansions": [
            "Lateral displacement is {u} Amperes instead of millimeters.",
            "Angle of emergence is 45 Watts instead of degrees."
        ],
        "unsure_expansions": [
            "does a rectangular glass slab bend the ray permanently at an angle or does it come out parallel?",
            "confused between lateral shift in a glass slab and angular deviation in a prism"
        ],
        "stem_expansions": [
            "A ray of light is incident at an angle of 45 degrees on the top face of a rectangular glass slab. Compare the direction of the emergent ray with the incident ray.",
            "In NCERT Science Class 10 Activity 10.10, light passes through a parallel-sided rectangular glass slab. Is there any permanent angular deviation in the emergent beam?"
        ],
        "param_expansions": [(14,), (18,), (22,)]
    },

    # 5. HUMAN EYE: VISION DEFECTS
    "HUMAN_EYE_VISION_DEFECTS": {
        "misc_expansions": [
            "A myopic person cannot see distant objects, so they need convex magnifying lenses in their glasses to make faraway objects look bigger.",
            "Myopia is corrected using convex lenses because convex lenses help converge light and zoom in on distant objects.",
            "To correct shortsightedness, a converging convex lens must be placed in front of the eye so distant rays can reach the retina.",
            "Since hypermetropia is farsightedness, we use concave glasses, and for myopia we use convex glasses.",
            "Myopic eyes have weak focusing power, so an additional convex lens is required to boost the refractive power."
        ],
        "correct_expansions": [
            "Myopia (nearsightedness) occurs when the eye lens has excessive converging power or the eyeball is elongated, causing rays from distant objects to focus in front of the retina; it is corrected using a concave (diverging) lens.",
            "A concave lens is required for myopia because it diverges the incoming parallel rays slightly before entering the eye, shifting the focal point back onto the retina.",
            "In a myopic eye, the image of a distant object forms in front of the retina. A concave lens of suitable focal length creates a virtual image at the person's far point, restoring clear vision.",
            "Corrective spectacles for myopia must use concave lenses of negative power (P < 0) to reduce the overall converging power of the defective eye."
        ],
        "slip_expansions": [
            "Correctly selected concave lens, but calculated lens power P = -{slip} D instead of -2.5 D due to formula inversion.",
            "Concave lens chosen, but power calculated as +2.5 D instead of -2.5 D due to sign slip."
        ],
        "unit_expansions": [
            "Corrective concave lens power is -2.5 Watts instead of Diopters.",
            "Required focal length is -40 Newtons instead of cm."
        ],
        "unsure_expansions": [
            "I always mix up whether myopia needs concave or convex spectacles",
            "sir which lens corrects myopia, is it converging or diverging?"
        ],
        "stem_expansions": [
            "A Class 10 student sitting at the back bench cannot read the blackboard clearly but reads his textbook with ease. Name the defect of vision and specify the corrective lens type.",
            "A person with myopia has a far point of 1.5 m. What kind of corrective lens must be prescribed, and what is its optical nature according to NCERT?"
        ],
        "param_expansions": [(150,), (200,), (120,)]
    },

    # 6. HUMAN EYE: PRISM DISPERSION
    "HUMAN_EYE_PRISM_DISPERSION": {
        "misc_expansions": [
            "Red light is deflected the most by a glass prism because red has the longest wavelength and highest energy.",
            "Red light bends through the greatest angle because it travels slowest in glass, so red is at the bottom of the spectrum.",
            "Violet light travels fastest in glass and therefore bends the least, appearing at the top of the spectrum.",
            "Because red is a stronger color, the glass prism refracts red light more than violet light.",
            "The deviation angle is highest for red and lowest for violet according to prism refraction rules."
        ],
        "correct_expansions": [
            "Violet light undergoes the greatest deviation and red undergoes the least deviation because refractive index of glass is highest for violet (which travels slowest in glass) and lowest for red (which travels fastest in glass).",
            "According to Cauchy's relation, refractive index varies inversely with wavelength: red light (longest wavelength) travels fastest in glass and deviates least, while violet light (shortest wavelength) travels slowest and deviates most.",
            "Violet bends the most because its speed in glass is minimum among visible colors (highest refractive index n), whereas red bends the least because its speed in glass is maximum.",
            "In the visible spectrum VIBGYOR, violet has the shortest wavelength and experiences the greatest refractive bending, forming the bottom band of the dispersed spectrum."
        ],
        "slip_expansions": [
            "Violet deviates most, but calculated angle of minimum deviation as {slip} degrees instead of 38 degrees.",
            "Identified VIBGYOR correctly, but wrote refractive index difference as 0.8 instead of 0.08 due to decimal slip."
        ],
        "unit_expansions": [
            "Angle of deviation for violet is 40 Amperes instead of degrees.",
            "Prism dispersion power reported with units of Joules."
        ],
        "unsure_expansions": [
            "confused whether red or violet bends more when passing through a prism",
            "sir does red travel faster or slower than violet inside the glass prism?"
        ],
        "stem_expansions": [
            "When a narrow beam of white light passes through a triangular glass prism, which constituent color undergoes the maximum deviation from its original path and why?",
            "In NCERT Science Class 10 Activity 11.2, white light is split into a seven-color spectrum by a glass prism. Explain the order of deviation of red versus violet light."
        ],
        "param_expansions": [(38,), (42,), (35,)]
    },

    # 7. HUMAN EYE: ATMOSPHERIC TWINKLING
    "HUMAN_EYE_ATMOSPHERIC_TWINKLING": {
        "misc_expansions": [
            "Stars twinkle because their nuclear energy fluctuated and they physically flash on and off in deep space.",
            "Twinkling occurs because clouds and space dust pass in front of the star, blocking and unblocking its light.",
            "Stars turn on and off periodically like flashing bulbs due to internal chemical pulsations.",
            "The distance to stars is so large that light pulses arrive intermittently, causing the twinkling effect.",
            "Twinkling is an intrinsic emission artifact caused by periodic solar flares on the star's surface."
        ],
        "correct_expansions": [
            "Twinkling of stars is caused by atmospheric refraction of starlight through continuously fluctuating air layers of varying temperatures, densities, and refractive indices.",
            "Starlight travels through turbulent atmospheric layers whose refractive index changes continuously; the apparent position and amount of starlight reaching the eye fluctuates rapidly, causing twinkling.",
            "Since stars are point sources of light at immense distances, continuous turbulence in Earth's atmosphere bends their incoming light randomly, creating the optical illusion of twinkling.",
            "Twinkling is purely an atmospheric refraction phenomenon: fluctuating atmospheric density shifts the ray path, varying the apparent intensity and position of the point source."
        ],
        "slip_expansions": [
            "Atmospheric refraction causes twinkling, but stated apparent star position shifts by {slip} degrees instead of arcseconds.",
            "Refraction changes apparent brightness, but miscalculated time delay as {slip} minutes instead of milliseconds."
        ],
        "unit_expansions": [
            "Fluctuation in starlight intensity is 5 Volts instead of percentage.",
            "Atmospheric density variation reported in Joules."
        ],
        "unsure_expansions": [
            "do stars actually pulse their light or is it just the air in between that causes twinkling?",
            "sir why do stars twinkle but planets do not twinkle?"
        ],
        "stem_expansions": [
            "Why do distant stars appear to twinkle on a clear night, whereas nearby planets do not twinkle according to NCERT Class 10?",
            "Explain whether the twinkling of stars is an intrinsic property of the star or an optical effect of the Earth's atmosphere."
        ],
        "param_expansions": [(1,), (2,), (5,)]
    },

    # 8. HUMAN EYE: RAYLEIGH SCATTERING
    "HUMAN_EYE_RAYLEIGH_SCATTERING": {
        "misc_expansions": [
            "The daytime sky appears blue because the huge oceans and seas reflect their blue water color up into the atmosphere.",
            "The sky is blue because the ozone layer is naturally blue and reflects sunlight like a blue mirror.",
            "Sea water acts as a giant mirror reflecting blue light upwards, which illuminates the sky blue.",
            "Atmospheric nitrogen and oxygen gases have an intrinsic blue chemical color that stains the sunlight blue.",
            "The blue color is due to the reflection of water vapor clouds floating in the upper atmosphere."
        ],
        "correct_expansions": [
            "The clear sky appears blue because fine atmospheric molecules (nitrogen and oxygen) scatter shorter wavelengths of sunlight (blue/violet) much more strongly than longer wavelengths (red), in accordance with Rayleigh scattering (scattering proportional to 1/lambda^4).",
            "Fine particles in the atmosphere have sizes smaller than the wavelength of visible light; they scatter shorter blue wavelengths about ten times more effectively than red light, directing blue light toward our eyes from all directions.",
            "Rayleigh scattering law dictates that scattering intensity is inversely proportional to the fourth power of wavelength, causing the blue component of white sunlight to be scattered in all directions by gas molecules.",
            "Sunlight is scattered by air molecules; because blue light has a short wavelength near 400 nm, it is scattered predominantly across the entire dome of the sky."
        ],
        "slip_expansions": [
            "Rayleigh scattering is proportional to 1/lambda^4, but calculated blue/red ratio as {slip} instead of 10 due to squaring error.",
            "Correct scattering formula, but miscalculated wavelength ratio as 2.5 instead of 1.7."
        ],
        "unit_expansions": [
            "Rayleigh scattering intensity measured in Amperes instead of arbitrary flux units.",
            "Wavelength of blue light given as 400 Newtons instead of nanometers."
        ],
        "unsure_expansions": [
            "is the sky blue because of ocean reflection or Rayleigh scattering of sunlight?",
            "why is the sky blue during day but turns reddish orange at sunset?"
        ],
        "stem_expansions": [
            "Why does the clear daytime sky appear blue to an observer on Earth, but appears dark black to an astronaut in space without an atmosphere?",
            "Explain the scientific reason for the blue color of the clear sky as described in NCERT Class 10 Chapter 11."
        ],
        "param_expansions": [(400,), (700,), (550,)]
    },

    # 9. ELECTRICITY: CURRENT CONSERVATION
    "ELECTRICITY_CURRENT_CONSERVATION": {
        "misc_expansions": [
            "The electric current gets consumed by the first bulb to produce light, so the second bulb in series receives less electric current.",
            "Current decreases along the circuit wire because electrical appliances consume the current as it flows through them.",
            "Ammeter A1 reads 1.5 A but ammeter A2 reads only 0.8 A because the intervening light bulb uses up electric current.",
            "Electrical current is used up by resistors, so the current exiting a load is always strictly less than the current entering it.",
            "The electric charge is burnt up in the filament to make glow, leaving less current in the return wire."
        ],
        "correct_expansions": [
            "Electric current is strictly conserved at all points in a single closed series circuit; both ammeters read identical values because electric charge cannot accumulate or be destroyed.",
            "Appliances consume electric potential energy, not electric current or charge; the rate of flow of charge (current I) entering a bulb is exactly equal to the rate of flow of charge leaving it.",
            "By the principle of conservation of electric charge, the current is identical everywhere in a series branch: I_1 = I_2 = I_total.",
            "Charge flow in a series circuit is analogous to continuous incompressible water in a closed pipe; no current is consumed by the components."
        ],
        "slip_expansions": [
            "Current is conserved (I1 = I2), but calculated circuit current I = V/R as {slip} A instead of 1.0 A due to division slip.",
            "Both ammeters read identical current, but arithmetic slip gave 0.75 A instead of 0.50 A."
        ],
        "unit_expansions": [
            "Current in series is conserved at 1.5 Volts instead of Amperes.",
            "Current reading on ammeter is 2.0 Ohms."
        ],
        "unsure_expansions": [
            "does the first bulb in series get more current than the second bulb or do they get the same?",
            "sir is current used up by bulbs or is energy used up?"
        ],
        "stem_expansions": [
            "Two identical electric lamps are connected in series with a 12V battery and two ammeters A1 and A2 placed before and after the first lamp. Compare the ammeter readings.",
            "In NCERT Class 10 Chapter 12, what does the principle of charge conservation tell us about the current at different points in a simple series circuit?"
        ],
        "param_expansions": [(12, 6), (6, 3), (24, 12)]
    },

    # 10. ELECTRICITY: PARALLEL BATTERY DELIVERY
    "ELECTRICITY_PARALLEL_BATTERY_DELIVERY": {
        "misc_expansions": [
            "A 12V battery supplies a fixed, constant electric current regardless of how many parallel resistors or branches you connect to it.",
            "Adding a third parallel branch divides the battery's fixed current into three smaller parts, so each branch receives less current.",
            "The battery delivers a constant total current of 2 A under all circumstances; connecting more appliances merely starves each appliance.",
            "Batteries are constant current generators, so total circuit current never changes when you add parallel loads.",
            "Every battery has a fixed current capacity that it always pushes out, independent of total equivalent resistance."
        ],
        "correct_expansions": [
            "A battery maintains a constant potential difference (voltage V), not a constant current; connecting additional branches in parallel decreases equivalent resistance and increases the total current drawn from the battery.",
            "Each parallel branch connected to a constant voltage battery operates independently with I_branch = V / R; adding more parallel branches increases total current I_total = sum(I_branch).",
            "The battery acts as an ideal voltage source: as total equivalent resistance decreases (1/R_eq = 1/R1 + 1/R2 + ...), the battery delivers more total current I = V / R_eq.",
            "In parallel domestic wiring, adding another appliance draws additional current from the supply while keeping branch voltage constant."
        ],
        "slip_expansions": [
            "Total current increases from 2 A to 4 A, but slip in addition gave {slip} A.",
            "Voltage is constant, but calculated total current as {slip} A due to division error."
        ],
        "unit_expansions": [
            "Battery maintains constant potential of 12 Amperes across parallel branches.",
            "Total current drawn is 4 Volts instead of Amperes."
        ],
        "unsure_expansions": [
            "when we turn on more appliances in parallel at home, does the battery supply more current or a fixed current?",
            "sir does adding parallel resistors increase or decrease total current drawn from the source?"
        ],
        "stem_expansions": [
            "A 12 V accumulator is connected to two 6-ohm resistors in parallel. A third 6-ohm resistor is connected in parallel. How does the total current delivered by the battery change?",
            "According to Ohm's law and NCERT Class 10, does an ideal battery supply constant voltage or constant current when circuit loads change?"
        ],
        "param_expansions": [(12, 6, 6), (24, 12, 12), (6, 3, 3)]
    },

    # 11. ELECTRICITY: OHM'S LAW RESISTANCE
    "ELECTRICITY_OHMS_LAW_RESISTANCE": {
        "misc_expansions": [
            "According to Ohm's law V = IR, increasing the voltage across a fixed metallic resistor causes its physical resistance R to increase proportionately.",
            "If you double the potential difference across a copper wire, its electrical resistance R automatically doubles.",
            "Resistance R changes when voltage changes because R is directly proportional to voltage V.",
            "Higher voltage creates more electrical resistance inside the conductor to stop the current.",
            "The resistance of a fixed metallic resistor is not constant; it increases linearly with applied voltage."
        ],
        "correct_expansions": [
            "For an ohmic metallic conductor at constant temperature, resistance R is an intrinsic constant property (R = V/I = constant); doubling the voltage doubles the current, leaving R strictly unchanged.",
            "Ohm's law states that current is directly proportional to potential difference (I proportional to V); the constant of proportionality is the conductor's resistance R, which is independent of V and I.",
            "Resistance depends only on the conductor's length, cross-sectional area, material, and temperature, not on the applied potential difference across it.",
            "Increasing voltage V causes a proportional increase in current I such that the ratio V/I remains constant (ohmic behavior)."
        ],
        "slip_expansions": [
            "Resistance remains constant at {R} ohms, but calculated current I = {V}/{R} as {slip} A due to arithmetic slip.",
            "R = {R} ohms is unchanged, but miscalculated new current when voltage was doubled."
        ],
        "unit_expansions": [
            "Resistance is constant at {R} Volts instead of Ohms.",
            "Calculated resistance of the conductor in Amperes."
        ],
        "unsure_expansions": [
            "sir if V increases in V = IR, does R increase or does I increase?",
            "does the resistance of a fixed resistor depend on applied voltage?"
        ],
        "stem_expansions": [
            "A fixed nichrome wire resistor has resistance {R} ohms. If the potential difference across it is increased from {V} V to {misc_val} V at constant temperature, what happens to its resistance?",
            "In NCERT Activity 12.1 (verifying Ohm's law), how does the ratio V/I behave as the number of electric cells is increased?"
        ],
        "param_expansions": [(10, 5, 2), (20, 10, 2), (15, 5, 3)]
    },

    # 12. ELECTRICITY: PARALLEL RESISTANCE ADDITION
    "ELECTRICITY_PARALLEL_RESISTANCE_ADDITION": {
        "misc_expansions": [
            "When two {R}-ohm resistors are connected in parallel, the total equivalent resistance is simply their sum: R_eq = {R} + {R} = {misc_val} ohms.",
            "Equivalent resistance in parallel is found by adding the individual resistances directly: R_eq = R1 + R2.",
            "Connecting resistors together always increases the total circuit resistance, so parallel resistance is higher than either branch.",
            "Two {R}-ohm resistors in parallel offer double the total resistance because there are two resistors obstructing the current.",
            "Parallel resistors add up directly just like series resistors: R_total = {misc_val} ohms."
        ],
        "correct_expansions": [
            "In parallel connection, the reciprocal of equivalent resistance equals the sum of reciprocals: 1/R_eq = 1/R1 + 1/R2 = 1/{R} + 1/{R} = 2/{R}, giving R_eq = {R}/2 = {cor_val} ohms (less than either individual resistor).",
            "Connecting resistors in parallel creates multiple parallel pathways for charge flow, increasing effective cross-sectional area and decreasing equivalent resistance to R_eq = {cor_val} ohms.",
            "According to NCERT Class 10 formula 1/R_p = 1/R1 + 1/R2, two identical {R}-ohm resistors in parallel produce an equivalent resistance of exactly {cor_val} ohms.",
            "The equivalent resistance of any parallel combination is strictly less than the smallest individual resistance; here R_eq = ({R} * {R}) / ({R} + {R}) = {cor_val} ohms."
        ],
        "slip_expansions": [
            "1/R_eq = 1/{R} + 1/{R} = 2/{R}, but forgot to take reciprocal at final step, reporting R_eq = 2/{R} ohms.",
            "Calculated reciprocal formula correctly, but slipped in addition: got R_eq = {slip} ohms."
        ],
        "unit_expansions": [
            "Equivalent parallel resistance is {cor_val} Amperes instead of Ohms.",
            "Parallel resistance result stated in Volts."
        ],
        "unsure_expansions": [
            "do parallel resistors add up directly (R1 + R2) or do their reciprocals add up (1/R1 + 1/R2)?",
            "sir is parallel resistance greater than or smaller than series resistance?"
        ],
        "stem_expansions": [
            "Two identical resistors of resistance {R} ohms each are connected in parallel. Calculate the equivalent resistance of the combination according to NCERT Chapter 12.",
            "A student connects two {R}-ohm resistors in parallel across a battery. What is the effective resistance encountered by the circuit current?"
        ],
        "param_expansions": [(8, 4), (12, 6), (16, 8)]
    },

    # 13. ELECTRICITY: POWER FORMULA MIS-SELECTION
    "ELECTRICITY_POWER_FORMULA_MISSELECTION": {
        "misc_expansions": [
            "In a parallel circuit across constant voltage, the bulb with higher resistance will dissipate more power because according to P = I^2 * R, power is directly proportional to resistance.",
            "Bulb with 100 ohms glows brighter than bulb with 50 ohms in parallel because power increases with resistance R.",
            "Since P = I^2 * R, higher resistance always means greater electric power consumption regardless of whether components are in series or parallel.",
            "The 100-ohm resistor dissipates twice the power of the 50-ohm resistor in parallel because power is directly proportional to R.",
            "I used P = I^2 * R for parallel circuit, concluding that the higher resistance bulb consumes more electrical energy."
        ],
        "correct_expansions": [
            "In parallel connection, both bulbs share the same potential difference V; therefore the appropriate power formula is P = V^2 / R, meaning power is inversely proportional to resistance, so the smaller resistance bulb glows brighter.",
            "Because voltage V is constant across parallel branches, P = V^2 / R indicates that lower resistance draws more current (I = V/R) and dissipates greater electric power.",
            "The formula P = I^2 * R is useful when current I is constant (in series), whereas P = V^2 / R is appropriate when potential difference V is constant (in parallel).",
            "Under constant voltage V, the 50-ohm resistor draws twice as much current as the 100-ohm resistor, dissipating twice the electric power (P = V^2 / R)."
        ],
        "slip_expansions": [
            "Selected P = V^2 / R correctly, but calculated power as {slip} W instead of 24 W due to squaring slip.",
            "Correct inverse relation P = V^2/R, but arithmetic error in division gave {slip} W."
        ],
        "unit_expansions": [
            "Electric power dissipated is 24 Joules instead of Watts.",
            "Calculated power output in Amperes."
        ],
        "unsure_expansions": [
            "should I use P = I^2 * R or P = V^2 / R to compare bulb brightness in parallel?",
            "does the higher resistance bulb glow brighter in parallel or in series?"
        ],
        "stem_expansions": [
            "Two electric bulbs of resistances 50 ohms and 100 ohms are connected in parallel to a 220V mains supply. Which bulb will glow brighter and consume more power?",
            "Explain why the formula P = V^2 / R is used instead of P = I^2 * R when comparing power dissipation in parallel circuits according to NCERT Class 10."
        ],
        "param_expansions": [(220, 50, 100), (12, 4, 8), (24, 6, 12)]
    },

    # 14. MAGNETIC EFFECTS: POLE-CHARGE EQUIVALENCE
    "MAGNETIC_EFFECTS_POLE_CHARGE_EQUIVALENCE": {
        "misc_expansions": [
            "A magnetic north pole is literally the same thing as a positive electrostatic charge, and a south pole is a negative electrostatic charge.",
            "Magnetic poles and electric charges are identical; a stationary proton will be attracted to a magnetic south pole just like to a negative charge.",
            "North pole has positive static electricity and south pole has negative static electricity.",
            "Breaking a magnet isolates positive charge at one end and negative charge at the other end.",
            "A magnetic field is just an electric field created by positive and negative poles."
        ],
        "correct_expansions": [
            "Magnetic poles and electrostatic charges are fundamentally distinct physical phenomena: magnetic poles always exist as inseparable dipoles (no isolated magnetic monopoles exist), and a stationary electric charge experiences zero magnetic force.",
            "Electrostatic charges (positive and negative) can exist in isolation as monopoles, whereas every magnet possesses both North and South poles; breaking a magnet produces two smaller complete dipole magnets.",
            "Magnetic fields are produced by moving charges or intrinsic spin, whereas electrostatic fields are produced by stationary charges; magnetic north does not carry positive electrostatic charge.",
            "Lorentz force equation F = q(v x B) shows that a stationary charge (v = 0) experiences no force from a magnetic field, proving magnetic poles are not electrostatic charges."
        ],
        "slip_expansions": [
            "Stationary charge experiences zero force (F = qvB sin theta = 0), but miscalculated force as {slip} N due to multiplication error.",
            "Differentiated poles from charges correctly, but stated magnetic field unit is Weber instead of Tesla."
        ],
        "unit_expansions": [
            "Magnetic pole strength measured in Coulombs instead of Ampere-meters.",
            "Magnetic field B reported with units of Volts/meter."
        ],
        "unsure_expansions": [
            "is a magnetic north pole positively charged or are magnetism and electricity different?",
            "sir will a stationary positive charge be attracted to a magnetic south pole?"
        ],
        "stem_expansions": [
            "A stationary positive charge +q is placed near the north pole of a strong permanent bar magnet. What electrostatic or magnetic force does it experience according to NCERT?",
            "Explain the fundamental physical difference between electric charges and magnetic poles as taught in NCERT Class 10 Chapter 13."
        ],
        "param_expansions": [(1,), (2,), (5,)]
    },

    # 15. MAGNETIC EFFECTS: FIELD LINES CROSSING
    "MAGNETIC_EFFECTS_FIELD_LINES_CROSSING": {
        "misc_expansions": [
            "Magnetic field lines can cross and intersect each other near strong poles where the magnetic field is very concentrated.",
            "At the magnetic poles where the force is strongest, multiple field lines cross each other at the same point.",
            "Field lines intersect whenever two like poles are pushed close together.",
            "Two magnetic lines of force cross each other at the neutral point between two magnets.",
            "Field lines can intersect because the magnetic force can point in two directions at once."
        ],
        "correct_expansions": [
            "No two magnetic field lines are found to cross each other; if they did, it would mean that at the point of intersection, a compass needle would point in two different directions simultaneously, which is physically impossible.",
            "The tangent to a magnetic field line gives the unique direction of the net magnetic field at that point; since the field vector must be unique, lines can never intersect.",
            "By NCERT Class 10 Section 13.2, magnetic field lines form continuous closed curves that never intersect, because the resultant magnetic force at any point has only one single direction.",
            "At any spatial point, the resultant magnetic field B is a single unique vector sum; two intersecting field lines would imply two distinct tangents and two directions of net field, which cannot occur."
        ],
        "slip_expansions": [
            "Lines never cross, but misquoted pole field density formula as B = {slip} Tesla.",
            "Correct unique direction principle, but stated compass deflection angle as {slip} degrees."
        ],
        "unit_expansions": [
            "Magnetic field line density measured in Newtons instead of Tesla or Weber/m^2.",
            "Magnetic flux reported in Amperes."
        ],
        "unsure_expansions": [
            "can magnetic field lines cross each other near the poles where the magnet is strongest?",
            "sir what would happen to a magnetic compass if two field lines crossed?"
        ],
        "stem_expansions": [
            "Why is it impossible for two magnetic field lines of force to cross or intersect each other according to NCERT Class 10 Chapter 13?",
            "A student draws two magnetic field lines crossing each other near the pole of a bar magnet. Explain why this diagram is scientifically incorrect."
        ],
        "param_expansions": [(1,), (2,), (3,)]
    },

    # 16. MAGNETIC EFFECTS: LORENTZ LEFT-HAND RULE
    "MAGNETIC_EFFECTS_LORENTZ_LEFT_HAND": {
        "misc_expansions": [
            "Fleming's Left-Hand Rule is applied using the right hand, with thumb representing magnetic field and index finger representing current.",
            "The direction of force on a current-carrying wire in a magnetic field is always parallel to the direction of current flow.",
            "I used Fleming's right-hand rule to find the mechanical force on a motor wire instead of left-hand rule.",
            "The magnetic force pushes the conductor along the direction of magnetic field lines towards the south pole.",
            "Force is always directed in the direction of the electric current."
        ],
        "correct_expansions": [
            "By Fleming's Left-Hand Rule: stretch the thumb, forefinger, and middle finger of the left hand mutually perpendicular. Forefinger = Field (B), Middle finger = Current (I), and Thumb points in the direction of Motion/Force (F).",
            "The magnetic Lorentz force F = I(L x B) acts perpendicular to both the conductor and the external magnetic field, determined strictly by Fleming's Left-Hand Rule.",
            "According to NCERT Section 13.4, the direction of mechanical force on a current-carrying conductor in a magnetic field is perpendicular to both current and field, given by the left hand thumb.",
            "Using Fleming's Left-Hand Rule with left hand: Forefinger points in field direction, Centre finger points in conventional current direction, then Thumb indicates the direction of thrust or force."
        ],
        "slip_expansions": [
            "Correct left-hand rule, but calculated force magnitude F = B*I*L as {slip} N instead of 1.2 N due to multiplication slip.",
            "Left-hand rule applied, but inverted 90 degree angle factor in calculation."
        ],
        "unit_expansions": [
            "Mechanical force on wire is 1.2 Tesla instead of Newtons.",
            "Magnetic flux density B given as 0.5 Joules."
        ],
        "unsure_expansions": [
            "do we use Fleming's Left-Hand Rule or Right-Hand Rule to find the direction of magnetic force on a motor wire?",
            "sir which finger represents current and which represents field in Fleming's rule?"
        ],
        "stem_expansions": [
            "A horizontal copper rod carrying conventional current towards the East is placed in a magnetic field directed vertically downwards. Determine the direction of the magnetic force acting on the rod.",
            "State Fleming's Left-Hand Rule and explain how it determines the direction of motion of a current-carrying conductor in a magnetic field (NCERT Class 10)."
        ],
        "param_expansions": [(10,), (15,), (20,)]
    },

    # 17. MAGNETIC EFFECTS: ELECTROMAGNETIC INDUCTION
    "MAGNETIC_EFFECTS_ELECTROMAGNETIC_INDUCTION": {
        "misc_expansions": [
            "A stationary bar magnet held motionless inside a wire coil induces a continuous steady electric current.",
            "As long as a strong magnet is present inside the coil, a steady voltage is continuously generated even if nothing moves.",
            "A constant, unchanging magnetic field induces a constant electric current in a closed loop.",
            "Galvanometer shows continuous deflection because the stationary magnet's field lines are present in the coil.",
            "Motion is not required; strong static magnetic field itself produces electric current."
        ],
        "correct_expansions": [
            "An induced current is generated in a coil only when there is relative motion between the magnet and coil that causes a CHANGE in magnetic flux linked with the circuit (Faraday's Law of Electromagnetic Induction).",
            "When the magnet is held stationary inside the coil, the magnetic flux through the coil is constant (dPhi/dt = 0); therefore induced electromotive force is zero and galvanometer deflection drops to zero.",
            "According to NCERT Class 10 Section 13.5, electric current is induced only during the duration of change in magnetic field or relative motion; static fields produce zero induced current.",
            "Induced EMF depends strictly on the rate of change of magnetic flux (EMF = -N * dPhi/dt); a stationary magnet has zero rate of change, so induced current is strictly zero."
        ],
        "slip_expansions": [
            "Induced EMF requires motion, but calculated induced voltage as {slip} V due to decimal slip.",
            "Current flows only during movement, but miscalculated induced charge as {slip} Coulombs."
        ],
        "unit_expansions": [
            "Induced EMF measured in Amperes instead of Volts.",
            "Rate of change of magnetic flux stated in Tesla instead of Weber/second (Volts)."
        ],
        "unsure_expansions": [
            "does a stationary magnet inside a coil produce current or must the magnet be moving?",
            "sir why does the galvanometer needle return to zero when the magnet stops moving?"
        ],
        "stem_expansions": [
            "A strong bar magnet is held stationary inside a solenoid connected to a sensitive galvanometer. What deflection is observed on the galvanometer scale?",
            "In NCERT Class 10 Activity 13.8 (Faraday's experiment), describe what happens to the induced current when relative motion between coil and magnet ceases."
        ],
        "param_expansions": [(10,), (20,), (30,)]
    },

    # 18. MOTION: SPEED DISTANCE TIME
    "MOTION_SPEED_DISTANCE_TIME": {
        "misc_expansions": [
            "Speed is calculated by multiplying distance and time together: speed = distance * time = {d} * {t} = {misc_val} m/s.",
            "To find average speed, we divide time by distance: speed = time / distance = {t} / {d} m/s.",
            "I multiplied {d} meters by {t} seconds to get the speed because distance and time both increase together.",
            "Speed = t / d because time comes first in the problem statement.",
            "Velocity formula is v = d * t, giving {misc_val} m/s."
        ],
        "correct_expansions": [
            "Speed is defined as the distance traveled per unit time: average speed = total distance / total time = {d} / {t} = {cor_val} m/s.",
            "According to NCERT Class 9 Chapter 8, speed v = s / t. Dividing distance {d} m by time {t} s yields {cor_val} m/s.",
            "Rate of change of position with respect to time is speed: v = distance / time = {d} / {t} = {cor_val} m/s.",
            "Using the fundamental kinematic formula v = d / t: speed equals {d} m divided by {t} s, giving exactly {cor_val} meters per second."
        ],
        "slip_expansions": [
            "Applied v = d / t correctly ({d} / {t}), but made an arithmetic slip in division, obtaining {slip} m/s.",
            "Divided distance by time, but calculated {d}/{t} as {slip} m/s."
        ],
        "unit_expansions": [
            "Speed is {cor_val} meters instead of meters per second (m/s).",
            "Speed reported with units m/s^2 (acceleration unit)."
        ],
        "unsure_expansions": [
            "is speed equal to distance divided by time or distance multiplied by time?",
            "sir do we divide distance by time or time by distance for velocity?"
        ],
        "stem_expansions": [
            "An automobile covers a straight distance of {d} meters in {t} seconds. Calculate its average speed in SI units (NCERT Class 9).",
            "A cyclist travels along a straight roadway covering {d} m in {t} s. Determine the cyclist's speed according to kinematic definitions."
        ],
        "param_expansions": [(120, 6), (180, 9), (240, 8)]
    },

    # 19. MOTION: SPEED VS ACCELERATION
    "MOTION_SPEED_VS_ACCELERATION": {
        "misc_expansions": [
            "A train traveling at a high steady velocity of {v} m/s must have a huge acceleration because it is moving so fast.",
            "Since speed is high ({v} m/s), acceleration is also high; fast moving objects always have large acceleration.",
            "High speed means high acceleration because acceleration and velocity are basically the same thing.",
            "The body moves at {v} m/s, so its acceleration is {v} m/s^2.",
            "Whenever an object moves with great speed, its acceleration is necessarily non-zero and large."
        ],
        "correct_expansions": [
            "Acceleration is the rate of CHANGE of velocity with time (a = (v - u) / t); since the train moves at a uniform steady velocity, change in velocity is zero (Delta v = 0), so acceleration is strictly zero (a = 0 m/s^2).",
            "Speed and acceleration are distinct physical quantities: speed describes how fast an object moves, while acceleration describes how rapidly speed changes; constant speed in a straight line means zero acceleration.",
            "According to NCERT Class 9 Section 8.3, uniform motion along a straight line has zero acceleration regardless of how large the constant velocity magnitude is.",
            "Acceleration a = dv/dt = 0 because the velocity is steady and unchanging; high velocity does not imply high acceleration."
        ],
        "slip_expansions": [
            "Acceleration is zero, but calculated distance traveled s = v * t as {slip} m due to arithmetic error.",
            "Identified a = 0, but miscalculated time to stop under braking."
        ],
        "unit_expansions": [
            "Acceleration is zero meters per second (m/s) instead of m/s^2.",
            "Reported acceleration in units of Newtons."
        ],
        "unsure_expansions": [
            "if an object is moving really fast at constant speed, does it have high acceleration or zero acceleration?",
            "sir does high speed always mean there is acceleration?"
        ],
        "stem_expansions": [
            "A bullet train travels along a straight track at a constant, uniform speed of {v} m/s for {t} seconds. What is the acceleration of the train during this period?",
            "In NCERT Class 9 Chapter 8, what is the acceleration of an object executing uniform motion in a straight line at {v} m/s?"
        ],
        "param_expansions": [(40, 5), (60, 10), (50, 4)]
    },

    # 20. FORCE: NEWTON'S FIRST LAW (IMPETUS)
    "FORCE_NEWTON_FIRST_LAW": {
        "misc_expansions": [
            "A moving object requires a continuous applied external force to keep moving; if the forward force stops, the object immediately stops.",
            "Constant velocity requires a constant forward net force because according to common sense, force is needed to sustain motion.",
            "An object cannot keep moving without a force pushing it from behind (impetus theory).",
            "The hockey puck moves because of the force trapped inside it from the hit; once that force is exhausted, it stops.",
            "To maintain a steady speed of 10 m/s, a constant push must be continuously applied."
        ],
        "correct_expansions": [
            "By Newton's First Law of Motion (Law of Inertia), an object in motion continues to move with constant velocity along a straight line unless acted upon by an unbalanced external net force; zero net force is required to sustain steady motion.",
            "Force causes a CHANGE in motion (acceleration), not motion itself; on a frictionless surface, an object requires zero forward force to maintain constant speed indefinitely.",
            "Aristotelian impetus theory is incorrect: in NCERT Class 9 Chapter 9, Galileo and Newton established that an object keeps moving with constant speed when net external force is zero.",
            "According to F_net = m*a, when acceleration is zero (constant velocity), the net force acting on the body must be exactly zero."
        ],
        "slip_expansions": [
            "Net force is zero (F_net = 0 N), but calculated momentum p = m*v as {slip} kg m/s due to multiplication slip.",
            "Applied Newton's first law correctly, but calculated inertia value with arithmetic slip."
        ],
        "unit_expansions": [
            "Net force required to sustain motion is 0 Joules instead of Newtons.",
            "Inertia measured in Newtons instead of kilograms."
        ],
        "unsure_expansions": [
            "does a body need a constant force to keep moving at constant speed or does it keep moving on its own?",
            "sir why does a sliding book stop on a table if no force is needed to sustain motion?"
        ],
        "stem_expansions": [
            "A space probe travels in deep interstellar space far from any celestial body at a constant speed of {v} m/s. What net forward thrust is needed to keep it moving at this speed?",
            "According to Newton's First Law of Motion in NCERT Class 9, does an object moving at constant velocity on a frictionless surface require an external force?"
        ],
        "param_expansions": [(100,), (250,), (500,)]
    },

    # 21. FORCE: NEWTON'S THIRD LAW (ACTION-REACTION)
    "FORCE_NEWTON_THIRD_LAW_ACTION_REACTION": {
        "misc_expansions": [
            "Action and reaction forces are equal and opposite, so they cancel each other out completely, which means nothing should ever be able to accelerate or move.",
            "Because Newton's third law says action equals minus reaction, the net force is always zero everywhere and motion is impossible.",
            "The horse cannot pull the cart because the cart pulls back on the horse with an equal force, canceling out the pull.",
            "Action and reaction act on the same object in opposite directions, canceling to zero net force.",
            "Whenever two bodies interact, the opposite forces cancel to zero, so acceleration cannot occur."
        ],
        "correct_expansions": [
            "Action and reaction forces never cancel each other out because they always act on TWO DIFFERENT interacting bodies, not on the same body.",
            "According to NCERT Class 9 Section 9.6, Newton's third law states forces occur in pairs on different bodies; acceleration of an individual body is determined by the net external force acting on THAT body alone.",
            "When a horse pulls a cart: the forward pull acts ON the cart, while the backward pull acts ON the horse; since they act on different objects, they cannot cancel.",
            "Cancellation requires opposing forces to act simultaneously on a single body; action-reaction pairs act on separate bodies (F_AB acts on A, F_BA acts on B)."
        ],
        "slip_expansions": [
            "Forces act on different bodies, but calculated net acceleration a = F/m as {slip} m/s^2 due to division slip.",
            "Identified third law correctly, but miscalculated contact force as {slip} N."
        ],
        "unit_expansions": [
            "Action force is 50 Joules instead of Newtons.",
            "Reaction force measured in kg m/s."
        ],
        "unsure_expansions": [
            "if action and reaction are equal and opposite, why don't they cancel each other out?",
            "sir why does a horse and cart move if the cart pulls back with equal force?"
        ],
        "stem_expansions": [
            "Explain why the equal and opposite action-reaction forces described by Newton's Third Law do not cancel each other out to prevent motion (NCERT Class 9).",
            "A swimmer pushes water backward with a force of 50 N. Why does the swimmer accelerate forward despite the equal and opposite reaction force?"
        ],
        "param_expansions": [(50,), (100,), (150,)]
    },

    # 22. GRAVITATION: FREE FALL
    "GRAVITATION_FREE_FALL": {
        "misc_expansions": [
            "A heavy 10 kg iron sphere falls significantly faster than a light 1 kg sphere because Earth's gravity pulls heavier objects harder.",
            "Heavier objects always hit the ground first in free fall because greater weight causes greater downward acceleration.",
            "The heavy ball reaches the ground first because its gravitational pull is ten times stronger.",
            "Heavier mass accelerates faster under gravity because F = mg gives more downward force.",
            "In vacuum, a bowling ball falls much faster than a feather because it has more mass."
        ],
        "correct_expansions": [
            "In the absence of air resistance (free fall), all objects accelerate towards Earth at the exact same rate g = G*M/R^2 (approx 9.8 m/s^2), completely independent of the object's mass; both heavy and light objects hit the ground simultaneously.",
            "Although the gravitational force on the heavier object is larger (F = m*g), its inertia (resistance to acceleration) is also proportionately larger by the exact same factor (a = F/m = mg/m = g), so acceleration is identical for all masses.",
            "According to NCERT Class 9 Chapter 10, Galileo's famous experiment demonstrated that acceleration due to gravity g is independent of the falling body's mass.",
            "Free fall acceleration g = 9.8 m/s^2 depends only on Earth's mass M and radius R, not on the mass m of the falling object; both spheres fall with identical speed and strike the ground together."
        ],
        "slip_expansions": [
            "Both fall at g = 9.8 m/s^2, but calculated fall time t = sqrt(2h/g) as {slip} s instead of 2.0 s due to square root slip.",
            "Both accelerate at same rate, but calculated final impact velocity as {slip} m/s due to arithmetic error."
        ],
        "unit_expansions": [
            "Acceleration due to gravity is 9.8 m/s instead of m/s^2.",
            "Free fall acceleration reported in Newtons."
        ],
        "unsure_expansions": [
            "does a heavier ball fall faster than a lighter ball in vacuum or do they land at the same time?",
            "sir why does a feather fall slower than a coin in air but together in vacuum?"
        ],
        "stem_expansions": [
            "Two solid metal spheres of mass 5 kg and 0.5 kg are dropped simultaneously from a height of {d} m in an evacuated vacuum chamber. Which sphere reaches the ground first?",
            "Explain why the acceleration of a body in free fall does not depend on its mass according to NCERT Class 9 Chapter 10."
        ],
        "param_expansions": [(20,), (45,), (80,)]
    },

    # 23. WORK ENERGY: WORK FORMULA
    "WORK_ENERGY_POWER_CLASS9": {
        "misc_expansions": [
            "Work done is always force multiplied by distance (W = F * d), regardless of the angle or direction between the force and displacement.",
            "A person holding a heavy 20 kg suitcase motionless on their head for two hours does a huge amount of work because they get tired.",
            "Work is done whenever a force is exerted, even if the object does not move at all.",
            "Carrying a luggage box horizontally across a platform does positive work against gravity equal to mgh.",
            "Work = F * d = 100 N * 5 m = 500 J, ignoring that force is perpendicular to displacement."
        ],
        "correct_expansions": [
            "Work done by a force is defined as W = F * d * cos(theta); when displacement is zero (holding a load motionless), work is strictly zero (W = 0 J), regardless of muscular fatigue.",
            "When displacement is perpendicular to force (theta = 90 degrees, such as gravity on a horizontally moving luggage), cos(90) = 0, so work done by that force is strictly zero.",
            "According to NCERT Class 9 Chapter 11, two conditions must be satisfied for scientific work to be done: a force must act, and the object must be displaced in the direction of the force.",
            "Holding an object stationary involves zero physical displacement (d = 0), so the mechanical work done on the object is W = F * 0 = 0 Joules."
        ],
        "slip_expansions": [
            "W = F * d * cos(0) = {d} * 10, but arithmetic slip in multiplication gave {slip} Joules.",
            "Applied work formula correctly, but slipped in unit conversion from kilojoules to joules."
        ],
        "unit_expansions": [
            "Work done is 500 Watts instead of Joules.",
            "Scientific work reported in Newtons."
        ],
        "unsure_expansions": [
            "if someone holds a heavy bag without moving, do they do scientific work or zero work?",
            "sir what is the work done by gravity when carrying a bag horizontally?"
        ],
        "stem_expansions": [
            "A porter carries a luggage of mass 15 kg on his head and walks horizontally a distance of 10 m across a railway platform. What is the work done by the porter against gravity?",
            "A student pushes against a rigid concrete wall with a force of 100 N for 10 minutes. The wall does not move. Calculate the work done on the wall (NCERT Class 9)."
        ],
        "param_expansions": [(15, 10), (20, 5), (10, 8)]
    },

    # 24. MOMENTUM CONSERVATION
    "MOMENTUM_CONSERVATION_CLASS9": {
        "misc_expansions": [
            "When a moving ball strikes a wall and stops, momentum is destroyed and the law of conservation of momentum is violated.",
            "Conservation of momentum only applies to elastic collisions, not when objects come to rest.",
            "If an object stops moving, its momentum vanishes from the universe.",
            "Momentum is lost because the final momentum is zero while initial momentum was positive.",
            "Stopping an object proves that total momentum is not conserved in real-world friction."
        ],
        "correct_expansions": [
            "The law of conservation of momentum states that total momentum of an ISOLATED system is conserved; when a ball hits a wall, momentum is transferred to the Earth-wall system, keeping total momentum constant.",
            "Momentum is never destroyed; the ball's momentum is transferred to the massive Earth, whose recoil velocity is imperceptibly tiny due to its enormous mass (Delta v_earth ~= 0).",
            "According to NCERT Class 9 Section 9.6, momentum is conserved in all collisions when all interacting bodies (including the wall/Earth) are included in the system boundary.",
            "External impulse from the wall changes the ball's individual momentum (Delta p = J), while imparting an equal and opposite impulse to the Earth, conserving total momentum."
        ],
        "slip_expansions": [
            "Total momentum conserved (m1*u1 = m2*v2), but calculated final recoil velocity as {slip} m/s due to division slip.",
            "Calculated momentum transfer as {slip} kg m/s due to arithmetic error."
        ],
        "unit_expansions": [
            "Momentum is conserved at 10 Joules instead of kg m/s.",
            "Momentum reported in units of Newtons."
        ],
        "unsure_expansions": [
            "is momentum destroyed when a moving car hits a wall and stops, or is it conserved?",
            "sir where does momentum go when a rolling ball stops?"
        ],
        "stem_expansions": [
            "A rubber ball of mass 0.2 kg moving at 10 m/s strikes a massive concrete wall and comes to a stop. Explain how momentum is conserved in this interaction according to NCERT Class 9.",
            "Does an inelastic collision where objects stick together or stop violate the universal law of conservation of momentum?"
        ],
        "param_expansions": [(10,), (15,), (20,)]
    },

    # 25. OPTICS: MAGNIFICATION SIGN
    "OPTICS_MAGNIFICATION_SIGN_INTERPRETATION": {
        "misc_expansions": [
            "A magnification of m = -2.5 means the image is smaller than the object because negative numbers are less than one.",
            "Since m is negative (-2.5), the image is diminished and shrunk down.",
            "Negative magnification means the image size has decreased below original size.",
            "m = -0.5 means the image is virtual because of the minus sign.",
            "The minus sign in magnification m = -2 indicates the image is smaller and reduced."
        ],
        "correct_expansions": [
            "The negative sign in magnification (m = -2.5) indicates that the image is REAL and INVERTED; the absolute value |m| = 2.5 > 1 indicates that the image is MAGNIFIED (enlarged).",
            "According to NCERT Class 10 Chapter 10, the sign of magnification indicates orientation (negative = inverted/real, positive = erect/virtual), whereas the magnitude |m| indicates relative size (|m| > 1 is enlarged, |m| < 1 is diminished).",
            "In m = -h'/h: the minus sign comes from inverted image height (h' < 0), meaning real inverted; since |m| = 2.5 is greater than 1, the image size is 2.5 times larger than the object.",
            "A magnification of m = -2.5 means: real, inverted, and enlarged by a factor of 2.5."
        ],
        "slip_expansions": [
            "Image is enlarged (|m|=2.5), but calculated image height h' as {slip} cm instead of 5 cm due to multiplication slip.",
            "Correctly identified inverted and magnified, but wrote focal length with arithmetic slip."
        ],
        "unit_expansions": [
            "Magnification is -2.5 cm instead of being a dimensionless ratio.",
            "Magnification reported in Diopters."
        ],
        "unsure_expansions": [
            "does a negative magnification like m = -2 mean the image is smaller or inverted?",
            "sir what does the minus sign in magnification formula represent?"
        ],
        "stem_expansions": [
            "A spherical mirror produces an image with a magnification of m = -2.5. Describe the nature (real/virtual) and relative size (enlarged/diminished) of the image (NCERT Class 10).",
            "A student calculates magnification of a lens as m = -1.5. What does the negative sign signify about the image orientation and type?"
        ],
        "param_expansions": [(2,), (3,), (1.5,)]
    },

    # 26. OPTICS: REFRACTIVE INDEX SPEED INVERSION
    "OPTICS_REFRACTIVE_INDEX_SPEED_INVERSION": {
        "misc_expansions": [
            "Medium A with higher refractive index (n = 1.65) allows light to travel faster than Medium B (n = 1.33) because higher index means better optical quality.",
            "Light moves fastest in optically denser media with large refractive index.",
            "Refractive index is directly proportional to light speed: v = c * n.",
            "Higher refractive index means light speeds up because it is guided better by the denser material.",
            "Light travels faster in diamond (n=2.42) than in water (n=1.33) because diamond has high refractive index."
        ],
        "correct_expansions": [
            "Refractive index n is inversely proportional to the speed of light in the medium: n = c / v, so light travels SLOWER in a medium with a higher refractive index.",
            "Medium with higher refractive index (n = 1.65) is optically denser, meaning light speed v = c / n is strictly less than in a medium with lower refractive index (n = 1.33).",
            "According to NCERT Class 10 Section 10.3.2, absolute refractive index n = c/v; therefore light travels fastest in the medium with the lowest refractive index.",
            "In diamond (n = 2.42), light travels at its slowest speed (v = c/2.42 ~= 1.24 x 10^8 m/s), whereas in water (n = 1.33) light travels much faster (v ~= 2.25 x 10^8 m/s)."
        ],
        "slip_expansions": [
            "v = c / n = 3e8 / 1.5, but division slip gave {slip}e8 m/s instead of 2.0e8 m/s.",
            "Correct inverse relation, but arithmetic slip in comparing speeds."
        ],
        "unit_expansions": [
            "Refractive index is 1.5 m/s instead of dimensionless.",
            "Speed of light in glass reported in Diopters."
        ],
        "unsure_expansions": [
            "does light travel faster or slower in a medium with a higher refractive index?",
            "sir is refractive index n directly or inversely proportional to light velocity?"
        ],
        "stem_expansions": [
            "The refractive indices of medium A and medium B are 1.50 and 1.33 respectively. In which medium does light travel faster according to NCERT Class 10 Chapter 10?",
            "Explain the physical relationship between the optical density (refractive index) of a transparent substance and the velocity of light passing through it."
        ],
        "param_expansions": [(1.5, 1.33), (1.65, 1.36), (2.42, 1.5)]
    },

    # 27. OPTICS: CONCAVE LENS REAL IMAGE FALLACY
    "OPTICS_CONCAVE_LENS_REAL_IMAGE_FALLACY": {
        "misc_expansions": [
            "A concave lens can form a real inverted image on a screen if the object is placed very far away beyond 2F.",
            "Placing an object beyond twice the focal length of a concave lens produces a sharp real image on a screen.",
            "Concave lenses produce real images when the object distance is large enough.",
            "Just like a concave mirror forms real images, a concave lens also forms real images on a viewing card.",
            "A concave lens converges distant parallel rays to a real focus point."
        ],
        "correct_expansions": [
            "A concave (diverging) lens can NEVER form a real image of a real object for any object position; it always forms a virtual, erect, and diminished image located between the optical center and the focus.",
            "Concave lenses always diverge incoming rays away from the principal axis; the refracted rays never physically intersect, so they cannot form a real image on a screen under any circumstances.",
            "According to NCERT Class 10 Table 10.5, for all positions of a real object (from infinity to optical center), a concave lens strictly produces a virtual, erect, and diminished image.",
            "Because 1/v = 1/f + 1/u and f < 0, u < 0, v is mathematically always negative, confirming the image is always virtual and located on the same side as the object."
        ],
        "slip_expansions": [
            "Image is virtual and erect, but calculated position v using lens formula with arithmetic slip as -{slip} cm.",
            "Identified virtual image correctly, but miscalculated magnification as -0.5 instead of +0.5."
        ],
        "unit_expansions": [
            "Virtual image distance is -10 Watts instead of cm.",
            "Focal length of concave lens is -20 Amperes."
        ],
        "unsure_expansions": [
            "can a concave lens ever form a real image on a screen if we place the object far away?",
            "sir does a concave lens always produce virtual images or can it produce real images too?"
        ],
        "stem_expansions": [
            "Can a student ever capture a real inverted image on a screen using a concave lens alone for any position of an object? Explain using NCERT principles.",
            "Describe the nature, orientation, and relative size of the image formed by a concave lens when an object is placed at infinity."
        ],
        "param_expansions": [(20,), (15,), (30,)]
    },

    # 28. HUMAN EYE: SUNSET RED SCATTERING
    "HUMAN_EYE_SUNSET_RED_SCATTERING": {
        "misc_expansions": [
            "The Sun appears reddish at sunrise and sunset because the atmosphere gets physically heated up and glows red like hot iron.",
            "The red color at sunset is caused by clouds absorbing red light and reflecting it down.",
            "Sun appears red at sunset because red light is scattered the most by dust particles in the evening.",
            "The atmosphere turns red because chemical smoke accumulated during the day tints the Sun red.",
            "At sunset the Sun cools down and emits only red light."
        ],
        "correct_expansions": [
            "At sunrise and sunset, sunlight travels through a much thicker layer of the Earth's atmosphere; shorter blue and violet wavelengths are almost completely scattered away out of the direct beam, leaving predominantly longer red wavelengths to reach our eyes.",
            "Near the horizon, sunlight traverses a greater distance through air; since Rayleigh scattering scatters short wavelengths (blue) 1/lambda^4 times more strongly, blue is scattered away from the sightline, allowing less-scattered red light to pass straight through.",
            "According to NCERT Class 10 Section 11.6.3, red light has the longest visible wavelength and undergoes the least scattering along the extended atmospheric path, giving the Sun its reddish appearance.",
            "The red appearance is not due to red scattering towards us, but rather the preferential scattering AWAY of blue light along the long optical path through the horizon atmosphere."
        ],
        "slip_expansions": [
            "Atmospheric path length is longer by factor of {slip}, scattering blue away.",
            "Correct Rayleigh explanation, but misstated red wavelength as {slip} nm instead of 700 nm."
        ],
        "unit_expansions": [
            "Red light wavelength given as 700 Joules instead of nanometers.",
            "Path length in atmosphere measured in Volts."
        ],
        "unsure_expansions": [
            "why does the Sun look red at sunset but white at noon?",
            "is the sunset red because red is scattered the most or because blue is scattered away?"
        ],
        "stem_expansions": [
            "Explain why the Sun appears reddish early in the morning and late in the evening, but appears white at midday (NCERT Class 10 Chapter 11).",
            "Why do danger signal lights use red color, and how does this relate to the reddish appearance of the Sun at sunset?"
        ],
        "param_expansions": [(700,), (650,), (400,)]
    },

    # 29. HUMAN EYE: ADVANCED SUNRISE / DELAYED SUNSET
    "HUMAN_EYE_ADVANCED_SUNRISE_DELAYED_SUNSET": {
        "misc_expansions": [
            "Advanced sunrise and delayed sunset happen because Earth speeds up its rotation during morning and evening.",
            "We see the Sun 2 minutes before actual sunrise because light travels in a curved path due to gravity.",
            "The 2-minute time difference is caused by the physical tilt of the Earth's equator.",
            "Atmospheric reflection creates a double image of the Sun that appears ahead of time.",
            "The Sun is seen earlier because morning air is colder and reflects light faster."
        ],
        "correct_expansions": [
            "Advanced sunrise (2 minutes early) and delayed sunset (2 minutes late) are caused by atmospheric refraction: rays from the Sun below the horizon pass from rarer space into denser atmosphere, bending continuously downwards toward normal so the Sun appears above the horizon.",
            "Due to atmospheric refraction, the apparent position of the Sun is elevated by about 0.5 degrees above its actual geometric position when near the horizon, lengthening daylight by about 4 minutes total.",
            "According to NCERT Class 10 Section 11.5, light coming from the Sun below the horizon bends downward as it enters increasingly dense air, allowing an observer to see the Sun before it actually crosses the horizon.",
            "Atmospheric refraction bends the optical rays around the curvature of the Earth, shifting the apparent sunrise 2 minutes earlier and sunset 2 minutes later."
        ],
        "slip_expansions": [
            "Refraction advances sunrise by 2 minutes, but calculation slip gave total day lengthening as {slip} minutes instead of 4 minutes.",
            "Angular shift is 0.5 degrees, but arithmetic slip gave {slip} degrees."
        ],
        "unit_expansions": [
            "Time advance is 2 Newtons instead of minutes.",
            "Apparent angular elevation reported in Amperes."
        ],
        "unsure_expansions": [
            "why is the Sun visible about 2 minutes before actual sunrise?",
            "sir does atmospheric refraction lengthen or shorten the apparent duration of the day?"
        ],
        "stem_expansions": [
            "The Sun is visible to us about 2 minutes before actual sunrise and 2 minutes after actual sunset. Explain the physical mechanism responsible for this (NCERT Class 10).",
            "How does atmospheric refraction affect the apparent length of a day on Earth compared to an planet with no atmosphere?"
        ],
        "param_expansions": [(2,), (4,), (0.5,)]
    },

    # 30. ELECTRICITY: VOLTAGE-CURRENT CONFLATION
    "ELECTRICITY_VOLTAGE_CURRENT_CONFLATION": {
        "misc_expansions": [
            "Voltage is the stuff that flows through the wires like water, while current is just the pressure pushing it.",
            "Electric voltage travels down the wire and gets used up by the resistor.",
            "Current and voltage are the exact same thing; 5 Volts means 5 Amperes are flowing.",
            "Voltage flows out of the battery through the positive terminal into the load.",
            "The circuit has a flow of 12 Volts moving through the light bulb."
        ],
        "correct_expansions": [
            "Voltage (potential difference) is the electrical energy per unit charge (V = W/Q in Joules/Coulomb) that drives the motion of charge, whereas current (I = Q/t in Amperes) is the actual rate of flow of electric charge; voltage does not flow, it exists ACROSS points.",
            "Current flows THROUGH a circuit component, while voltage (potential difference) is maintained ACROSS the component; conflating the two confuses the driving potential with the resulting charge flow.",
            "According to NCERT Class 10 Section 12.2, electric potential difference is the work done in moving a unit positive charge between two points, providing the electric pressure that causes current to flow.",
            "Voltage is the electrical pressure difference measured between two points; current is the physical flow rate of electrons caused by that voltage."
        ],
        "slip_expansions": [
            "V = W / Q = {slip} V due to division slip in calculating work per unit charge.",
            "Current I = Q / t calculated with arithmetic slip as {slip} A."
        ],
        "unit_expansions": [
            "Potential difference measured in Amperes instead of Volts.",
            "Current flow measured in Volts instead of Coulombs/second."
        ],
        "unsure_expansions": [
            "does voltage flow through the wire or does current flow through the wire?",
            "sir what is the fundamental difference between Volts and Amperes in a circuit?"
        ],
        "stem_expansions": [
            "A student says: '12 Volts of electricity is flowing through this resistor.' Correct the student's statement using proper NCERT scientific terminology.",
            "Distinguish clearly between electric current and electric potential difference in terms of their physical definitions and SI units (NCERT Class 10)."
        ],
        "param_expansions": [(12,), (24,), (6,)]
    },

    # 31. ELECTRICITY: RESISTIVITY VS RESISTANCE
    "ELECTRICITY_RESISTIVITY_VS_RESISTANCE": {
        "misc_expansions": [
            "Cutting a copper wire into two equal halves halves its electrical resistivity rho to rho/2.",
            "Resistivity depends directly on the length and thickness of the wire, so a longer wire has greater resistivity.",
            "If you double the length of a wire, both its resistance and its resistivity double.",
            "Resistivity of a wire changes whenever its physical dimensions or geometry are altered.",
            "Thin wires have higher resistivity than thick wires made of the same metal."
        ],
        "correct_expansions": [
            "Resistivity (rho) is an intrinsic characteristic property of the material and depends only on the nature of the substance and temperature, NOT on its length or cross-sectional area; cutting the wire in half leaves resistivity rho strictly UNCHANGED.",
            "While resistance R = rho * L / A changes when dimensions change (halving length halves resistance to R/2), resistivity rho is an intensive material property that remains identical for each piece.",
            "According to NCERT Class 10 Section 12.5, resistivity is a characteristic property of the material of the conductor (e.g., copper has rho = 1.62 x 10^-8 ohm-m), completely independent of its shape or size.",
            "Resistance depends on geometry (R proportional to L/A), but resistivity depends only on material composition and temperature; both halves are still copper, so rho is unchanged."
        ],
        "slip_expansions": [
            "Resistivity is unchanged, but new resistance R' = R/2 calculated with arithmetic slip as {slip} ohms.",
            "Identified constant resistivity, but miscalculated new area when stretched."
        ],
        "unit_expansions": [
            "Resistivity is measured in Ohms instead of Ohm-meters (ohm m).",
            "Resistance reported in Ohm-meters."
        ],
        "unsure_expansions": [
            "if we cut a wire in half, does its resistivity change or only its resistance change?",
            "sir what is the difference between resistance and resistivity when a wire is stretched?"
        ],
        "stem_expansions": [
            "A cylindrical copper wire of resistance R and resistivity rho is cut into two equal halves. What are the resistance and resistivity of each half according to NCERT Class 10?",
            "A wire of length L and cross-section A has resistivity rho. If the wire is drawn out to double its length, how does its resistivity change?"
        ],
        "param_expansions": [(10,), (20,), (5,)]
    },

    # 32. ELECTRICITY: SHORT CIRCUIT FALLACY
    "ELECTRICITY_SHORT_CIRCUIT_FALLACY": {
        "misc_expansions": [
            "When a zero-resistance wire is connected in parallel with a bulb, the electric current splits equally between the wire and the bulb.",
            "Current always divides proportionally in parallel, so the bulb will still glow brightly with half the current.",
            "Connecting a bypass wire does not extinguish the bulb; current shares both paths.",
            "Electricity flows equally through all available closed loops regardless of resistance.",
            "The bulb still glows because current from the battery enters both branches."
        ],
        "correct_expansions": [
            "A zero-resistance bypass wire placed in parallel creates a short circuit: because electric current follows the path of minimum resistance (I = V/R, with R_wire ~= 0), virtually 100% of the current bypasses the bulb, extinguishing it completely.",
            "In parallel, branch current is inversely proportional to branch resistance (I1/I2 = R2/R1); with R2 = 0, all current shunts through the shorting wire and zero current flows through the bulb.",
            "According to NCERT Class 10 Section 13.7, a short circuit occurs when a path of zero resistance is provided, causing an extremely high current through the shorting path and zero current through parallel loads.",
            "The equivalent resistance of the parallel combination becomes zero (1/R_eq = 1/R_bulb + 1/0 = infinity => R_eq = 0), so the voltage across the bulb drops to zero, and the bulb turns off."
        ],
        "slip_expansions": [
            "Bulb turns off (I_bulb = 0), but calculated short-circuit surge current with arithmetic slip as {slip} A.",
            "Identified short circuit correctly, but miscalculated fuse rating."
        ],
        "unit_expansions": [
            "Short circuit current is 50 Volts instead of Amperes.",
            "Zero resistance reported as 0 Watts."
        ],
        "unsure_expansions": [
            "does a bulb stay on or turn off when a plain wire is connected across its terminals?",
            "sir why does current prefer the zero-resistance path completely in a short circuit?"
        ],
        "stem_expansions": [
            "A bulb glowing in a circuit is suddenly bypassed by connecting a thick copper wire of negligible resistance across its two terminals. What happens to the bulb and the circuit current?",
            "Explain the physical and electrical consequences of a short circuit across a load in terms of Ohm's law and current distribution (NCERT Class 10)."
        ],
        "param_expansions": [(12,), (24,), (6,)]
    },

    # 33. MAGNETIC EFFECTS: UNIVERSAL METALLIC MAGNETISM
    "MAGNETIC_EFFECTS_UNIVERSAL_METALLIC_MAGNETISM": {
        "misc_expansions": [
            "All metals like aluminium, copper, silver, and gold are strongly attracted to permanent bar magnets because all metals are magnetic.",
            "Since copper and aluminium conduct electricity, they are magnetic and stick firmly to a magnet.",
            "Every metallic object in daily life will be picked up by a powerful electromagnet.",
            "Aluminium foil is pulled towards a magnet just like iron.",
            "All good conductors of electricity are ferromagnetic and strongly attracted by magnets."
        ],
        "correct_expansions": [
            "Only ferromagnetic materials (principally iron, nickel, cobalt, and their alloys like steel) are strongly attracted to permanent magnets; common metals like copper, aluminium, brass, gold, and silver are non-magnetic.",
            "Electrical conductivity and ferromagnetism are distinct physical phenomena: aluminium and copper are excellent electrical conductors but are non-magnetic and experience no noticeable attraction to a bar magnet.",
            "According to NCERT Class 10 Chapter 13, magnetic attraction is selective to ferromagnetic substances; a magnet does not attract aluminium cans or copper wires.",
            "Ferromagnetism requires unpaired electron spins aligned in magnetic domains, which exist in iron and nickel but do not exist in copper or aluminium."
        ],
        "slip_expansions": [
            "Aluminium is non-magnetic, but calculated magnetic force on moving aluminium plate as {slip} N due to eddy current formula slip.",
            "Identified iron as magnetic, but misquoted Curie temperature with arithmetic slip."
        ],
        "unit_expansions": [
            "Magnetic susceptibility of aluminium reported in Newtons.",
            "Magnetic attraction force measured in Joules."
        ],
        "unsure_expansions": [
            "are all metals attracted to magnets, or only iron and steel?",
            "sir why doesn't an aluminium soda can stick to a strong bar magnet?"
        ],
        "stem_expansions": [
            "A student brings a strong neodymium bar magnet near a copper coin and an aluminium rod. What magnetic attraction will be observed according to NCERT Class 10?",
            "Explain why electrical conductors like copper and aluminium are not attracted by ordinary permanent magnets."
        ],
        "param_expansions": [(1,), (2,), (5,)]
    },

    # 34. MAGNETIC EFFECTS: FORCE COLLINEAR
    "MAGNETIC_EFFECTS_FORCE_COLLINEAR": {
        "misc_expansions": [
            "A current-carrying wire placed in a magnetic field experiences a force that pulls it directly along the direction of the magnetic field lines.",
            "The magnetic force on an electric current always points towards the magnetic north or south pole.",
            "Magnetic force is collinear with the magnetic field lines, pushing the wire parallel to the field.",
            "Current is attracted along the field lines just like electric charges are pulled along electric field lines.",
            "The conductor moves in the direction of the magnetic field vector B."
        ],
        "correct_expansions": [
            "The magnetic force on a current-carrying conductor is strictly PERPENDICULAR to both the magnetic field lines and the direction of current flow (F = I(L x B)), given by Fleming's Left-Hand Rule; it never acts parallel or collinear to the field lines.",
            "Unlike electrostatic force (which acts parallel to electric field lines), magnetic Lorentz force is a cross-product force that acts at right angles (90 degrees) to both field B and current I.",
            "According to NCERT Class 10 Section 13.4, when a conductor carrying current is placed perpendicular to a magnetic field, the resulting force is mutually perpendicular to both, causing sideways displacement.",
            "If current is parallel to field lines, magnetic force is zero (sin(0) = 0); when perpendicular, force is maximum and acts orthogonal to the plane containing current and field."
        ],
        "slip_expansions": [
            "Force is perpendicular (F = I*L*B*sin(90)), but calculated magnitude as {slip} N due to multiplication error.",
            "Correct perpendicular direction, but slipped on sine value in non-90 angle."
        ],
        "unit_expansions": [
            "Magnetic force on conductor is 2.5 Tesla instead of Newtons.",
            "Force vector magnitude reported in Amperes."
        ],
        "unsure_expansions": [
            "is the magnetic force on a wire directed along the magnetic field lines or perpendicular to them?",
            "sir why does magnetic force act at 90 degrees instead of pulling along the field lines?"
        ],
        "stem_expansions": [
            "A wire carrying current towards the North is placed in a horizontal magnetic field directed towards the East. In what direction does the magnetic force act (NCERT Class 10)?",
            "Contrast the direction of electrostatic force on a charge in an electric field with the direction of magnetic force on a moving charge in a magnetic field."
        ],
        "param_expansions": [(90,), (45,), (60,)]
    },

    # 35. MOTION: DISTANCE VS DISPLACEMENT
    "MOTION_DISTANCE_VS_DISPLACEMENT": {
        "misc_expansions": [
            "Distance and displacement are identical physical quantities; if an athlete runs one complete 400 m circular lap, their displacement is 400 meters.",
            "Displacement cannot be zero if the runner ran a long distance and feels tired.",
            "Since the total path length is 400 m, the displacement must also be 400 m.",
            "Displacement equals the odometer reading of distance traveled.",
            "Completing a full round trip of 400 m produces a displacement of 400 m."
        ],
        "correct_expansions": [
            "Distance is the actual total path length traveled (a scalar, 400 m), whereas displacement is the shortest straight-line vector distance from initial to final position; returning to the starting point means displacement is strictly ZERO.",
            "According to NCERT Class 9 Section 8.1, displacement can be zero even when distance traveled is non-zero, whenever the initial and final positions of the moving object coincide.",
            "Distance is a scalar quantity that is always positive or zero; displacement is a vector quantity that is zero for any completed closed loop.",
            "For a complete circular lap: initial position = final position, therefore delta x = x_final - x_initial = 0 meters, while distance traveled equals circumference (400 m)."
        ],
        "slip_expansions": [
            "Displacement is zero, but calculated average speed = distance/time with arithmetic slip as {slip} m/s.",
            "Displacement = 0 m, but calculated track radius as {slip} m due to pi division error."
        ],
        "unit_expansions": [
            "Displacement is 0 Joules instead of meters.",
            "Distance reported with units of m/s."
        ],
        "unsure_expansions": [
            "can displacement be zero when a runner covers 400 meters around a circular track?",
            "sir what is the difference between distance and displacement for a round trip?"
        ],
        "stem_expansions": [
            "An athlete completes one round of a circular track of diameter 200 m in 40 seconds. What will be the distance covered and the displacement at the end of 40 seconds (NCERT Class 9)?",
            "Explain why the magnitude of displacement can be equal to or less than distance, but can never exceed distance."
        ],
        "param_expansions": [(400,), (200,), (800,)]
    },

    # 36. MOTION: NEGATIVE ACCELERATION DECELERATION
    "MOTION_NEGATIVE_ACCELERATION_DECELERATION": {
        "misc_expansions": [
            "Negative acceleration always means that an object is slowing down (decelerating), without exception.",
            "A negative value of acceleration (-a) cannot describe an object that is speeding up.",
            "Whenever acceleration is negative, speed must decrease.",
            "Negative acceleration and deceleration are exact synonyms under all circumstances.",
            "If an object has a = -5 m/s^2, it is impossible for its speed to increase."
        ],
        "correct_expansions": [
            "Negative acceleration does NOT always mean deceleration; whether an object speeds up or slows down depends on the relative directions of velocity and acceleration: if both velocity and acceleration are negative (pointing in the -x direction), the object SPEEDS UP in the negative direction.",
            "According to NCERT Class 9 Chapter 8, acceleration is a vector defined by chosen coordinate signs: negative acceleration means acceleration directed in the -x direction; it only causes deceleration if velocity is in the +x direction.",
            "An object dropped from rest downward (taking upward as +x) has negative velocity and negative acceleration (a = -g), yet its speed INCREASES rapidly downward.",
            "Deceleration occurs when velocity and acceleration have OPPOSITE signs; when they share the SAME sign (both negative), the object accelerates and speeds up."
        ],
        "slip_expansions": [
            "Object speeds up in -x direction, but calculated final velocity v = u + at as -{slip} m/s due to addition slip.",
            "Correct sign analysis, but arithmetic slip in speed magnitude."
        ],
        "unit_expansions": [
            "Negative acceleration is -5 m/s instead of m/s^2.",
            "Deceleration reported in Newtons."
        ],
        "unsure_expansions": [
            "does negative acceleration always mean the body is slowing down, or can it speed up?",
            "sir can an object speed up with negative acceleration?"
        ],
        "stem_expansions": [
            "A car moving in the negative x-direction has an acceleration of -3 m/s^2. Is the car speeding up or slowing down? Explain using NCERT Class 9 concepts.",
            "Give an authentic physical example where an object has negative acceleration yet its speed is continuously increasing."
        ],
        "param_expansions": [(3,), (5,), (2,)]
    },

    # 37. MOTION: AVERAGE SPEED ARITHMETIC MEAN
    "MOTION_AVERAGE_SPEED_ARITHMETIC_MEAN": {
        "misc_expansions": [
            "If a car travels from A to B at 60 km/h and returns at 40 km/h, the average speed for the round trip is simply the arithmetic mean: (60 + 40) / 2 = 50 km/h.",
            "Average speed is calculated by adding the two speeds and dividing by two: v_avg = (v1 + v2) / 2 = 50 km/h.",
            "The average speed for equal distances is the simple average of the speeds.",
            "v_avg = (60 + 40) / 2 = 50 km/h because both speeds are equally weighted.",
            "Since one trip was 60 and the other was 40, the middle value 50 km/h is the true average speed."
        ],
        "correct_expansions": [
            "Average speed is defined as TOTAL distance divided by TOTAL time (v_avg = 2d / (t1 + t2)), which gives the harmonic mean 2*v1*v2 / (v1 + v2) = 2*60*40 / (60 + 40) = 48 km/h, NOT the simple arithmetic average of 50 km/h.",
            "Because the car travels slower on the return trip (40 km/h), it spends MORE TIME at the lower speed; therefore average speed is time-weighted toward the slower speed, resulting in 48 km/h.",
            "According to NCERT Class 9 Example 8.2, average speed = total distance / total time; with t1 = d/60 and t2 = d/40, v_avg = 2d / (d/60 + d/40) = 48 km/h.",
            "The simple arithmetic mean (v1 + v2)/2 only applies if the object traveled for equal INTERVALS OF TIME, not for equal distances."
        ],
        "slip_expansions": [
            "v_avg = 2*v1*v2 / (v1+v2) = 4800 / 100, but arithmetic slip gave {slip} km/h.",
            "Calculated total time with fraction addition slip, getting {slip} hours."
        ],
        "unit_expansions": [
            "Average speed is 48 km instead of km/h.",
            "Average speed reported in m/s^2."
        ],
        "unsure_expansions": [
            "is average speed for a round trip (v1 + v2)/2 or total distance divided by total time?",
            "sir why is the average speed 48 km/h instead of 50 km/h for equal distances?"
        ],
        "stem_expansions": [
            "An automobile travels from town X to town Y at an average speed of 60 km/h and returns along the same route at 40 km/h. Calculate the average speed for the entire round trip (NCERT Class 9).",
            "Why is average speed for equal distances different from the simple arithmetic average of the two speeds?"
        ],
        "param_expansions": [(60, 40), (30, 20), (75, 50)]
    },

    # 38. FORCE: MASS VS WEIGHT
    "FORCE_MASS_VS_WEIGHT": {
        "misc_expansions": [
            "An astronaut on the Moon has less mass than on Earth because the Moon's gravity is only 1/6th of Earth's gravity.",
            "Mass decreases when you go to outer space or the Moon where there is less gravity.",
            "Mass and weight are the exact same thing, both measured in kilograms.",
            "A person weighing 60 kg on Earth will have a mass of only 10 kg on the Moon.",
            "Your body loses mass in zero gravity because gravity is what creates mass."
        ],
        "correct_expansions": [
            "Mass is the fundamental measure of the amount of matter in a body (and its inertia), which remains strictly CONSTANT everywhere in the universe (a 60 kg person has mass 60 kg on Earth, Moon, and deep space); WEIGHT is the gravitational force (W = m*g) which decreases to 1/6th on the Moon because g_moon = g_earth / 6.",
            "According to NCERT Class 9 Section 10.4, mass is an intrinsic scalar property measured in kg that never changes with location, whereas weight is a force measured in Newtons (W = mg) that varies with local gravitational field g.",
            "On the Moon: mass m = 60 kg (unchanged), but weight W = m * g_moon = 60 * 1.63 = 98 N (one-sixth of Earth weight 588 N).",
            "Mass does not depend on gravity; only weight changes when gravitational acceleration changes."
        ],
        "slip_expansions": [
            "Mass is constant (60 kg), but calculated lunar weight W = 60 * 1.63 as {slip} N due to multiplication slip.",
            "Weight on Moon is 1/6th of 600 N, but calculated as {slip} N due to division slip."
        ],
        "unit_expansions": [
            "Weight on the Moon is 98 kg instead of Newtons.",
            "Mass measured in Newtons instead of kilograms."
        ],
        "unsure_expansions": [
            "does mass change on the Moon or does only weight change?",
            "sir what is the exact difference between mass in kg and weight in Newtons?"
        ],
        "stem_expansions": [
            "An object has a mass of 60 kg on Earth. What will be its mass and weight on the surface of the Moon where g_moon = 1/6 * g_earth (NCERT Class 9)?",
            "Explain why mass is an invariant scalar property while weight varies from place to place across celestial bodies."
        ],
        "param_expansions": [(60,), (42,), (90,)]
    },

    # 39. GRAVITATION: INVERSE SQUARE FALLACY
    "GRAVITATION_INVERSE_SQUARE_FALLACY": {
        "misc_expansions": [
            "If the distance between two masses is doubled from r to 2r, the gravitational force between them is halved to F/2.",
            "Gravitational force is inversely proportional to distance r, so doubling distance divides force by two.",
            "F' = F / 2 = 50 N because distance is doubled.",
            "Gravity weakens linearly with distance: twice the distance means half the gravitational pull.",
            "The force decreases by a factor of 2 when separation increases from r to 2r."
        ],
        "correct_expansions": [
            "According to Newton's Universal Law of Gravitation (F = G*m1*m2 / r^2), gravitational force is inversely proportional to the SQUARE of the distance; doubling distance (r' = 2r) reduces the force to ONE-FOURTH (F' = F / 2^2 = F / 4 = 25 N).",
            "By NCERT Class 9 Section 10.1, the inverse-square law dictates that increasing distance by factor k decreases force by factor k^2; doubling distance reduces force by factor 4, not factor 2.",
            "F_new = G*m1*m2 / (2r)^2 = (1/4) * (G*m1*m2 / r^2) = F / 4 = 25 N.",
            "The geometric spreading of gravitational flux follows an inverse-square relationship; doubling the separation quarter the gravitational attraction."
        ],
        "slip_expansions": [
            "F' = F / 4 = 100 / 4, but calculated with division slip as {slip} N.",
            "Tripled distance reduces force by 9, but calculated {slip} N instead of 11.1 N."
        ],
        "unit_expansions": [
            "Gravitational force is 25 Joules instead of Newtons.",
            "Universal gravitational constant G reported in Newtons."
        ],
        "unsure_expansions": [
            "if distance between two planets is doubled, does gravity become half or one-fourth?",
            "sir why does gravity follow inverse square law instead of inverse linear law?"
        ],
        "stem_expansions": [
            "The gravitational force between two point masses separated by distance r is 100 N. If the distance between them is doubled to 2r, what is the new gravitational force (NCERT Class 9)?",
            "State Newton's Universal Law of Gravitation and explain what happens to the attraction when separation is tripled."
        ],
        "param_expansions": [(100,), (200,), (80,)]
    },

    # 40. ENERGY: KINETIC VELOCITY LINEARITY
    "ENERGY_KINETIC_VELOCITY_LINEARITY": {
        "misc_expansions": [
            "If the speed of a vehicle is doubled from v to 2v, its kinetic energy simply doubles (KE' = 2*KE).",
            "Kinetic energy is directly proportional to speed, so twice the speed means twice the kinetic energy.",
            "Doubling speed from 10 m/s to 20 m/s doubles the kinetic energy from 1000 J to 2000 J.",
            "KE increases linearly with velocity according to common intuition.",
            "Speed is multiplied by 2, so energy is multiplied by 2."
        ],
        "correct_expansions": [
            "Kinetic energy is proportional to the SQUARE of velocity (KE = (1/2)*m*v^2); doubling velocity (v' = 2v) increases kinetic energy by a factor of FOUR (KE' = (1/2)*m*(2v)^2 = 4 * KE).",
            "According to NCERT Class 9 Section 11.2.2, kinetic energy depends on v^2; doubling speed quadruples kinetic energy and quadruples the braking distance required to stop.",
            "KE_final = (1/2) * m * (2v)^2 = 4 * ((1/2) * m * v^2) = 4 * KE_initial, proving a fourfold increase.",
            "Because work done to accelerate a body from rest is integral of F*dx = (1/2)*m*v^2, kinetic energy grows with the square of speed, not linearly."
        ],
        "slip_expansions": [
            "KE quadruples (KE' = 4*KE), but calculated 4 * 1000 J as {slip} J due to multiplication slip.",
            "Calculated KE = 0.5 * m * v^2 with squaring slip, getting {slip} Joules."
        ],
        "unit_expansions": [
            "Kinetic energy is 4000 Watts instead of Joules.",
            "Kinetic energy reported in Newtons."
        ],
        "unsure_expansions": [
            "does doubling a car's speed double its kinetic energy or quadruple it?",
            "sir why does kinetic energy depend on velocity squared instead of velocity?"
        ],
        "stem_expansions": [
            "A car of mass 1000 kg moves with a speed of 10 m/s. If its speed is doubled to 20 m/s, by what factor does its kinetic energy increase (NCERT Class 9)?",
            "Explain why the braking distance of a vehicle quadruples when its speed is doubled in terms of the work-energy theorem."
        ],
        "param_expansions": [(1000, 10), (500, 15), (800, 20)]
    },

    # 41. WORK ENERGY: ZERO WORK IN CIRCULAR ORBIT
    "WORK_ENERGY_ZERO_WORK_CIRCULAR_ORBIT": {
        "misc_expansions": [
            "Earth's gravity does continuous positive work on a satellite orbiting in a circular path because gravity is constantly pulling it.",
            "Since the satellite is moving fast around Earth under gravitational pull, work done by gravity is positive and very large.",
            "Work done by gravity in one complete circular orbit equals force times the orbital circumference (W = F * 2*pi*r).",
            "Gravity keeps the satellite in orbit, so it must do mechanical work to keep it moving.",
            "Gravity does work because the satellite covers millions of kilometers in its circular trajectory."
        ],
        "correct_expansions": [
            "The gravitational force acts radially inward toward Earth's center, which is strictly perpendicular (theta = 90 degrees) to the satellite's tangential displacement at every instant; therefore cos(90) = 0, and the work done by gravity is strictly ZERO (W = 0 Joules).",
            "According to NCERT Class 9 Section 11.1, when the force acting on an object is perpendicular to its direction of motion, zero work is done (W = F * s * cos(90) = 0); the satellite's speed and orbital kinetic energy remain constant.",
            "In circular orbit, gravitational force serves purely as a centripetal force perpendicular to velocity; centripetal forces do zero work on moving objects.",
            "Because work done by gravity is zero, no energy is added or removed, allowing natural satellites and moons to orbit indefinitely without consuming fuel."
        ],
        "slip_expansions": [
            "Work is zero (W = 0 J), but calculated orbital speed v = sqrt(GM/r) with arithmetic slip as {slip} m/s.",
            "Centripetal force does zero work, but miscalculated orbital period."
        ],
        "unit_expansions": [
            "Work done by gravity is 0 Watts instead of Joules.",
            "Centripetal force measured in Joules instead of Newtons."
        ],
        "unsure_expansions": [
            "does gravity do work on a satellite moving in a circular orbit around the Earth?",
            "sir why is the work done by centripetal force zero in circular motion?"
        ],
        "stem_expansions": [
            "A satellite of mass m revolves around Earth in a circular orbit of radius r under the influence of gravitational force F. Calculate the work done by gravity in one full revolution (NCERT Class 9).",
            "Explain why the work done by Earth's gravity on a satellite in a circular orbit is zero, using the scientific definition of work."
        ],
        "param_expansions": [(1000, 7000), (500, 8000), (2000, 6500)]
    }
}
