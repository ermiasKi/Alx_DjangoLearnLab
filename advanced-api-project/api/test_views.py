from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from django.urls import reverse


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Authenticate client
        self.client.force_authenticate(user=self.user)

        # Create author
        self.author = Author.objects.create(name="John Doe")

        # Create books
        self.book1 = Book.objects.create(title="Django Basics", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Python Advanced", publication_year=2018, author=self.author)

    # -----------------
    # CRUD Tests
    # -----------------
    def test_create_book(self):
        url = reverse("book-list")  # from DRF router
        data = {"title": "New Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_retrieve_book_list(self):
        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Basics")

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        data = {"title": "Django Basics Updated", "publication_year": 2021, "author": self.author.id}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Django Basics Updated")

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # -----------------
    # Filtering / Search / Ordering
    # -----------------
    def test_filter_books_by_publication_year(self):
        url = reverse("book-list") + "?publication_year=2020"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["publication_year"] == 2020 for book in response.data))

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Django"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Django" in book["title"] for book in response.data))

    def test_order_books_by_year(self):
        url = reverse("book-list") + "?ordering=publication_year"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

    # -----------------
    # Permissions
    # -----------------
    def test_unauthenticated_user_cannot_create_book(self):
        self.client.login()
        self.client.logout()
        url = reverse("book-list")
        data = {"title": "Unauthorized Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
