import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def get_sample_data():
    schemes=[
        {"ID":"SCH_001","Name":"PM-KISAN","Description":"PM-KISAN scheme provides Rs 6000 per year directly to farmer bank accounts. Covers small and marginal farmers with landholding up to 2 hectares. Payment in three equal installments every 4 months. Launched in December 2018 by Ministry of Agriculture."},
        {"ID":"SCH_002","Name":"Ayushman Bharat","Description":"Ayushman Bharat Pradhan Mantri Jan Arogya Yojana provides health coverage of Rs 5 lakh per family per year. Free treatment at empanelled public and private hospitals. Covers secondary and tertiary hospitalization. Benefits for economically vulnerable families."},
        {"ID":"SCH_003","Name":"PMAY Housing","Description":"Pradhan Mantri Awas Yojana aims to provide affordable housing for all by 2022. Financial assistance for constructing pucca houses. Interest subsidy on home loans. Covers urban and rural poor families from EWS and LIG categories."},
        {"ID":"SCH_004","Name":"MUDRA Loan","Description":"MUDRA Yojana provides collateral-free loans up to 10 lakh rupees to small businesses. Three categories: Shishu up to 50k, Kishore 50k-5L, Tarun 5L-10L. For non-corporate non-farm enterprises in manufacturing trading and services."},
        {"ID":"SCH_005","Name":"Startup India","Description":"Startup India initiative supports entrepreneurs with tax benefits for 3 years. Simplified compliance regulations. Fast-track patent examination. Funding support through Fund of Funds. Self-certification for labor and environment laws for startups."}
    ]
    return pd.DataFrame(schemes)

def scrape_schemes():
    url="https://en.wikipedia.org/wiki/List_of_government_schemes_in_India"
    headers={"User-Agent":"Mozilla/5.0"}
    try:
        response=requests.get(url,headers=headers,timeout=10)
        soup=BeautifulSoup(response.content,"html.parser")
        schemes=[]
        for ul in soup.find_all("ul"):
            for li in ul.find_all("li"):
                text=li.get_text().strip()
                if len(text)>40 and "scheme" in text.lower():
                    schemes.append(text)
        for table in soup.find_all("table",class_="wikitable"):
            for row in table.find_all("tr")[1:]:
                cells=row.find_all(["td","th"])
                if len(cells)>=2:
                    text=" ".join([c.get_text().strip() for c in cells])
                    if len(text)>40:
                        schemes.append(text)
        schemes=list(set(schemes))
        data=[]
        for i,scheme in enumerate(schemes[:100]):
            name=scheme.split(".")[0].split("-")[0].strip()[:60]
            data.append({"ID":f"SCH_{i+1:03d}","Name":name,"Description":scheme})
        df_schemes=pd.DataFrame(data)
        print(f"Scraped {len(df_schemes)} schemes successfully!")
        return df_schemes
    except Exception as e:
        print(f"Scraping failed: {e}")
        print("Using backup sample data...")
        return get_sample_data()

df_schemes=scrape_schemes()
df_schemes.to_csv("schemes.csv",index=False)
print(df_schemes.head())
print("\nSaved to 'schemes.csv'.")
