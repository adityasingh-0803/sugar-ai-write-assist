# sugar-ai-write-assist

# Sugar AI Write Assist ✍️🧠

Enhancing the Sugar Labs Write Activity with AI-powered grammar correction and writing assistance.

## 🚀 Features

- ✅ Real-time grammar correction using LanguageTool
- 🧠 AI-powered sentence and story suggestions using distilGPT2
- 🎨 GTK-based lightweight frontend for children-friendly interaction

## 📦 Backend API

### POST `/correct`

```json
{
  "text": "He go to school everyday."
}
```
Response:
```json
{
  "original": "He go to school everyday.",
  "corrected": "He goes to school every day."
}
```
###POST `/suggest`
```json
{
  "text": "Once upon a time,"
}
```
Response:
```json
{
  "prompt": "Once upon a time,",
  "suggestion": "there was a little fox who loved exploring the woods."
}
```
