from app.services import report_generator


def test_create_experiment_report_creates_pdf(tmp_path):
    output_file = tmp_path / "experiment_report.pdf"

    generated_file = report_generator.create_experiment_report(
        output_path=output_file,
        carrier_type="Image PNG",
        operation="Embed and Encrypt",
        result="Message successfully hidden in image.",
        detection_result={
            "balance_score": 0.94,
            "suspicion": "medium",
            "total_bits_analyzed": 30000,
        },
    )

    assert generated_file == output_file
    assert output_file.exists()
    assert output_file.read_bytes().startswith(b"%PDF")
    assert output_file.stat().st_size > 100