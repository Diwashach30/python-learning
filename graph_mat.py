import matplotlib.pyplot as plt

# Given data
data = {
    "ApexTech": 33,
    "Pujana Banstola": 28,
    "Nitesh Bishwokarma": 45,
    "Hari Bisthari Bista": 26,
    "Tolak Raj Chapagain": 39,
    "Sanjib Chaudhary": 31,
    "Som Prakash Chaudhary": 29,
    "Kiran Don": 40,
    "Dilip Singh Karki": 36,
    "Shankarsan Khadka": 23,
    "Kiran Paudel": 22,
    "Bishworaj Poudel": 34,
    "Nishan Poudel": 27,
    "Padam Rai": 32,
    "Aatreya Rangun": 50,
    "Kishor Saud": 41,
    "Suren Shakya": 30,
    "Binay Shrestha": 37,
    "Runiv Thapamgr": 25,
    "Nabin Timsina": 42
}

# Sort data by values in descending order
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
names = [item[0] for item in sorted_data]
values = [item[1] for item in sorted_data]

# Create figure and axis
plt.figure(figsize=(14, 8))

# Create bar plot
bars = plt.bar(names, values, color='skyblue')

# Customize the plot
plt.title('Scores by Person', fontsize=16, pad=20)
plt.xlabel('Names', fontsize=12)
plt.ylabel('Scores', fontsize=12)
plt.xticks(rotation=90, fontsize=8)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}',
             ha='center', va='bottom', fontsize=8)

# Adjust layout to prevent cutting off labels
plt.tight_layout()
plt.show()