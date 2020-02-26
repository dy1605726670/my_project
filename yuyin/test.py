import generate

if __name__ == '__main__':
    setting = {
        'TEXT':'大扎好，我系喳喳灰', 
        'PER':1, 
        'SPD':5, 
        'PIT':5, 
        'VOL':5, 
        'AUE':6,
        "filename":"test."
    }

    generate.Generate(setting)