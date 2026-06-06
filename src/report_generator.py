from reportlab.pdfgen import canvas

def generate_report(
    score,
    matched,
    missing
):

    file_name = "report.pdf"

    c = canvas.Canvas(
        file_name
    )

    c.drawString(
        100,
        800,
        f"ATS Score: {score}%"
    )

    c.drawString(
        100,
        760,
        f"Matched Skills: {', '.join(matched)}"
    )

    c.drawString(
        100,
        720,
        f"Missing Skills: {', '.join(missing)}"
    )

    c.save()

    return file_name