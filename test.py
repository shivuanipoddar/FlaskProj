from FlaskProj import app
import unittest


class LoginTest(unittest.TestCase):

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_home(self):
            tester = app.test_client(self)
            response = tester.get("/home")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

    def test_register(self):
            tester = app.test_client(self)
            response = tester.get("/register")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

    def test_aboutus(self):
            tester = app.test_client(self)
            response = tester.get("/about-us")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

    def test_service(self):
            tester = app.test_client(self)
            response = tester.get("/service")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

    # def test_profile(self):
    #         tester = app.test_client(self)
    #         response = tester.get("/profile")
    #         statuscode = response.status_code
    #         self.assertEqual(statuscode, 200)

    def test_term(self):
            tester = app.test_client(self)
            response = tester.get("/term")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

    def test_product(self):
            tester = app.test_client(self)
            response = tester.get("/product")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

    def test_contact(self):
            tester = app.test_client(self)
            response = tester.get("/contact-us")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

    def test_register_post(self):
        tester = app.test_client(self)
        response = tester.post("/register", data={"username": "sarvan", "password": "1234"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == "__main__":
    unittest.main()