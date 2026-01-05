# NexVerse-Translations 🌐

A powerful Streamlit-based translation application that supports text and PDF translation with audio playback capabilities.

## Features

- **Text Translation**: Translate sentences between multiple languages
- **PDF Translation**: Upload and translate entire PDF documents
- **Audio Playback**: Listen to both original and translated text
- **Language Categories**: Organized into Indian Languages and World Languages
- **Audio Download**: Download translated audio as MP3 files
- **Language Detection**: Automatically detect source language
- **User Feedback**: Built-in feedback system

## Technologies Used

- **Streamlit**: Web application framework
- **Google Translate API**: Text translation
- **gTTS**: Text-to-speech conversion
- **PyPDF2**: PDF text extraction

## Local Installation

1. Clone the repository:
```bash
git clone https://github.com/nikhilesh9ix/NexVerse-Translations.git
cd NexVerse-Translations
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run final_p.py
```

4. Open your browser and navigate to `http://localhost:8501`

## Deployment Options

### Option 1: Streamlit Community Cloud (Recommended - FREE)

1. **Push your code to GitHub**:
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository: `nikhilesh9ix/NexVerse-Translations`
   - Main file path: `final_p.py`
   - Click "Deploy"

3. Your app will be live at: `https://[your-app-name].streamlit.app`

### Option 2: Render

1. Go to [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run final_p.py --server.port $PORT --server.address 0.0.0.0`
5. Deploy

### Option 3: Railway

1. Go to [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect and deploy your Streamlit app

### Option 4: Heroku

1. Create a `Procfile`:
```
web: streamlit run final_p.py --server.port $PORT --server.address 0.0.0.0
```

2. Create a `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

3. Deploy using Heroku CLI or GitHub integration

## Environment Configuration

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
