"""
LCD Display problem

Read in a segment size along with a number to convert to an LCD style Ascii art
"""

import file_reader as fr
import file_writer as fw

class Problem3:

    def __init__(self, segment_size, number_to_convert):
        self.segment_size = int(segment_size)
        self.number_to_convert = number_to_convert
        self.top_string = ""
        self.upper_string = ""
        self.middle_string = ""
        self.lower_string = ""
        self.bottom_string = ""

    def build_top(self):
        for i in self.number_to_convert:
            if i == "1" or i == "4":
                self.top_string += " "*(self.segment_size+2)+ " "
            else:
                self.top_string += " " + "-"*self.segment_size + "  "
        return self.top_string
        
    def build_upper(self):
        self.upper_string = ""
        for i in self.number_to_convert:
            if i == "1" or i == "2" or i == "3" or i == "7":
                self.upper_string += " "*(self.segment_size+1) + "|" + " "
            elif i == "5" or i == "6":
                self.upper_string += "|" + " "*(self.segment_size+1) + " "
            else:
                self.upper_string += "|" + " "*self.segment_size + "|" + " "
        return self.upper_string

    def build_middle(self):
        for i in self.number_to_convert:
            if i == "0" or i == "1" or i == "7":
                self.middle_string += " "*(self.segment_size+2)+ " "
            else:
                self.middle_string += " " + "-"*self.segment_size + "  "
        return self.middle_string
    
    def build_lower(self):
        self.lower_string = ""
        for i in self.number_to_convert:
            if i == "1" or i == "3" or i == "4" or i == "5" or i == "7" or i == "9":
                self.lower_string += " "*(self.segment_size+1) + "|" + " "
            elif i == "2":
                self.lower_string += "|" + " "*(self.segment_size+1) + " "
            else:
                self.lower_string += "|" + " "*self.segment_size + "|" + " "
        return self.lower_string
    
    def build_bottom(self):
        for i in self.number_to_convert:
            if i == "1" or i == "4" or i == "7":
                self.bottom_string += " "*(self.segment_size+2)+ " "
            else:
                self.bottom_string += " " + "-"*self.segment_size + "  "
        return self.bottom_string


def execute_main():
    input_file = fr.FileReader("inputFile.txt")
    raw_input = input_file.file_read_all_str_list()

    #calculate position strings
    exe_problem2 = Problem3(raw_input[0], raw_input[2:])
    top = exe_problem2.build_top()
    
    for i in range(int(raw_input[0])):
        upper = exe_problem2.build_upper()
        upper += "\n"+ upper
                
    middle = exe_problem2.build_middle()

    for i in range(int(raw_input[0])):
        lower = exe_problem2.build_lower()
        lower += "\n" + lower

    bottom = exe_problem2.build_bottom()

    #combine position strings
    output_string = top + "\n" + upper + "\n" + middle + "\n" + lower +"\n" + bottom

    output_file = fw.FileWriter("PyProblem3-Output.txt")
    output_file.file_write_all_str(output_string)


if __name__ == "__main__":
    execute_main()