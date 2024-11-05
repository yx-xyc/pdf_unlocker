import PyPDF2
import os
from pathlib import Path

def unlock_pdf(input_path, output_path, password):
    """
    Creates an unlocked copy of a password-protected PDF.
    Parameters:
    input_path (str): Path to the locked PDF file
    output_path (str): Path where the unlocked PDF will be saved
    password (str): Password for the locked PDF
    """
    try:
        # Open the locked PDF
        reader = PyPDF2.PdfReader(input_path)
        # Check if PDF is encrypted
        if reader.is_encrypted:
            # Decrypt with provided password
            result = reader.decrypt(password)
            if result == 0:
                raise ValueError("Incorrect password")
            
            # Create a writer object for the unlocked copy
            writer = PyPDF2.PdfWriter()
            # Copy all pages to the writer
            for page in reader.pages:
                writer.add_page(page)
            
            # Write the unlocked PDF to the output file
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            print(f"Successfully created unlocked PDF at: {output_path}")
        else:
            print(f"PDF is not encrypted: {input_path}")
            
    except FileNotFoundError:
        print("Error: Input file not found")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def process_folder(folder_path, password):
    """
    Process all PDF files in the specified folder and create unlocked copies if needed.
    Parameters:
    folder_path (str): Path to the folder containing PDF files
    password (str): Password to try for locked PDFs
    """
    try:
        # Convert folder path to Path object for easier handling
        folder = Path(folder_path)
        
        if not folder.exists():
            raise FileNotFoundError(f"Folder not found: {folder_path}")
        
        # Get all PDF files in the folder
        pdf_files = list(folder.glob("*.pdf"))
        
        if not pdf_files:
            print(f"No PDF files found in {folder_path}")
            return
        
        print(f"Found {len(pdf_files)} PDF files in the folder")
        
        for pdf_file in pdf_files:
            # Skip files that start with "Unlocked-"
            if pdf_file.name.startswith("Unlocked-"):
                print(f"Skipping already unlocked file: {pdf_file.name}")
                continue
                
            # Check if an unlocked version already exists
            unlocked_name = f"Unlocked-{pdf_file.name}"
            unlocked_path = pdf_file.parent / unlocked_name
            
            if unlocked_path.exists():
                print(f"Unlocked version already exists for: {pdf_file.name}")
                continue
            
            print(f"\nProcessing: {pdf_file.name}")
            unlock_pdf(str(pdf_file), str(unlocked_path), password)
            
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred while processing folder: {str(e)}")

if __name__ == '__main__':
    # Example usage
    folder_path = "/Users/yanchong/Dropbox/Documents/nyu_mscs/CSCI-GA-2262/Slides"
    password = "DCNFALL2024%-"
    
    process_folder(folder_path, password)