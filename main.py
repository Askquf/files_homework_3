def union_files(filenames, file_quantity):
    all_files = read_all_files(filenames)
    all_files = dict(sorted(all_files.items(), key=lambda item: len(item[1])))
    write_union_file(all_files)

def read_all_files(filenames):
    all_files = {}
    for filename in filenames:
        with open('files\\'+filename, encoding='UTF-8') as f:
            all_files.setdefault(filename, f.readlines())
    return all_files

def write_union_file(all_files):
    with open('union_file.txt', 'w', encoding='UTF-8') as f:
        for file, file_lines in all_files.items():
            f.write(f'{file}\n{str(len(file_lines))}\n')
            f.writelines(file_lines)
            f.write('\n')

union_files(['1.txt', '2.txt', '3.txt'], 3)