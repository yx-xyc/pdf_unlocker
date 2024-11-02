import PyPDF2

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
        
    except FileNotFoundError:
        print("Error: Input file not found")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == '__main__':
    unlock_pdf(
        "/Users/yanchong/Downloads/Lab6TransportLayer.pdf",
        "/Users/yanchong/Downloads/UnlockedLab6TransportLayer.pdf",
        "DCNFALL2024%-"
        )
# unlock_pdf('locked.pdf', 'unlocked.pdf', 'your_password')