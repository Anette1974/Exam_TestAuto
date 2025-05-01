
import re
from behave import given, when, then
from playwright.sync_api import expect

@given(u'Jag navigerar till webbsidan "Läslistan"')
def step_given_start(context):
    context.page.goto(context.base_url)
    expect(context.page).to_have_title(re.compile("Läslistan"))

@when(u'jag klickar på knappen "Lägg till bok"')
def step_when_add_book_button(context):
    add_book_button = context.page.get_by_test_id("add-book")
    add_book_button.click()
    context.add_book_button = add_book_button

@then(u'ska knappen "Lägg till bok" ändra färg och inte gå att klicka på')
def step_then_add_book_disabled(context):
    expect(context.add_book_button).to_be_disabled()

@then(u'jag klickar på knappen "Mina böcker"')
def step_when_my_books(context):
    my_books_button = context.page.get_by_test_id("favorites")
    my_books_button.click()
    context.my_books_button = my_books_button

@then(u'ska knappen "Mina böcker" ändra färg och inte gå att klicka på')
def step_then_my_books_disabled(context):
    expect(context.my_books_button).to_be_disabled()

@then(u'jag klickar på knappen "Katalog"')
def step_then_catalogue(context):
    catalog_button = context.page.get_by_test_id("catalog")
    catalog_button.click()
    context.catalogue_button = catalog_button

@then(u'ska knappen "Katalog" ändra färg och inte gå att klicka på')
def step_then_catalogue_disabled(context):
    expect(context.catalogue_button).to_be_disabled()