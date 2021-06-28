from style_transfer import neural_style
from style_transfer import utils

map_style_model_path = {'Candy':'saved_models/candy.pth',
                        'Mosaic':'saved_models/mosaic.pth',
                        'Rain Princess':'saved_models/rain_princess.pth',
                        'Udnie': 'saved_models/udnie.pth'}

def stylize_image(input_image_b64_str):
    image_str = neural_style.stylize(input_image_b64_str, model="saved_models/udnie.pth", content_scale=2)
    return image_str