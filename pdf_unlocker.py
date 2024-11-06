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

def process_path(input_path, password):
    """
    Process either a single PDF file or all PDF files in a folder.
    
    Parameters:
    input_path (str): Path to either a PDF file or a folder containing PDF files
    password (str): Password to try for locked PDFs
    """
    try:
        # Convert input path to Path object
        path = Path(input_path)
        
        if not path.exists():
            raise FileNotFoundError(f"Path not found: {input_path}")
        
        if path.is_file():
            # Process single file
            if path.suffix.lower() == '.pdf':
                if path.name.startswith("Unlocked-"):
                    print(f"Skipping already unlocked file: {path.name}")
                    return
                    
                unlocked_name = f"Unlocked-{path.name}"
                unlocked_path = path.parent / unlocked_name
                
                if unlocked_path.exists():
                    print(f"Unlocked version already exists for: {path.name}")
                    return
                    
                print(f"\nProcessing file: {path.name}")
                unlock_pdf(str(path), str(unlocked_path), password)
            else:
                print(f"Error: {path.name} is not a PDF file")
                
        elif path.is_dir():
            # Process all PDFs in folder
            pdf_files = list(path.glob("*.pdf"))
            
            if not pdf_files:
                print(f"No PDF files found in {input_path}")
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
        else:
            print(f"Error: {input_path} is neither a file nor a directory")
            
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred while processing path: {str(e)}")

if __name__ == '__main__':
    # Example usage
    # For a single file:
    file_path = "/Users/yanchong/Dropbox/Documents/nyu_mscs/CSCI-GA-2433/Project/ProjectPart2.pdf"
    password = "DMSFALL2024%-"
    process_path(file_path, password)
    
    # For a folder:
    # folder_path = "/path/to/your/pdf/folder"
    # process_path(folder_path, password)