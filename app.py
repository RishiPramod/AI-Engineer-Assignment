
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import json

# ---------------- Enhanced SEM Plan Generator Class ---------------- #
class EnhancedSEMPlanGenerator:
    def __init__(self, brand_website, competitor_website, service_locations, total_budget):
        self.brand_website = brand_website
        self.competitor_website = competitor_website
        self.service_locations = service_locations
        self.total_budget = total_budget
        self.target_cpa = 50
        self.conversion_rate = 0.02  # 2% conversion rate
        
    def calculate_ad_budgets(self) -> dict:
        """Calculate ad budgets based on total budget"""
        shopping_ads_budget = self.total_budget * 0.333
        search_ads_budget = self.total_budget * 0.467
        pmax_ads_budget = self.total_budget * 0.200
        
        return {
            "Shopping Ads Budget": shopping_ads_budget,
            "Search Ads Budget": search_ads_budget,
            "PMax Ads Budget": pmax_ads_budget,
            "Total Monthly Budget": self.total_budget,
            "Daily Shopping Budget": shopping_ads_budget / 30,
            "Daily Search Budget": search_ads_budget / 30,
            "Daily PMax Budget": pmax_ads_budget / 30
        }
    
    def generate_seed_keywords(self, website_url: str) -> list:
        """Generate 10 seed keywords based on website"""
        try:
            domain = website_url.replace('https://', '').replace('http://', '').split('.')[0]
        except:
            domain = "product"
        
        keywords = [
            {"keyword": f"{domain} software", "search_volume": 8500, "competition": "High", "cpc_low": 0.50, "cpc_high": 2.50},
            {"keyword": f"{domain} platform", "search_volume": 6200, "competition": "Medium", "cpc_low": 0.75, "cpc_high": 3.00},
            {"keyword": f"{domain} solution", "search_volume": 4800, "competition": "Medium", "cpc_low": 0.60, "cpc_high": 2.80},
            {"keyword": f"best {domain}", "search_volume": 7200, "competition": "High", "cpc_low": 1.20, "cpc_high": 4.50},
            {"keyword": f"{domain} alternatives", "search_volume": 3900, "competition": "Medium", "cpc_low": 0.90, "cpc_high": 3.20},
            {"keyword": f"{domain} pricing", "search_volume": 5600, "competition": "High", "cpc_low": 1.10, "cpc_high": 3.80},
            {"keyword": f"{domain} reviews", "search_volume": 4200, "competition": "Medium", "cpc_low": 0.80, "cpc_high": 2.90},
            {"keyword": f"{domain} demo", "search_volume": 2800, "competition": "Low", "cpc_low": 0.70, "cpc_high": 2.60},
            {"keyword": f"{domain} free trial", "search_volume": 5100, "competition": "High", "cpc_low": 1.30, "cpc_high": 4.20},
            {"keyword": f"{domain} features", "search_volume": 3400, "competition": "Medium", "cpc_low": 0.85, "cpc_high": 3.10}
        ]
        return keywords
    
    def group_keywords_by_ad_group(self, keywords: list) -> dict:
        """Group keywords by logical ad groups"""
        ad_groups = {
            "Brand Terms": [],
            "Category Terms": [],
            "Competitor Terms": [],
            "Location-based Queries": [],
            "Long-Tail Informational": []
        }
        
        for keyword in keywords:
            kw = keyword["keyword"].lower()
            
            if any(term in kw for term in ["brand", "company", "official"]):
                ad_groups["Brand Terms"].append(keyword)
            elif any(term in kw for term in ["alternative", "vs", "competitor"]):
                ad_groups["Competitor Terms"].append(keyword)
            elif any(loc.lower() in kw for loc in self.service_locations):
                ad_groups["Location-based Queries"].append(keyword)
            elif len(kw.split()) >= 4:
                ad_groups["Long-Tail Informational"].append(keyword)
            else:
                ad_groups["Category Terms"].append(keyword)
        
        return ad_groups
    
    def calculate_cpc_recommendations(self, keywords: list) -> list:
        """Calculate CPC recommendations based on 2% conversion rate"""
        recommendations = []
        
        for keyword in keywords:
            target_cpc = self.target_cpa * self.conversion_rate
            
            competition_multiplier = {"Low": 0.8, "Medium": 1.0, "High": 1.2}
            adjusted_cpc = target_cpc * competition_multiplier[keyword["competition"]]
            
            suggested_match_types = []
            if len(keyword["keyword"].split()) <= 2:
                suggested_match_types = ["Exact", "Phrase"]
            else:
                suggested_match_types = ["Phrase", "Broad Match Modifier"]
            
            recommendations.append({
                **keyword,
                "target_cpc": round(adjusted_cpc, 2),
                "suggested_match_types": suggested_match_types,
                "expected_conversions": round(keyword["search_volume"] * self.conversion_rate),
                "expected_cost": round(keyword["search_volume"] * adjusted_cpc)
            })
        
        return recommendations
    
    def generate_search_themes(self) -> dict:
        """Generate search themes for Performance Max campaigns"""
        try:
            domain = self.brand_website.replace('https://', '').replace('http://', '').split('.')[0]
        except:
            domain = "product"
        
        return {
            "Product Category Themes": [
                f"{domain} software", f"{domain} platform", f"{domain} tools"
            ],
            "Use-case Based Themes": [
                f"{domain} for teams", f"{domain} for business", f"{domain} for productivity"
            ],
            "Demographic Themes": [
                f"{domain} for professionals", f"{domain} for startups", f"{domain} for remote teams"
            ],
            "Location-based Themes": [f"{domain} {loc}" for loc in self.service_locations]
        }
    
    def generate_shopping_campaign_bids(self) -> list:
        """Generate shopping campaign bids"""
        budgets = self.calculate_ad_budgets()
        shopping_budget = budgets["Shopping Ads Budget"]
        
        products = [
            {"product": "Basic Plan", "price_range": [29, 49], "priority": "High"},
            {"product": "Pro Plan", "price_range": [79, 129], "priority": "High"},
            {"product": "Enterprise Plan", "price_range": [199, 299], "priority": "Medium"},
            {"product": "Add-on Features", "price_range": [19, 39], "priority": "Medium"}
        ]
        
        shopping_bids = []
        for product in products:
            avg_price = np.mean(product["price_range"])
            target_cpc = (avg_price * 0.1) * self.conversion_rate
            
            priority_multiplier = {"High": 1.2, "Medium": 1.0, "Low": 0.8}
            adjusted_cpc = target_cpc * priority_multiplier[product["priority"]]
            
            shopping_bids.append({
                "product": product["product"],
                "suggested_cpc": round(adjusted_cpc, 2),
                "daily_budget": round(shopping_budget / 30 / len(products), 2),
                "expected_conversions": round(shopping_budget / 30 / len(products) * self.conversion_rate / adjusted_cpc, 2),
                "priority": product["priority"]
            })
        
        return shopping_bids

def main():
    st.set_page_config(
        page_title="SEM Campaign Builder",
        layout="wide"
    )
    
    st.title("SEM Campaign Builder")
    # st.markdown("Professional SEM planning with Ad Budgets and Google Keyword Planner simulation")
    
    # Sidebar configuration
    st.sidebar.header("Campaign Configuration")
    
    brand_website = st.sidebar.text_input("Brand Website URL",value="",placeholder="https://cubehq.com")
    competitor_website = st.sidebar.text_input("Competitor Website URL",value="",placeholder="https://cubehq.com")
    # service_locations = st.sidebar.multiselect(
    #     "Service Locations",
    #     ["New York", "San Francisco", "Los Angeles", "Chicago", "Austin", "Seattle", "Denver", "Miami"],
    #     default=["New York", "San Francisco"]
    # )/
    with st.sidebar:
        st.header("Choose Location")
    
        service_locations = st.multiselect(
            "Select Service Locations",
            ["New York", "San Francisco", "Los Angeles", "Chicago", "Austin", "Seattle", "Denver", "Miami"],
            default=[]  # start empty so user must choose
        )
    
    total_budget = st.sidebar.number_input(
        "Total Monthly Budget ($)", 
        min_value=1000, 
        max_value=100000, 
        value=15000,
        step=100
    )
    
    target_cpa = st.sidebar.number_input(
        "Target CPA ($)", 
        min_value=10, 
        max_value=200, 
        value=50,
        step=5
    )
    
    if st.sidebar.button("Generate SEM Plan", type="primary"):
        with st.spinner("Generating comprehensive SEM plan..."):
            generator = EnhancedSEMPlanGenerator(
                brand_website, 
                competitor_website, 
                service_locations, 
                total_budget
            )
            generator.target_cpa = target_cpa
            
            # Calculate ad budgets
            ad_budgets = generator.calculate_ad_budgets()
            
            # Generate keywords
            brand_keywords = generator.generate_seed_keywords(brand_website)
            competitor_keywords = generator.generate_seed_keywords(competitor_website)
            
            # Group keywords
            all_keywords = brand_keywords + competitor_keywords
            ad_groups = generator.group_keywords_by_ad_group(all_keywords)
            
            # Calculate CPC recommendations
            cpc_recommendations = generator.calculate_cpc_recommendations(all_keywords)
            
            # Generate themes and bids
            search_themes = generator.generate_search_themes()
            shopping_bids = generator.generate_shopping_campaign_bids()
            
            st.success("SEM Plan Generated Successfully!")
            
            # Display Ad Budgets
            st.header("Ad Budgets Breakdown")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Shopping Ads Budget", f"${ad_budgets['Shopping Ads Budget']:,.0f}")
                st.metric("Daily Shopping Budget", f"${ad_budgets['Daily Shopping Budget']:,.0f}")
            
            with col2:
                st.metric("Search Ads Budget", f"${ad_budgets['Search Ads Budget']:,.0f}")
                st.metric("Daily Search Budget", f"${ad_budgets['Daily Search Budget']:,.0f}")
            
            with col3:
                st.metric("PMax Ads Budget", f"${ad_budgets['PMax Ads Budget']:,.0f}")
                st.metric("Daily PMax Budget", f"${ad_budgets['Daily PMax Budget']:,.0f}")
            
            with col4:
                st.metric("Total Monthly Budget", f"${ad_budgets['Total Monthly Budget']:,.0f}")
                st.metric("Total Daily Budget", f"${ad_budgets['Daily Shopping Budget'] + ad_budgets['Daily Search Budget'] + ad_budgets['Daily PMax Budget']:,.0f}")
            
            # Display results in tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "Ad Budgets & Keywords", 
                "Keyword Groups", 
                "CPC Recommendations", 
                "Search Themes", 
                "Shopping Campaign Bids"
            ])
            
            with tab1:
                st.subheader("Ad Budgets")
                budget_df = pd.DataFrame([
                    {"Campaign Type": "Shopping Ads", "Monthly Budget": ad_budgets['Shopping Ads Budget'], "Daily Budget": ad_budgets['Daily Shopping Budget']},
                    {"Campaign Type": "Search Ads", "Monthly Budget": ad_budgets['Search Ads Budget'], "Daily Budget": ad_budgets['Daily Search Budget']},
                    {"Campaign Type": "PMax Ads", "Monthly Budget": ad_budgets['PMax Ads Budget'], "Daily Budget": ad_budgets['Daily PMax Budget']}
                ])
                st.dataframe(budget_df)
                
                st.subheader("Seed Keywords")
                keywords_df = pd.DataFrame(cpc_recommendations)
                st.dataframe(keywords_df)
            
            with tab2:
                st.subheader("Keywords Grouped by Ad Groups")
                for group_name, keywords in ad_groups.items():
                    if keywords:
                        st.subheader(f"{group_name}")
                        group_df = pd.DataFrame(keywords)
                        st.dataframe(group_df)
            
            with tab3:
                st.subheader("CPC Recommendations (2% Conversion Rate)")
                recommendations_df = pd.DataFrame(cpc_recommendations)
                st.dataframe(recommendations_df)
            
            with tab4:
                st.subheader("Search Themes for Performance Max Campaign")
                for theme_type, themes in search_themes.items():
                    st.subheader(f"{theme_type}")
                    for theme in themes:
                        st.write(f"• {theme}")
            
            with tab5:
                st.subheader("🛒 Shopping Campaign Bids")
                shopping_df = pd.DataFrame(shopping_bids)
                st.dataframe(shopping_df)
            
            # Download buttons
            st.header("Download Results")
            
            # Prepare data for download
            results = {
                "ad_budgets": ad_budgets,
                "keywords": cpc_recommendations,
                "ad_groups": {k: v for k, v in ad_groups.items() if v},
                "search_themes": search_themes,
                "shopping_bids": shopping_bids
            }
            
            # Create download buttons
            col1, col2 = st.columns(2)
            
            with col1:
                csv = pd.DataFrame(cpc_recommendations).to_csv(index=False)
                st.download_button(
                    label="Download Keywords CSV",
                    data=csv,
                    file_name="sem_keywords.csv",
                    mime="text/csv"
                )
            
            with col2:
                json_data = json.dumps(results, indent=2)
                st.download_button(
                    label="Download Full Plan JSON",
                    data=json_data,
                    file_name="sem_plan.json",
                    mime="application/json"
                )

if __name__ == "__main__":
    main()
