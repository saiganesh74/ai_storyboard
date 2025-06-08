from modules.input_handler import get_scene_description
from modules.gpt_ai import generate_storyboard 
def main():
    print("Welcome to the AI story board generator !!!")
    scene = get_scene_description()
    storyboard = generate_storyboard(scene)
if __name__ == '__main__':
    main()