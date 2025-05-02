import re
from behave import given
from playwright.sync_api import expect

@given(u'Jag navigerar till webbsidan "Läslistan"')
def step_given_start(context):
    context.page.goto(context.base_url)
    expect(context.page).to_have_title(re.compile("Läslistan"))