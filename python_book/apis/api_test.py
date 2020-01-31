import unittest
from python_repos import make_request, get_repos

class StatusCodeTestCase(unittest.TestCase):
    """Tests 'get_repos' function"""

    def test_status_code(self):
        """Tests to check if the api call returns a 200 Status Code"""
        request = make_request(lang='python')
        status_code = request.status_code
        self.assertEqual(status_code, 200)

    def test_repo_count(self):
        """Tests to check if enough repos are returned"""
        request = make_request(lang='python')
        response_dict = get_repos(request) 
        min_repos = 25
        repo_count = response_dict['total_count']
        self.assertGreaterEqual(repo_count, 25)

unittest.main()
        

