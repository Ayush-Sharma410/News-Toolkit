import unittest
from newsapi_articles_tool import GetNewsArticlesTool, GetNewsArticlesInput

class GetNewsArticlesToolTestCase(unittest.TestCase):

    def setUp(self):
        self.tool = GetNewsArticlesTool()

    def test_tool_name(self):
        self.assertEqual(self.tool.name, "Get News Articles")

    def test_tool_args_schema(self):
        self.assertEqual(self.tool.args_schema, GetNewsArticlesInput)

    def test_tool_description(self):
        self.assertEqual(self.tool.description, "Retrieves news articles from NewsAPI.")

    def test_successful_retrieval(self):
        # Create a tool instance
        news_tool = GetNewsArticlesTool()
        
        # Define sample input parameters for successful retrieval
        keywords = "Python programming"
        max_results = 10

        # Execute the tool
        result = news_tool.execute(keywords=keywords, max_results=max_results)

        # Ensure the response contains articles
        articles = result.get("articles")
        self.assertIsNotNone(articles)
        self.assertIsInstance(articles, list)
        self.assertTrue(len(articles) > 0)

    def test_no_results(self):
        # Create a tool instance
        news_tool = GetNewsArticlesTool()
        
        # Define sample input parameters for a query with no results
        keywords = "Zzzzzzzzzzz"  # Unlikely to yield news articles
        max_results = 10

        # Execute the tool
        result = news_tool.execute(keywords=keywords, max_results=max_results)

        # Ensure the response is empty
        articles = result.get("articles")
        self.assertIsNotNone(articles)
        self.assertIsInstance(articles, list)
        self.assertEqual(len(articles), 0)

    def test_invalid_input(self):
        # Create a tool instance
        news_tool = GetNewsArticlesTool()
        
        # Define sample input parameters with invalid values
        keywords = 12345  # Invalid input (not a string)
        max_results = -5  # Invalid input (negative value)

        # Execute the tool and catch potential errors
        with self.assertRaises(ValueError):
            news_tool.execute(keywords=keywords, max_results=max_results)

if __name__ == '__main__':
    unittest.main()
