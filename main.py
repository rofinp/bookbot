def main():
	book_path = "books/frankenstein.txt"
	content = get_book_content(book_path)
	num_words = get_num_words(content)
	dict_count_chars = get_chars_dict(content)
	char_list = convert_dict_to_list(dict_count_chars)
	char_list.sort(key=lambda x: x["occur"], reverse=True)
	print(f"--- Begin report of {book_path} ---")
	print(f"A total of {num_words} words were found in the document\n")
	for item in char_list:
		print(f"The '{item['character']}' character was found {item['occur']} times")
	print(f"\n--- End report of {book_path} ---")

def get_book_content(path):
	try:
		with open(path) as f:
			return f.read()
	except FileNotFoundError:
		print("The file does not exist! Please check the path.")

def get_num_words(text):
	try:
		return len(text.split())
	except Exception as e:
		print(f"An error occurred while counting words: {e}")

def get_chars_dict(text):
	chars_dict = {}
	for char in text:
		char_lowered = char.lower()
		if char_lowered.isalpha():
			if char_lowered in chars_dict:
				chars_dict[char_lowered] += 1
			else:
				chars_dict[char_lowered] = 1
	return chars_dict

def convert_dict_to_list(dict):
    return [{'character': char, 'occur': occur} for char, occur in dict.items()]

if __name__ == "__main__":
	main()