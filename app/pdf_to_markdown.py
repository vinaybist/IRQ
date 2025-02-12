#IGNORE-IGNORE-IGNORE
# This is independent utility. Not part of the project
import fitz  # PyMuPDF
import re
import argparse
from pathlib import Path

def extract_text_with_formatting(page):
    """Extract text while preserving basic formatting"""
    blocks = page.get_text("dict")["blocks"]
    text_parts = []
    current_text = []
    
    for block in blocks:
        if "lines" in block:
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"]
                    font_size = span["size"]
                    is_bold = "bold" in span.get("font", "").lower()
                    
                    # Detect headings based on font size
                    if font_size > 14:  # Assuming larger font indicates heading
                        if current_text:
                            text_parts.append(" ".join(current_text))
                            current_text = []
                        text_parts.append(f"\n## {text}\n")
                    elif font_size > 12:  # Subheading
                        if current_text:
                            text_parts.append(" ".join(current_text))
                            current_text = []
                        text_parts.append(f"\n### {text}\n")
                    else:
                        # Handle bold text
                        if is_bold:
                            text = f"**{text}**"
                        current_text.append(text)
                
                # Add line break at the end of each line
                if current_text:
                    text_parts.append(" ".join(current_text))
                    current_text = []
                text_parts.append("\n")
    
    return "".join(text_parts)

def clean_markdown(text):
    """Clean and format the markdown text"""
    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Fix list items
    text = re.sub(r'(?m)^[-•]\s', '- ', text)
    
    # Fix numbered lists
    text = re.sub(r'(?m)^\d+[\.)]\s', '1. ', text)
    
    # Fix spaces around bold text
    text = re.sub(r'\*\*\s+', '**', text)
    text = re.sub(r'\s+\*\*', '**', text)
    
    return text.strip()

def pdf_to_markdown(pdf_path, output_path=None):
    """Convert PDF to Markdown"""
    try:
        # Open PDF
        doc = fitz.open(pdf_path)
        markdown_content = []
        
        # Process each page
        for page_num in range(len(doc)):
            page = doc[page_num]
            markdown_content.append(extract_text_with_formatting(page))
        
        # Combine and clean content
        markdown_text = clean_markdown("\n".join(markdown_content))
        
        # Determine output path
        if output_path is None:
            output_path = Path(pdf_path).with_suffix('.md')
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        
        print(f"Successfully converted {pdf_path} to {output_path}")
        return True
    
    except Exception as e:
        print(f"Error converting PDF: {str(e)}")
        return False
    
    finally:
        if 'doc' in locals():
            doc.close()

def main():
    parser = argparse.ArgumentParser(description='Convert PDF to Markdown')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Output markdown file path (optional)')
    
    args = parser.parse_args()
    pdf_to_markdown(args.pdf_path, args.output)

if __name__ == "__main__":
    main()
