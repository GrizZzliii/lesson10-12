from behave import given, when, then

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    context.browser.get('http://example.com/login')

@when('the user enters valid credentials')
def step_when_user_enters_credentials(context):
    context.browser.find_element_by_name('username').send_keys('valid_user')
    context.browser.find_element_by_name('password').send_keys('valid_password')
    context.browser.find_element_by_name('submit').click()

@then('the user should be redirected to the dashboard')
def step_then_user_redirected(context):
    assert context.browser.current_url == 'http://example.com/dashboard'

@given('the user is logged in')
def step_given_user_logged_in(context):
    step_given_user_on_login_page(context)
    step_when_user_enters_credentials(context)

@when('the user selects a room from the list')
def step_when_user_selects_room(context):
    context.browser.find_element_by_id('room-select').click()

@then('the selected room should be displayed in the dashboard')
def step_then_room_displayed(context):
    selected_room = context.browser.find_element_by_id('selected-room').text
    assert selected_room is not None

@given('the user is on the room dashboard')
def step_given_user_on_room_dashboard(context):
    step_given_user_logged_in(context)
    context.browser.get('http://example.com/room_dashboard')

@when('the user selects a cleaning program')
def step_when_user_selects_cleaning_program(context):
    context.browser.find_element_by_id('cleaning-program-select').click()

@then('the selected cleaning program should be active')
def step_then_cleaning_program_active(context):
    active_program = context.browser.find_element_by_id('active-program').text
    assert active_program is not None

@given('the user is on the cleaning program page')
def step_given_user_on_cleaning_program_page(context):
    step_given_user_on_room_dashboard(context)
    context.browser.get('http://example.com/cleaning_program')

@when('the user sets a cleaning schedule')
def step_when_user_sets_cleaning_schedule(context):
    context.browser.find_element_by_id('schedule-input').send_keys('09:00 AM')
    context.browser.find_element_by_id('save-schedule').click()

@then('the schedule should be saved successfully')
def step_then_schedule_saved(context):
    success_message = context.browser.find_element_by_id('success-message').text
    assert "Schedule saved" in success_message

@given('the user is on the dashboard')
def step_given_user_on_dashboard(context):
    step_given_user_logged_in(context)
    context.browser.get('http://example.com/dashboard')

@when('the user clicks on the statistics button')
def step_when_user_clicks_statistics_button(context):
    context.browser.find_element_by_id('statistics-button').click()

@then('the cleaning statistics should be displayed')
def step_then_statistics_displayed(context):
    statistics = context.browser.find_element_by_id('cleaning-statistics').text
    assert statistics is not None