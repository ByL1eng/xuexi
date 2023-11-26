class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        new_draft = self.crew * 1.5
        if self.draft - new_draft > 20:
            return True
        else:
            return False