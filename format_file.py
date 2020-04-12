import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fname")
    parser.add_argument("--frame-height", type=int)
    parser.add_argument("--frame-width", type=int)

    try:
        args = parser.parse_args()
    except Exception as e:
        print(str(e))
        exit(1)
    else:
        fname = args.fname
        height = args.frame_height
        width = args.frame_width

        formatted = format_text_block(height, width, fname)
        print(formatted)


def format_text_block(height, width, fname):
    try:
        with open(fname) as file:
            text = ''.join(file.readlines()[:height])
            text = text[:min(len(text), height * width)]
            lines = text.split('\n')
    except Exception as e:
        return str(e)
    else:
        formatted = ''
        n = height
        for line in lines:
            if len(line) <= width:
                formatted += line + '\n'
                n -= 1
            else:
                while line and n:
                    if len(line) > width:
                        slice = line[:width]
                        line = line[width:]
                    else:
                        slice = line
                        line = ''
                    formatted += slice + '\n'
                    n -= 1
            if not n:
                break
        return formatted[:-1]


if __name__ == '__main__':
    main()