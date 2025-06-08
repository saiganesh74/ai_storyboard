# :: AI STORYBOARD GENERATOR ::
The AI Storyboard Generator is a Python-based tool that transforms a simple scene description into a sequence of visual storyboard frames using AI.
###  What it does
- Takes a one-line scene description from the user
- Uses OpenAI's GPT model to break it down into a 6-frame textual storyboard
- (Future updates) Uses OpenAI’s DALL·E to generate images for each frame
- Outputs a storyboard that includes both text descriptions and AI-generated visuals

## Example
```
A girl with an umbrella
```
## Output
```
Frame 1: A girl is standing outside holding an umbrella.
Frame 2: The umbrella opens as it starts to rain.
Frame 3: The girl looks up at the cloudy sky.
....
```
## Usage
```
sudo apt install python3
git clone https://github.com/saiganesh74/Ai_storyboard
cd Ai_storyboard
python3 main.py
```
## Dependencies
- openai 
- python-dotenv
Install them with
```
pip install requirements.txt
```
## Future Updates 
- Adding a GUI for non-tech's
- Image generation using DALL-E API's
- Downloading the image sets

## Contributing
Pull requests are welcome! If you’d like to contribute ideas, code, or bug fixes, feel free to open an issue or submit a PR.

