"""
disease_info.py
---------------
Static lookup table: disease → description, precautions, and severity level.
"""

DISEASE_INFO = {
    "Fungal infection": {
        "description": "A fungal infection is a skin disease caused by fungus, commonly affecting nails, feet, and skin folds.",
        "precautions": ["Keep skin clean and dry", "Use antifungal creams", "Avoid sharing personal items", "Wear breathable clothing"],
        "severity": "Low",
    },
    "Allergy": {
        "description": "An allergy is an immune system reaction to a foreign substance not typically harmful, such as pollen, dust, or food.",
        "precautions": ["Avoid known allergens", "Take antihistamines", "Use air purifiers", "Consult an allergist"],
        "severity": "Low",
    },
    "GERD": {
        "description": "Gastroesophageal reflux disease (GERD) is a chronic digestive disorder where stomach acid flows back into the esophagus.",
        "precautions": ["Avoid spicy and fatty foods", "Don't lie down after eating", "Elevate head while sleeping", "Maintain healthy weight"],
        "severity": "Moderate",
    },
    "Chronic cholestasis": {
        "description": "Chronic cholestasis is a condition where bile flow from the liver is reduced or blocked for a prolonged period.",
        "precautions": ["Avoid alcohol", "Follow a low-fat diet", "Take prescribed medications", "Regular liver function tests"],
        "severity": "High",
    },
    "Drug Reaction": {
        "description": "An adverse drug reaction is an unintended, harmful response to medication taken at normal dosages.",
        "precautions": ["Stop the suspected drug", "Consult a doctor immediately", "Carry allergy records", "Avoid self-medication"],
        "severity": "High",
    },
    "Peptic ulcer diseae": {
        "description": "Peptic ulcers are open sores that develop on the stomach lining and the upper part of the small intestine.",
        "precautions": ["Avoid NSAIDs", "Reduce stress", "Avoid spicy foods", "Take antacids as prescribed"],
        "severity": "Moderate",
    },
    "AIDS": {
        "description": "AIDS is a chronic immune system disease caused by the HIV virus that damages immune cells.",
        "precautions": ["Use protection during intercourse", "Avoid sharing needles", "Take antiretroviral therapy", "Regular medical check-ups"],
        "severity": "Critical",
    },
    "Diabetes ": {
        "description": "Diabetes is a metabolic disease causing high blood sugar due to insufficient insulin production or response.",
        "precautions": ["Monitor blood sugar regularly", "Follow a balanced diet", "Exercise regularly", "Take prescribed medications"],
        "severity": "High",
    },
    "Gastroenteritis": {
        "description": "Gastroenteritis is inflammation of the stomach and intestines, typically caused by a bacterial or viral infection.",
        "precautions": ["Stay hydrated", "Wash hands frequently", "Avoid contaminated food", "Rest adequately"],
        "severity": "Moderate",
    },
    "Bronchial Asthma": {
        "description": "Bronchial asthma is a chronic respiratory condition causing airways to narrow, swell, and produce extra mucus.",
        "precautions": ["Use inhalers as prescribed", "Avoid triggers like dust and smoke", "Monitor peak flow", "Follow an asthma action plan"],
        "severity": "High",
    },
    "Hypertension ": {
        "description": "Hypertension is a condition where blood pressure in the arteries is persistently elevated.",
        "precautions": ["Reduce salt intake", "Exercise regularly", "Avoid smoking and alcohol", "Take prescribed medication"],
        "severity": "High",
    },
    "Migraine": {
        "description": "Migraine is a neurological condition causing severe recurring headaches often accompanied by nausea and light sensitivity.",
        "precautions": ["Identify and avoid triggers", "Stay hydrated", "Get adequate sleep", "Take prescribed pain relief"],
        "severity": "Moderate",
    },
    "Cervical spondylosis": {
        "description": "Cervical spondylosis is age-related wear on the spinal discs in the neck causing pain and stiffness.",
        "precautions": ["Maintain good posture", "Do neck exercises", "Use ergonomic furniture", "Physiotherapy sessions"],
        "severity": "Moderate",
    },
    "Paralysis (brain hemorrhage)": {
        "description": "Paralysis from brain hemorrhage occurs when bleeding in the brain damages the tissue controlling movement.",
        "precautions": ["Seek emergency care immediately", "Control blood pressure", "Physiotherapy", "Avoid blood thinners without guidance"],
        "severity": "Critical",
    },
    "Jaundice": {
        "description": "Jaundice is a condition where the skin and whites of the eyes turn yellow due to excess bilirubin in the blood.",
        "precautions": ["Stay hydrated", "Avoid alcohol", "Rest and follow doctor's advice", "Eat light nutritious meals"],
        "severity": "Moderate",
    },
    "Malaria": {
        "description": "Malaria is a life-threatening disease caused by Plasmodium parasites transmitted through infected mosquito bites.",
        "precautions": ["Use mosquito repellent", "Sleep under insecticide-treated nets", "Take antimalarial drugs", "Wear protective clothing"],
        "severity": "High",
    },
    "Chicken pox": {
        "description": "Chickenpox is a highly contagious viral infection causing an itchy blister-like rash, fever and fatigue.",
        "precautions": ["Avoid contact with infected persons", "Get vaccinated", "Keep nails short", "Use calamine lotion"],
        "severity": "Moderate",
    },
    "Dengue": {
        "description": "Dengue is a mosquito-borne viral infection causing severe flu-like illness and potentially fatal complications.",
        "precautions": ["Eliminate mosquito breeding sites", "Use insect repellent", "Stay hydrated", "Seek medical attention for high fever"],
        "severity": "High",
    },
    "Typhoid": {
        "description": "Typhoid fever is a bacterial infection caused by Salmonella Typhi, spread through contaminated food and water.",
        "precautions": ["Drink clean water", "Wash hands before eating", "Get vaccinated", "Avoid raw or undercooked food"],
        "severity": "High",
    },
    "Hepatitis A": {
        "description": "Hepatitis A is a viral liver infection spread through contaminated food and water.",
        "precautions": ["Get vaccinated", "Wash hands thoroughly", "Avoid contaminated water", "Avoid raw shellfish"],
        "severity": "Moderate",
    },
    "Hepatitis B": {
        "description": "Hepatitis B is a viral liver infection spread through blood, sexual contact and from mother to child.",
        "precautions": ["Get vaccinated", "Avoid sharing needles", "Use protection during intercourse", "Regular liver monitoring"],
        "severity": "High",
    },
    "Hepatitis C": {
        "description": "Hepatitis C is a blood-borne viral infection causing liver inflammation and potentially liver damage.",
        "precautions": ["Avoid sharing needles", "Test blood donors", "Use barrier contraception", "Seek antiviral treatment"],
        "severity": "High",
    },
    "Hepatitis D": {
        "description": "Hepatitis D is a serious liver disease caused by the hepatitis D virus which only infects those with hepatitis B.",
        "precautions": ["Get vaccinated for Hepatitis B", "Avoid sharing needles", "Practice safe sex", "Regular liver check-ups"],
        "severity": "High",
    },
    "Hepatitis E": {
        "description": "Hepatitis E is a liver disease caused by the hepatitis E virus, transmitted through contaminated drinking water.",
        "precautions": ["Drink clean boiled water", "Maintain good hygiene", "Avoid raw meat", "Seek medical care if pregnant"],
        "severity": "Moderate",
    },
    "Alcoholic hepatitis": {
        "description": "Alcoholic hepatitis is inflammation of the liver caused by drinking too much alcohol over a long period.",
        "precautions": ["Stop alcohol consumption", "Nutritional support", "Medical supervision", "Avoid acetaminophen"],
        "severity": "High",
    },
    "Tuberculosis": {
        "description": "Tuberculosis is a serious infectious bacterial disease primarily affecting the lungs, spread through airborne particles.",
        "precautions": ["Complete full TB medication course", "Isolate during infectious period", "Improve ventilation", "Get BCG vaccine"],
        "severity": "High",
    },
    "Common Cold": {
        "description": "The common cold is a viral infection of the upper respiratory tract causing runny nose, sneezing and sore throat.",
        "precautions": ["Wash hands frequently", "Avoid close contact with infected people", "Stay warm and rested", "Stay hydrated"],
        "severity": "Low",
    },
    "Pneumonia": {
        "description": "Pneumonia is an infection that inflames air sacs in one or both lungs, which may fill with fluid.",
        "precautions": ["Get vaccinated", "Practice good hygiene", "Avoid smoking", "Seek prompt medical treatment"],
        "severity": "High",
    },
    "Dimorphic hemmorhoids(piles)": {
        "description": "Piles (haemorrhoids) are swollen veins in the lower rectum and anus causing pain, bleeding and discomfort.",
        "precautions": ["Eat high-fiber diet", "Drink plenty of water", "Avoid straining during bowel movements", "Sitz baths"],
        "severity": "Moderate",
    },
    "Heart attack": {
        "description": "A heart attack occurs when blood flow to a part of the heart muscle is blocked, causing damage to heart tissue.",
        "precautions": ["Seek emergency care immediately", "Take aspirin if advised", "Maintain healthy diet", "Regular cardiac check-ups"],
        "severity": "Critical",
    },
    "Varicose veins": {
        "description": "Varicose veins are enlarged, twisted veins visible just under the skin surface, usually in the legs.",
        "precautions": ["Elevate legs regularly", "Wear compression stockings", "Exercise regularly", "Avoid prolonged standing"],
        "severity": "Low",
    },
    "Hypothyroidism": {
        "description": "Hypothyroidism is a condition where the thyroid gland doesn't produce enough thyroid hormone.",
        "precautions": ["Take prescribed thyroid hormone replacement", "Regular TSH monitoring", "Balanced diet with iodine", "Regular exercise"],
        "severity": "Moderate",
    },
    "Hyperthyroidism": {
        "description": "Hyperthyroidism is a condition where the thyroid gland produces too much thyroid hormone.",
        "precautions": ["Take prescribed antithyroid medications", "Regular thyroid function tests", "Avoid iodine-rich foods", "Manage stress"],
        "severity": "Moderate",
    },
    "Hypoglycemia": {
        "description": "Hypoglycemia is a condition where blood sugar levels drop dangerously low, requiring immediate treatment.",
        "precautions": ["Carry glucose tablets", "Eat regular balanced meals", "Monitor blood glucose", "Adjust medications with doctor"],
        "severity": "High",
    },
    "Osteoarthristis": {
        "description": "Osteoarthritis is a degenerative joint disease causing breakdown of cartilage and underlying bone.",
        "precautions": ["Maintain healthy weight", "Low-impact exercise", "Physical therapy", "Use joint support devices"],
        "severity": "Moderate",
    },
    "Arthritis": {
        "description": "Arthritis is inflammation of one or more joints causing pain, swelling and reduced range of motion.",
        "precautions": ["Regular gentle exercise", "Take anti-inflammatory medication", "Hot and cold therapy", "Protect joints from injury"],
        "severity": "Moderate",
    },
    "(vertigo) Paroymsal  Positional Vertigo": {
        "description": "Benign paroxysmal positional vertigo (BPPV) is a disorder causing brief episodes of mild to intense dizziness.",
        "precautions": ["Perform Epley maneuver", "Move slowly when changing positions", "Avoid triggers", "Physiotherapy"],
        "severity": "Moderate",
    },
    "Acne": {
        "description": "Acne is a skin condition that occurs when hair follicles are plugged with oil and dead skin cells.",
        "precautions": ["Wash face twice daily", "Avoid picking pimples", "Use non-comedogenic products", "Consult a dermatologist"],
        "severity": "Low",
    },
    "Urinary tract infection": {
        "description": "A urinary tract infection (UTI) is an infection in any part of the urinary system including kidneys and bladder.",
        "precautions": ["Stay well hydrated", "Urinate frequently", "Practice good hygiene", "Take prescribed antibiotics"],
        "severity": "Moderate",
    },
    "Psoriasis": {
        "description": "Psoriasis is a skin disease that causes red, itchy scaly patches, most commonly on the knees, elbows and scalp.",
        "precautions": ["Moisturize skin regularly", "Avoid triggers like stress", "Use prescribed topical treatments", "Limit alcohol"],
        "severity": "Moderate",
    },
    "Impetigo": {
        "description": "Impetigo is a highly contagious bacterial skin infection causing red sores or blisters that rupture and crust over.",
        "precautions": ["Keep sores covered", "Wash hands frequently", "Use prescribed antibiotic cream", "Avoid sharing personal items"],
        "severity": "Low",
    },
    "hepatitis A": {
        "description": "Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus, spread through contaminated food or water.",
        "precautions": ["Get vaccinated", "Wash hands with soap", "Avoid untreated water", "Practice food safety"],
        "severity": "Moderate",
    },
}

SEVERITY_COLOR = {
    "Low":      "#22c55e",
    "Moderate": "#f59e0b",
    "High":     "#ef4444",
    "Critical": "#7c3aed",
}

def get_disease_info(disease_name: str) -> dict:
    """Return info dict for the given disease, with a fallback."""
    stripped = disease_name.strip()
    if stripped in DISEASE_INFO:
        return DISEASE_INFO[stripped]
    # case-insensitive fallback
    lower = stripped.lower()
    for key, val in DISEASE_INFO.items():
        if key.lower() == lower:
            return val
    return {
        "description": "Information not available for this disease.",
        "precautions": ["Consult a licensed medical professional immediately."],
        "severity": "Unknown",
    }
