import json
import os
import random
from pathlib import Path

import pytest
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from playwright.sync_api import Playwright, APIRequestContext, expect, Page

from core.facad import ApiClient

load_dotenv()

import logging

logger = logging.getLogger('setUp')


@pytest.fixture(scope="session")
def console_error_log(tmp_path_factory) -> Path:
    """Ініціалізує файл для збору помилок консолі браузера на рівні тестової сесії."""
    log_dir = Path(__file__).resolve().parent / "reports"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "console_errors.json"

    # Створюємо або перезаписуємо порожнім JSON-об'єктом
    log_file.write_text(json.dumps({}), encoding="utf-8")
    return log_file


@pytest.fixture(scope="function")
def ui_test_fixture(page: Page, request, console_error_log) -> Page:
    test_name = request.node.name
    console_logs = []

    page.on("console", lambda msg: console_logs.append(msg))

    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    try:
        test_failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed
        console_errors = [msg.text for msg in console_logs if msg.type == "error"]

        if test_failed:
            log_text = "\n".join([f"{msg.type.upper()} - {msg.text}" for msg in console_logs])
            if log_text:
                attach(log_text, name="Browser Console Log", attachment_type=AttachmentType.TEXT)

            screenshot = page.screenshot(full_page=True)
            attach(screenshot, name=f"{test_name}_screenshot", attachment_type=AttachmentType.PNG)

        if test_failed or console_errors:
            traces_dir = os.path.join(os.path.dirname(__file__), "..", "..", "traces")
            os.makedirs(traces_dir, exist_ok=True)
            safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in test_name)
            local_trace_path = os.path.join(traces_dir, f"{safe_name}.zip")
            page.context.tracing.stop(path=local_trace_path)
            logger.info(f"Trace saved: {os.path.abspath(local_trace_path)}")
            with open(local_trace_path, "rb") as f:
                attach(f.read(), name=f"{test_name}_trace.zip", attachment_type="application/zip")

            if console_errors:
                data = json.loads(console_error_log.read_text(encoding="utf-8"))
                data[test_name] = {
                    "errors": console_errors,
                    "trace_path": str(Path(local_trace_path).resolve()),
                }
                console_error_log.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        else:
            page.context.tracing.stop()
    except Exception as e:
        logger.warning(f"Error while capturing diagnostics: {e}")


@pytest.fixture(scope="session")
def api() -> ApiClient:
    return ApiClient()


@pytest.fixture()
def api_browser(playwright: Playwright):
    api_browser = playwright.request.new_context(
        base_url=os.getenv('BASIC_URL')
    )

    yield api_browser

    api_browser.dispose()


@pytest.fixture()
def api_pl(api_browser: APIRequestContext):
    response_login = api_browser.post(
        url='/api/auth/signin',
        data={
            "email": os.getenv('USER_LOGIN'),
            "password": os.getenv('USER_PASSWORD'),
        }
    )
    expect(response_login).to_be_ok()
    yield api_browser


@pytest.fixture
def delete_car_api(api):
    list_obj_to_delete = []
    yield list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            car_id_to_delete = api.car.delete_car(resp)
            car_reps_id = api.car.get_car_by_id(resp, 404)


@pytest.fixture
def delete_car(api):
    list_obj_to_delete = []
    yield api, list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            car_id = resp.json().get('data').get('id')
            car_id_to_delete = api.car.delete_car(car_id)
            car_reps_id = api.car.get_car_by_id(car_id, 404)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "base_url": os.getenv('BASIC_URL'),
        "http_credentials": {
            "username": os.getenv('BASIC_AUTH_USER'),
            "password": os.getenv('BASIC_AUTH_PASS')
        }
    }


@pytest.fixture
def our_first_fixture():
    str_to_test = f'ID USER {random.choice(range(1, 23454))}'

    yield str_to_test
    print(f'I DELETE USER {our_first_fixture}')


@pytest.fixture
def create_and_delete_user(our_first_fixture):
    print(f'I CREATE USER {our_first_fixture}')
    yield our_first_fixture
    print(f'I DELETE USER {our_first_fixture}')


@pytest.fixture
def create_and_delete_user_1():
    print(f'I CREATE USER')


@pytest.fixture
def create_user():
    value_to_return = 'I CREATE USER {random.choice(range(1, 23454))} _V2'
    print(value_to_return)
    yield our_first_fixture


@pytest.fixture(scope='function')
def delete_user():
    object_values = []
    yield object_values
    if object_values:
        for value in object_values:
            ids = value
            print(f'DELETE USER {ids}')


#

@pytest.fixture
def create_and_delete_user_v2(create_user, delete_user):
    create_user, delete_user = create_user, delete_user
    yield create_user, delete_user
