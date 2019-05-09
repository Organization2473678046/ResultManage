import subprocess
import os


# output = subprocess.check_output(["soffice","--headless","--invisible","--convert-to","docxs","/home/ltcx/code/RW_doc/word/text1.doc","--outdir","/home/ltcx/code/RW_doc/docxs"]


def transfer_format(out_dir, filepath):
    out_format = "docx"
    subprocess.check_output(
        ["soffice", "--headless", "--invisible", "--convert-to", out_format, filepath, "--outdir", out_dir])


if __name__ == '__main__':
    out_dir = "/home/ltcx/python_code/docx_data"
    filepath = "/home/ltcx/python_code/doc_data/分发单模板01.doc"

    transfer_format(out_dir,filepath)

