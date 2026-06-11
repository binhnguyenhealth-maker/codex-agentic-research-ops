from pathlib import Path

from scripts.validate_packet import validate, TASK_REQUIRED, RESULT_REQUIRED


def test_task_packet_example_passes():
    path = Path("examples/fake-ml-cycle/task-packet.md")
    assert validate(path, TASK_REQUIRED) == []


def test_worker_result_example_passes():
    path = Path("examples/fake-ml-cycle/worker-result.md")
    assert validate(path, RESULT_REQUIRED) == []


def test_unsafe_phrase_is_rejected(tmp_path):
    path = tmp_path / "bad.md"
    path.write_text("\n".join(TASK_REQUIRED) + "\ndo whatever\n", encoding="utf-8")
    errors = validate(path, TASK_REQUIRED)
    assert "unsafe phrase: do whatever" in errors
