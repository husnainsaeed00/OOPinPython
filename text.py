class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        line_length = 0
        
        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                result.append(line)
                line = [word]
                line_length = len(word)
        
        # Handle the last line
        last_line = " ".join(line)
        last_line += " " * (maxWidth - len(last_line))
        result.append(last_line)
        
        # Justify each line
        for i in range(len(result) - 1):
            line = result[i]
            num_words = len(line)
            total_spaces = maxWidth - sum(len(word) for word in line)
            
            if num_words == 1:
                result[i] = line[0] + " " * total_spaces
            else:
                num_gaps = num_words - 1
                spaces_per_gap = total_spaces // num_gaps
                extra_spaces = total_spaces % num_gaps
                
                justified_line = ""
                for j in range(num_words - 1):
                    justified_line += line[j]
                    justified_line += " " * spaces_per_gap
                    if j < extra_spaces:
                        justified_line += " "
                
                justified_line += line[-1]  # Add the last word without extra spaces
                result[i] = justified_line
        
        return result
