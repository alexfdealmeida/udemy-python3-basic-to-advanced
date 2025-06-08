text_1 = "Text 1"
text_2 = "Text 2"
number_1 = 1.1

all = "text_1={parameter_1}, text_2={parameter_2}, number_1={parameter_3:.2f}"

formatted_text = all.format(parameter_1=text_1, parameter_2=text_2, parameter_3=number_1)

print(formatted_text)