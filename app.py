import os
from flask import Flask, request, send_file, render_template_string
from PIL import Image
import pytesseract
import pandas as pd
import io

# 🚨 CRITICAL FIX: SET THE TESSERACT EXECUTABLE PATH HERE 🚨
# Use 'r' before the string (r'...') to handle backslashes correctly
# REPLACE THE EXAMPLE PATH BELOW WITH YOUR ACTUAL PATH!
# The original error message implies this is the path:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
# ... rest of your code ...
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# A simple HTML template for a single-file application
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image to Excel Converter</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; text-align: center; }
        .container { max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; }
        input[type="file"] { margin: 15px 0; }
        button { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #45a049; }
        #status { margin-top: 20px; font-weight: bold; }
        #download-link { display: none; margin-top: 20px; }
        #download-link a { text-decoration: none; color: royalblue; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Image (PNG/JPG) to Excel Converter</h2>
        <form id="upload-form" enctype="multipart/form-data">
            <input type="file" name="file" id="file-input" accept=".png, .jpg, .jpeg" required>
            <br>
            <button type="submit">Convert and Download Excel</button>
        </form>
        <div id="status"></div>
        <div id="download-link">
            <a id="download-anchor" href="#" download="converted_table.xlsx">✅ Download Converted Excel File</a>
        </div>
    </div>

    <script>
        document.getElementById('upload-form').addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const statusDiv = document.getElementById('status');
            const downloadLinkDiv = document.getElementById('download-link');
            const downloadAnchor = document.getElementById('download-anchor');
            
            statusDiv.textContent = 'Processing... Please wait.';
            downloadLinkDiv.style.display = 'none';

            const formData = new FormData(this);

            try {
                const response = await fetch('/convert', {
                    method: 'POST',
                    body: formData
                });
                
                if (response.ok) {
                    // Get the file content as a Blob
                    const blob = await response.blob();
                    
                    // Create a URL for the Blob
                    const fileURL = URL.createObjectURL(blob);
                    
                    // Set the download link properties
                    downloadAnchor.href = fileURL;
                    
                    // Display the success message and download link
                    statusDiv.textContent = 'Conversion successful!';
                    downloadLinkDiv.style.display = 'block';

                    // Optional: Clean up the blob URL after a short delay
                    setTimeout(() => URL.revokeObjectURL(fileURL), 30000); 

                } else {
                    const errorText = await response.text();
                    statusDiv.textContent = 'Error: ' + errorText;
                }
            } catch (error) {
                statusDiv.textContent = 'Network Error: ' + error.message;
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Renders the HTML form."""
    return HTML_TEMPLATE

@app.route('/convert', methods=['POST'])
def convert_image_to_excel():
    """Handles file upload, OCR, and Excel conversion/download."""
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    if file:
        try:
            # 1. Image Processing with PIL
            img = Image.open(file.stream)
            
            # 2. OCR with Tesseract
            # Use 'psm 6' (Assume a single uniform block of text) and 'TESSDATA_CONFIG' for table-specific settings
            # The 'preserve_interword_spaces=False' is often helpful for structured data
            text = pytesseract.image_to_string(img, config='--psm 6')
            
            # 3. Simple Table Conversion (The most complex and error-prone step)
            # This is a basic attempt. Real table extraction is much harder!
            
            # Split the text into lines
            lines = text.strip().split('\n')
            
            # Simple assumption: data is separated by tabs/spaces or a consistent delimiter
            # We'll treat the output as a single block of text and try to parse it.
            # A common simple method is to create a list of lists (rows of cells)
            data = []
            for line in lines:
                # Basic attempt to split based on multiple spaces (common in tables)
                # This is highly unreliable and depends heavily on the image quality/structure.
                cells = [cell.strip() for cell in line.split('  ') if cell.strip()] 
                if cells:
                    data.append(cells)
            
            # Find the maximum number of columns for consistent dataframe creation
            max_cols = max(len(row) for row in data) if data else 0
            
            # Pad shorter rows to match the max columns
            padded_data = [row + [''] * (max_cols - len(row)) for row in data]

            # 4. Create a DataFrame and Excel file in memory
            df = pd.DataFrame(padded_data)
            
            # Use io.BytesIO to keep the file in memory
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, header=False, sheet_name='Extracted Data')
            
            output.seek(0) # Go back to the start of the stream

            # 5. Return the file for download
            return send_file(
                output,
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                as_attachment=True,
                download_name='converted_table.xlsx' # The filename for the download
            )

        except Exception as e:
            # Catch errors during processing
            return str(e), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True) # Run with 'debug=True' for development