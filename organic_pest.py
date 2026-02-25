# ==========================================
# Crop-wise Organic Pest Management
# Covers ALL listed crops
# ==========================================

ORGANIC_PESTS = {

    # ================= CEREALS & MILLETS =================
    "rice": ["Neem oil spray", "Light traps", "Trichogramma cards"],
    "wheat": ["Neem seed kernel extract", "Yellow sticky traps"],
    "maize": ["Neem oil spray", "Pheromone traps"],
    "sorghum": ["Neem oil spray", "Bird perches"],
    "pearl millet": ["Neem seed extract", "Light traps"],
    "ragi": ["Neem oil spray", "Intercropping"],
    "panivaragu": ["Neem oil spray"],
    "samai": ["Neem oil spray"],
    "thinai": ["Neem oil spray"],
    "varagu": ["Neem oil spray"],
    "kudiraivali": ["Neem oil spray"],

    # ================= PULSES =================
    "black gram": ["Neem oil spray", "Chilli–garlic extract"],
    "green gram": ["Neem seed kernel extract", "Sticky traps"],
    "cowpea": ["Neem oil spray", "Sticky traps"],
    "bengalgram": ["Neem oil spray", "Pheromone traps"],
    "horsegram": ["Neem oil spray"],
    "red gram": ["Neem oil spray", "Trichoderma (soil)"],
    "soyabean": ["Neem oil spray", "Yellow sticky traps"],

    # ================= OILSEEDS =================
    "groundnut": ["Neem oil spray", "Castor as trap crop"],
    "sunflower": ["Neem oil spray", "Bird perches"],
    "gingely": ["Neem oil spray", "Light traps"],
    "castor": ["Neem oil spray"],

    # ================= COMMERCIAL CROPS =================
    "cotton": ["Neem oil spray", "Trichoderma (soil)"],
    "jute": ["Neem oil spray"],
    "sugarcane": ["Trichogramma cards", "Neem cake application"],
    "sugarbeet": ["Neem oil spray"],

    # ================= VEGETABLES =================
    "tomato": ["Neem oil spray", "Bt spray"],
    "onion": ["Neem oil spray", "Sticky traps"],
    "small onion": ["Neem oil spray", "Sticky traps"],
    "chillies": ["Neem oil spray", "Yellow sticky traps"],
    "cabbage": ["Neem oil spray", "Bt spray"],
    "bhendi": ["Neem oil spray", "Sticky traps"],
    "brinjal": ["Neem oil spray", "Pheromone traps"],
    "capsicum": ["Neem oil spray"],
    "pumpkin": ["Neem oil spray"],
    "snake gourd": ["Neem oil spray"],
    "ribbed gourd": ["Neem oil spray"],
    "bottle gourd": ["Neem oil spray"],
    "bitter gourd": ["Neem oil spray"],
    "ash gourd": ["Neem oil spray"],
    "cucumber": ["Neem oil spray"],
    "watermelon": ["Neem oil spray"],
    "muskmelon": ["Neem oil spray"],
    "tinda": ["Neem oil spray"],
    "chowchow": ["Neem oil spray"],
    "cluster bean": ["Neem oil spray"],
    "vegetable cowpea": ["Neem oil spray"],
    "french bean": ["Neem oil spray"],
    "peas": ["Neem oil spray"],
    "annual moringa": ["Neem oil spray"],
    "carrot": ["Neem oil spray"],
    "beetroot": ["Neem oil spray"],
    "radish": ["Neem oil spray"],
    "sweet potato": ["Neem oil spray"],
    "tapioca": ["Neem oil spray"],
    "elephant foot yam": ["Neem oil spray"],
    "cauliflower": ["Neem oil spray", "Bt spray"],
}

# ==========================================
# Helper Function
# ==========================================
def get_organic_pest_control(crop):
    return ORGANIC_PESTS.get(
        crop.lower(),
        ["Neem oil spray (general organic pest control)"]
    )
