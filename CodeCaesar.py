#print(ord("a"),ord("z"),ord("A"),ord("Z"))

def cipher(text, shift):
	result = ""
	if shift==0:
		return text
	else:
		for i in text:
			if shift>0 and (97 <= ord(i) <= 122 - shift or 65 <= ord(i) <= 90 - shift):
				result += chr(ord(i)+shift)
			elif shift>0 and 122 - shift < ord(i) <= 122:
				g = 122 - ord(i)
				result += chr(97 + shift - g - 1)
			elif shift>0 and 90 - shift < ord(i) <= 90:
				g = 90 - ord(i)
				result += chr(65 + shift - g - 1)
			elif shift<0 and (97-shift <= ord(i) <= 122 or 65-shift <= ord(i) <=90):
				result += chr(ord(i)+shift)
			elif shift<0 and 97 <= ord(i) < 97-shift:
				g = ord(i) - 97
				result += chr(122 + shift +1 + g)
			elif shift<0 and 65 <= ord(i) < 65-shift:
				g = ord(i) - 65
				result += chr(90 + shift +1 + g)
			else:
				result += i
		return result
