def StringChallenge(strParam):
  compressed_str = ""
  current_count = 1

  for i in range(1, len(strParam)):
    if strParam[i] == strParam[i-1]:
      current_count += 1
    else:
      compressed_str += str(current_count) + strParam[i-1]
      current_count = 1
  
  # Add the last character and its count after the loop
  compressed_str += str(current_count) + strParam[-1]

  challenge_token = "7bdymo04fe"
  final_output = ""
  token_index = 0

  for c in compressed_str:
    final_output += c
    if token_index < len(challenge_token):
      final_output += challenge_token[token_index]
      token_index += 1
  
  return final_output

# Example test
print(StringChallenge("aabbcde"))
