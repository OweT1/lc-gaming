class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        neighbours, in_degree = {}, defaultdict(int)
        for ingrdnts, recipe in zip(ingredients, recipes):
            for ingrdnt in ingrdnts:
                if ingrdnt not in neighbours:
                    neighbours[ingrdnt] = []
                neighbours[ingrdnt].append(recipe)
                in_degree[recipe] += 1
        
        res = []
        recipes_set = set(recipes)
        while supplies:
            supply = supplies.pop()
            if supply not in neighbours: continue

            for nb in neighbours[supply]:
                in_degree[nb] -= 1
                if in_degree[nb] == 0:
                    supplies.append(nb)
                    if nb in recipes_set:
                        res.append(nb)
        return res
            
