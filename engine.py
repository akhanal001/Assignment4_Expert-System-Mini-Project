from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        # """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        # """TODO: Return True if all antecedents are true and consequent not yet known."""
        
        return all(a in self.facts for a in rule.antecedents) and rule.consequent not in self.facts

    def run(self) -> None:
        
        
        # """TODO: Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        
        
        fired = True
        
        while fired:
            fired = False
            for rule in sorted(self.rules, key=lambda r: -r.priority):
                if self.can_fire(rule):
                    self.facts.add(rule.consequent)
                    self.trace.append({
                        "rule": rule.name,
                        "added": rule.consequent
                    })
                    fired = True
                    break
                
                
        # """TODO: Return separated results (recommendations, specs, other facts)."""
    def conclusions(self) -> Dict[str, List[str]]:
        recs = []
        specs = []
        others = []

        for fact in self.facts:
            if fact.startswith("recommend:"):
                recs.append(fact.split("recommend:")[1])
            elif fact.startswith("spec:"):
                specs.append(fact.split("spec:")[1])
            else:
                others.append(fact)

        return {
            "recommendations": recs,
            "specifications": specs,
            "other_facts": others,
            "trace": self.trace
        }

