from playwright.sync_api import Page


class NoResultsModal:
    def __init__(self, page: Page):
        self.page = page
        self.no_resultsButton = page.get_by_text("No Results")

    def get_no_results_button(self):
        self.no_resultsButton.is_visible(timeout=5000)
        return self.no_resultsButton

    def no_results_click(self):
        self.no_resultsButton.is_visible(timeout=5000)
        self.no_resultsButton.click()
