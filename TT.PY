if __name__ == "__main__":
    icp = {
        "industry": "SaaS",
        "company_size": "200-500 employees",
        "job_titles": ["Marketing Manager", "VP of Marketing"],
        "locations": ["New York"]
    }
    
    # Step 1: Find companies that match the ICP
    companies_list = search_companies(icp)
    
    all_leads = []
    
    # Step 2: Iterate through each company to find leads
    for company in companies_list:
        print(f"Searching for leads at {company['name']}...")
        leads_from_company = find_leads_on_website(company['website'], icp['job_titles'])
        all_leads.extend(leads_from_company)
        
    # Step 3: Save the data
    df = pd.DataFrame(all_leads)
    df.to_csv("discovered_leads.csv", index=False)
    print("Lead discovery complete. Data saved to discovered_leads.csv")