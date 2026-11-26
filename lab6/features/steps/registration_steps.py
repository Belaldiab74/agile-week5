from behave import given, then, when

from registration import RegistrationError, Student


@given('a student with ID "{student_id}"')
def step_student(context, student_id):
    context.student = Student(student_id)
    context.error = None


@given("the student already has {hours:d} registered hours")
def step_existing_hours(context, hours):
    context.student.register("FILLER", hours)


@given('the student is registered for "{code}" worth {hours:d} hours')
def step_registered(context, code, hours):
    context.student.register(code, hours)


@when('the student registers for "{code}" worth {hours:d} hours')
def step_register(context, code, hours):
    context.error = None
    try:
        context.student.register(code, hours)
    except RegistrationError as error:
        context.error = str(error)


@when('the student drops "{code}"')
def step_drop(context, code):
    context.student.drop(code)


@then("the student has {hours:d} registered hours")
def step_hours(context, hours):
    assert context.student.total_hours == hours


@then('the registration is refused with "{text}"')
def step_refused(context, text):
    assert context.error is not None and text in context.error, context.error


@then('the result is "{result}"')
def step_result(context, result):
    actual = "refused" if context.error else "accepted"
    assert actual == result, actual
