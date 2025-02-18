# data_handler.py

def getText():
    # List the specific text files you want to concatenate
    files_to_concat = [
        "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/Posters/texts/french/FL4984936_29_DIGI_0035_00029_VIEW_MAIN.jpg.txt",
        "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/Posters/texts/french/FL4984941_30_DIGI_0035_00030_VIEW_MAIN.jpg.txt",
        "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/Posters/texts/french/FL4984946_31_DIGI_0035_00031_VIEW_MAIN.jpg.txt",
        "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/Posters/texts/french/FL4984951_32_DIGI_0035_00032_VIEW_MAIN.jpg.txt",
        "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/Posters/texts/french/FL4984956_33_DIGI_0035_00033_VIEW_MAIN.jpg.txt"
    ]
    
    # Initialize an empty string to hold the concatenated text
    combined_text = ""
    
    # Loop through the specified files and read their content
    for file_path in files_to_concat:
        with open(file_path, "r") as f:
            combined_text += f.read() + "\n"  # Adding newline between files
  
    return combined_text

