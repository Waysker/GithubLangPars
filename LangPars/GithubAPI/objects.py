class RepoLanguages(object):
    def __init__(self, name, languages):
        self.name = name
        self.languages = languages

    def toJson(self):
        return {
            'name': self.name,
            'languages': self.languages
        }


class LanguagePercentage(object):
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage

    def toJson(self):
        return {
            'name': self.name,
            'percentage': self.percentage
        }
