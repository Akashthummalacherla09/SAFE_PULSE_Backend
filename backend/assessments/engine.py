class AssessmentEngine:
    # --- DAILY TRACKER STANDARDS ---
    GOAL_WATER = 2.5
    GOAL_STEPS = 8000
    GOAL_SLEEP = 7.5
    GOAL_CALORIES = 2500

    @staticmethod
    def calculate_daily_score(water, smoked, steps, sleep, calories):
        score = 0
        if water >= AssessmentEngine.GOAL_WATER: score += 20
        if not smoked: score += 20
        if steps >= AssessmentEngine.GOAL_STEPS: score += 20
        if sleep >= AssessmentEngine.GOAL_SLEEP: score += 20
        if 0 < calories <= AssessmentEngine.GOAL_CALORIES: score += 20
        return score

    @staticmethod
    def calculate_kidney(gfr, protein_present):
        """
        Original logic (Kidney):
        gfr >= 90: Stage 1, riskVal 0
        gfr >= 60: Stage 2, riskVal 0
        gfr >= 45: Stage 3, riskVal 1
        gfr >= 30: Stage 3, riskVal 1
        gfr >= 15: Stage 4, riskVal 2
        else: Stage 5, riskVal 3
        """
        risk_val = 0
        stage = ""

        if gfr >= 90: stage = "Stage 1 • Normal"; risk_val = 0
        elif gfr >= 60: stage = "Stage 2 • Mild"; risk_val = 0
        elif gfr >= 45: stage = "Stage 3 • Moderate"; risk_val = 1
        elif gfr >= 30: stage = "Stage 3 • Moderate"; risk_val = 1
        elif gfr >= 15: stage = "Stage 4 • Severe"; risk_val = 2
        else: stage = "Stage 5 • Kidney Failure"; risk_val = 3

        if protein_present:
            risk_val += 1
            if risk_val > 3: risk_val = 3

        risk_level = "Low"
        score = 90
        if risk_val == 1: risk_level = "Medium"; score = 70
        elif risk_val == 2: risk_level = "High"; score = 40
        elif risk_val == 3: risk_level = "Critical"; score = 20

        return {
            "riskLevel": risk_level,
            "score": score,
            "stage": stage
        }

    @staticmethod
    def calculate_heart(sys, dia, chol, ldl, sugar, abnormal_ecg):
        pts = 0
        if sys >= 140 or dia >= 90: pts += 2
        elif sys >= 120 or dia >= 80: pts += 1

        if chol >= 240: pts += 2
        elif chol >= 200: pts += 1

        if ldl >= 160: pts += 2
        elif ldl >= 100: pts += 1

        if sugar >= 126: pts += 2
        elif sugar >= 100: pts += 1

        if abnormal_ecg: pts += 2

        if pts >= 6: risk_level = "High Risk"; risk_percent = 35
        elif pts >= 3: risk_level = "Medium Risk"; risk_percent = 20
        else: risk_level = "Low Risk"; risk_percent = 5

        return {
            "riskLevel": risk_level,
            "riskPercentage": f"{risk_percent}%",
            "score": 100 - risk_percent
        }

    @staticmethod
    def calculate_liver(alt, ast, bili, albu, alp):
        pts = 0
        if alt > 300: pts += 3
        elif alt > 120: pts += 2
        elif alt > 56: pts += 1

        if ast > 300: pts += 3
        elif ast > 100: pts += 2
        elif ast > 40: pts += 1

        if bili > 3.0: pts += 3
        elif bili > 2.0: pts += 2
        elif bili > 1.2: pts += 1

        if albu < 2.5: pts += 3
        elif albu < 3.0: pts += 2
        elif albu < 3.5: pts += 1

        if alp > 400: pts += 3
        elif alp > 250: pts += 2
        elif alp > 147: pts += 1

        if pts <= 2: risk_level, status, score = "Low Risk", "Normal", 95
        elif pts <= 6: risk_level, status, score = "Moderate Risk", "Mild", 75
        elif pts <= 10: risk_level, status, score = "High Risk", "Moderate", 50
        else: risk_level, status, score = "Very High Risk", "Severe", 25

        return {
            "riskLevel": risk_level,
            "status": status,
            "score": score
        }

    @staticmethod
    def calculate_lung(fev1, ratio, spo2, is_smoker):
        r_fev1 = 0 if fev1 >= 80 else 1 if fev1 >= 50 else 2 if fev1 >= 30 else 3
        r_ratio = 1 if ratio < 0.70 else 0
        r_spo2 = 0 if spo2 >= 95 else 1 if spo2 >= 90 else 3

        risk_val = max(r_fev1, r_ratio, r_spo2)
        if is_smoker and risk_val < 3: risk_val += 1

        if risk_val == 0: risk_level, status, score = "LOW", "Normal", 95
        elif risk_val == 1: risk_level, status, score = "LOW-MEDIUM", "Mild", 75
        elif risk_val == 2: risk_level, status, score = "MEDIUM", "Moderate", 50
        else: risk_level, status, score = "HIGH", "Severe", 25

        return {
            "riskLevel": risk_level,
            "status": status,
            "score": score
        }

    @staticmethod
    def calculate_cancer(tumor_size, lymph_node, metastasis, biopsy_grade):
        # tumor_size (T1-T4), lymph_node (boolean), metastasis (boolean), biopsy_grade (Low/High)
        # Note: tumour_size is expected as 'T1', 'T2', 'T3', 'T4'
        stage = "Stage I"
        base_risk_val = 1
        
        if metastasis:
            stage = "Stage IV"
            base_risk_val = 4
        elif (tumor_size in ["T3", "T4"]) and lymph_node:
            stage = "Stage III"
            base_risk_val = 3
        elif tumor_size == "T4" and not lymph_node:
            stage = "Stage III"
            base_risk_val = 3
        elif ((tumor_size in ["T2", "T3"]) and not lymph_node) or lymph_node:
            stage = "Stage II"
            base_risk_val = 2
        else:
            stage = "Stage I"
            base_risk_val = 1

        risk_val = base_risk_val
        if biopsy_grade.lower() == "high" and risk_val < 4:
            risk_val += 1

        risk_level = "Low" if risk_val == 1 else "Moderate" if risk_val == 2 else "High" if risk_val == 3 else "Very High"
        score = 85 if stage == "Stage I" else 65 if stage == "Stage II" else 40 if stage == "Stage III" else 20

        return {
            "stage": stage,
            "riskLevel": risk_level,
            "score": score
        }

    @staticmethod
    def calculate_brain(mmse, age, clinical, family_history):
        pts = 0
        if mmse >= 27: pts += 0
        elif mmse >= 21: pts += 15
        elif mmse >= 10: pts += 35
        else: pts += 50

        if clinical.lower() == "mci": pts += 15
        elif clinical.lower() == "dementia": pts += 30

        if age >= 70: pts += 10
        elif age >= 60: pts += 5
        
        if family_history: pts += 10

        if pts <= 25: risk_level = "Low Risk"
        elif pts <= 50: risk_level = "Mild Risk"
        elif pts <= 75: risk_level = "Moderate Risk"
        else: risk_level = "High Risk"
        
        score = round((mmse / 30.0) * 100)

        return {
            "riskLevel": risk_level,
            "score": score,
            "points": pts
        }
