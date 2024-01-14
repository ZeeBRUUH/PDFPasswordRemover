import argparse
import pikepdf

def remove_pdf_password(input_pdf_path, output_pdf_path, password):
    try:
        # Open the PDF with the provided password
        with pikepdf.open(input_pdf_path, password=password) as pdf:
            # Save the PDF without a password
            pdf.save(output_pdf_path)
        print(f"Password removed successfully. Saved as '{output_pdf_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Remove password from a PDF file.")

    # Add the arguments
    parser.add_argument("input_pdf", help="The path to the input PDF file.")
    parser.add_argument("output_pdf", help="The path to save the output PDF file.")
    parser.add_argument("password", help="The password of the PDF file.")

    # Execute the parse_args() method
    args = parser.parse_args()

    remove_pdf_password(args.input_pdf, args.output_pdf, args.password)

if __name__ == "__main__":
    main()
