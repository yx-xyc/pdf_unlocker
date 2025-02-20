# PDF Unlocker

A Python script that unlocks password-protected PDF files.

## Description

Given a locked PDF and its password, this script creates an unlocked version of the PDF file.

## Prerequisites

- Python 3.x
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf-unlocker.git
cd pdf-unlocker
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python pdf_unlocker.py [input_pdf] [password]
```

Example:
```bash
python pdf_unlocker.py locked.pdf mypassword123
```

## Project Structure
```
pdf-unlocker/
├── .venv/              # Virtual environment directory
├── pdf_unlocker.py     # Main script
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## License

[Include your license information here]

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request