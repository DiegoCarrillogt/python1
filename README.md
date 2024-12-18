# NFC Web Reader

A full-stack web application that enables browser-based NFC communication using Python and Flask.

## Prerequisites

- Python 3.7 or higher
- NFC Reader hardware compatible with nfcpy
- Modern web browser
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your NFC reader is connected to your computer via USB.

2. Start the Flask application:
```bash
python src/app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Features

- Real-time NFC reader status monitoring
- NFC tag reading capability
- Modern web interface
- Automatic status updates
- JSON API endpoints for NFC operations

## API Endpoints

- GET `/api/nfc/status` - Check NFC reader connection status
- GET `/api/nfc/read` - Read current/last NFC tag data

## Troubleshooting

1. If the NFC reader is not detected:
   - Ensure the NFC reader is properly connected via USB
   - Check if you have the necessary permissions to access the USB device
   - On Linux, you might need to run the application with sudo

2. If the web interface shows "disconnected":
   - Refresh the page
   - Check if the Flask server is running
   - Verify the NFC reader connection

## Security Notes

This application is designed for local use. If you plan to deploy it in a production environment, additional security measures should be implemented:

- Enable HTTPS
- Add authentication
- Implement rate limiting
- Configure proper CORS settings

## License

MIT License
