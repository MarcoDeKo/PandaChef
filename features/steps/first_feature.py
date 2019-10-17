import behave

@given('the number {number:d}')
def given_first(context, number):
    context.first = number

@given('the other number {number:d}')
def given_second(context, number):
    context.second = number

@when('I add them')
def when_add(context):
    context.actual = context.first + context.second

@then('I get {expected:d}')
def then_res(context, expected):
    assert context.actual == expected

