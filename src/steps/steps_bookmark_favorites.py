import re
from playwright.sync_api import expect

@when(u'jag är på sidan "Katalog"')
def step_when_catalog(context):
    catalog_button = context.page.get_by_test_id("catalog")
    context.catalog_button = catalog_button
    expect(context.catalog_button).to_be_disabled()


@then(u'jag hovrar över en bok')
def step_then_hoover(context):
    book_cat = context.page.get_by_test_id("star-Min katt är min chef")
    book_cat.hover()


@then(u'Ser jag att raden med boken ändrar färg och att det visas ett hjärta i början av raden')
def step_then_show_heart(context):
    book_cat_heart = context.page.get_by_test_id("star-Min katt är min chef")
    expect(book_cat_heart).to_have_class(re.compile(r"\bstar\b"))


@then(u'Klickar jag på hjärtat för att favoritmärka vald bok')
def step_then_click_heart(context):
    book_cat_click_heart = context.page.get_by_test_id("star-Min katt är min chef")
    book_cat_click_heart.click()
    expect(book_cat_click_heart).to_have_class(re.compile(r"\bselected\b"))


@then(u'navigerar jag till sidan "Mina böcker"')
def step_then_my_books(context):
    my_books_button = context.page.get_by_test_id("favorites")
    my_books_button.click()


@then(u'kontrollerar jag att min senast favoritmarkerad bok finns i listan')
def step_then_verify_favorit_book(context):
    #my_book_cat = context.page.get_by_role('listitem')
    my_book_cat = context.page.get_by_test_id("fav-Min katt är min chef")
    expect(my_book_cat).to_have_text("Min katt är min chef")