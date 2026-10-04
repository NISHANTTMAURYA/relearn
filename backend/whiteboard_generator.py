"""
Dynamic Whiteboard Plan Generator for Re:Learn
Generates structured vector drawing commands and speech narration for any physics misconception.
Follows the structured Drawing DSL specified in docs/RELEARN_TECHNICAL_PROJECT_DOCUMENTATION.md.
"""

from typing import Dict, List, Any

def generate_dynamic_whiteboard_plan(
    concept: str,
    question_stem: str,
    student_response: str,
    misconception_label: str
) -> Dict[str, Any]:
    concept_lower = (concept + " " + question_stem + " " + misconception_label).lower()

    # 1. OPTICS: HALF-LENS & APERTURE
    if "lens" in concept_lower or "mirror" in concept_lower or "opt" in misconception_label.lower() or "light" in concept_lower:
        return {
            "board_title": "Geometric Optics: Aperture Transmission vs. Image Geometry",
            "concept_domain": "Ray Optics",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Optical Axis & Apparatus Setup",
                    "narration": "Let's first set up our principal optical axis, the convex lens of focal length f, and the illuminated candle object placed at distance u.",
                    "board_instruction": "draw_axis(from=[30, 150], to=[570, 150]); draw_lens(type='convex', x=300, y=150, f=15); draw_object(x=90, y=80)",
                    "actions": [
                        {"tool": "line", "x1": 30, "y1": 150, "x2": 570, "y2": 150, "stroke": "#94A3B8", "width": 1.5, "dash": "4 4"},
                        {"tool": "lens", "x": 300, "y": 150, "rx": 14, "ry": 95, "type": "convex", "stroke": "#0284C7", "fill": "#F0F9FF"},
                        {"tool": "text", "x": 280, "y": 265, "text": "Convex Lens", "color": "#0369A1", "weight": "bold"},
                        {"tool": "candle", "x": 90, "y": 80, "height": 70, "label": "Candle Object"},
                        {"tool": "screen", "x": 510, "y": 45, "height": 210, "label": "Viewing Screen"}
                    ]
                },
                {
                    "step_number": 2,
                    "title": "Tracing Real Ray Cones",
                    "narration": "Notice that the candle tip emits infinite light rays in all directions. Ray 1 travels parallel to the axis and refracts through focus F. Ray 2 travels straight through the optical center.",
                    "board_instruction": "draw_ray(from=[90, 80], to=[300, 80], refract_to=[510, 220], color='#D97706'); draw_ray(from=[90, 80], to=[300, 150], refract_to=[510, 220], color='#2563EB')",
                    "actions": [
                        {"tool": "ray", "x1": 90, "y1": 80, "x2": 300, "y2": 80, "x3": 510, "y3": 220, "stroke": "#D97706", "width": 2, "label": "Ray 1 (Parallel)"},
                        {"tool": "ray", "x1": 90, "y1": 80, "x2": 300, "y2": 150, "x3": 510, "y3": 220, "stroke": "#2563EB", "width": 2, "label": "Ray 2 (Center)"},
                        {"tool": "ray", "x1": 90, "y1": 80, "x2": 300, "y2": 120, "x3": 510, "y3": 220, "stroke": "#10B981", "width": 1.5, "dash": "2 2", "label": "Ray 3 (General)"},
                        {"tool": "point", "cx": 510, "cy": 220, "r": 4, "fill": "#DC2626"}
                    ]
                },
                {
                    "step_number": 3,
                    "title": "Applying Experimental Constraint (Opaque Mask)",
                    "narration": "Now we wrap black paper around the lower half. Rays hitting the bottom are blocked. But look at the top half: rays from every point of the candle still pass through!",
                    "board_instruction": "draw_mask(x=286, y=150, width=28, height=95, color='#1E293B'); highlight('Upper Aperture Exposed')",
                    "actions": [
                        {"tool": "mask", "x": 286, "y": 150, "width": 28, "height": 95, "fill": "#1E293B", "label": "Opaque Black Paper"},
                        {"tool": "callout", "x": 220, "y": 40, "width": 220, "height": 38, "fill": "#FEF3C7", "stroke": "#D97706", "title": "Aperture Masked: 50% Area Blocked"}
                    ]
                },
                {
                    "step_number": 4,
                    "title": "Counter-Intuitive Scientific Resolution",
                    "narration": "Because every point on the lens receives light from all parts of the object, the full image is still formed on the screen! The only physical change is a 50% reduction in image brightness.",
                    "board_instruction": "draw_inverted_image(x=510, y=150, height=70, opacity=0.5); write_formula('Image Shape = 100% INTACT | Brightness = 50%')",
                    "actions": [
                        {"tool": "inverted_candle", "x": 510, "y": 150, "height": 70, "opacity": 0.6},
                        {"tool": "callout", "x": 330, "y": 45, "width": 250, "height": 55, "fill": "#ECFDF5", "stroke": "#059669", "title": "✓ FULL IMAGE REMAINS INTACT", "subtitle": "Intensity drops to 50%; picture is NOT cut."}
                    ]
                }
            ]
        }

    # 2. ELECTRICITY: CURRENT CONSERVATION & OHM'S LAW
    elif "circuit" in concept_lower or "electric" in concept_lower or "current" in concept_lower or "bulb" in concept_lower:
        return {
            "board_title": "Current Electricity: Conservation of Electric Charge in Closed Loops",
            "concept_domain": "Circuit Dynamics",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Closed Series Circuit Setup",
                    "narration": "Let's construct a series circuit loop with a 6-Volt battery, two identical light bulbs, and ammeters to monitor charge flow.",
                    "board_instruction": "draw_circuit_loop(x=80, y=50, w=440, h=180); draw_battery(6V); place_bulbs([B1, B2])",
                    "actions": [
                        {"tool": "wire_loop", "x": 80, "y": 50, "width": 440, "height": 180, "stroke": "#334155", "width_px": 3.5},
                        {"tool": "battery", "x": 80, "y": 140, "label": "6V Battery"},
                        {"tool": "bulb", "x": 300, "y": 50, "label": "Bulb 1"},
                        {"tool": "bulb", "x": 520, "y": 140, "label": "Bulb 2"}
                    ]
                },
                {
                    "step_number": 2,
                    "title": "Installing Ammeters A1 and A2",
                    "narration": "We insert Ammeter A1 before Bulb 1, and Ammeter A2 directly between Bulb 1 and Bulb 2 to measure current in amperes.",
                    "board_instruction": "place_ammeter(A1, x=200, y=50); place_ammeter(A2, x=400, y=50); place_ammeter(A3, x=300, y=230)",
                    "actions": [
                        {"tool": "ammeter", "x": 200, "y": 50, "name": "A₁", "val": "0.90 A"},
                        {"tool": "ammeter", "x": 400, "y": 50, "name": "A₂", "val": "0.90 A"},
                        {"tool": "ammeter", "x": 300, "y": 230, "name": "A₃", "val": "0.90 A"}
                    ]
                },
                {
                    "step_number": 3,
                    "title": "Visualizing Mobile Electron Flow",
                    "narration": "Electric current is the continuous rate of charge flow: I equals Q divided by t. Charges are not eaten or depleted by resistors.",
                    "board_instruction": "draw_charge_carriers(direction='counter_clockwise'); write_equation('I = Q / t')",
                    "actions": [
                        {"tool": "electrons", "count": 12, "color": "#3B82F6"},
                        {"tool": "formula", "x": 220, "y": 115, "text": "I = Q / t = Rate of Flow of Charge"}
                    ]
                },
                {
                    "step_number": 4,
                    "title": "Charge Conservation Reconciled",
                    "narration": "Both ammeters read identical values (0.90 A). Bulbs convert electrical potential energy into heat and light, but every electron entering Bulb 1 exits to Bulb 2.",
                    "board_instruction": "highlight('A1 = A2 = 0.90A'); callout('Current is CONSERVED, not consumed!')",
                    "actions": [
                        {"tool": "callout", "x": 160, "y": 105, "width": 280, "height": 55, "fill": "#ECFDF5", "stroke": "#059669", "title": "✓ CHARGE CONSERVATION: I₁ = I₂ = 0.90 A", "subtitle": "Current is never consumed or depleted."}
                    ]
                }
            ]
        }

    # 3. MECHANICS & GRAVITATION
    else:
        return {
            "board_title": "Kinematics & Gravitation: Mass-Independent Acceleration",
            "concept_domain": "Mechanics",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Free Fall Tower & Initial State",
                    "narration": "Consider dropping a 10 kg iron ball and a 1 kg wooden ball simultaneously from a 20-meter tower in vacuum.",
                    "board_instruction": "draw_tower(height=20); draw_mass(10kg, x=180); draw_mass(1kg, x=320)",
                    "actions": [
                        {"tool": "line", "x1": 80, "y1": 40, "x2": 80, "y2": 240, "stroke": "#64748B", "width": 3},
                        {"tool": "line", "x1": 60, "y1": 240, "x2": 520, "y2": 240, "stroke": "#334155", "width": 4},
                        {"tool": "mass", "x": 180, "y": 50, "r": 18, "label": "10 kg", "color": "#334155"},
                        {"tool": "mass", "x": 320, "y": 50, "r": 10, "label": "1 kg", "color": "#F59E0B"}
                    ]
                },
                {
                    "step_number": 2,
                    "title": "Newton's Second Law & Gravitational Force",
                    "narration": "Earth attracts the 10 kg ball with 10 times more gravitational force: F equals m times g. That is why students think it falls faster!",
                    "board_instruction": "draw_vector(F1=98N, mass=10kg); draw_vector(F2=9.8N, mass=1kg)",
                    "actions": [
                        {"tool": "vector", "x": 180, "y": 70, "dy": 60, "label": "F = 98 N", "color": "#DC2626"},
                        {"tool": "vector", "x": 320, "y": 62, "dy": 25, "label": "F = 9.8 N", "color": "#DC2626"}
                    ]
                },
                {
                    "step_number": 3,
                    "title": "Mass Cancellation in Acceleration",
                    "narration": "However, Newton's second law also states that inertia opposes acceleration: a equals F divided by m. Notice that mass m cancels out completely!",
                    "board_instruction": "write_equation('a = F / m = (m * g) / m = g'); highlight('Mass cancels out')",
                    "actions": [
                        {"tool": "formula", "x": 150, "y": 140, "text": "a = F / m = (m · g) / m = g = 9.8 m/s²"}
                    ]
                },
                {
                    "step_number": 4,
                    "title": "Simultaneous Touchdown",
                    "narration": "Because acceleration is identical for both objects regardless of mass, both spheres hit the ground at the exact same instant!",
                    "board_instruction": "touchdown(both_masses_at_ground); callout('Both hit ground simultaneously!')",
                    "actions": [
                        {"tool": "callout", "x": 140, "y": 80, "width": 320, "height": 55, "fill": "#ECFDF5", "stroke": "#059669", "title": "✓ SIMULTANEOUS IMPACT: t = √(2h/g)", "subtitle": "Acceleration is independent of falling mass."}
                    ]
                }
            ]
        }
