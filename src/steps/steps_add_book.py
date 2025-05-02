import re
from playwright.sync_api import expect

@then(u'Jag klickar på fältet "Titel" och lägger till en boktitel')
def step_then_title(context):
    title_input = context.page.get_by_test_id("add-input-title")
    title_input.click()
    title_input.fill("Min första bok")


@then(u'Jag klickar på fältet "Författare" och lägger till bokens författare')
def step_then_author(context):
    author_input = context.page.get_by_test_id("add-input-author")
    author_input.click()
    author_input.fill("Anette Cedergren")


@then(u'Jag klickar på knappen "Lägg till ny bok"')
def step_then_save(context):
    save_button = context.page.get_by_test_id("add-submit")
    save_button.click()


@then(u'Det ska inte gå att klicka på knappen "Lägg till ny bok"')
def step_then_disable_save(context):
    save_button = context.page.get_by_test_id("add-submit")
    expect(save_button).to_be_disabled()


@then(u'jag verifierar att boken finns med som jag precis skapade')
def step_added_book(context):
    my_book = context.page.locator(".book").filter(has_text=re.compile(r"Min första bok", re.IGNORECASE))
    expect(my_book).to_have_text(re.compile(r'Min första bok'))

