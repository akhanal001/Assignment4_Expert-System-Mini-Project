from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    
    # # TODO: Ask more questions to collect facts for reasoning
    
    #Portable or Display centric laptop
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    
    # Screen size preference
    if input("Do you need large screen (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    
    # Battery life preference    
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
        
    budget = input("What is your budget? High (h), Medium (m), or Low (l): ").lower()
    if budget.startswith("h"):
        facts.append("budget_high")
    elif budget.startswith("m"):
        facts.append("budget_medium")
    else:
        facts.append("budget_low")
        
    # Usage type for gaming
    if input("Will you use it for gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
     
    # Usage type for creative work
    if input("Do you need it for the creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    
    #This is to check if it is for travel or office if not office use than for travel
    if input("Is this for the office use onlyy? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    
    if input("Will you be traveling often with it? (y/n): ").lower().startswith("y"):
            facts.append("travel_often")
    
    #OS preferance options of windows, macos, linux of non preferance than user need to choose one to make decision easier
    os_preferance = input("What Os you prefer Windows OS? (w/o/l): ").lower()
    
    #of os preferance starts with w than windows, o for macos and l for linux
    if os_preferance.startswith("l"):
        facts.append("pref_os_linux")
        
    elif os_preferance.startswith("o"):
        facts.append("pref_os_macos")
    
    #else for windows(w) rule is not inculded so it recommant the defelt laptop with windows os.
    
        
    #AI acceleration requirement
    if input("Do you need AI accleration and Better  ? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
        
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    
    initial_facts = collect_initial_facts()
    engine.assert_facts(initial_facts)
    
    engine.run()
    result = engine.conclusions()
    
    print ("__________________________________________________________________")
    if result["recommendations"]:
           print(f" Recommend Laptop: {result['recommendations'][0]}")
    else:
        print("Recommend Laptop: default_laptop_model(no specific recommendation)") 
        
    print ("__________________________________________________________________")

    for r in engine.trace:
        if r ["added"].startswith("recommend:"):
            print(f"Explanation : derived from rule '{r['rule']}'")
            break
    print ("__________________________________________________________________")
    
    
    print (f"Specifications suggested based on prority:")
    for s in result["specifications"]:
        print(f"{s.replace('specification:', '')}")        
    print ("__________________________________________________________________")

        
if __name__ == "__main__":
    main()
    