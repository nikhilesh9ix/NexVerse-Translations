# NexVerse-Translations 🌐

> A powerful and intuitive multilingual translation application with text-to-speech capabilities, built with Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nexverse-translations.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🚀 **[Live Demo](https://nexverse-translations.streamlit.app/)** | 📚 [Documentation](#-table-of-contents) | 🐛 [Report Bug](https://github.com/nikhilesh9ix/NexVerse-Translations/issues)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

NexVerse-Translations is a user-friendly web application that breaks down language barriers by providing instant text and document translation services. With support for multiple languages categorized into Indian and World languages, users can translate text, upload PDF documents for translation, and even listen to the translated output with text-to-speech functionality.

## ✨ Features

### 🔤 Text Translation
- **Real-time Translation**: Instantly translate text between 50+ supported languages
- **Auto Language Detection**: Automatically detects the source language of your input
- **Bilingual Audio Playback**: Listen to both original and translated text
- **Audio Download**: Save translated audio as MP3 files for offline use

### 📄 PDF Translation
- **Document Upload**: Upload PDF files for complete document translation
- **Text Extraction**: Automatically extracts text from PDF documents
- **Batch Translation**: Translate entire documents in seconds
- **Audio Generation**: Convert translated PDF content to speech

### 🌍 Language Support
- **Categorized Languages**: Easy navigation with Indian and World language categories
- **Indian Languages**: Hindi, Bengali, Telugu, Marathi, Tamil, Urdu, Gujarati, Malayalam, Kannada, Odia, Punjabi
- **World Languages**: English, Spanish, French, German, Chinese, Japanese, and 40+ more

### 💡 Additional Features
- **User Feedback System**: Built-in feedback mechanism for continuous improvement
- **Clean & Intuitive UI**: Modern interface built with Streamlit
- **Responsive Design**: Works seamlessly across different screen sizes
- **No API Keys Required**: Utilizes free translation services

## 🎬 Demo

### 🌟 [Try Live Demo](https://nexverse-translations.streamlit.app/)

Experience NexVerse-Translations in action! The application is deployed and ready to use.

**Quick Start Guide:**
```
1. Visit https://nexverse-translations.streamlit.app/
2. Select "Translate Sentence" or "Translate PDF"
3. Choose language category (Indian/World Languages)
4. Enter text or upload PDF
5. Select target language
6. Click "Translate" to see results with audio playback
7. Download audio files for offline use
```

[Add screenshots or GIF of your application here]

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web application framework |
| **Deep Translator** | Translation engine (Google Translate API) |
| **gTTS** | Google Text-to-Speech for audio generation |
| **PyPDF2** | PDF text extraction |
| **langdetect** | Automatic language detection |

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/nikhilesh9ix/NexVerse-Translations.git
   cd NexVerse-Translations
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run final_p.py
   ```

5. **Open in browser**
   - The app will automatically open in your default browser
   - Or navigate to `http://localhost:8501`

## 🚀 Usage

### Translating Text

1. Select **"Translate Sentence"** option
2. Enter your text in the input field
3. Choose language category (Indian or World Languages)
4. Select your target language from the dropdown
5. Click **"Translate"** button
6. View detected language and play original audio
7. View translated text and play translated audio
8. Download the audio file if needed

### Translating PDF Documents

1. Select **"Translate PDF"** option
2. Upload your PDF file using the file uploader
3. View the extracted text from your PDF
4. Choose language category for translation
5. Select your target language
6. Click **"Translate PDF Text"** button
7. View translated text with audio playback option
8. Download the translated audio file

### Providing Feedback

- Use the sidebar feedback form to share your experience
- Enter your feedback (max 500 characters)
- Click "Submit Feedback" to send

## 📁 Project Structure

```
NexVerse-Translations/
│
├── final_p.py              # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
│
├── .gitignore             # Git ignore file
└── LICENSE                # License file
```

### Key Functions

- `get_key(val)`: Retrieves language code from language name
- `categorize_languages()`: Separates languages into Indian and World categories
- `read_pdf(file)`: Extracts text from uploaded PDF files
- `translate_pdf_text(pdf_text, dest_lang)`: Translates PDF text to target language
- `collect_feedback()`: Handles user feedback collection
- `main()`: Main application logic and UI rendering

## 🌐 Deployment

### Streamlit Community Cloud (Recommended - FREE)

1. **Prepare your repository**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click **"New app"**
   - Select repository: `nikhilesh9ix/NexVerse-Translations`
   - Set main file path: `final_p.py`
   - Click **"Deploy"**

3. **Access your live app**
   - Your app will be available at: `https://[your-app-name].streamlit.app`
   - **Example**: This project is live at [nexverse-translations.streamlit.app](https://nexverse-translations.streamlit.app/)

### Alternative Deployment Options

<details>
<summary><b>Render</b></summary>

1. Visit [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run final_p.py --server.port $PORT --server.address 0.0.0.0`
5. Deploy
</details>

<details>
<summary><b>Railway</b></summary>

1. Visit [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect and deploy your Streamlit app
</details>

<details>
<summary><b>Heroku</b></summary>

1. Create `Procfile`:
   ```
   web: streamlit run final_p.py --server.port $PORT --server.address 0.0.0.0
   ```

2. Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   headless = true
   port = $PORT
   enableCORS = false
   " > ~/.streamlit/config.toml
   ```

3. Deploy using Heroku CLI or GitHub integration
</details>

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Areas for Contribution

- [ ] Add support for more file formats (DOCX, TXT, etc.)
- [ ] Implement translation history
- [ ] Add user authentication
- [ ] Improve UI/UX design
- [ ] Add more language pairs
- [ ] Implement offline translation capabilities
- [ ] Add batch file translation
- [ ] Create mobile-responsive design improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Nikhilesh**
- GitHub: [@nikhilesh9ix](https://github.com/nikhilesh9ix)
- Repository: [NexVerse-Translations](https://github.com/nikhilesh9ix/NexVerse-Translations)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Google Translate](https://translate.google.com/) for translation services
- [gTTS](https://github.com/pndurette/gTTS) for text-to-speech functionality
- All contributors and users of this project

---

<div align="center">

**Made with ❤️ by Nikhilesh**

If you found this project helpful, please consider giving it a ⭐!

</div>

The app is pre-configured for deployment with:
- `.streamlit/config.toml` for Streamlit settings
- `requirements.txt` for Python dependencies
- `.gitignore` for excluding temporary files

## Usage

1. **Translate Sentence**:
   - Enter your text
   - Select language category (Indian/World)
   - Choose target language
   - Click "Translate"
   - Listen to or download the audio

2. **Translate PDF**:
   - Upload a PDF file
   - Select language category
   - Choose target language
   - Click "Translate PDF Text"
   - Listen to or download the translated audio

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created by [nikhilesh9ix](https://github.com/nikhilesh9ix)

## Support

For issues or questions, please open an issue on GitHub.
