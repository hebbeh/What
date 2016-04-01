from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

# Add two items to our main menu
Menu.add_item("main", MenuItem("Tools",
                               reverse("addStudent"))

Menu.add_item("main", MenuItem("Reports",
                               reverse("addTask"))
