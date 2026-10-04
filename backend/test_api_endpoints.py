import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_all_endpoints():
    print("=" * 60)
    print("RUNNING RE:LEARN FULL-STACK BACKEND ENDPOINT INTEGRATION TESTS")
    print("=" * 60)

    # 1. Health
    res = client.get("/api/health")
    assert res.status_code == 200, f"Health check failed: {res.text}"
    health = res.json()
    print(f"[1/9] Health Check: PASS (Device: {health['model_a_device']}, Baseline: {health['model_a_baseline_loaded']})")

    # 2. Topics
    res = client.get("/api/topics")
    assert res.status_code == 200
    topics = res.json()["topics"]
    assert len(topics) >= 4
    print(f"[2/9] Topics: PASS ({len(topics)} chapters loaded)")

    # 3. Diagnose (Model A)
    q_text = "A student forms a sharp image of a lighted candle on a screen using a convex lens of focal length 15 cm. The lower half of the lens is covered with black paper. What happens to the image on the screen?"
    student_ans = "The top half of the candle image is completely missing because the bottom half is blocked."
    res = client.post("/api/diagnose", json={
        "question_id": "DIAG-OPT-001",
        "question_text": q_text,
        "student_response": student_ans,
        "topic": "Optics"
    })
    assert res.status_code == 200
    diag = res.json()
    assert "MISC-OPT-001" in diag["label"] or diag["category"] == "misconception"
    print(f"[3/9] Diagnose Model A: PASS -> {diag['label']} (Confidence: {diag['confidence']:.2f})")

    # 3b. Abstention check on vague response
    res_abstain = client.post("/api/diagnose", json={
        "question_id": "DIAG-OPT-001",
        "question_text": q_text,
        "student_response": "idk forgot formula skip please",
        "topic": "Optics"
    })
    diag_abstain = res_abstain.json()
    assert diag_abstain["label"] == "UNSURE_INSUFFICIENT_EVIDENCE"
    print(f"[3b/9] Model A Abstention Check: PASS -> {diag_abstain['label']} ({diag_abstain['suggested_action']})")

    # 4. Sequence Pattern (Model B)
    seq_payload = {
        "sequence_id": "SESSION-TEST-01",
        "student_id": "STU-TEST",
        "topic": "Electricity",
        "ordered_attempts": [
            {
                "step": 1,
                "question_id": "DIAG-ELEC-001",
                "question_stem": "Two identical bulbs in series with 6V battery.",
                "student_response": "Bulb 1 uses up current so bulb 2 is dimmer",
                "individual_diagnosis": "MISC-ELEC-001: Current Attenuation",
                "confidence": 0.95
            },
            {
                "step": 2,
                "question_id": "DIAG-ELEC-002",
                "question_stem": "Three resistors in series.",
                "student_response": "Current drops sequentially after each resistor",
                "individual_diagnosis": "MISC-ELEC-001: Current Attenuation",
                "confidence": 0.96
            }
        ]
    }
    res = client.post("/api/sequence-pattern", json=seq_payload)
    assert res.status_code == 200
    seq = res.json()
    print(f"[4/9] Sequence Analyzer Model B: PASS -> {seq['predicted_pattern']} ({seq['status']})")

    # 5. Intervention
    res = client.get("/api/intervention/MISC-OPT-001")
    assert res.status_code == 200
    intv = res.json()
    assert "whiteboard_commands" in intv
    print(f"[5/9] Intervention POE: PASS -> {intv['misconception_name']} ({len(intv['whiteboard_commands'])} whiteboard commands)")

    # 6. Reassessment Item
    res = client.get("/api/reassessment/MISC-OPT-001")
    assert res.status_code == 200
    reassess = res.json()
    assert "post_intervention_reassessment_item" in reassess
    print(f"[6/9] Reassessment Item: PASS -> {reassess['pair_id']}")

    # 7. Evaluate Reassessment with BKT
    res = client.post("/api/evaluate-reassessment", json={
        "misc_id": "MISC-OPT-001",
        "question_id": "REASSESS-OPT-001",
        "student_selection_key": "B",
        "correct_key": "B",
        "prior_mastery": 0.15
    })
    assert res.status_code == 200
    eval_res = res.json()
    assert eval_res["verdict"] == "RESOLVED_WITH_TRANSFER"
    assert eval_res["bkt_update"]["posterior_mastery"] > 0.60
    assert eval_res["bkt_update"]["delta"] > 0
    print(f"[7/9] Reassessment BKT Evaluation: PASS -> {eval_res['verdict']} (Mastery: {eval_res['bkt_update']['prior_mastery']} -> {eval_res['bkt_update']['posterior_mastery']})")

    # 8. Analytics
    res = client.get("/api/analytics")
    assert res.status_code == 200
    analytics = res.json()
    assert analytics["dataset_summary"]["total_individual_responses"] == 21000
    assert analytics["dataset_summary"]["total_longitudinal_sequences"] == 2700
    print(f"[8/9] Analytics: PASS (21,000 responses, 2,700 sequences, 42 families)")

    # 9. Taxonomy
    res = client.get("/api/taxonomy")
    assert res.status_code == 200
    tax = res.json()
    assert len(tax["misconceptions_index"]) == 21
    print(f"[9/9] Taxonomy: PASS (21 NCERT codified misconceptions)")

    # 10. 3D Character Speech & Visemes Synthesis
    res = client.post("/api/character/speak", json={
        "misconception_id": "MISC-OPT-001"
    })
    assert res.status_code == 200
    spk = res.json()
    assert "text" in spk
    assert "visemes" in spk
    print(f"[10/10] 3D Character Speak Endpoint: PASS -> Text length: {len(spk['text'])}, Audio output present: {spk['audio_base64'] is not None}")

    print("=" * 60)
    print("ALL 10 BACKEND ENDPOINT INTEGRATION TESTS SUCCEEDED WITH ZERO FAILURES!")
    print("=" * 60)

if __name__ == "__main__":
    test_all_endpoints()
