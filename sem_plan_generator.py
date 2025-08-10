import json
from datetime import datetime

class SEMPlanGenerator:
    def __init__(self, brand_name, locations, budgets):
        self.brand_name = brand_name
        self.locations = locations
        self.budgets = budgets
        self.plan = {
            "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "campaigns": []
        }

    def create_search_campaigns(self):
        # Branded Search Campaign
        branded_campaign = {
            "campaign_name": f"{self.brand_name} - Branded Search",
            "campaign_type": "Search",
            "monthly_budget": "$2,000",
            "ad_groups": [
                {
                    "name": "Brand Terms",
                    "keywords": [
                        {"text": f"{self.brand_name.lower()} nutrition", "match_type": "Exact"},
                        {"text": f"{self.brand_name.lower()} protein", "match_type": "Phrase"},
                        {"text": f"{self.brand_name.lower()} supplements", "match_type": "Exact"}
                    ],
                    "max_cpc": "$1.50 - $2.50",
                    "expected_cvr": "5-7%"
                }
            ]
        }

        # Non-Branded Search Campaign
        non_branded_campaign = {
            "campaign_name": f"{self.brand_name} - Non-Branded Search",
            "campaign_type": "Search",
            "monthly_budget": "$3,000",
            "ad_groups": [
                {
                    "name": "Protein Products",
                    "keywords": [
                        {"text": "vegan protein powder", "match_type": "Phrase"},
                        {"text": "whey protein isolate", "match_type": "Exact"},
                        {"text": "collagen protein powder", "match_type": "Phrase"}
                    ],
                    "max_cpc": "$2.00 - $3.00"
                },
                {
                    "name": "Health & Nutrition",
                    "keywords": [
                        {"text": "plant based supplements", "match_type": "BMM"},
                        {"text": "gluten free nutrition", "match_type": "Phrase"},
                        {"text": "keto friendly shake", "match_type": "BMM"}
                    ],
                    "max_cpc": "$1.80 - $2.80"
                }
            ]
        }

        # Local Search Campaign
        local_keywords = []
        for location in self.locations:
            local_keywords.extend([
                {"text": f"protein powder in {location}", "match_type": "Phrase"},
                {"text": f"best nutrition store {location}", "match_type": "Phrase"}
            ])

        local_campaign = {
            "campaign_name": f"{self.brand_name} - Local Search",
            "campaign_type": "Search",
            "monthly_budget": "$1,500",
            "ad_groups": [
                {
                    "name": "City-Specific Terms",
                    "keywords": local_keywords,
                    "max_cpc": "$1.80 - $2.80"
                }
            ]
        }

        self.plan["campaigns"].extend([branded_campaign, non_branded_campaign, local_campaign])

    def create_pmax_campaign(self):
        pmax_campaign = {
            "campaign_name": f"{self.brand_name} - Performance Max",
            "campaign_type": "Performance Max",
            "monthly_budget": "$2,000",
            "asset_groups": [
                {
                    "name": "Protein Products",
                    "headlines": ["Premium Protein Blends", "Fuel Your Fitness"],
                    "descriptions": ["Shop our range of high-quality protein supplements"],
                    "image_types": ["Product shots", "Lifestyle images"]
                },
                {
                    "name": "Special Diets",
                    "headlines": ["Vegan & Keto Friendly", "Clean Nutrition"],
                    "descriptions": ["Nutrition that fits your lifestyle"],
                    "image_types": ["Dietary badges", "Ingredient close-ups"]
                }
            ],
            "target_roas": "400%",
            "optimization_goal": "Conversions"
        }
        self.plan["campaigns"].append(pmax_campaign)

    def create_shopping_campaign(self):
        shopping_campaign = {
            "campaign_name": f"{self.brand_name} - Smart Shopping",
            "campaign_type": "Shopping",
            "monthly_budget": "$3,000",
            "product_groups": [
                {
                    "name": "High-Margin Products",
                    "target_roas": "400%",
                    "priority": "High"
                },
                {
                    "name": "New Products",
                    "target_roas": "300%",
                    "priority": "Medium"
                },
                {
                    "name": "Clearance Items",
                    "target_roas": "200%",
                    "priority": "Low"
                }
            ],
            "bidding_strategy": "Target ROAS",
            "optimization_goal": "Conversion value"
        }
        self.plan["campaigns"].append(shopping_campaign)

    def add_ad_copy_guidelines(self):
        self.plan["ad_copy_guidelines"] = {
            "headlines": [
                "{Price} Off {Product}",
                "Free Shipping on Orders ${Amount}+",
                "Limited Time Offer - {Discount}% Off"
            ],
            "descriptions": [
                "Doctor formulated {product} for optimal results. {usp}.",
                "{Benefit} with our premium {product}. {Offer}."
            ],
            "usps": [
                "Free Shipping",
                "30-Day Money Back Guarantee",
                "Premium Quality Ingredients"
            ]
        }

    def add_tracking_plan(self):
        self.plan["tracking_plan"] = {
            "conversion_tracking": [
                "Website purchases",
                "Lead form submissions",
                "Phone calls",
                "Email signups"
            ],
            "optimization_schedule": {
                "daily": [
                    "Monitor spend vs. budget",
                    "Check for disapproved ads"
                ],
                "weekly": [
                    "Performance by campaign/ad group",
                    "Top performing keywords",
                    "Conversion trends"
                ],
                "monthly": [
                    "Full performance review",
                    "Budget allocation adjustments",
                    "Strategy refinement"
                ]
            }
        }

    def generate_plan(self):
        self.create_search_campaigns()
        self.create_pmax_campaign()
        self.create_shopping_campaign()
        self.add_ad_copy_guidelines()
        self.add_tracking_plan()
        return self.plan

def save_plan_to_json(plan, filename="sem_plan.json"):
    with open(filename, 'w') as f:
        json.dump(plan, f, indent=2)

def main():
    # Configuration
    brand_name = "FitFuel"
    locations = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
    budgets = {
        "search": 5000,
        "shopping": 3000,
        "pmax": 2000
    }

    # Generate plan
    generator = SEMPlanGenerator(brand_name, locations, budgets)
    sem_plan = generator.generate_plan()
    
    # Save to JSON
    save_plan_to_json(sem_plan)
    print(f"SEM plan generated and saved to sem_plan.json")

    # Print summary
    print("\n--- SEM Plan Summary ---")
    print(f"Total Campaigns: {len(sem_plan['campaigns'])}")
    print(f"Total Monthly Budget: ${sum([int(budgets[k]) for k in budgets])}")
    print(f"Locations: {', '.join(locations)}")

if __name__ == "__main__":
    main()
