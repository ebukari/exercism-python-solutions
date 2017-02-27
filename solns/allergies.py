class Allergies:
    ALLERGIES = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, score=0):
        _score = reversed(bin(score)[2:])
        self.score = ''.join(_score)

    def is_allergic_to(self, allergen):
        index = Allergies.ALLERGIES.index(allergen)
        try:
            return self.score[index] == '1'
        except IndexError:
            return False

    @property
    def lst(self):
        return [allergen for allergen in Allergies.ALLERGIES if self.is_allergic_to(allergen)]


if __name__ == "__main__":
    new = Allergies(2)
