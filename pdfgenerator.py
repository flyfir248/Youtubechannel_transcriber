from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(input_filename, output_filename, encoding='utf-8'):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    with open(input_filename, 'r', encoding=encoding) as f:
        lines = f.readlines()

    paragraphs = []
    for line in lines:
        line = line.strip()
        if line:
            paragraph = Paragraph(line, styles['Normal'])
            paragraphs.append(paragraph)
            paragraphs.append(Spacer(1, 12))  # Add some space between paragraphs

    doc.build(paragraphs)


if __name__ == "__main__":
    input_filename = "Transcripts.txt"  # Provide the input text file name
    output_filename = "output.pdf"  # Provide the desired output PDF file name

    create_pdf(input_filename, output_filename)
    print(f"PDF generated: {output_filename}")
