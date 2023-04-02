from solution import solve, cross, Map, Rectangle

from PIL import Image, ImageDraw
import random

def rnd(limit):
    return random.randint(limit // 10, limit)


def get_image(map, rectangles):
    image = Image.new(mode="RGB",size=(map.width, map.height), color="white")
    image_draw = ImageDraw.Draw(image, "RGB")

    for rectangle in rectangles:
        image_draw.rectangle([
            (rectangle.x, rectangle.y),
            (rectangle.x + rectangle.width, rectangle.y + rectangle.height),
        ], fill='black', outline='green')

    for i in range(len(rectangles)):
        for j in range(i):
            a = rectangles[i]
            b = rectangles[j]
            rectangle = cross(a, b)

            if rectangle:
                image_draw.rectangle([
                    (rectangle.x, rectangle.y),
                    (rectangle.x + rectangle.width, rectangle.y + rectangle.height),
                ], fill='gray', outline='red')
    return image


def save(map, rectangles, filename):
    image = get_image(map, rectangles)
    image.save(filename)

ITERATIONS = 1000

def main():
    random.seed(924)

    map, rectangles = Map(200, 200), [
        Rectangle(rnd(100), rnd(100), rnd(90), rnd(90)) for _ in range(20)
    ]

    save(map, rectangles, "in.png")

    frames = []
    for _ in range(1000):
        if solve(map, rectangles):
            frames.append(get_image(map, rectangles))
        else:
            break

    frames[0].save(
        'record.gif',
        save_all=True,
        append_images=frames[1:],  # Срез который игнорирует первый кадр.
        optimize=True,
        duration=100,
        loop=0
    )

    save(map, rectangles, "out.png")


if __name__ == "__main__":
    main()