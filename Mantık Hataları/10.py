#İsim soyisim oluşturucu
import random

def generate_name():
    first_names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
    last_names = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]
    return "{} {}".format(random.choice(last_names), random.choice(first_names))

for i in range(5):
    print(generate_name())