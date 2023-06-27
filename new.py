import csv
import json

data = csv.DictReader(open('Data.csv', encoding='latin-1'))

name_info = {}
for row in data:
    name = row['Name']
    if name not in name_info:
        name_info[name] = []
    name_info[name].append({
        'Qu Id': row['Qu Id'],
        'Manufacturers': row['Name (Manufacturers)'],
        'Categories': row['Name (Categories)'],
        'Weight': row['Weight (Packages)'],
        'Height': row['Height (Packages)'],
        'Length': row['Length (Packages)'],
        'Width': row['Width (Packages)']
    })

prompt_completion_pairs = []
for name, info_list in name_info.items():
    prompt_text = f"{name}"
    completion_text = ""
    if len(info_list) == 1:
        info = info_list[0]
        completion_text = f"Qu Id: {info['Qu Id']}, Manufacturers: {info['Manufacturers']}, Categories: {info['Categories']}, Weight: {info['Weight']}, Height: {info['Height']}, Length: {info['Length']}, Width: {info['Width']}"
    else:
        completion_text = "There are: \n "
        for i, info in enumerate(info_list):
            completion_text += f"{i + 1}. 'Qu Id: {info['Qu Id']}, Manufacturers: {info['Manufacturers']}, Categories: {info['Categories']}, Weight: {info['Weight']}, Height: {info['Height']}, Length: {info['Length']}, Width: {info['Width']}'\n\n "

    prompt_completion_pairs.append({
        'prompt': prompt_text,
        'completion': completion_text
    })

with open('jacobian.json', 'w') as outfile:
    json.dump(prompt_completion_pairs, outfile)
