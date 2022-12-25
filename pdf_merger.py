from PyPDF2 import PdfReader, PdfWriter

# test:
#    dict_path:
#    /home/hardli/python/pytorch/04.Gradient&Perceptron/1 Gradients
#    files:
#    A_Gradient.pdf
#    B_Gradients_OrdinaryFunctions.pdf
#    C_ActivationFunctions.pdf
#    D_LossError.pdf


def get_files():

    dict_path = input('enter the path of files you want to merge: ')
    over = False
    file_lst = []

    while over == False:
        file_name = input('give the name of a file to merge: ')
        file_path = dict_path + '/' + file_name
        file_lst.append(file_path)
        yn = input('more files? y or n: ')
        if yn == 'y':
            continue
        elif yn == 'n':
            over = True
            break
        else:
            print('please give y or n')
            continue

    return dict_path, file_lst

def merge_pdf(dict_path, file_lst):

    new_file = input('give a name to new file: ')
    output_path = dict_path + '/' + new_file

    writer = PdfWriter()

    for file in file_lst:
        # create reader for each PDF
        reader = PdfReader(file)
        # each page of current PDF
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

    # write out merged PDF
    with open(output_path,'wb') as out:
        writer.write(out)

if __name__ == '__main__':

    dict_path, file_lst = get_files()
    print(file_lst)
    merge_pdf(dict_path, file_lst)