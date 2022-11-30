{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "#Importing the libraries \n",
        "import os\n",
        "import unittest\n",
        "import sys\n",
        "import requests\n",
        "\n",
        "#Defining the  file path\n",
        "sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))\n",
        "from board import app, db\n",
        "\n",
        "TEST_DB = 'test.db'\n",
        "\n",
        "\"\"\"\n",
        "Primary class containing all the tests \n",
        "\"\"\"\n",
        "class Basic(unittest.TestCase):\n",
        "    '''\n",
        "    These instructions are executed prior to each test\n",
        "    '''    \n",
        "    def setUp(self):\n",
        "        app.config['TESTING'] = True\n",
        "        app.config['WTF_CSRF_ENABLED'] = False\n",
        "        app.config['DEBUG'] = False\n",
        "        self.app = app.test_client()\n",
        "    '''\n",
        "    These instructions are executed after each test\n",
        "    '''\n",
        "    def tearDown(self):\n",
        "        pass\n",
        "    '''\n",
        "    This function tests if the primary page is loaded or not \n",
        "    '''\n",
        "    def test_main_page(self):        \n",
        "        req = self.app.get('/main', follow_redirects=True)\n",
        "        self.assertEqual(req.status_code, 200)\n",
        "    '''\n",
        "    This function tests that login page is shown to new users \n",
        "    '''\n",
        "    def test_login(self):\n",
        "        req = requests.get('http://127.0.0.1:5000/')\n",
        "        self.assertEqual(req.url, 'http://127.0.0.1:5000/login')\n",
        "\n",
        "    '''\n",
        "    This functions tests that the registration page works properly and redirects users to the main page after registering \n",
        "    '''\n",
        "    def test_registration(self):\n",
        "        \n",
        "        details = {'username':'Dolly', 'password':'ncelekckln!mv', 'repeat':'ncelekckln!mv'}\n",
        "        req = requests.post('http://127.0.0.1:5000/register', data = details)\n",
        "        req = requests.post('http://127.0.0.1:5000/login', data = details)\n",
        "        self.assertEqual(req.url, 'http://127.0.0.1:5000/main')\n",
        "\n",
        "    '''\n",
        "    This functions tests that users with the proper credentials can login and view their data. \n",
        "    '''\n",
        "    def test_correct_login(self):        \n",
        "        details = {'username':'Dolly',  'password':'ncelekckln!mv'}\n",
        "        req = requests.post('http://127.0.0.1:5000/login', data = details)\n",
        "        self.assertEqual(req.url, 'http://127.0.0.1:5000/main')\n",
        "    '''\n",
        "    This function tests that users that are not registered cannot login \n",
        "    '''\n",
        "    def test_faulty_login(self):\n",
        "        details = {'username':'Rita', 'password':'fake'}\n",
        "        req = requests.post('http://127.0.0.1:5000/login', data = details)\n",
        "        self.assertEqual(req.url, 'http://127.0.0.1:5000/login')\n",
        "\n",
        "#Running the tests\n",
        "if __name__ == \"__main__\":\n",
        "    unittest.main()"
      ],
      "metadata": {
        "id": "nsGLLSe2GnKi"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}