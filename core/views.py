from django.shortcuts import render


def home(request):
    questions = [
        {
            "title": "How can I fix a Django template not found error?",
            "excerpt": "I'm building a Django application and my view loads correctly, but Django keeps returning a TemplateDoesNotExist error when I try to render the page. What should I check in my template configuration?",
            "votes": 24,
            "answers": 3,
            "views": 182,
            "tag1": "django",
            "tag2": "python",
            "tag3": "templates",
            "author": "Aarav",
            "reputation": "1,420",
            "time": "asked 18 minutes ago",
        },
        {
            "title": "Why is my JavaScript fetch request returning an empty response?",
            "excerpt": "My API endpoint works when I test it directly, but the fetch request from my JavaScript code does not return the expected JSON data. How can I debug this?",
            "votes": 17,
            "answers": 2,
            "views": 96,
            "tag1": "javascript",
            "tag2": "fetch",
            "tag3": "api",
            "author": "Riya",
            "reputation": "860",
            "time": "asked 42 minutes ago",
        },
        {
            "title": "How do I join two tables using Django ORM?",
            "excerpt": "I have a Customer model and an Order model and need to display orders along with customer information. What is the recommended way to handle this using Django's ORM?",
            "votes": 31,
            "answers": 5,
            "views": 241,
            "tag1": "django",
            "tag2": "python",
            "tag3": "django-orm",
            "author": "Kabir",
            "reputation": "2,130",
            "time": "asked 1 hour ago",
        },
        {
            "title": "Why does my CSS grid layout break on smaller screens?",
            "excerpt": "The layout looks correct on desktop, but some grid items overflow when the browser width becomes smaller. How can I make the grid responsive?",
            "votes": 9,
            "answers": 1,
            "views": 73,
            "tag1": "css",
            "tag2": "html",
            "tag3": "responsive-design",
            "author": "Neha",
            "reputation": "540",
            "time": "asked 2 hours ago",
        },
        {
            "title": "What is the difference between INNER JOIN and LEFT JOIN in SQL?",
            "excerpt": "I'm learning SQL joins and understand the basic syntax, but I'm still confused about when I should use an INNER JOIN versus a LEFT JOIN. Can someone explain the practical difference?",
            "votes": 14,
            "answers": 4,
            "views": 128,
            "tag1": "sql",
            "tag2": "mysql",
            "tag3": "database",
            "author": "Dev",
            "reputation": "1,080",
            "time": "asked 3 hours ago",
        },
    ]


    return render(request, "home.html", {"questions": questions})
